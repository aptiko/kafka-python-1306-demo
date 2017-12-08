#!/bin/bash
service zookeeper start
exec /usr/local/kafka/bin/kafka-server-start.sh /tmp/server.properties
