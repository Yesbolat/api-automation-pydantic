from enum import Enum


class APIRoutes(str, Enum):
    CAMPAIGNS = '/admin/api/v1/campaign/list'
    CAMPAIGN = '/admin/api/v1/campaign/'
    AUTH_ADMIN_NEW = '/admin/api/v2/iam/login'
    CAMPAIGN_DETAILS = '/details/state'
    CAMPAIGN_RUN = '/run'
    CAMPAIGN_PAUSE = '/pause'
    CAMPAIGN_STOP = '/stop'

    def __str__(self) -> str:
        return self.value
