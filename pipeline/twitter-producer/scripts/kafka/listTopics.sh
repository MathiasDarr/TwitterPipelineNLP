#!/bin/bash
docker exec kafka bin/kafka-topics.sh --list --bootstrap-server kafka:9092
