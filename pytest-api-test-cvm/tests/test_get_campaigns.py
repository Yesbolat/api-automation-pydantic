from http import HTTPStatus
import allure
import pytest

from base.api.campaigns_api import CampaignsClient

from models.notification_campaign import CampaignListList
from utils.assertions.base.solutions import assert_status_code, assert_sorted_by_field
from utils.assertions.schema import validate_schema


@pytest.mark.questions
@allure.feature('CVM Campaign')
@allure.story('GET Campaign')
class TestGetCampaigns:

    @allure.title('Check Get Campaign List Status code and schema')
    def test_get_campaign_list(self, class_campaign_client: CampaignsClient):
        response = class_campaign_client.get_campaigns_api()
        json_response = response.json()
        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_schema(json_response, CampaignListList.model_json_schema())

    @pytest.mark.skip(reason="This test was disabled due to authorization issue")
    @allure.title('Get Campaign List 401 w/o Auth"')
    def test_get_campaign_list_non_auth(self, class_campaign_client_non_auth: CampaignsClient):
        response = class_campaign_client_non_auth.get_campaigns_api()
        json_response = response.json()
        assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)
        validate_schema(json_response, CampaignListList.model_json_schema())

    @allure.title("Сheck Campaign List Order")
    def test_check_campaign_list_order(self, class_campaign_client: CampaignsClient):
        response = class_campaign_client.get_campaigns_api()
        json_response = response.json()
        assert_sorted_by_field(json_response, "created", True)
