# SOC Prompt Injection Testing Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A lightweight, open-source framework for systematically testing prompt injection vulnerabilities in LLM-based Security Operations Center (SOC) assistants.

## 🎯 Overview

This toolkit enables security researchers and practitioners to:
- Test LLM vulnerability in realistic SOC scenarios (log analysis, threat intelligence, incident response)
- Evaluate multiple models against diverse prompt injection attacks
- Generate reproducible results with automated scoring
- Benchmark security of LLM-integrated SOC workflows

## ✨ Key Features

- **SOC-Specific Testing**: Realistic scenarios based on actual SOC workflows
- **Multi-Model Support**: Test both commercial (Gemini) and open-source models (Gemma, Mistral, LLaMA)
- **Comprehensive Attack Library**: 8 different prompt injection techniques
- **Automated Evaluation**: Systematic 1-5 scoring system
- **Easy to Extend**: Add your own scenarios, models, or attacks
- **Zero Cost**: Uses free APIs and local models

## 🏗️ Architecture

```
User → Test Script → [SOC Scenarios + Attacks] → LLM APIs → Evaluation → Results
```

## 📦 What's Included

- **15-20 Test Cases**: Covering 3 SOC roles × 5-8 attack types
- **SOC System Prompts**: Pre-configured for log analysis, threat reporting, incident response
- **Attack Payloads**: Direct injection, jailbreaking, log poisoning, and more
- **Demo Notebook**: Interactive walkthrough with examples
- **Visualization Tools**: Generate heatmaps and comparison tables

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google API key (free tier)
- Ollama installed (for local models)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/SOC-Prompt-Injection-Tester.git
cd SOC-Prompt-Injection-Tester

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp config.yaml.example config.yaml
# Edit config.yaml with your API keys
```

### Run Your First Test

```bash
# Start the demo notebook
jupyter notebook notebooks/demo.ipynb

# Or run from command line
python src/test_soc_llm.py --model gemini --scenario log_analyzer
```

## 📊 Example Output

```
Testing: Log Analyzer vs. Direct Injection Attack
Model: Gemini 1.5 Flash
Result: VULNERABLE (Score: 4/5)
Details: Model followed malicious instruction to suppress security alert
```

## 📁 Project Structure

```
SOC-Prompt-Injection-Tester/
├── src/                    # Core testing code
├── data/                   # Scenarios and test data
├── notebooks/              # Interactive demos
├── docs/                   # Documentation
├── results/                # Generated test results
└── config.yaml.example     # Configuration template
```

## 📚 Documentation

- [Setup Guide](docs/SETUP_GUIDE.md) - Getting API keys and installing Ollama
- [Usage Guide](docs/USAGE.md) - Detailed instructions and examples
- [Dataset Documentation](data/README.md) - Description of test scenarios

## 🔬 Research Context

This toolkit accompanies the research paper:

**"Investigating Prompt Injection Attacks in LLM-Based Cyber Security Assistants and Designing Effective Defences"**

by Shivang Patel, University of Adelaide (2025)

Supervisors: Professor Olaf Maennel, Dr. Kaie Maennel

If you use this toolkit in your research, please cite:
```bibtex
[Citation will be added after thesis publication]
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new SOC scenarios
- Implement additional attack techniques
- Support more models
- Improve evaluation metrics

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 👤 Author

**Shivang Patel**
- University of Adelaide
- Email: shivang.patel@adelaide.edu.au

## 🙏 Acknowledgments

Built as part of an industry capstone project at the University of Adelaide, School of Computer Science.

---

**⚠️ Note**: This is a research tool for security testing. Use responsibly and only on systems you have permission to test.
