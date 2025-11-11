# dummy change to trigger redeploy
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

app = FastAPI()

# Input model (this is what Zapier will send)
class RequestData(BaseModel):
    notes: str
    client_email: str

# Output model (this is what Zapier will receive)
class EmailResponse(BaseModel):
    email_subject: str
    email_body: str

# Your LLM
def get_llm():
    return ChatOpenAI(model="gpt-4o-mini")


@app.post("/generate-email", response_model=EmailResponse)
def generate_email(data: RequestData):
    llm = get_llm()

    prompt = f"""
    [Your prompt goes here — you will write it]
    SDR Notes: {data.notes}
    Client Email: {data.client_email}

    Return ONLY:
    - email_subject
    - email_body
    """

    result = llm.invoke(prompt)

    return EmailResponse(
        email_subject="Subject from LLM",
        email_body=result.content
    )
