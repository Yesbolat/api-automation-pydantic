import time

from base.api.campaigns_api import CampaignsClient
from models.notification_campaign import DefaultCampaign, CampaignItem, CustomCampaign


class CampaignStatusHelper:

    @staticmethod
    def wait_expected_state(class_campaign_client: CampaignsClient, expected_state: str, timeout: int, campaign_id: str, max_retries: int):
        retry_count = 0
        while retry_count < max_retries:

            response = class_campaign_client.get_campaign_by_id_api(campaign_id)
            state = response.json().get("state")
            if state == expected_state:
                return
            else:
                retry_count += 1
                if retry_count < max_retries:
                    time.sleep(timeout)
        raise RuntimeError("Maximum number of retries reached")

    @staticmethod
    def get_campaign_by_state(class_campaign_client: CampaignsClient, expected_state: str, timeout: int, max_retries: int) -> DefaultCampaign:
        payload = DefaultCampaign()
        response = class_campaign_client.get_campaigns_api()
        campaign_list = response.json()
        filtered_campaigns = [cmp for cmp in campaign_list if expected_state == cmp.get("state")]
        if filtered_campaigns:
            campaign_data = filtered_campaigns[0]
            campaign = CampaignItem(**campaign_data)
            return campaign

        else:
            if expected_state == "COMPLETED":
                create_response = class_campaign_client.post_campaign_api(payload)
                campaign_data = create_response.json()
                campaign = DefaultCampaign(**campaign_data)
                class_campaign_client.run_campaign_by_id_api(campaign.id)
                CampaignStatusHelper.wait_expected_state(class_campaign_client, expected_state, timeout, campaign.id, max_retries)
                return campaign

            if expected_state == "RUN":
                payload = CustomCampaign()
                create_response = class_campaign_client.post_campaign_api(payload)
                campaign_data = create_response.json()
                campaign = DefaultCampaign(**campaign_data)
                CampaignStatusHelper.wait_expected_state(class_campaign_client, 'CREATED', timeout, campaign.id, max_retries)
                class_campaign_client.run_campaign_by_id_api(campaign.id)
                CampaignStatusHelper.wait_expected_state(class_campaign_client, expected_state, timeout, campaign.id, max_retries)
                return campaign

            if expected_state == "PAUSED":
                create_response = class_campaign_client.post_campaign_api(payload)
                campaign_data = create_response.json()
                campaign = DefaultCampaign(**campaign_data)
                CampaignStatusHelper.wait_expected_state(class_campaign_client, 'CREATED', timeout, campaign.id, max_retries)
                class_campaign_client.run_campaign_by_id_api(campaign.id)
                class_campaign_client.pause_campaign_by_id_api(campaign.id)
                CampaignStatusHelper.wait_expected_state(class_campaign_client, expected_state, timeout, campaign.id, max_retries)
                return campaign

            if expected_state == "DRAFT":
                payload = CustomCampaign()
                create_response = class_campaign_client.post_campaign_api(payload)
                campaign_data = create_response.json()
                campaign = DefaultCampaign(**campaign_data)
                CampaignStatusHelper.wait_expected_state(class_campaign_client, expected_state, timeout, campaign.id, max_retries)
                return campaign

            if expected_state == "STOPPED":
                create_response = class_campaign_client.post_campaign_api(payload)
                campaign_data = create_response.json()
                campaign = DefaultCampaign(**campaign_data)
                CampaignStatusHelper.wait_expected_state(class_campaign_client, 'CREATED', timeout, campaign.id, max_retries)
                class_campaign_client.run_campaign_by_id_api(campaign.id)
                class_campaign_client.stop_campaign_by_id_api(campaign.id)
                return campaign