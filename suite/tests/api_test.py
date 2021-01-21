import pytest
from suite.library.api.apiLibrary import ApiLibrary
from suite.library.testData.testData import DataGenerator


@pytest.mark.usefixtures("api_setup")
class TestApi():
    dataGen = DataGenerator()
    reqTypes = ApiLibrary()

    def test_check_api_is_empty(self):
        response = self.reqTypes.get_request(self.dataGen.get_api())
        assert len(response.json()) == 0
        # End Of If Statement
    # End Of Definition

    def test_verify_title_and_author_is_required(self):
        response = self.reqTypes.put_request(self.dataGen.get_api(),
                                             self.reqTypes.get_header(self.dataGen.get_mimetype()))
        assert response.status_code == 400
    # End Of Definition

    def test_verify_title_and_author_is_not_empty(self):
        response = self.reqTypes.put_request(self.dataGen.get_api(),
                                             self.reqTypes.get_header(self.dataGen.get_mimetype()),
                                             self.reqTypes.get_data())
        assert response.status_code == 400
    # End Of Definition

    def test_verify_book_creation(self):
        response = self.reqTypes.put_request(self.dataGen.get_api(),
                                             self.reqTypes.get_header(self.dataGen.get_mimetype()),
                                             self.reqTypes.get_data(self.dataGen.get_author(),
                                                                    self.dataGen.get_title()))
        assert response.status_code == 200
    # End Of Definition

    def test_verify_adding_existing_book(self):
        response = self.reqTypes.put_request(self.dataGen.get_api(),
                                             self.reqTypes.get_header(self.dataGen.get_mimetype()),
                                             self.reqTypes.get_data(self.dataGen.get_author(),
                                                                    self.dataGen.get_title()))
        assert response.status_code == 400
    # End Of Definition
# End Of Class
