from http.client import responses

# print(responses[206])
# my_responses = responses.copy()
# my_responses[206] = " Partial Content"
class HttpRequest:
    def __init__(self, version, method, path, headers, data):
        self.version = version
        self.method = method
        self.path = path
        self.headers = headers
        self.cookies = {}
        if "Cookie" in self.headers:
            cookies = self.headers["Cookie"].split(";")
            for cookie in cookies:
                key, value = cookie.split("=")
                self.cookies[key.strip()] = value.strip()
        self.data = data

    def __repr__(self):
        req = f"{self.method} {self.path} {self.version}\r\n"
        for key in self.headers:
            req += f"{key}: {self.headers[key]}\r\n"
        try:
            d = self.data.decode("utf-8")
            # req += "\r\n" + d
        except:
            pass
        return req


def parse_request(http_request):
    lines = http_request.split(b"\r\n")
    first_line = lines[0].decode().split(" ")
    http_method = first_line[0]
    path = first_line[1]
    version = first_line[2]
    headers = {}
    i = 1
    while True:
        if lines[i] == b"":
            break
        # print(lines[i])
        key_value = lines[i].decode().split(": ")
        headers[key_value[0]] = key_value[1]
        i += 1
    i += 1
    # print("lines[-1]:", lines[-1])
    data = b"\r\n".join(lines[i:])
    # print(http_method, path, version)
    # print(headers)
    # print("data:", data)
    return HttpRequest(version, http_method, path, headers, data)


def wrap_response(version, status_code, headers, data=""):
    res = f"{version} {status_code} {responses[status_code]}\r\n"
    for key in headers:
        res += f"{key}: {headers[key]}\r\n"
    res += "\r\n"
    print(res)
    res = res.encode("utf-8")
    if type(data) == str:
        res += data.encode("utf-8")
    else:
        res += data
    # print(res)
    return res


basic_header = {
    "Access-Control-Allow-Origin": "http://localhost:3000",
    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
    "Access-Control-Allow-Credentials": "true",
}
