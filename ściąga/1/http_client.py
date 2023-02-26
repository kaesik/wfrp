import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://jrpizzamamadjango3.herokuapp.com/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizza_dict = []
            for i in data:
                pizza_dict.append(i["fields"])
            print("data_received")
            if on_complete:
                on_complete(pizza_dict)

        def data_error(req, error):
            print("data_error")
            if on_error:
                on_error(str(error))

        def data_failure(req, result):
            print("data_failure")
            if on_error:
                on_error("Server Error: " + str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)
