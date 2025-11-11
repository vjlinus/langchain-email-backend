from langchain_openai import ChatOpenAI
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/generate-email")
async def generate_email(request: Request):
    data = await request.json()
    notes = data.get("notes", "")
    client_email = data.get("email", "")

    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
    Based on the SDR notes below, generate:

    - A clear email subject line
    - A full email body
    - Friendly, professional tone

    SDR Notes:
    {notes}
    """

    result = llm.invoke(prompt)

    return {
        "email_subject": "Generated Email",
        "email_body": result.content,
        "client_email": client_email
    }

@app.get("/")
def root():
    return {"status": "running"}
