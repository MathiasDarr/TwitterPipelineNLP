# Twitter 2020 election & virus data pipeline & analysis  #

### This repository contains a data pipeline & analysis of twitter data pertaining to the 2020 presidential election and the coronavirus.

### This Repository Contains ###
* [Data Pipeline](pipeline/README.md)
    * Java application pushes tweets data to elastisearch & kafka topics
    * Data pipeline uses to airflow to schedule workflow that quer
* [Spark ML NLP Analys](analysis/README.md)
    * Perform NLP analysis on tweets
* [Elasticsearch query API](twitter-query-service/README.md)  
    * Spring Boot API for querying tweets in elasticsearch
        - makes use of the Java highlevel elasticsearch client
  