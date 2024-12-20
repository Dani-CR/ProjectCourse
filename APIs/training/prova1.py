import coverage 

# Create a coverage object with the source option 
cov = coverage.Coverage(include=["prova1.py"]) 

# Start the coverage measurement 
cov.start() 

def my_function(): 
    print("Hello, world!") 

if __name__ == "__main__": 
    my_function() 

# Stop the coverage measurement 
cov.stop() 

# Save the coverage data 
cov.save() 

# Report the coverage 
#cov.report()
