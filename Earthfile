VERSION 0.6
ARG TARGETARCH
FROM DOCKERFILE -f ./Dockerfile.dapper --build-arg=DAPPER_HOST_ARCH=${TARGETARCH} .

deps:
    COPY --dir go.mod go.sum vendor ./
    RUN go mod download
    RUN go mod vendor
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum
    SAVE ARTIFACT vendor AS LOCAL vendor

build:
    FROM +deps
    COPY --dir .git app integration package pkg proto scripts tracing vendor_proto \
        main.go ./
    RUN go get ./...
    RUN go mod vendor
    SAVE ARTIFACT vendor AS LOCAL vendor

    ARG GOARCH
    RUN GOARCH=${GOARCH} ./scripts/build

    SAVE ARTIFACT bin

docker-context:
    ARG TARGETARCH
    WORKDIR context
    COPY (+build/bin --GOARCH=${TARGETARCH}) ./bin/
    COPY --dir package .
    SAVE ARTIFACT .

docker:
    FROM DOCKERFILE --build-arg=ARCH=${TARGETARCH} -f +docker-context/context/package/Dockerfile +docker-context/context/*

docker-all:
    BUILD +docker --platform=linux/arm64 --platform=linux/amd64
    ENV USER=root
    SAVE IMAGE --push ghcr.io/jaysonsantos/longhorn-instance-manager:tracing
