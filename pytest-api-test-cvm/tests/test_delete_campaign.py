import uuid
from http import HTTPStatus
import allure
import pytest

from base.api.campaigns_api import CampaignsClient

from models.notification_campaign import DefaultCampaign
from models.error import ErrorResponse

from utils.assertions.base.solutions import assert_status_code, assert_sorted_by_field
from utils.assertions.schema import validate_schema


@pytest.mark.questions
@allure.feature('CVM Campaign')
@allure.story('DELETE Campaign')
class TestDeleteCampaign:

    @pytest.mark.skip(reason="This test was disabled due to authorization issue")
    @allure.title('DELETE Campaign 401 w/o Auth')
    def test_delete_campaign_non_auth(self, function_campaign: DefaultCampaign,
                                      class_campaign_client_non_auth: CampaignsClient):
        response = class_campaign_client_non_auth.delete_campaign_api(function_campaign.id)
        json_response = response.json()
        assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)
        validate_schema(json_response, ErrorResponse.model_json_schema())

    @allure.title('DELETE Campaign 500 w/o campaign id')
    def test_delete_campaign_without_id(self,
                                        class_campaign_client: CampaignsClient):
        response = class_campaign_client.delete_campaign_without_id_api()
        json_response = response.json()
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        validate_schema(json_response, ErrorResponse.model_json_schema())

    @allure.title('DELETE Campaign 500 Delete Non-Existing Campaign')
    def test_delete_non_existing_campaign(self,
                                          class_campaign_client: CampaignsClient):
        random_uuid = str(uuid.uuid4())
        response = class_campaign_client.delete_campaign_api(random_uuid)
        json_response = response.json()
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        validate_schema(json_response, ErrorResponse.model_json_schema())

    @allure.title('GET Deleted Campaign 200')
    def test_get_deleted_campaign(self,
                                  function_campaign: DefaultCampaign,
                                  class_campaign_client: CampaignsClient):
        class_campaign_client.delete_campaign_api(function_campaign.id)
        response = class_campaign_client.get_campaign_by_id_api(function_campaign.id)
        json_response = response.json()
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        validate_schema(json_response, ErrorResponse.model_json_schema())

    @allure.title('GET Deleted Campaign 200')
    def test_delete_campaign(self,
                             function_campaign: DefaultCampaign,
                             class_campaign_client: CampaignsClient):
        response = class_campaign_client.delete_campaign_api(function_campaign.id)

        assert_status_code(response.status_code, HTTPStatus.OK)
