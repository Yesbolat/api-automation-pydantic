import allure
from httpx import Response

from models.notification_campaign import DefaultCampaign
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class CampaignsClient(APIClient):
    @allure.step('Getting all campaigns')
    def get_campaigns_api(self) -> Response:
        return self.client.get(APIRoutes.CAMPAIGNS)

    @allure.step('Getting campaign by id')
    def get_campaign_by_id_api(self, campaign_id: str) -> Response:
        return self.client.get(f'{APIRoutes.CAMPAIGN}/{campaign_id}{APIRoutes.CAMPAIGN_DETAILS}')

    @allure.step('Post campaign')
    def post_campaign_api(self, payload: DefaultCampaign) -> Response:
        return self.client.post(APIRoutes.CAMPAIGN, json=payload.model_dump(by_alias=True))

    @allure.step('Delete campaign')
    def delete_campaign_api(self, campaign_id: str) -> Response:
        return self.client.delete(f'{APIRoutes.CAMPAIGN}/{campaign_id}')

    @allure.step('Delete campaign')
    def delete_campaign_without_id_api(self) -> Response:
        return self.client.delete(f'{APIRoutes.CAMPAIGN}/')

    @allure.step('Run campaign by id')
    def run_campaign_by_id_api(self, campaign_id: str) -> Response:
        return self.client.put(f'{APIRoutes.CAMPAIGN}/{campaign_id}{APIRoutes.CAMPAIGN_RUN}')

    @allure.step('Pause campaign by id')
    def pause_campaign_by_id_api(self, campaign_id: str) -> Response:
        return self.client.put(f'{APIRoutes.CAMPAIGN}/{campaign_id}{APIRoutes.CAMPAIGN_PAUSE}')

    @allure.step('Stop campaign by id')
    def stop_campaign_by_id_api(self, campaign_id: str) -> Response:
        return self.client.put(f'{APIRoutes.CAMPAIGN}/{campaign_id}{APIRoutes.CAMPAIGN_STOP}')

    def create_campaign(self) -> DefaultCampaign:
        payload = DefaultCampaign()
        response = self.post_campaign_api(payload)
        return DefaultCampaign(**response.json())