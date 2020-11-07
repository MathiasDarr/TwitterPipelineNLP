### Hive Instructions ###

docker exec -it twitter_hive-server_1 bash
/opt/hive/bin/beeline -u jdbc:hive2://localhost:10000

List tables

CREATE TABLE transactions (id INT, amount DOUBLE, date1 STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ';';