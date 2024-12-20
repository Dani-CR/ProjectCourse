#FROM openjdk:8-jdk-alpine
#VOLUME /tmp
#ADD build/libs/live-streaming.jar app.jar
#ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

#Start new version
# Use the OpenJDK 8 base image
FROM openjdk:8-jdk-alpine

# Create a directory for JaCoCo agent
RUN mkdir /jacoco

# Download the JaCoCo agent JAR file
ADD https://repo1.maven.org/maven2/org/jacoco/org.jacoco.agent/0.8.7/org.jacoco.agent-0.8.7-runtime.jar /jacoco/jacoco-agent.jar

VOLUME /tmp

# Add your application JAR
ADD build/libs/live-streaming.jar app.jar

# Run the application with JaCoCo agent in TCP server mode
ENTRYPOINT ["java", "-javaagent:/jacoco/jacoco-agent.jar=output=tcpserver,address=*,port=6300", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app.jar"]
