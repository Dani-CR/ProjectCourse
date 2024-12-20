""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /api/books, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("books"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("bibkeys="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ISBN:0201558025"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("jscmd="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/books"
)
req_collection.add_request(request)

# Endpoint: /api/volumes/brief/{key_type}/{value}.json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("volumes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("brief"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(".json"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/volumes/brief/{key_type}/{value}.json"
)
req_collection.add_request(request)

# Endpoint: /authors/{olid}.json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authors"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(".json"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/authors/{olid}.json"
)
req_collection.add_request(request)

# Endpoint: /authors/{olid}/works.json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authors"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("works.json"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/authors/{olid}/works.json"
)
req_collection.add_request(request)

# Endpoint: /books/{olid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("books"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["OL53924W"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/books/{olid}"
)
req_collection.add_request(request)

# Endpoint: /covers/{key_type}/{value}-{size}.jpg, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("covers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("-"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(".jpg"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/covers/{key_type}/{value}-{size}.jpg"
)
req_collection.add_request(request)

# Endpoint: /isbn/{isbn}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("isbn"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/isbn/{isbn}"
)
req_collection.add_request(request)

# Endpoint: /search.json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search.json"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/search.json"
)
req_collection.add_request(request)

# Endpoint: /search/authors.json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authors.json"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/search/authors.json"
)
req_collection.add_request(request)

# Endpoint: /subjects/{subject}.json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subjects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(".json"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("details="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subjects/{subject}.json"
)
req_collection.add_request(request)

# Endpoint: /works/{olid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("works"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/works/{olid}"
)
req_collection.add_request(request)
