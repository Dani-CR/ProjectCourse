#outpout for schemathesis run_1 for CS03
============================================ Schemathesis test session starts ============================================
Schema location: file:///home/daniela/Documents/Tests/CS03/schemathesis/../swagger-specification.json
Base URL: http://localhost:8080/swagger-ui.html
Specification version: Swagger 2.0
Random seed: 201893631717506139122824254070475770756
Workers: 1
Collected API operations: 5
Collected API links: 0
API probing: SUCCESS
Schema analysis: SKIP

POST /swagger-ui.html/api/v1.0/users/sign-up .                                                                      [ 20%]
GET /swagger-ui.html/api/v1.0/videos/download/{id} .                                                                [ 40%]
GET /swagger-ui.html/api/v1.0/videos/get/{id} .                                                                     [ 60%]
GET /swagger-ui.html/api/v1.0/videos/list .                                                                         [ 80%]
POST /swagger-ui.html/api/v1.0/videos/upload .                                                                      [100%]

======================================================== SUMMARY =========================================================

Performed checks:
    not_a_server_error                    401 / 401 passed          PASSED 

WARNING: All API responses have a 404 status code. Did you specify the proper API location?

Compressed report size: 53 KB
Report is saved to run_1.tar.gz


