# -*- coding: utf-8 -*-
# Dictionary of status codes
# for use
# call the function ' print_info(status_code) '
# pass the numeric status code to the function
# the function will print information about the status code to the terminal
# import requests_info_status_code
# requests_info_status_code.print_info(status_code)

dict_status_code = {
# Information responses
                    100: '100 Continue\n\
This interim response indicates that everything so far is OK\n\
and that the client should continue the request,\n\
or ignore the response if the request is already finished.\n',

                    101:'101 Switching Protocol\n\
This code is sent in response to an Upgrade request header from the client,\n\
and indicates the protocol the server is switching to.\n',

                    102: '102 Processing (WebDAV)\n\
This code indicates that the server has received and is processing the request,\n\
but no response is available yet.\n',

                    103: '103 Early Hints\n\
This status code is primarily intended to be used with the Link header,\n\
letting the user agent start preloading resources while the server prepares a response.\n',

# Successful responses
                    200: '200 OK\n\
The request has succeeded. The meaning of the success depends on the HTTP method:\n\
GET: The resource has been fetched and is transmitted in the message body.\n\
HEAD: The entity headers are in the message body.\n\
PUT or POST: The resource describing the result \n\
of the action is transmitted in the message body.\n\
TRACE: The message body contains the request message as received by the server.\n',

                    201: '201 Created\n\
The request has succeeded and a new resource has been created as a result.\n\
This is typically the response sent after POST requests, or some PUT requests.\n',

                    202: '202 Accepted\n\
The request has been received but not yet acted upon.\n\
It is noncommittal, since there is no way in HTTP\n\
to later send an asynchronous response indicating the outcome of the request.\n\
It is intended for cases where another process or server handles the request,\n\
or for batch processing.\n',

                    203: '203 Non-Authoritative Information\n\
This response code means the returned meta-information is not exactly the same\n\
as is available from the origin server, but is collected from a local\n\
or a third-party copy. This is mostly used for mirrors or backups of another resource.\n\
Except for that specific case, the "200 OK" response is preferred to this status.\n',

                    204: '204 No Content\n\
There is no content to send for this request,\n\
but the headers may be useful.\n\
The user-agent may update its cached headers for this resource with the new ones.\n',

                    205: '205 Reset Content\n\
Tells the user-agent to reset the document which sent this request.\n',

                    206: '206 Partial Content\n\
This response code is used when the Range header is sent\n\
from the client to request only part of a resource.\n',

                    207: '207 Multi-Status (WebDAV)\n\
Conveys information about multiple resources,\n\
for situations where multiple status codes might be appropriate.\n',

                    208: '208 Already Reported (WebDAV)\n\
Used inside a <dav:propstat> response element to avoid\n\
repeatedly enumerating the internal members\n\
of multiple bindings to the same collection.\n',

                    226: '226 IM Used (HTTP Delta encoding)\n\
The server has fulfilled a GET request for the resource,\n\
and the response is a representation of the result of one\n\
or more instance-manipulations applied to the current instance.\n',

# Redirection messages
                    300: '300 Multiple Choice\n\
The request has more than one possible response.\n\
The user-agent or user should choose one of them. \n\
(There is no standardized way of choosing one of the responses,\n\
but HTML links to the possibilities are recommended so the user can pick.)\n',

                    301: '301 Moved Permanently\n\
The URL of the requested resource has been changed permanently.\n\
The new URL is given in the response.\n',

                    302: '302 Found\n\
This response code means that the URI \n\
of requested resource has been changed temporarily. \n\
Further changes in the URI might be made in the future. \n\
Therefore, this same URI should be used by the client in future requests.\n',

                    303: '303 See Other\n\
The server sent this response to direct the client to get \n\
the requested resource at another URI with a GET request.\n',

                    304: '304 Not Modified\n\
This is used for caching purposes. It tells the client that \n\
the response has not been modified, \n\
so the client can continue to use the same cached version of the response.\n',

                    305: '305 Use Proxy\n\
Defined in a previous version of the HTTP specification to \n\
indicate that a requested response must be accessed by a proxy. \n\
It has been deprecated due to security concerns regarding \n\
in-band configuration of a proxy.\n',

                    306: '306 unused\n\
This response code is no longer used; it is just reserved. \n\
It was used in a previous version of the HTTP/1.1 specification.\n',

                    307: '307 Temporary Redirect\n\
The server sends this response to direct the client \n\
to get the requested resource at another URI with same method \n\
that was used in the prior request. \n\
This has the same semantics as the 302 Found HTTP response code, \n\
with the exception that the user agent must not change the HTTP method used: \n\
If a POST was used in the first request, a POST must be used in the second request.\n',

                    308: '308 Permanent Redirect\n\
This means that the resource is now permanently located at another URI, \n\
specified by the Location: HTTP Response header. \n\
This has the same semantics as the 301 Moved Permanently HTTP response code, \n\
with the exception that the user agent must not change the HTTP method used: \n\
If a POST was used in the first request, a POST must be used in the second request.\n',

# Client error responses
                    400: '400 Bad Request\n\
The server could not understand the request due to invalid syntax.\n',

                    401: '401 Unauthorized\n\
Although the HTTP standard specifies "unauthorized", \n\
semantically this response means "unauthenticated". \n\
That is, the client must authenticate itself to get the requested response.\n',

                    402: '402 Payment Required\n\
This response code is reserved for future use. \n\
The initial aim for creating this code was using it for digital payment systems, \n\
however this status code is used very rarely and no standard convention exists.\n',

                    403: '''403 Forbidden\n\
The client does not have access rights to the content; \n\
that is, it is unauthorized, so the server is refusing to give the requested resource. \n\
Unlike 401, the client's identity is known to the server.\n''',

                    404: '404 Not Found\n\
The server can not find the requested resource. \n\
In the browser, this means the URL is not recognized. \n\
In an API, this can also mean that the endpoint is valid but the resource itself does not exist. \n\
Servers may also send this response instead of 403 to \n\
hide the existence of a resource from an unauthorized client. \n\
This response code is probably the most famous one due to its frequent occurrence on the web.\n',

                    405: '405 Method Not Allowed\n\
The request method is known by the server but has been disabled and cannot be used. \n\
For example, an API may forbid DELETE-ing a resource. \n\
The two mandatory methods, GET and HEAD, must never be disabled and should not return this error code.\n',

                    406: '''406 Not Acceptable\n\
This response is sent when the web server, \n\
after performing server-driven content negotiation, \n\
doesn't find any content that conforms to the criteria given by the user agent.\n''',

                    407: '407 Proxy Authentication Required\n\
This is similar to 401 but authentication is needed to be done by a proxy.\n',

                    408: '408 Request Timeout\n\
This response is sent on an idle connection by some servers, \n\
even without any previous request by the client. \n\
It means that the server would like to shut down this unused connection. \n\
This response is used much more since some browsers, like \n\
Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. \n\
Also note that some servers merely shut down the connection without sending this message.\n',

                    409: '409 Conflict\n\
This response is sent when a request conflicts with the current state of the server.\n',

                    410: '410 Gone\n\
This response is sent when the requested content has been permanently deleted from server, \n\
with no forwarding address. Clients are expected to remove their caches and links to the resource. \n\
The HTTP specification intends this status code to be used for "limited-time, promotional services". \n\
APIs should not feel compelled to indicate resources that have been deleted with this status code.\n',

                    411: '411 Length Required\n\
Server rejected the request because the Content-Length \n\
header field is not defined and the server requires it.\n',

                    412: '412 Precondition Failed\n\
The client has indicated preconditions in its headers which the server does not meet.\n',

                    413: '413 Payload Too Large\n\
Request entity is larger than limits defined by server; \n\
the server might close the connection or return an Retry-After header field.\n',

                    414: '''414 URI Too Long\n\
The URI requested by the client is longer than the server is willing to interpret.\n''',

                    415: '''415 Unsupported Media Type\n\
The media format of the requested data is not supported by the server,
so the server is rejecting the request.\n''',

                    416: '''416 Range Not Satisfiable\n\
The range specified by the Range header field in the request can't be fulfilled; \n\
it's possible that the range is outside the size of the target URI's data.\n''',

                    417: '''417 Expectation Failed\n\
This response code means the expectation indicated by \n\
the Expect request header field can't be met by the server.\n''',

                    418: '''418 I'm a teapot\n\
The server refuses the attempt to brew coffee with a teapot.\n''',

                    421: '421 Misdirected Request\n\
The request was directed at a server that is not able to produce a response. \n\
This can be sent by a server that is not configured to produce responses for \n\
the combination of scheme and authority that are included in the request URI.\n',

                    422: '422 Unprocessable Entity (WebDAV)\n\
The request was well-formed but was unable to be followed due to semantic errors.\n',

                    423: '423 Locked (WebDAV)\n\
The resource that is being accessed is locked.\n',

                    424: '424 Failed Dependency (WebDAV)\n\
The request failed due to failure of a previous request.\n',

                    425: '425 Too Early\n\
Indicates that the server is unwilling to risk processing a request that might be replayed.\n',

                    426: '426 Upgrade Required\n\
The server refuses to perform the request using the current protocol \n\
but might be willing to do so after the client upgrades to a different protocol. \n\
The server sends an Upgrade header in a 426 response to indicate the required protocol(s).\n',

                    428: '''428 Precondition Required\n\
The origin server requires the request to be conditional. \n\
This response is intended to prevent the 'lost update' problem, \n\
where a client GETs a resource's state, modifies it, and PUTs it back to the server,\n\
when meanwhile a third party has modified the state on the server, leading to a conflict.\n''',

                    429: '429 Too Many Requests\n\
The user has sent too many requests in a given amount of time ("rate limiting").\n',

                    431: '431 Request Header Fields Too Large\n\
The server is unwilling to process the request because its header fields are too large. \n\
The request may be resubmitted after reducing the size of the request header fields.\n',

                    451: '451 Unavailable For Legal Reasons\n\
The user-agent requested a resource that cannot legally be provided, \n\
such as a web page censored by a government.\n',

# Server error responses
                    500: '''500 Internal Server Error\n\
The server has encountered a situation it doesn't know how to handle.\n''',

                    501: '501 Not Implemented\n\
The request method is not supported by the server and cannot be handled. \n\
The only methods that servers are required to support \n\
(and therefore that must not return this code) are GET and HEAD.\n',

                    502: '502 Bad Gateway\n\
This error response means that the server, \n\
while working as a gateway to get a response needed to handle the request, \n\
got an invalid response.\n',

                    503: '503 Service Unavailable\n\
The server is not ready to handle the request. \n\
Common causes are a server that is down for maintenance or that is overloaded.\n\
Note that together with this response, \n\
a user-friendly page explaining the problem should be sent. \n\
This responses should be used for temporary conditions and the Retry-After: \n\
HTTP header should, if possible, contain the estimated time before the recovery of the service. \n\
The webmaster must also take care about \n\
the caching-related headers that are sent along with this response, \n\
as these temporary condition responses should usually not be cached.\n',

                    504: '''504 Gateway Timeout\n\
This error response is given when the server is acting as
a gateway and cannot get a response in time.\n''',

                    505: '505 HTTP Version Not Supported\n\
The HTTP version used in the request is not supported by the server.\n',

                    506: '506 Variant Also Negotiates\n\
The server has an internal configuration error: \n\
the chosen variant resource is configured to engage in \n\
transparent content negotiation itself, \n\
and is therefore not a proper end point in the negotiation process.\n',

                    507: '507 Insufficient Storage (WebDAV)\n\
The method could not be performed on the resource because the server is \n\
unable to store the representation needed to successfully complete the request.\n',

                    508: '508 Loop Detected (WebDAV)\n\
The server detected an infinite loop while processing the request.\n',

                    510: '510 Not Extended\n\
Further extensions to the request are required for the server to fulfil it.\n',

                    511: '511 Network Authentication Required\n\
The 511 status code indicates that the client needs to authenticate to gain network access.\n'}

def print_info(status_code):
    '''
    pass the integer number status code to the function
    the function will print information about the status code to the terminal
    '''
    print(dict_status_code[status_code])
