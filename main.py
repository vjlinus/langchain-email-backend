from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

app = FastAPI()

# Input model
class RequestData(BaseModel):
    notes: str
    client_email: str

# Output model
class EmailResponse(BaseModel):
    email_subject: str
    email_body: str

# Create LLM when needed
def get_llm():
    return ChatOpenAI(model="gpt-4o-mini")

@app.post("/generate-email", response_model=EmailResponse)
def generate_email(data: RequestData):
    llm = get_llm()

    # You will write your own real prompt later
    prompt = f"""
    SDR Notes: {data.notes}

    Generate:
    - email_subject
    - email_body
    """

    result = llm.invoke(prompt)

    return EmailResponse(
        email_subject="Email Subject Placeholder",
        email_body=result.content
    )

