from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def answer_node(state):
    print("Executing Answer Node")
    context = state["context"]

    if not context.strip():
        state["final_answer"] = (
            "No relevant information found in the knowledge base."
        )
        return state

    prompt = f"""
Context:
{context}

Question:
{state["user_query"]}

Answer only from the provided context.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    state["final_answer"] = (
        response.choices[0].message.content
    )

    return state