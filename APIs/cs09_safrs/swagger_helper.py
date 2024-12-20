import json

# Load the Swagger JSON file
with open("swagger.json", "r") as file:
    swagger_data = json.load(file)

# Function to remove "default" fields from parameters
def remove_defaults_from_parameters(paths):
    for path, methods in paths.items():
        for method, details in methods.items():
            if "parameters" in details:
                for parameter in details["parameters"]:
                    if "default" in parameter:
                        del parameter["default"]

# Remove "default" from all parameters in the Swagger JSON
remove_defaults_from_parameters(swagger_data["paths"])

# Save the modified Swagger JSON back to a file
with open("modified_swagger.json", "w") as file:
    json.dump(swagger_data, file, indent=4)

print("Default values removed and saved to 'modified_swagger.json'")

