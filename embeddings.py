from langchain.embeddings import HuggingFaceEmbeddings

def get_embedding():
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return model