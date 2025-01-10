# output Schemathesis for CS04 run_1
============================================ Schemathesis test session starts ============================================
Schema location: file:///home/daniela/Documents/Tests/CS04/schemathesis/../openapi_specification.json
Base URL: http://localhost:9966/petclinic
Specification version: Swagger 2.0
Random seed: 16360387357231023740645894961287152939
Workers: 1
Collected API operations: 47
Collected API links: 0
API probing: SUCCESS
Schema analysis: SKIP

GET /petclinic/ .                                                                                                   [  2%]
HEAD /petclinic/ .                                                                                                  [  4%]
POST /petclinic/ .                                                                                                  [  6%]
PUT /petclinic/ .                                                                                                   [  8%]
DELETE /petclinic/ .                                                                                                [ 10%]
OPTIONS /petclinic/ .                                                                                               [ 12%]
PATCH /petclinic/ .                                                                                                 [ 14%]
GET /petclinic/api/owners .                                                                                         [ 17%]
POST /petclinic/api/owners .                                                                                        [ 19%]
GET /petclinic/api/owners/*/lastname/{lastName} F                                                                   [ 21%]
GET /petclinic/api/owners/{ownerId} .                                                                               [ 23%]
PUT /petclinic/api/owners/{ownerId} .                                                                               [ 25%]
DELETE /petclinic/api/owners/{ownerId} .                                                                            [ 27%]
GET /petclinic/api/pets .                                                                                           [ 29%]
POST /petclinic/api/pets .                                                                                          [ 31%]
GET /petclinic/api/pets/pettypes .                                                                                  [ 34%]
GET /petclinic/api/pets/{petId} .                                                                                   [ 36%]
PUT /petclinic/api/pets/{petId} .                                                                                   [ 38%]
DELETE /petclinic/api/pets/{petId} .                                                                                [ 40%]
GET /petclinic/api/pettypes .                                                                                       [ 42%]
POST /petclinic/api/pettypes .                                                                                      [ 44%]
GET /petclinic/api/pettypes/{petTypeId} .                                                                           [ 46%]
PUT /petclinic/api/pettypes/{petTypeId} .                                                                           [ 48%]
DELETE /petclinic/api/pettypes/{petTypeId} .                                                                        [ 51%]
GET /petclinic/api/specialties .                                                                                    [ 53%]
POST /petclinic/api/specialties .                                                                                   [ 55%]
GET /petclinic/api/specialties/{specialtyId} .                                                                      [ 57%]
PUT /petclinic/api/specialties/{specialtyId} .                                                                      [ 59%]
DELETE /petclinic/api/specialties/{specialtyId} .                                                                   [ 61%]
POST /petclinic/api/users .                                                                                         [ 63%]
GET /petclinic/api/vets .                                                                                           [ 65%]
POST /petclinic/api/vets .                                                                                          [ 68%]
GET /petclinic/api/vets/{vetId} .                                                                                   [ 70%]
PUT /petclinic/api/vets/{vetId} .                                                                                   [ 72%]
DELETE /petclinic/api/vets/{vetId} .                                                                                [ 74%]
GET /petclinic/api/visits .                                                                                         [ 76%]
POST /petclinic/api/visits .                                                                                        [ 78%]
GET /petclinic/api/visits/{visitId} .                                                                               [ 80%]
PUT /petclinic/api/visits/{visitId} .                                                                               [ 82%]
DELETE /petclinic/api/visits/{visitId} .                                                                            [ 85%]
GET /petclinic/error F                                                                                              [ 87%]
HEAD /petclinic/error F                                                                                             [ 89%]
POST /petclinic/error F                                                                                             [ 91%]
PUT /petclinic/error F                                                                                              [ 93%]
DELETE /petclinic/error F                                                                                           [ 95%]
OPTIONS /petclinic/error .                                                                                          [ 97%]
PATCH /petclinic/error F                                                                                            [100%]

======================================================== FAILURES ========================================================
____________________________________ GET /petclinic/api/owners/*/lastname/{lastName} _____________________________________
1. Test Case ID: ezBS2p

- Server error

[500] Internal Server Error:

    `{"timestamp":"2024-12-05T10:28:04.120+0000","status":500,"error":"Internal Server Error","message":"The request was rejected because the URL contained a potentially malicious String \"%3B\"","path":"/petclinic/api/owners/*/lastname/%3B"}`

Reproduce with: 

    curl -X GET 'http://localhost:9966/petclinic/api/owners/*/lastname/%3B'

__________________________________________________ GET /petclinic/error __________________________________________________
1. Test Case ID: 2vxtH6

- Server error

[500] Internal Server Error:

    `{"timestamp":"2024-12-05T10:29:08.905+0000","status":999,"error":"None","message":"No message available"}`

Reproduce with: 

    curl -X GET http://localhost:9966/petclinic/error

_________________________________________________ HEAD /petclinic/error __________________________________________________
1. Test Case ID: lgiUBa

- Server error

[500] Internal Server Error:

Reproduce with: 

    curl -X HEAD http://localhost:9966/petclinic/error

_________________________________________________ POST /petclinic/error __________________________________________________
1. Test Case ID: 1BNGuN

- Server error

[500] Internal Server Error:

    `{"timestamp":"2024-12-05T10:29:09.038+0000","status":999,"error":"None","message":"No message available"}`

Reproduce with: 

    curl -X POST http://localhost:9966/petclinic/error

__________________________________________________ PUT /petclinic/error __________________________________________________
1. Test Case ID: 8xLTiL

- Server error

[500] Internal Server Error:

    `{"timestamp":"2024-12-05T10:29:09.090+0000","status":999,"error":"None","message":"No message available"}`

Reproduce with: 

    curl -X PUT http://localhost:9966/petclinic/error

________________________________________________ DELETE /petclinic/error _________________________________________________
1. Test Case ID: v6nUFq

- Server error

[500] Internal Server Error:

    `{"timestamp":"2024-12-05T10:29:09.447+0000","status":999,"error":"None","message":"No message available"}`

Reproduce with: 

    curl -X DELETE http://localhost:9966/petclinic/error

_________________________________________________ PATCH /petclinic/error _________________________________________________
1. Test Case ID: VRGOPc

- Server error

[500] Internal Server Error:

    `{"timestamp":"2024-12-05T10:29:09.518+0000","status":999,"error":"None","message":"No message available"}`

Reproduce with: 

    curl -X PATCH http://localhost:9966/petclinic/error

======================================================== SUMMARY =========================================================

Performed checks:
    not_a_server_error                    2627 / 2654 passed          FAILED 

Note: Use the 'X-Schemathesis-TestCaseId' header to correlate test case ids from failure messages with server logs for debugging.

Note: To replicate these test failures, rerun with `--hypothesis-seed=16360387357231023740645894961287152939`

Compressed report size: 290 KB
Report is saved to run_1.tar.gz

============================================= 40 passed, 7 failed in 77.58s ==============================================
