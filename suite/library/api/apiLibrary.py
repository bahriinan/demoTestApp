import json
import requests


class ApiLibrary():

    def get_request(self, url):
        return requests.get(url=url)
    # End Of Definition

    def put_request(self, url, headers, data=None):
        return requests.put(url=url, data=data, headers=headers)
    # End Of Definition

    def get_header(self, mimetype):
        return {'Content-Type': mimetype, 'Accept': mimetype}
    # End Of Definition

    def get_data(self, author=None, title=None):
        return json.dumps({
            "Author": author,
            "Title": title
        })
    # End Of Definition
# End Of Class
