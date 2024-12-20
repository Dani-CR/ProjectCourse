# output schemathesis run_2 for CS03
============================================ Schemathesis test session starts ============================================
Schema location: http://localhost:8080/v2/api-docs?group=live-streaming-api-v1.0
Base URL: http://localhost:8080/swagger-ui.html
Specification version: Swagger 2.0
Random seed: 299776469159666872716593043794152665847
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

Compressed report size: 47 KB
Report is saved to run_2.tar.gz

