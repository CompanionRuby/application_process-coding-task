import typer
from fastapi import FastAPI
import uvicorn

# Initialize FastAPI for the HTTP endpoints
api = FastAPI(title="Coding Task API")

# Initialize Typer for the CLI interface
cli = typer.Typer()

@api.get("/")
def health_check():
    return {"status": "API is running"}

@cli.command()
def start_server(port: int = 8000):
    """Start the FastAPI server via the CLI."""
    uvicorn.run("main:api", host="127.0.0.1", port=port, reload=True)

if __name__ == "__main__":
    cli()