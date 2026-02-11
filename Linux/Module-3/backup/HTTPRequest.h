//
// HTTPRequest.h 
//

#ifndef HTTPRequest_h
#define HTTPRequest_h

enum HTTPMethods{
  GET,
  POST,
  PUT,
  HEAD,
  PATCH,
  DELETE,
  CONNECT,
  OPTIONS,
  TRACE
};

// requests return the http method
struct HTTPRequest{
  int Method;
  char *URI;
  float HTTPVersion;
};

struct HTTPRequest http_request_constructor(char *request_string);

#endif // !HTTPRequest_h

// HTTP Header example
/* 
POST /api/login HTTP/1.1\r\n
Host: api.example.com\r\n
Content-Type: application/json\r\n
Content-Length: 56\r\n
User-Agent: MyApp/1.0.0\r\n
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\r\n
Accept: application/json\r\n
Accept-Charset: utf-8\r\n
Accept-Encoding: gzip, deflate\r\n
Connection: keep-alive\r\n
Origin: https://www.example.com\r\n
Referer: https://www.example.com/login\r\n
Cache-Control: no-cache\r\n
X-Requested-With: XMLHttpRequest\r\n
X-API-Key: abc123def456\r\n
\r\n
{"username": "john_doe", "password": "secret123"} 
*/
