from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class LLMIntegration:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"  # gpt-3.5-turbo, llama-3.1-latest

    def generate_response(self, query, retrieved_chunks):
        context = "\n\n".join(retrieved_chunks)
        prompt = f"""
        - You are a helpful chatbot for SSM Learning Excellence Centre. Using the following context, answer the user's query clearly and concisely. If the context doesn't fully answer, provide a general response based on your knowledge.
        - If the user's query is not related to the context, respond with "I'm sorry, I don't have an answer for that."
        - If the user's query is related to the context, provide a detailed response.
        - If the user's query is a greeting, respond with a friendly greeting.
        - If the user's query is a farewell, respond with a friendly farewell.
        - If the user's query is a question, respond with a detailed answer.
        - If the user ask the question, then revise the question and provide the best answer that can help the user and match the maximum keywords from the markdown file and provide the most accureate answer.
    

        Context:
        {context}

        Query: {query}
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant for SSM LEC."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

if __name__ == "__main__":
    llm = LLMIntegration()
    chunks = ["SSM offers courses like AVEVA InTouch HMI and .NET programming."]
    response = llm.generate_response("What courses does SSM offer?", chunks)
    print(response)