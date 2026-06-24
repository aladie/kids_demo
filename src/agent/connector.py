from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.callbacks import get_usage_metadata_callback
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from better_profanity import profanity
import os

load_dotenv(override=True)

MODEL_NAME = str(os.environ.get("GOOGLE_LLM_MODEL"))

# Prepare LLM chain
llm = ChatGoogleGenerativeAI(model=MODEL_NAME)
chain = llm | StrOutputParser()

# Read system prompt
with open("src/prompts/SYSTEM_PROMPT.md", "r", encoding="UTF-8") as file:
    system_prompt = file.read()

def send_request(user_prompt: str):
    """Sends the user prompt and the defined system prompt to the LLM. Streams the output to the console."""
    prompts = [("system", system_prompt), ("human", user_prompt)]

    with get_usage_metadata_callback() as cb:
        acc = ""

        for chunk in chain.stream(prompts):
            acc += chunk

            if profanity.contains_profanity(acc):
                print("\n\n--- Streaming halted due to detected profanity. ---")
                break

            print(chunk, end="", flush=True)

        # Get useage metadata
        metadata = cb.usage_metadata.get(MODEL_NAME, {})
        total_tokens = metadata.get("total_tokens", 0)
        input_tokens = metadata.get("input_tokens", 0)
        output_tokens = metadata.get("output_tokens", 0)

        total_cost = ((input_tokens / 1_000_000 * float(os.environ.get("INPUT_TOKEN_COST", 0))) + 
                      (output_tokens / 1_000_000 * float(os.environ.get("OUTPUT_TOKEN_COST", 0))))

        print("\n\n-------------\n" +
              f"Total token useage: {total_tokens}" +
              f"\nTotal cost: {total_cost}$" +
              "\n-------------\n")