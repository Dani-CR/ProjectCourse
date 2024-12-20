import subprocess
import os

# List of commands to be executed sequentially
commands = [
    "cd /home/daniela/Documents/Tests/PetStore/evomaster/try1_30min",  # Change directory to Fuzz1_30min
    "java -jar /home/daniela/Documents/Evomaster_folder/evomaster.jar --blackBox true --bbSwaggerUrl file:///home/daniela/Documents/Tests/PetStore/openapi.yaml --outputFormat JAVA_JUNIT_4 --maxTime 30m --bbTargetUrl http://localhost:8080/",  # Fuzz with 30-minute time budget
    "cd /home/daniela/Documents/Tests/PetStore/evomaster/try1_1hr",  # Change directory to Fuzz1_1hr
    "java -jar /home/daniela/Documents/Evomaster_folder/evomaster.jar --blackBox true --bbSwaggerUrl file:///home/daniela/Documents/Tests/PetStore/openapi.yaml --outputFormat JAVA_JUNIT_4 --maxTime 60m --bbTargetUrl http://localhost:8080/",  # Fuzz with 1-hour time budget
    "cd /home/daniela/Documents/Tests/PetStore/evomaster/try2_30min",  # Change directory to Fuzz2_30min
    "java -jar /home/daniela/Documents/Evomaster_folder/evomaster.jar --blackBox true --bbSwaggerUrl file:///home/daniela/Documents/Tests/PetStore/openapi.yaml --outputFormat JAVA_JUNIT_4 --maxTime 30m --bbTargetUrl http://localhost:8080/",  # Fuzz with 30-minute time budget
    "cd /home/daniela/Documents/Tests/PetStore/evomaster/try2_1hr",  # Change directory to Fuzz2_1hr
    "java -jar /home/daniela/Documents/Evomaster_folder/evomaster.jar --blackBox true --bbSwaggerUrl file:///home/daniela/Documents/Tests/PetStore/openapi.yaml --outputFormat JAVA_JUNIT_4 --maxTime 60m --bbTargetUrl http://localhost:8080/"  # Fuzz with 1-hour time budget
]

# Variable to hold the last directory from a 'cd' command
last_directory = None

# Run the commands sequentially
for i, command in enumerate(commands):
    try:
        print(f"Running: {command}")
        
        # If it's a 'cd' command, handle it separately and store the directory
        if command.startswith("cd "):
            last_directory = command.split("cd ")[1]  # Extract directory from the 'cd' command
            subprocess.run(f"cd {last_directory}", shell=True, check=True)
            print(f"Changed directory to: {last_directory}")
        
        else:
            # For 'fuzz' commands, run them inside the directory set by the last 'cd' command
            if last_directory:
                # Run the 'fuzz' command in the directory where it is supposed to save files
                result = subprocess.run(command, cwd=last_directory, shell=True, check=True)
                print(f"Command executed successfully in {last_directory}")
            else:
                print("Error: No previous 'cd' command to set the directory!")
                break  # Stop if there is no directory set by a 'cd' command

    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code: {e.returncode}")
        break  # Stop execution if any command fails

