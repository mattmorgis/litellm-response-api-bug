# LiteLLM Responses API Bug

This repo demonstrates an issue with the OpenAI Agents SDK using the Responses API through Azure/LiteLLM `v1.77.5-stable`.

The bug happens when making a follow up request through LiteLLM. When hitting Azure directly the calls succeed.

## Steps to Reproduce

### OpenAI directly

1. Set your `OPENAI_BASE_URL` and `OPENAI_API_KEY` to azure values.

```bash
# set in .env
cp .env.example .env

# or set in shell before running
export OPENAI_BASE_URL=https://<your-azure-here>.openai.azure.com/openai/v1
export OPENAI_API_KEY=
```

2. Run the script

```bash
uv run main.py

user: tell me an interesting fact
assistant: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs—over 3,000 years old—that are still perfectly edible.

user: tell me another
assistant: Octopuses have three hearts and blue blood. Two hearts pump blood to the gills, while the third pumps it to the rest of the body, and their copper-based blood (hemocyanin) helps them thrive in cold, low-oxygen waters.

```

### LiteLLM

1. Add your Azure URL to `litellm_config.yaml` and `AZURE_API_KEY` to `start_litellm.sh` script and start the proxy.

```bash
./start_litellm.sh

INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:4000 (Press CTRL+C to quit)

```

2. Set `OPENAI_BASE_URL` to LiteLLM and `OPENAI_API_KEY` to a LiteLLM key.

```bash
cp .env.example .env

# or set in your shell
export OPENAI_BASE_URL=http://localhost:4000
export OPENAI_BASE_URL=sk-...
```

3. Run the script

```bash
uv run main.py

```

```
user: tell me an interesting fact
assistant: Octopuses have three hearts: two pump blood to the gills, while the third pumps it to the rest of the body. Even more unusual, their blood is blue because it uses a copper-containing protein called hemocyanin to transport oxygen, which works better than hemoglobin in cold, low-oxygen seawater.

user: tell me another
Error getting response: Error code: 400 - {'error': {'message': 'litellm.BadRequestError: AzureException BadRequestError - {\n  "error": {\n    "message": "Unknown parameter: \'input[1].status\'.",\n    "type": "invalid_request_error",\n    "param": "input[1].status",\n    "code": "unknown_parameter"\n  }\n}. Received Model Group=gpt-5-mini\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}. (request_id: None)
```
