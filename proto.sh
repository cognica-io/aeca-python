#!/bin/bash

SRC=src/aeca/protobuf
FILES=(document_db.proto key_value_db.proto fts_analysis_pipeline.proto sentence_transformer.proto)

python -m grpc_tools.protoc -I $SRC --python_out=$SRC $SRC/document.proto

for file in "${FILES[@]}"; do
    python -m grpc_tools.protoc -I $SRC --python_out=$SRC --grpc_python_out=$SRC $SRC/$file
done
