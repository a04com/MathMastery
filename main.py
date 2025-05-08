import os
from groq import Groq

GROQ_API_KEY="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"
# Initialize the Groq client
client = Groq(
    api_key=GROQ_API_KEY,
)

SYSTEM_PROMPT = """You are a helpful AI assistant for teaching math.
When answering math questions, you will:
1. Write formulas using plain Markdown formatting (e.g., a^2 + b^2 = c^2)
2. Explain each step of the solution clearly and logically
3. Keep explanations concise but complete—neither too short nor too long
4. Give examples when useful, but stay focused on the main problem
5. Use simple, clear language appropriate for a student audience
6. Always explain why each step is taken, not just what to do
7. Be honest if you're unsure, and guide the user on how to find the answer
"""

def ask_ai(user_question, exercise_context=None):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    # Add context if provided
    if exercise_context:
        messages.append({"role": "user", "content": f"Exercise context: {exercise_context}"})
    messages.append({"role": "user", "content": user_question})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=1000,
    )
    return chat_completion.choices[0].message.content

# For CLI testing
if __name__ == "__main__":
    user_input = input("You: ")
    print(ask_ai(user_input))