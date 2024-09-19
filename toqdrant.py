#!/usr/bin/env python
import os
import sys

# python3 -m pip install requests
#  or
# python3 -m pip install requests
import requests

# QDRANT
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = os.getenv("QDRANT_PORT", 6333)


def deleteVectorDB(DBName):
    __url = f"http://{QDRANT_HOST}:{QDRANT_PORT}/collections/{DBName}"
    response = requests.delete(__url)
    print(response.text)
    return response.text


def checkVectorDB(DBName):
    __url = f"http://{QDRANT_HOST}:{QDRANT_PORT}/collections/{DBName}"
    response = requests.get(__url)
    rsJson = response.json()
    result = rsJson.get("result", {})
    vectors_count = result.get("vectors_count", 0)
    return vectors_count


def createVectorDB(DBName, size=384, distance="Cosine"):
    __url = f"http://{QDRANT_HOST}:{QDRANT_PORT}/collections/{DBName}"
    __headers = {"Content-Type": "application/json"}
    __data = {"vectors": {"size": size, "distance": distance, "on_disk": True}}
    response = requests.put(__url, headers=__headers, json=__data)
    print(response.text)
    return response.text


# Create Embeddings
def createEmbeddings(DBName, model_name, size, filepath):
    command = f"wasmedge --dir .:. --nn-preload default:GGML:AUTO:{model_name} create_embeddings.wasm default {DBName} {size} {filepath} "
    print(command)
    os.system(command)


def text2qdrant(filepath, db_name="default"):
    # Delete DB
    deleteVectorDB(db_name)
    # Create Vector Database
    createVectorDB(db_name, 768, "Cosine")
    # Create Embeddings
    createEmbeddings(db_name, "nomic-embed-text-v1.5.f16.gguf", 768, filepath)

    checkVectorDB(db_name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python toqdrant.py filepath")
        sys.exit(1)
    text2qdrant(sys.argv[1])
