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
@allure.story('DELETE Campaign by state')
class TestDeleteCampaignByState:

    def test_campaign_deleted_with_wrong_state(self, campaign_with_wrong_state,
                                               class_campaign_client: CampaignsClient):
        allure.dynamic.title(f'DELETE Campaign W/ Wrong State')
        response = class_campaign_client.delete_campaign_api(campaign_with_wrong_state.id)
        json_response = response.json()
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        validate_schema(json_response, ErrorResponse.model_json_schema())

    def test_campaign_deleted_with_right_state(self, campaign_with_right_state,
                                               class_campaign_client: CampaignsClient):
        allure.dynamic.title(f'DELETE Campaign W/ Right State ')
        response = class_campaign_client.delete_campaign_api(campaign_with_right_state.id)
        assert_status_code(response.status_code, HTTPStatus.OK)
