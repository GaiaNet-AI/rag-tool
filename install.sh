#!/bin/bash

set -e

# target name
target=$(uname -m)

# path to the gaianet base directory
gaianet_base_dir="$HOME/gaianet"



check_curl() {
    curl --retry 3 --progress-bar -L "$1" -o "$2"

    if [ $? -ne 0 ]; then
        error "    * Failed to download $1"
        exit 1
    fi
}

check_curl https://github.com/YuanTony/chemistry-assistant/raw/main/rag-embeddings/create_embeddings.wasm create_embeddings.wasm 
check_curl https://github.com/0xP0/toqdrant/releases/latest/download/toqdrant.py toqdrant.py                                                                                                                   