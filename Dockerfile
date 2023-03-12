FROM alpine:3.17.2

RUN apk add --no-cache mysql-client
ENTRYPOINT ["mysql"]
