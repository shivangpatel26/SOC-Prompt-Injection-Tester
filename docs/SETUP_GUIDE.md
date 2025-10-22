# Setup Guide

## Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Get Google Gemini API Key (FREE)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key
5. Paste it in `config.yaml` under `google_api_key`

**Note**: Gemini offers a generous free tier - plenty for testing!

## Step 3: Install Ollama (for Local Models)

### On macOS/Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### On Windows:
Download from [https://ollama.com/download](https://ollama.com/download)

### Verify Installation:
```bash
ollama --version
```

## Step 4: Download Models

Pull the models you want to test:

```bash
# Gemma (lightweight, fast)
ollama pull gemma:2b

# Mistral (balanced)
ollama pull mistral:7b

# LLaMA 2 (optional)
ollama pull llama2:7b

# DeepSeek (optional)
ollama pull deepseek-r1:7b
```

## Step 5: Start Ollama Server

```bash
ollama serve
```

This starts a local API server at `http://localhost:11434`

## Step 6: Configure the Toolkit

```bash
# Copy the example config
cp config.yaml.example config.yaml

# Edit config.yaml with your favorite editor
nano config.yaml  # or vim, code, etc.

# Add your Google API key
# Enable/disable models as needed
```

## Step 7: Test Your Setup

```bash
# Test Gemini connection (replace YOUR_KEY with actual key)
python -c "import google.generativeai as genai; genai.configure(api_key='YOUR_KEY'); print('Gemini: OK')"

# Test Ollama connection
curl http://localhost:11434/api/tags
```

## Troubleshooting

### "Ollama not found"
- Make sure Ollama is installed and `ollama serve` is running

### "Invalid API key"
- Double-check your Google API key in config.yaml
- Make sure there are no extra spaces

### "Model not found"
- Run `ollama list` to see downloaded models
- Pull missing models with `ollama pull <model-name>`

### Rate limiting
- Increase `delay_between_tests` in config.yaml
- Use fewer concurrent tests

## Next Steps

Once setup is complete, proceed to [USAGE.md](USAGE.md) to run your first test!
