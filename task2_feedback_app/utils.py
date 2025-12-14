import os
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

DATA_FILE = "data.csv"

def generate_user_response(review, rating):
    prompt = f"""
    A customer gave a {rating}-star rating and wrote the following review:

    "{review}"

    Write a polite and friendly response.
    """
    return llm.invoke(prompt).content


def summarize_review(review):
    prompt = f"""
    Summarize the following customer review in one sentence:

    "{review}"
    """
    return llm.invoke(prompt).content


def recommend_action(review):
    prompt = f"""
    Based on the following customer review, suggest one clear recommended action:

    "{review}"
    """
    return llm.invoke(prompt).content


def save_feedback(rating, review, ai_response, summary, action):
    df = pd.read_csv(DATA_FILE)
    new_row = {
        "rating": rating,
        "review": review,
        "ai_response": ai_response,
        "summary": summary,
        "recommended_action": action
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
