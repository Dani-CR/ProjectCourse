""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /api/ticket, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ticket"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/ticket"
)
req_collection.add_request(request)

# Endpoint: /api/ticket, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ticket"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "ticketCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "flight":
        {
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "departureDateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "arrivalDateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "duration":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "quota":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "quotaFilled":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "quotaFilledPercentage":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "route":
                {
                    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "departureAirport":
                        {
                            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "capacity":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "arrivalAirport":
                        {
                            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "capacity":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "plane":
                {
                    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "numberOfSeats":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "company":
                        {
                            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
        }
    ,
    "price":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "isSold":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/ticket"
)
req_collection.add_request(request)

# Endpoint: /api/ticket, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ticket"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "ticketCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "price":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "isSold":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "flightId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/ticket"
)
req_collection.add_request(request)

# Endpoint: /api/route, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("route"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/route"
)
req_collection.add_request(request)

# Endpoint: /api/route, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("route"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "departureAirport":
        {
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "capacity":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "arrivalAirport":
        {
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "capacity":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/route"
)
req_collection.add_request(request)

# Endpoint: /api/route, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("route"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "departureAirportId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "arrivalAirportId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/route"
)
req_collection.add_request(request)

# Endpoint: /api/plane, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plane"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/plane"
)
req_collection.add_request(request)

# Endpoint: /api/plane, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plane"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "numberOfSeats":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "company":
        {
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/plane"
)
req_collection.add_request(request)

# Endpoint: /api/plane, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plane"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Boeing 747"]),
    primitives.restler_static_string(""",
    "numberOfSeats":"""),
    primitives.restler_fuzzable_int("1", examples=["300"]),
    primitives.restler_static_string(""",
    "companyId":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/plane"
)
req_collection.add_request(request)

# Endpoint: /api/flight, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("flight"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/flight"
)
req_collection.add_request(request)

# Endpoint: /api/flight, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("flight"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "departureDateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "arrivalDateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "duration":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "quota":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "quotaFilled":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "quotaFilledPercentage":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "route":
        {
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "departureAirport":
                {
                    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "capacity":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "arrivalAirport":
                {
                    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "capacity":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "plane":
        {
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "numberOfSeats":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "company":
                {
                    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/flight"
)
req_collection.add_request(request)

# Endpoint: /api/flight, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("flight"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "departureDateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "arrivalDateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "duration":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "quota":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "planeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "routeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/flight"
)
req_collection.add_request(request)

# Endpoint: /api/company, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("company"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/company"
)
req_collection.add_request(request)

# Endpoint: /api/company, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("company"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/company"
)
req_collection.add_request(request)

# Endpoint: /api/company, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("company"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/company"
)
req_collection.add_request(request)

# Endpoint: /api/airport, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("airport"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/airport"
)
req_collection.add_request(request)

# Endpoint: /api/airport, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("airport"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "capacity":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/airport"
)
req_collection.add_request(request)

# Endpoint: /api/airport, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("airport"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "capacity":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/airport"
)
req_collection.add_request(request)

# Endpoint: /api/ticket/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ticket"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/ticket/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/ticket/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ticket"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/ticket/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/route/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("route"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/route/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/route/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("route"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/route/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/plane/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plane"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/plane/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/plane/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plane"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/plane/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/flight/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("flight"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/flight/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/flight/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("flight"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/flight/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/company/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("company"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/company/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/company/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("company"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/company/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/airport/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("airport"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/airport/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/airport/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("airport"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/airport/{id}"
)
req_collection.add_request(request)
