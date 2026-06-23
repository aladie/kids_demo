import typer
from src.agent.connector import send_request

app = typer.Typer()

@app.command()
def invoke_llm(
    prompt: str = typer.Argument(help="The User prompt")
):
    """
    Prompt the kids demo LLM
    """
    send_request(prompt)

if __name__ == "__main__":
    app()
