from vector_store import VectorStore
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, vector_store_path="vector_store.faiss"):
        self.vector_store = VectorStore()
        self.vector_store.load(vector_store_path)
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')

    def retrieve(self, query, top_k=3):
        query_embedding = self.embedder.encode([query], convert_to_numpy=True)
        distances, indices = self.vector_store.index.search(query_embedding, top_k)
        retrieved_chunks = [self.vector_store.chunks[idx] for idx in indices[0]]
        return retrieved_chunks

if __name__ == "__main__":
    retriever = Retriever()
    results = retriever.retrieve("What courses does SSM offer?")
    for i, chunk in enumerate(results):
        print(f"Result {i+1}: {chunk}\n")