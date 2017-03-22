all: js java go

js:
	mkdir -p js
	protoc --js_out=library=apkpure_proto_libs,binary:js protos/*.proto

java:
	mkdir -p java
	protoc --javanano_out=java protos/*.proto

go:
	mkdir -p go
	protoc --go_out=go protos/*.proto

clean:
	rm -rf java js go
