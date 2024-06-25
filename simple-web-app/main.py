from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path

HOST_NAME = "localhost"
SERVER_PORT = 8080
APP_PATH = path.dirname(path.abspath(__file__))

index_path = path.join(APP_PATH, "index.html")


class MyServer(BaseHTTPRequestHandler):
    """ Сервер без лишней логики """

    def __get_index(self):
        with open(index_path, encoding="UTF-8") as file:
            content = file.read()
        return content

    def do_GET(self):
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), MyServer)
    print("Server started http://%s:%s" % (HOST_NAME, SERVER_PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
