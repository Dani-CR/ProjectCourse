#requirements
-install SAFRS: pip3 install safrs
-install flask-admin: pip3 install flask-admin

#run 
-for demo version go to: http://thomaxxl.pythonanywhere.com/
-for local version run: python3 examples/demo_pythonanywhere_com.py localhost 8080 
-for code coverage: coverage run examples/demo_pythonanywhere_com.py localhost 8080 --> //end application --> coverage report / coverage html

#notes:
-in the file demo_pythonanywhere_com.py remove, if present, the SAFRSRestAPI component that is useless and cause problems
-to visit the swagger page of the application go to localhost:8080
-in localhost:8080/api --> APIs exposed
-in localhost:8080/admin --> sql alchemy db status
