from pathlib import Path
from typing import List, Optional
import json
from pydantic import BaseModel, ValidationError

# Définition de la structure d'un document
class Document(BaseModel):
    id: int
    title: str
    tags: Optional[List[str]] = []
    published: Optional[bool] = False
    metadata: Optional[dict] = None

# Fonction pour charger et valider les documents JSON
def load_documents(file_path: str) -> List[Document]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"{file_path} not found")
    
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    
    documents: List[Document] = []
    for doc_data in data:
        try:
            documents.append(Document(**doc_data))
        except ValidationError as e:
            print(f"Validation error for document {doc_data.get('id')}: {e}")
    return documents

# Fonction pour afficher les documents
def display_documents(documents: List[Document]) -> None:
    for doc in documents:
        print(f"ID: {doc.id}")
        print(f"Title: {doc.title}")
        print(f"Tags: {', '.join(doc.tags) if doc.tags else 'No tags'}")
        print(f"Published: {doc.published}")
        if doc.metadata:
            for key, value in doc.metadata.items():
                print(f"{key.capitalize()}: {value}")
        print("-" * 30)

# Exemple d'utilisation
if __name__ == "__main__":
    docs = load_documents("data/documents.json")
    display_documents(docs)
