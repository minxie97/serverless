from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "pokemon" in dic:
            url = "https://pokeapi.co/api/v2/pokemon/"
            r = requests.get(url + dic["pokemon"])
            data = r.json()
            chosen_poke = dic["pokemon"].title()
            type_1 = data["types"][0]["type"]["name"].title()
            if len(data["types"]) == 2:
                type_2 = data["types"][1]["type"]["name"].title()
                message = f"{chosen_poke} is a {type_1} and {type_2} typed Pokemon."
            elif len(data["types"]) == 1:
                message = f"{chosen_poke} is a {type_1} typed Pokemon."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        
        return