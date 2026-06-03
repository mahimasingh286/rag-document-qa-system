from langchain.vectorstores import Chroma
from embeddings import get_embedding
from transformers import pipeline


pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)


def ask_question(q):

    db = Chroma(
        persist_directory="data",
        embedding_function=get_embedding()
    )

    docs = db.similarity_search(q, k=2)

    context = ""

    for d in docs:
        context += d.page_content + " "

    prompt = (
        "Answer from context.\n"
        f"Context: {context}\n"
        f"Question: {q}\n"
        "Answer:"
    )

    result = pipe(prompt, max_new_tokens=60)[0]["generated_text"]

    answer = result.replace(prompt, "")

    return answer.strip()