FROM openjdk:8-jdk-alpine

# Download the JaCoCo agent JAR file
ADD https://repo1.maven.org/maven2/org/jacoco/org.jacoco.agent/0.8.7/org.jacoco.agent-0.8.7-runtime.jar /jacoco-agent.jar

ADD /target/airline-ticket.jar airline-ticket.jar
ENTRYPOINT ["java","-javaagent:/jacoco-agent.jar=output=tcpserver,address=*,port=6302","-jar","airline-ticket.jar"]
