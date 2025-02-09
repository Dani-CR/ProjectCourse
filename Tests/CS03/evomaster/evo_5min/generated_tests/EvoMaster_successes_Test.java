import  org.junit.AfterClass;
import  org.junit.BeforeClass;
import  org.junit.Before;
import  org.junit.Test;
import static org.junit.Assert.*;
import  java.util.Map;
import  java.util.List;
import static org.evomaster.test.utils.EMTestUtils.*;
import  org.evomaster.client.java.controller.SutHandler;
import  io.restassured.RestAssured;
import static io.restassured.RestAssured.given;
import  io.restassured.response.ValidatableResponse;
import static org.hamcrest.Matchers.*;
import  io.restassured.config.JsonConfig;
import  io.restassured.path.json.config.JsonPathConfig;
import static io.restassured.config.RedirectConfig.redirectConfig;
import static org.evomaster.client.java.controller.contentMatchers.NumberMatcher.*;
import static org.evomaster.client.java.controller.contentMatchers.StringMatcher.*;
import static org.evomaster.client.java.controller.contentMatchers.SubStringMatcher.*;




/**
*  This file was automatically generated by EvoMaster on 2025-01-10T18:27:11.359232085+01:00[Europe/Rome]
 * <br>
*  The generated test suite contains 3 tests
 * <br>
*  Covered targets: 6
 * <br>
*  Used time: 0h 5m 0s
 * <br>
*  Needed budget for current results: 52%
 * <br>
*  This file contains test cases that represent successful calls.
*/
public class EvoMaster_successes_Test {

    
    private static String baseUrlOfSut = "http://localhost:8080";
    
    
    @BeforeClass
    public static void initClass() {
        RestAssured.enableLoggingOfRequestAndResponseIfValidationFails();
        RestAssured.useRelaxedHTTPSValidation();
        RestAssured.urlEncodingEnabled = false;
        RestAssured.config = RestAssured.config()
            .jsonConfig(JsonConfig.jsonConfig().numberReturnType(JsonPathConfig.NumberReturnType.DOUBLE))
            .redirect(redirectConfig().followRedirects(false));
    }
    
    
    
    
    
    
    
    
    @Test(timeout = 60000)
    public void test_0() throws Exception {
        
        given().accept("*/*")
                .get(baseUrlOfSut + "/api/v1.0/videos/get/6013767895428533925")
                .then()
                .statusCode(200)
                .assertThat()
                .body(isEmptyOrNullString());
    }
    
    
    @Test(timeout = 60000)
    public void test_1() throws Exception {
        
        given().accept("*/*")
                .get(baseUrlOfSut + "/api/v1.0/videos/list")
                .then()
                .statusCode(200)
                .assertThat()
                .contentType("application/json")
                .body("size()", equalTo(0));
    }
    
    
    @Test(timeout = 60000)
    public void test_2() throws Exception {
        
        given().accept("*/*")
                .contentType("application/json")
                .body(" { " + 
                    " \"created\": \"2010-04-04T15:26:32\", " + 
                    " \"password\": \"WlhLkyH1I\", " + 
                    " \"videos\": [ " + 
                    " { " + 
                    " \"modified\": \"1940-06-16T13:15:37\", " + 
                    " \"size\": 0.33173296746033565, " + 
                    " \"url\": \"LE2y\" " + 
                    " }, " + 
                    " { " + 
                    " \"id\": 520799066, " + 
                    " \"size\": 0.3152537559078098, " + 
                    " \"url\": \"hOHxTs\" " + 
                    " }, " + 
                    " { " + 
                    " \"created\": \"2011-06-18T04:44:57\", " + 
                    " \"modified\": \"2096-07-23T09:44:14\" " + 
                    " } " + 
                    " ] " + 
                    " } ")
                .post(baseUrlOfSut + "/api/v1.0/users/sign-up")
                .then()
                .statusCode(200)
                .assertThat()
                .body(isEmptyOrNullString());
    }


}
