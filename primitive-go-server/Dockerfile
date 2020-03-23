FROM golang:alpine AS build-env
ADD . /work
WORKDIR /work
RUN CGO_ENABLED=0 go build -o hello main.go

FROM busybox
COPY --from=build-env /work/hello /usr/local/bin/hello
ENTRYPOINT ["/usr/local/bin/hello"]