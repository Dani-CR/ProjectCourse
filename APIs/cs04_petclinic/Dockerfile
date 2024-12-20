FROM openjdk:8-jdk-alpine

# Download the JaCoCo agent JAR file
ADD https://repo1.maven.org/maven2/org/jacoco/org.jacoco.agent/0.8.7/org.jacoco.agent-0.8.7-runtime.jar /jacoco-agent.jar

ADD /target/spring-petclinic-rest-2.2.5.jar spring-petclinic-rest-2.2.5.jar
ENTRYPOINT ["java", "-javaagent:/jacoco-agent.jar=output=tcpserver,address=*,port=6301", "-jar", "spring-petclinic-rest-2.2.5.jar"]




