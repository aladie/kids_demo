from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

prompts = [("system", ""), ("human", "")]

chain = llm | StrOutputParser()

for chunk in chain.stream(prompts):
    print(chunk, end="", flush=True)