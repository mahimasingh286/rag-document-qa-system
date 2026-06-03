
from langchain.vectorstores import Chroma
from embeddings import get_embedding
from load_docs import load_pdf


def create_db(pdf_path):

    docs = load_pdf(pdf_path)

    embedding = get_embedding()

    db = Chroma.from_documents(
        docs,
        embedding,
        persist_directory="data"
    )

    db.persist()

    return db