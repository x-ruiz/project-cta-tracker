# project-cta-tracker

## Set Up
### Kafka
https://developer.confluent.io/get-started/python/#introduction

### Flink
https://nightlies.apache.org/flink/flink-docs-release-1.9/getting-started/tutorials/local_setup.html

mvn archetype:generate -DgroupId=com.xavierruiz.app -DartifactId=flink-consumer -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.5 -DinteractiveMode=false

mvn clean package -DskipTests

make sure to build a fat jar for flink which includes all dependencies

flink run target/flink-consumer-1.0-SNAPSHOT.jar 9000