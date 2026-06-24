# Onoo Kids Demo

This demo uses LangChain with Gemini in combination with a kids proof system prompt and a profanity check to yield kid safe AI responses.
The estimated cost calculation for the input/output tokens can be edited in the environment file and adapted to the chosen LLM.

## Installation
- Install [UV](https://docs.astral.sh/uv/) on your system and run `uv sync` before runnig the demo.
- Copy the contents of the [.env_sample](.env_sample) file to your local `.env` file and provide your Gemini API-KEY
- Activate the local environment created by UV

## Useage
Run `kids-demo "*YOUR PROMPT HERE*"` to execute the demo.