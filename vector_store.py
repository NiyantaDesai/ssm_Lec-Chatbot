from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

class VectorStore:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.chunks = []

    def build_index(self, chunks):
        # Extract text content if chunks are Document objects
        self.chunks = [chunk.page_content if hasattr(chunk, 'page_content') else chunk for chunk in chunks]
        embeddings = self.embedder.encode(self.chunks, convert_to_numpy=True)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def save(self, path="vector_store.faiss"):
        # Save both the FAISS index and the chunks
        faiss.write_index(self.index, path)
        chunks_path = path + ".chunks"
        with open(chunks_path, 'wb') as f:
            pickle.dump(self.chunks, f)

    def load(self, path="vector_store.faiss"):
        # Load both the FAISS index and the chunks
        self.index = faiss.read_index(path)
        chunks_path = path + ".chunks"
        with open(chunks_path, 'rb') as f:
            self.chunks = pickle.load(f)

    def similarity_search(self, query, k=3):
        query_embedding = self.embedder.encode([query], convert_to_numpy=True)
        return self.index.search(query_embedding, k)

if __name__ == "__main__":
    from document_processor import load_and_split_document
    chunks = load_and_split_document("slec_document.md")
    store = VectorStore()
    store.build_index(chunks)
    store.save()
    print("Vector store created and saved.")