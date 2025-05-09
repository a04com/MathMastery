from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key='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',
)

def main():
    # System message to set up the assistant's behavior
    messages = [
        {
            "role": "system",
            "content": """You are a helpful AI assistant for learning mathematics.
When answering math questions, you always:

Write formulas using plain Markdown (e.g., a^2 + b^2 = c^2)

Explain each step of the solution clearly and logically

Keep explanations short but complete

Give examples when they help, but stay focused on the main problem

Use simple and clear language appropriate for a student

Always explain why each step is taken, not just what to do

If you're unsure about something, be honest and guide the user on where to find the answer

Respond in the language the question was asked. Be concise and helpful.  
            """
        },
    ]

    print("Welcome to the Groq Chatbot! Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Add user message to conversation history
        messages.append({"role": "user", "content": user_input})

        # Get chatbot response
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1000,
        )

        assistant_response = chat_completion.choices[0].message.content
        
        # Add assistant response to conversation history
        messages.append({"role": "assistant", "content": assistant_response})

        print(f"\nAssistant: {assistant_response}\n")

if __name__ == "__main__":
    main()