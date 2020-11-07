### NLP Analysis ###

### How do I Reproduce the NLP & Sentiment Analysis?    ###
* The spark NLP analysis performed in this repository has the following dependencies
    - Spark 2.4.6
    - Stanford CoreNLP
        - https://stanfordnlp.github.io/CoreNLP/download.html
    - nltk
    - boto3
    - pandas
    - plotly
      
* Run the CoreNLP server
    - unzip the download, cd to the stanford-corenlp-x.x.x directory 
    -  java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
            -preload tokenize,ssplit,pos,lemma,ner,parse,depparse \
            -status_port 9000 -port 9000 -timeout 15000 &

* Load raw data, create spark dataframe & save dataframe to parquet 
    - Unzip the provided dataset into a 'data' folder in the root directory  
    - python3 create_dataframe_from_supplied_data.py 
    - dataframe can be loaded from parquet as demonstrated in the load_dataframe_from_parquet.py file. 
    
* Transform the data & save transformed dataframe to parquet
    - the dataframe_transformations.py script demonstrates how to use the spark.ml Pipeline & Transforms to perform feature engineering
    - python3 dataframe_transformations.py
        - creates column of identified language (using nltk stop words)
        - generates sentiment columns for subjects provided to the Transformer (for instance biden & trump)
        - parses the tweet users location string to assign tweet to a U.S state
* Generate the concatenated dataframe & save to parquet
    - python3 generate_joint_dataset.py
        
* Run the sample script demonstrating dependency parsing using the nltk CoreNLPDependencyParser 
    - python3 sentiment_analysis/nltk_sentimenet_analysis.py


### Combining the provided data & the data received from the API ###
This project makes use of disparate data sources.  A demonstration of how to join the datasets into a single dataframe can be found in the join_dataframe.py file


### Plot the sentiment analysis ### 
* python3 plot_sentiment_analysis.py  (be patient this might take a secon)


### Spark relies on Java 8 so if you have Java 11 set as your current java version you can switch between them as follows  ### 
* update-java-alternatives --list
* sudo update-java-alternatives --set /path_to_java_version