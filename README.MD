# LLM Code Reviewer

This repossitory are forked from tusgino/llm-code-reviewer, modify for gitea and openai compatible API.

This GitHub Action automatically reviews Pull Requests using multiple Language Models (LLMs) including OpenAI's GPT and Google's Gemini models. Get intelligent code reviews directly in your PR comments!

## Features

- 🤖 Multi-model support (OpenAI GPT, Google Gemini, Anthropic ClaudeAI)
- 🔄 Automatic PR code review
- 🌍 Multiple language support
- ⚙️ Configurable model selection
- 🚫 File exclusion patterns
- 🎯 Primary model selection capability

## Setup

### Prerequisites

1. Create a GitHub token with appropriate permissions
2. (Optional) Obtain API keys for:
   - Google Gemini API
   - OpenAI API
   - Anthropic API (ClaudeAI)

### Usage

Add the following workflow file to your repository (e.g., `.github/workflows/code-review.yml`):

```yaml
name: Code Review

on:
  pull_request:
    types: [opened, synchronize]    # Trigger on PR open or update

jobs:
  review:
    runs-on: ubuntu-latest
    
    steps:
      - uses: jason-webcomm/llm-code-reviewer@develop
        with:
          GITEA_TOKEN: ${{ secrets.TECH_PAT }}
          GITEA_URL: ${{ secrets.GITEA_URL }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          API_KEY: ${{ secrets.API_KEY }}
          AI_MODEL: "Qwen/Qwen2.5-Coder-32B-Instruct-AWQ"
          # Optional - Exclude files from review
          INPUT_EXCLUDE: "*.md,**/*.txt"
          # Optional - Set review language
          HUMAN_LANGUAGE: "TW"
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `GITEA_TOKEN` | GITEA token for repository interaction | Yes | - |
| `GITEA_URL` | GITEA URL | Yes | - |
| `OPENAI_BASE_URL` | OpenAI compatible API URL | Yes | - |
| `API_KEY` | AI Endpoint API key | No | - |
| `AI_MODEL` | AI model to use | No | `gpt-4o` |
| `INPUT_EXCLUDE` | Comma-separated file patterns to exclude | No | - |
| `HUMAN_LANGUAGE` | Language for review comments | No | `en` |


## Examples

### Basic Usage

```yaml
- uses: jason-webcomm/llm-code-reviewer@develop
  with:
    GITEA_TOKEN: ${{ secrets.TECH_PAT }}
    GITEA_URL: ${{ secrets.GITEA_URL }}
    OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
    API_KEY: ${{ secrets.API_KEY }}
    AI_MODEL: "Qwen/Qwen2.5-Coder-32B-Instruct-AWQ"
    # Optional - Exclude files from review
    INPUT_EXCLUDE: ""
    # Optional - Set review language
    HUMAN_LANGUAGE: "TW"
```


## Language Support

Set `HUMAN_LANGUAGE` to receive reviews in your preferred language. Examples:
- `en` - English (default)
- `vi` - Vietnamese
- `ja` - Japanese
- `TW` - Taiwan
- And more...

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by [@tusgino](https://github.com/tusgino)

## Support

If you encounter any issues or have questions, please file them in the [Issues](https://github.com/tusgino/llm-code-reviewer/issues) section.
