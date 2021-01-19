#!/bin/bash

docker exec -it kafka bin/kafka-console-consumer.sh --topic trump --from-beginning --property print.key=true --bootstrap-server kafka:9092