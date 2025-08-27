import ollama
import chromadb

from hello_rag_load import *
from hello_rag_split import *

EMBEDDING_MODEL = get_config()["embedding_model"]
COLLECTION_NAME = "ragdb"
DOCUMENT_NAME = "docs.txt"

chroma = chromadb.HttpClient(host="localhost", port=8000)
chroma.delete_collection(name=COLLECTION_NAME)
collection = chroma.get_or_create_collection(name=COLLECTION_NAME)

def embedding_and_save():
    with open(DOCUMENT_NAME) as f:
        lines = f.readlines()
        for filename in lines:
            # 加载文档内容
            text = load_text(filename)

            # 将文档分割成知识块
            chunks = split_text_by_sentences(text=text, sentences_per_chunk=8, overlap=0)

            # 依次对知识块进行处理
            for index, chunk in enumerate(chunks):
                embed = ollama.embeddings(model=EMBEDDING_MODEL, prompt=chunk)['embedding']
                collection.add(
                    [filename+str(index)],
                    [embed],
                    documents=[chunk],
                    metadatas={'source':filename}
                )