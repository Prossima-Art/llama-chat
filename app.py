from fastapi import FastAPI, Query
from ollama import Client

app = FastAPI()

client = Client(host='http://localhost:11434')


# llama3.2
@app.get("/chat")
async def chat(
    model: str = Query(..., description="LLM"),
    messages: str = Query(..., description="Message to process"),
):
    message = {'role': 'user', 'content': messages}
    response = client.chat(model=model, messages=[message])
    return response


@app.get("/generate")
async def generate(
    model: str = Query(..., description="LLM"),
    prompt: str = Query(..., description="Message to process"),
):
    response = client.generate(model=model, prompt=prompt)
    return response
