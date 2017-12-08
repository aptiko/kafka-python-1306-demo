FROM ubuntu:16.04

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install wget zookeeperd && \
    wget http://ftp.fau.de/apache/kafka/1.0.0/kafka_2.11-1.0.0.tgz && \
    tar xzf kafka_2.11-1.0.0.tgz && \
    mv kafka_2.11-1.0.0 /usr/local/kafka && \
    mkdir /var/log/kafka

COPY ./docker/kafkaserver/docker-entrypoint.sh /
COPY ./docker/kafkaserver/server.properties /tmp/

EXPOSE 9092

ENTRYPOINT ["/docker-entrypoint.sh"]
