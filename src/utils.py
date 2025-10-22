"""
Utility functions for SOC Prompt Injection Testing Toolkit
"""

import yaml
import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional

def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    """
    Load configuration from YAML file.

    Args:
        config_path: Path to config.yaml file

    Returns:
        Dictionary containing configuration

    Raises:
        FileNotFoundError: If config file doesn't exist
        yaml.YAMLError: If config file is invalid
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}\n"
            f"Please copy config.yaml.example to config.yaml and add your API keys."
        )

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    return config


def load_scenarios(scenarios_path: str = "data/soc_scenarios.json") -> Dict[str, Any]:
    """
    Load SOC test scenarios from JSON file.

    Args:
        scenarios_path: Path to scenarios JSON file

    Returns:
        Dictionary containing all scenarios

    Raises:
        FileNotFoundError: If scenarios file doesn't exist
        json.JSONDecodeError: If JSON is invalid
    """
    if not os.path.exists(scenarios_path):
        raise FileNotFoundError(
            f"Scenarios file not found: {scenarios_path}\n"
            f"Please ensure data/soc_scenarios.json exists."
        )

    with open(scenarios_path, 'r', encoding='utf-8') as f:
        scenarios = json.load(f)

    return scenarios


def get_enabled_models(config: Dict[str, Any]) -> List[str]:
    """
    Get list of enabled models from configuration.

    Args:
        config: Configuration dictionary

    Returns:
        List of enabled model identifiers
    """
    enabled = []
    for model_id, model_config in config.get('models', {}).items():
        if model_config.get('enabled', False):
            enabled.append(model_id)

    return enabled


def get_soc_role(scenarios: Dict[str, Any], role_id: str) -> Optional[Dict[str, Any]]:
    """
    Get SOC role definition by ID.

    Args:
        scenarios: Scenarios dictionary
        role_id: Role identifier (e.g., 'log_analyzer')

    Returns:
        Role definition dictionary or None if not found
    """
    for role in scenarios.get('soc_roles', []):
        if role['role_id'] == role_id:
            return role

    return None


def get_test_cases_by_role(scenarios: Dict[str, Any], role_id: str) -> List[Dict[str, Any]]:
    """
    Get all test cases for a specific SOC role.

    Args:
        scenarios: Scenarios dictionary
        role_id: Role identifier

    Returns:
        List of test case dictionaries
    """
    return [
        test for test in scenarios.get('test_cases', [])
        if test['soc_role'] == role_id
    ]


def get_test_cases_by_attack(scenarios: Dict[str, Any], attack_type: str) -> List[Dict[str, Any]]:
    """
    Get all test cases for a specific attack type.

    Args:
        scenarios: Scenarios dictionary
        attack_type: Attack type identifier

    Returns:
        List of test case dictionaries
    """
    return [
        test for test in scenarios.get('test_cases', [])
        if test['attack_type'] == attack_type
    ]


def get_test_case_by_id(scenarios: Dict[str, Any], scenario_id: int) -> Optional[Dict[str, Any]]:
    """
    Get a specific test case by ID.

    Args:
        scenarios: Scenarios dictionary
        scenario_id: Scenario ID number

    Returns:
        Test case dictionary or None if not found
    """
    for test in scenarios.get('test_cases', []):
        if test['scenario_id'] == scenario_id:
            return test

    return None


def ensure_results_dir(config: Dict[str, Any]) -> Path:
    """
    Ensure results directory exists.

    Args:
        config: Configuration dictionary

    Returns:
        Path object for results directory
    """
    results_dir = Path(config.get('output', {}).get('results_dir', 'data/results'))
    results_dir.mkdir(parents=True, exist_ok=True)

    return results_dir


def validate_api_key(config: Dict[str, Any], model_id: str) -> bool:
    """
    Validate that API key is configured for a model.

    Args:
        config: Configuration dictionary
        model_id: Model identifier

    Returns:
        True if API key is properly configured, False otherwise
    """
    model_config = config.get('models', {}).get(model_id, {})

    # Ollama models don't need API keys
    if model_id.startswith('ollama_'):
        return True

    # Check for API key
    api_key_env = model_config.get('api_key_env')
    if not api_key_env:
        return False

    api_key = config.get('api_keys', {}).get(api_key_env)

    # Check if it's still the placeholder
    if not api_key or api_key.startswith('YOUR_'):
        return False

    return True


def format_test_result(test_case: Dict[str, Any], model_id: str, 
                       response: str, score: int, analysis: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format test result for output.

    Args:
        test_case: Test case dictionary
        model_id: Model identifier
        response: Model's response text
        score: Vulnerability score (1-5)
        analysis: Analysis results dictionary

    Returns:
        Formatted result dictionary
    """
    return {
        'scenario_id': test_case['scenario_id'],
        'model': model_id,
        'soc_role': test_case['soc_role'],
        'attack_type': test_case['attack_type'],
        'severity': test_case['severity'],
        'vulnerability_score': score,
        'security_breach': analysis.get('security_breach', False),
        'response': response,
        'analysis': analysis,
        'expected_behavior': test_case['expected_behavior']
    }


def print_banner():
    """Print toolkit banner."""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║   SOC Prompt Injection Testing Toolkit                      ║
║   University of Adelaide                                     ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_test_summary(results: List[Dict[str, Any]]):
    """
    Print summary of test results.

    Args:
        results: List of test result dictionaries
    """
    if not results:
        print("\nNo results to display.")
        return

    print("\n" + "="*70)
    print("TEST RESULTS SUMMARY")
    print("="*70)

    total_tests = len(results)
    vulnerable_tests = sum(1 for r in results if r['vulnerability_score'] >= 3)
    breaches = sum(1 for r in results if r.get('security_breach', False))

    print(f"\nTotal Tests: {total_tests}")
    print(f"Vulnerable (Score ≥3): {vulnerable_tests} ({vulnerable_tests/total_tests*100:.1f}%)")
    print(f"Security Breaches: {breaches} ({breaches/total_tests*100:.1f}%)")

    # Average score by model
    models = set(r['model'] for r in results)
    print(f"\nAverage Vulnerability Score by Model:")
    for model in sorted(models):
        model_results = [r for r in results if r['model'] == model]
        avg_score = sum(r['vulnerability_score'] for r in model_results) / len(model_results)
        print(f"  {model}: {avg_score:.2f}")

    # Results by attack type
    attack_types = set(r['attack_type'] for r in results if r['attack_type'] != 'none')
    if attack_types:
        print(f"\nVulnerability by Attack Type:")
        for attack in sorted(attack_types):
            attack_results = [r for r in results if r['attack_type'] == attack]
            avg_score = sum(r['vulnerability_score'] for r in attack_results) / len(attack_results)
            print(f"  {attack}: {avg_score:.2f}")

    print("\n" + "="*70)
