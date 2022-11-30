from http.server import BaseHTTPRequestHandler, HTTPServer

import logging
import json

from Reto.StreetModel import StreetModel

# iniciar el modelo en el servidor
model = StreetModel()


def update_positions():
    model.step()

    # funcion del modelo que regresa una arreglo con coordenadas
    positions = model.get_agent_positions()

    return positions


def positionsToJSON(ps):
    posDICT = []
    for p in ps:
        pos = {
            "x": p[0],
            "y": p[1]
        }
        posDICT.append(pos)

    return json.dumps(posDICT)


class Server(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        # esto es solo para logging
        logging.info("GET request, \nPath: %s \nHeaders:\n%s \n", str(self.path), str(self.headers))

        positions = update_positions()

        self._set_response()

        resp = "{:" + positionsToJSON(positions) + "}"

        # con el arreglo data
        # resp = "{\"data\":" + positionsToJSON(positions) + "}"

        self.wfile.write(resp.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))

        # esto es solo para logging
        logging.info("POST request, \nPath: %s \nHeaders:\n%s \n\nBody:\n%s \n", str(self.path), str(self.headers),
                     json.dumps(post_data))

        positions = update_positions()

        self._set_response()

        resp = "{\"data\":" + positionsToJSON(positions) + "}"

        self.wfile.write(resp.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=Server, port=3005):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting httpd...\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    logging.info("Stopping httpd...\n")


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))

    else:
        run()
