# SCS application

## Run
Run the application without jacoco agent:

        mvn clean package
        mvn spring-boot:run
        
Run with jacoco:
        
        mvn clean package
        java -javaagent:./jacoco_0_8_7_runtime.jar=destfile=./target/jacoco.exec,output=file -jar target/rest-scs-sut.jar
        
To see the APIs go to http://localhost:8080/swagger-ui.html
