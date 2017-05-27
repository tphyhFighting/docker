all:  go py

go:
	mkdir -p go
	protoc --go_out=plugins=grpc:go protos/*.proto

py:
	mkdir -p py
	python -m grpc_tools.protoc -I./protos --python_out=./py --grpc_python_out=. ./protos/youtube.proto

clean:
	rm -rf go py
