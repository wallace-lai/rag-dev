from hello_rag_embed import *

embedding_model="milkey/dmeta-embedding-zh:f16"
mainmodel="qwen:32b"

if __name__ == '__main__':
    while True:
        query = input("Enter your query: ")
        if query.lower == 'quit':
            break

        query_embeddings = ollama.embeddings(model=embedding_model, prompt=query)['embedding']
        results = collection.query(query_embeddings=query_embeddings, n_results=3)

        for result in results['documents'][0]:
            print('-' * 40)
            print(result)