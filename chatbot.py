from retriever import Retriever
from llm_integration import LLMIntegration
# from main import main

class Chatbot:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMIntegration()

    def chat(self, query):
        retrieved_chunks = self.retriever.retrieve(query)
        response = self.llm.generate_response(query, retrieved_chunks)
        return response

    def run(self):
        print("Welcome to the SSM Learning Excellence Centre Chatbot!")
        print("Type 'exit' to quit.")
        while True:
            query = input("You: ")
            if query.lower() == "exit":
                print("Goodbye!")
                break
            response = self.chat(query)
            print(f"Bot: {response}\n")

if __name__ == "__main__":
    bot = Chatbot()
    bot.run()