## Twitter Streaming ETL Pipeline  ##

* Data Pipeline
    - Multithreaded java application that pushes twitter data into several destinations
        - Use the twitter4j library to stream tweets (requires twitter API keys)
            - http://twitter4j.org/en/
        - pushes data into 
            - individual kafka topics for each keyword provided at run time (uses avro serialization)
            - individual elasticsearch indices for each each keyword provided at run time
    
    - Airflow DAG
        - Use apache airflow to schedule workflows
        - Every hour
            - query the elastic-search indices & save data to S3 as parquet files.
            - delete data from the index (save disk space) 
        
    - Kafka connect connectors
        - elasticsearch sink connectors to move data directly into elasticsearch from kafka (these aren't currently working and I'm not sure what changed?) 
    - TODO     
        - The kafka connect elasticsearch sink isn't working properly, this would be preferable than pushing to ES directly from the twitter-producer java application (there
    are parsing errors at the moment due to unescaped protected characters resulting in not all of the data reaching elastic search.) 
elastic searh###


### Running the twitter streaming pipeline  ### 
* The data pipeline has the following dependencies
    - docker
        - https://docs.docker.com/get-docker/
    - docker-compose
        - https://docs.docker.com/compose/install/
    - maven (If you want to compile the java code)
        - https://maven.apache.org/install.html 
    - airflow
        - pip install apache-airflow
    - python elasticsearch client
    - boto3
        - pip install boto3
        - ensure aws credentials are correct.
        - Create a  
    - twitter API key
        - the twitter4j library requires a twitter API key
        - Set these environment variables on your computer.  The java application make use of these when configuring the client.  
            - export TWITTER_CONSUMER_KEY="your consumer key"
            - export TWITTER_CONSUMER_SECRET="your consumer secret"
            - export TWITTER_ACCESS_TOKEN="your access token"
            - export TWITTER_ACCESS_TOKEN_SECRET="your access token secret"


* Start zookeeper, schema registry,  kafka broker & elastic search
    - cd twitter-producer
    - docker-compose up --build
    
* Run the java application 
    - mvn clean package (compile with maven)
    - java -jar twitter-producer/target/twitter-producer-1.0-SNAPSHOT.jar http://localhost:9092 http://localhost:8081 localhost 29200 trump biden

* View the tweets coming into kafka
    - bash scripts/kafka/avro-consumer.sh trump
    - bash scripts/kafka/avro-consumer.sh biden
    
* View the tweets in elasticsearch
    - bash scripts/elasticsearch/queryES.sh trump
    - bash scripts/elasticsearch/queryES.sh biden
    
* Run the airflow DAG
    - airflow initdb (only required the first time )
    - run the airflow webserver 
        - airflow webserver -p 8080
    - run the airflow scheduler
        airflow scheduler
    - create an S3 bucket & edit the BUCKET variable at the top of dags/tweets_dag.py to the bucket just created
    - copy the airflow dag into the default airflow DAGs folder
        cp dags/tweets_dag.py $HOME/airflow/dags/tweets_dag.py (Copy the DAG file into the airflow DAGs folder)
    - the dag be triggered  from the airflow web client, however I am certain there is a method of doing this from the CLI.
    
* TODO
    - modify the script to allow a caller to pass a sentence or tweet lengthed input text to the script instead of the hardcoded text 
    







