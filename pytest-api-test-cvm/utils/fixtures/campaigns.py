import pytest

from base.api.campaigns_api import CampaignsClient
from models.authentication import Authentication, AdminAuthUser
from models.notification_campaign import DefaultCampaign
from utils.campaign.campaign_status_helper import CampaignStatusHelper
from utils.clients.http.builder import get_http_client


@pytest.fixture(scope="class")
def class_campaign_client() -> CampaignsClient:
    auth_credentials = AdminAuthUser()
    auth = Authentication(user=auth_credentials)
    client = get_http_client(auth=auth)
    return CampaignsClient(client=client)


@pytest.fixture(scope="class")
def class_campaign_client_non_auth() -> CampaignsClient:
    client = get_http_client()
    return CampaignsClient(client=client)


@pytest.fixture(params=["RUN", "PAUSED", "STOPPED", "COMPLETED"])
def campaign_with_wrong_state(request, class_campaign_client: CampaignsClient):
    campaign = CampaignStatusHelper.get_campaign_by_state(class_campaign_client, request.param, timeout=25,
                                                          max_retries=5)
    yield campaign
    if hasattr(campaign, 'id'):
        class_campaign_client.stop_campaign_by_id_api(campaign.id)


@pytest.fixture(params=["DRAFT", "CREATED"])
def campaign_with_right_state(request, class_campaign_client: CampaignsClient):
    return CampaignStatusHelper.get_campaign_by_state(class_campaign_client, request.param, timeout=25,
                                                      max_retries=5)


@pytest.fixture(scope='function')
def function_campaign(class_campaign_client: CampaignsClient) -> DefaultCampaign:
    campaign = class_campaign_client.create_campaign()
    yield campaign
    class_campaign_client.delete_campaign_api(campaign.id)
