from vector_db import create_db

pdf_path = "upload_docs/UNIT.pdf"

create_db(pdf_path)

print("DB created")