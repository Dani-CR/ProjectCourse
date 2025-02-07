# Project Course

This repository presents the actual applications used for the fuzzing project and the Tests runned on them.
One application (spring-hotel) is not in the repository since it has been forked from another github repo. To go to the application visit the [repo](https://github.com/Dani-CR/spring-hotel) in which there is the code to run it.
The other applications where originally downloaded from the github repo [api_case_studies](https://github.com/SeUniVr/api_case_studies), from which the names were kept, but then modified to run properly in this project; and from the github repo [EMB](https://github.com/WebFuzzing/EMB). Specifically, the CS02 was substancially modified due to problems in the orginal schema and structure and the pom.xml of ncs and scs were changed to fit the structure of this repository.

## Structure
6 API applications used:
- CS02 (airline) --> requires maven, docker compose, java 8;
- CS03 (streaming) --> requires gradlew 4.8.1, docker compose, java 8;
- CSO4 (petclinic) --> requires maven, docker compose, java 8;
- spring-hotel --> requires JDK 1.8, maven 3.X.
- ncs --> requires maven, java 8;
- scs --> requires maven,, java 8;

4 Fuzzing Tools:
- [Restler](https://github.com/microsoft/restler-fuzzer) (version which required python 3.8.1 and .NET 6) 
- [Evomaster](https://github.com/WebFuzzing/EvoMaster?tab=readme-ov-file) (V.3.2.0 - [jar](https://drive.google.com/drive/folders/1P2yMD6k1RsrYu-nGCAchroespuiLcEq6?usp=sharing))
- [Cats](https://endava.github.io/cats/docs/getting-started/installation/) (V.12.0.0 - [jar](https://drive.google.com/drive/folders/1P2yMD6k1RsrYu-nGCAchroespuiLcEq6?usp=sharing)) --> requires at least java 17
- [Schemathesis](https://schemathesis.readthedocs.io/en/stable/index.html) (V.3.36.2)

1 Code Coverage Tool:
- jacoco agent (present in each folder of the application eighter as .jar or inside dockerfile as download in the image)
- jacoco [cli](https://repo1.maven.org/maven2/org/jacoco/org.jacoco.cli/) (V.0.8.7 - [jar](https://drive.google.com/drive/folders/1P2yMD6k1RsrYu-nGCAchroespuiLcEq6?usp=sharing))

## Experiment
Each application has two runs for each fuzzer:
- Restler: 5minutes and 10minutes;
- Evomaster: 5minutes and 10minutes;
- Schemathesis: first and second run;
- Cats: first and second run.

Restler and Evomaster presented the option to run for a specific time frame and so they have been tested on 5 and 10 minutes period, instead the others did not present this option and has been run twice and annotated the execution period of time.
Each run has been executed individually, no fuzzer has been used in parallel with another one and neighter have the applications. Once a test was running it was the only one in action: one application with one fuzzer. Only when the test ended and the application stopped, another test could be executed.

Flow of execution for each test:
1. Start application; 
2. Start jacoco (to monitor code coverage);
3. Start fuzzer;
4. End fuzzer;
5. Collect jacoco report;
6. End application.

### Replicate experiment
Inside each folder of the APIs there are README.md files which have been used to understand how to run the applications, use it in case of doubts.

#### Start application
The following are the instructions to start each application alonside with jacoco for the code coverage:
- CS02: since it uses docker and a makefile, the start of jacoco agent has been inserted in the dockerfile and gives the output at localhost:6302. To start the application open a terminal inside the main folder with the Makefile, ensure you have sudo priviledge to run docker and make commands before moving foward, then execute the following commands:

      make build-source
      make build
      make start (to start in detached mode)
      make start-dev (to start and see the actions in terminal)
  
- CS03: since it uses docker and makefile, the start of jacoco agent has been inserted in the Dockerfile and gives the output at localhost:6300. To start the application follow the same commands of CS02.
- CS04: since it uses docker and makefile, the start of jacoco agent has been inserted in the Dockerfile and gives the output at localhost:6301. To start the application follow the same commands of CS02.
- spring-hotel: since it doesn't use docker the jacoco agent has been inserted into the command to start the application. Open terminal in the main folder and use the following commands to run the application:

      mvn clean package // to create the application jar
      java -javaagent:./jacoco_0_8_7_runtime.jar=destfile=./target/jacoco.exec,output=file -jar -Dspring.profiles.active=test target/spring-boot-rest-example-0.5.0.war

- ncs and scs: same as for spring-hotel

      mvn clean package
      java -javaagent:./jacoco_0_8_7_runtime.jar=destfile=./target/jacoco.exec,output=file -jar target/<file_sut.jar>
  
### Start fuzzer

- Restler
  - Compile the applicatio (a sub folder “Compile” will be created in the current path)

        <path_to_restler_bin/restler.exe> compile --api_spec <path_to_schema.json_or_.yaml>
      
  - Test/Fuzz-lean/Fuzz (a sub folder will be created “Test”/””/”” in the current path) [the time_budget is needed only for Fuzz mode, 0.084 = 5min and 0.167 = 10min)

        <path to restler_bin/restler.exe> test/fuzz-lean/fuzz --grammar_file <path_to_./Compile/grammar.py> --dictionary_file <path_to_./Compile/dict.json> --settings <path_to_./Compile/engine_settings.json> --no_ssl --time_budget 0.084
    
- Evomaster

      java -jar <path_to_evomaster.jar> --blackBox true --bbSwaggerUrl <path_to_swagger_schema_url> --outputFormat JAVA_JUNIT_4 --maxTime 5m --bbTargetUrl <url_API_http>
    
- Schemathesis

      st run <path_to_schema> -b <url_api_http> --report <path_to_save_report_into_your_choise>
    
- Cats

      java -jar <path_to_cats.jar> -c <path_to_schema> -s <url_api_http>
  
### Get jacoco report
 Instructions to get jacoco report:
 - for CS02, CS03, and CS04 that use docker the procedure is the same, move into the folder you want to create the report then run these commands:

       java -jar <abs_path_to_jacococli.jar> dump --address localhost --port <jacoco_agent_output_port> --destfile ./jacoco.exec
       java -jar <abs_path_to_jacococli.jar> report ./jacoco.exec  \
       --classfiles <abs_path_to_build_classes> \
       --sourcefiles <abs_path_to_src_classes> \
       --html <abs_path_to_folder_for_report> \
       --name "<Report_name>"

  Explanation:
   1) Create the jacoco.exe file fisrt, which has binary information saved about the execution.Insert the absolute path to the jacococli.jar downloaded in <abs_path_to_jacococli.jar>, for destfile then insert the path you want your file to be created into, for the port insert the one which jacoco agent is listening into (it'll be eighter 6300, 6301, or 6302);
   2) Insert the absolute path in which you have the build folder of the application, same for the source folder of the application, the –html and –name are up to you to chose: those are respectively the path where to insert the folder report and the name of that folder.

- for spring-hotel, ncs and scs: these applications have the generation of the report inside its maven cycle, so when the fuzzer finishes, to create th jacoco.exec the applications has just to stop and the file will be created inside the target folder of the application, the go indie that folder and run th following command to create the report (which will be saved in target/site folder):

      mvn jacoco:report
  
