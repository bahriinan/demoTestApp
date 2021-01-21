import yaml
import pathlib


class DataGenerator(object):

    def __init__(self):
        with open(pathlib.Path(__file__).parent / 'data.yaml') as file:
            self.data = yaml.load(file, Loader=yaml.FullLoader)
        # End Of  With Statement
    # End Of  Definition

    def get_base_url(self):
        return self.data["BASE_URL"]
    # End Of Definition

    def get_username(self):
        return self.data["USERNAME"]
    # End Of Definition

    def get_password(self):
        return self.data["PASSWORD"]
    # End Of Definition

    def get_api(self):
        return self.data["API"]
    #  End Of Definition

    def get_mimetype(self):
        return self.data['MIMTYPE']
    # End Of Definition

    def get_author(self):
        return self.data['AUTHOR_NAME']
    # End Of Definition

    def get_title(self):
        return self.data['BOOK_NAME']
    # End Of Definition
# End Of Class
