from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv(override=True)

# Prepare LLM chain
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
chain = llm | StrOutputParser()

# Read system prompt
with open("src/prompts/SYSTEM_PROMPT.md", "r", encoding="UTF-8") as file:
    system_prompt = file.read()

def send_request(user_prompt: str):
    """Sends the user prompt and the defined system prompt to the LLM. Streams the output to the console."""
    prompts = [("system", system_prompt), ("human", user_prompt)]

    for chunk in chain.stream(prompts):
        print(chunk, end="", flush=True)