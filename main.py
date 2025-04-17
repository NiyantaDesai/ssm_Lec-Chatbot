from document_processor import load_and_split_document
from vector_store import VectorStore
from chatbot import Chatbot

def setup():
    # Load and process document
    chunks = load_and_split_document("slec_document.md")
    
    # Build vector store (run this once, then comment out after saving)
    vector_store = VectorStore()
    vector_store.build_index(chunks)
    vector_store.save()
    print("Setup complete. Vector store saved.")

def main():
    setup()
    chatbot = Chatbot()
    chatbot.run()

if __name__ == "__main__":
    main()