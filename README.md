# Create Embeddings with Ease

This RAG tool simplifies the process of creating embeddings. Ensure that your Gaia node is running on the same machine before proceeding. The snapshot generated by this RAG tool will seamlessly replace the current snapshot on your node.

## Prerequisites

Follow the [Quick Start](https://docs.gaianet.ai/node-guide/quick-start) guide to set up and run your Gaia node. Before you proceed, please check the following items:

1. **Ensure your Qdrant instance is running.**

   Run the following command:

   ```bash
   curl http://localhost:6333
   ```
   The expected terminal response should be:
   ```
   {"title":"qdrant - vector search engine","version":"1.10.1","commit":"4aac02315bb3ca461a29484094cf6d19025fce99"}%
   ```
2. **Ensure your Gaia node is running correctly.**
    You can send an API request to test your node:
    ```
    curl -X POST http://localhost:8080/v1/chat/completions \
     -H 'accept: application/json' \ 
     -H 'Content-Type: application/json' \ 
     -D '{"messages":[{"role":"system", "content": "You are a helpful assistant."}, {"role":"user", "content": "Where is Paris?"}]}'
    ```
3. Ensure you have chunked text ready.


## Creating Embeddings Using the Tool

Once your Gaia node is running smoothly, you can update the snapshot without stopping the node.

```
# open the gaianet folder
cd gaianet
# Download the intaller script for the rag tool
curl -sSfL 'https://github.com/0xP0/toqdrant/releases/releases/latest/download/install.sh' | bash

```

Next, we wil use the following command line to create embeddings, and generate, replace the snapshot.


```
pyhton3 toqdrant.py file_name.txt
```

Be sure to replace `file_name.txt` with the actual name of your text file.

Once the process is complete, test your node by asking it a question to verify that the snapshot has been successfully updated.
