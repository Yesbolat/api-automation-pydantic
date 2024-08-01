from datetime import date

from pydantic import BaseModel, Field, RootModel
from typing import List, Optional
from enum import Enum
from utils.fakers import random_string


class Config:
    allow_population_by_field_name = True


class RunMode(Enum):
    MANUAL = "MANUAL"
    AUTO = "AUTO"


class NotificationCategory(Enum):
    ACCOUNTS = "ACCOUNTS"
    CARDS = "CARDS"
    PAYMENTS = "PAYMENTS"
    FOREIGN = "FOREIGN"
    TARIFFS = "TARIFFS"
    ONLINE_ACCOUNTING = "ONLINE_ACCOUNTING"
    LOANS = "LOANS"
    LETTERS = "LETTERS"
    NEWS = "NEWS"
    DEPOSITS = "DEPOSITS"
    TOLE = "TOLE"
    NOT_PUSH = "NOT_PUSH"


class ChannelType(Enum):
    PUSH = "PUSH"
    EMAIL = "EMAIL"
    SMS = "SMS"
    PUSH_TO_SMS = "PUSH_TO_SMS"
    PUSH_TO_EMAIL = "PUSH_TO_EMAIL"


class State(Enum):
    CREATED = "CREATED"
    READY_FOR_RUN = "READY_FOR_RUN"
    RUN = "RUN"
    STOPPED = "STOPPED"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    DRAFT = "DRAFT"


class CampaignItem(BaseModel):
    id: Optional[str] = Field(None, alias='id')
    name: str = Field(..., alias='name')
    created: Optional[str] = Field(None, alias='created')
    edit_date: Optional[str] = Field(None, alias='editDate')
    title_kz: Optional[str] = Field(None, alias='titleKz')
    title_ru: Optional[str] = Field(None, alias='titleRu')
    title_en: Optional[str] = Field(None, alias='titleEn')
    message_kz: Optional[str] = Field(None, alias='messageKz')
    message_ru: Optional[str] = Field(None, alias='messageRu')
    message_en: Optional[str] = Field(None, alias='messageEn')
    image_url: Optional[str] = Field(None, alias='imageUrl')
    run_mode: RunMode = Field(..., alias='runMode')
    start_date: Optional[str] = Field(None, alias='startDate')
    end_date: Optional[str] = Field(None, alias='endDate')
    notification_category: NotificationCategory = Field(..., alias='notificationCategory')
    button_name_kz: Optional[str] = Field(None, alias='buttonNameKz')
    button_name_ru: Optional[str] = Field(None, alias='buttonNameRu')
    button_name_en: Optional[str] = Field(None, alias='buttonNameEn')
    button_link: Optional[str] = Field(None, alias='buttonLink')
    segment_mode: Optional[str] = Field(None, alias='segmentMode')
    segment_type: Optional[str] = Field(None, alias='segmentType')
    client_type: Optional[str] = Field(None, alias='clientType')
    channel_type: ChannelType = Field(..., alias='channelType')
    state: State = Field(..., alias='state')
    count_in_batch: Optional[int] = Field(None, alias='countInBatch')
    interval_in_minutes: Optional[int] = Field(None, alias='intervalInMinutes')
    sms_text_kz: Optional[str] = Field(None, alias='smsTextKz')
    sms_text_ru: Optional[str] = Field(None, alias='smsTextRu')
    sms_text_en: Optional[str] = Field(None, alias='smsTextEn')
    email_title: Optional[str] = Field(None, alias='emailTitle')
    email_text: Optional[str] = Field(None, alias='emailText')
    details: Optional[str] = Field(None, alias='details')
    file_bytes: Optional[str] = Field(None, alias='fileBytes')
    department_code: Optional[str] = Field(None, alias='departmentCode')
    company_type: Optional[str] = Field(None, alias='companyType')
    exclude_wrong_details: Optional[bool] = Field(None, alias='excludeWrongDetails')
    segment_query_joins: Optional[str] = Field(None, alias='segmentQueryJoins')
    segment_query_conditions: Optional[str] = Field(None, alias='segmentQueryConditions')
    web_button_link: Optional[str] = Field(None, alias='webButtonLink')
    web_button_name_en: Optional[str] = Field(None, alias='webButtonNameEn')
    web_button_name_kz: Optional[str] = Field(None, alias='webButtonNameKz')
    web_button_name_ru: Optional[str] = Field(None, alias='webButtonNameRu')
    notification_type: Optional[str] = Field(None, alias='notificationType')


class CompanyDetails(BaseModel):
    company_bin: Optional[str] = Field(default=None, alias='companyBin')


def create_default_details():
    return [CompanyDetails(companyBin="050140014478")]


class DefaultCampaign(BaseModel):
    id: Optional[str] = Field(None, alias='id')
    count_in_batch: int = Field(default=50, alias='countInBatch')
    interval_in_minutes: int = Field(default=1, alias='intervalInMinutes')
    name: Optional[str] = Field(default="Test Campaign Specific User", alias='name')
    channel_type: str = Field(default="PUSH", alias='channelType')
    notification_category: str = Field(default="ACCOUNTS", alias='notificationCategory')
    title_kz: Optional[str] = Field(default_factory=random_string, alias='titleKz')
    title_ru: Optional[str] = Field(default_factory=random_string, alias='titleRu')
    title_en: Optional[str] = Field(default_factory=random_string, alias='titleEn')
    image_url: Optional[str] = Field(default=None, alias='imageUrl')
    message_ru: Optional[str] = Field(default_factory=random_string, alias='messageRu')
    message_kz: Optional[str] = Field(default_factory=random_string, alias='messageKz')
    message_en: Optional[str] = Field(default_factory=random_string, alias='messageEn')
    sms_text_ru: Optional[str] = Field(default=None, alias='smsTextRu')
    sms_text_kz: Optional[str] = Field(default=None, alias='smsTextKz')
    sms_text_en: Optional[str] = Field(default=None, alias='smsTextEn')
    button_name_ru: Optional[str] = Field(default=None, alias='buttonNameRu')
    button_name_kz: Optional[str] = Field(default=None, alias='buttonNameKz')
    button_name_en: Optional[str] = Field(default=None, alias='buttonNameEn')
    button_link: Optional[str] = Field(default=None, alias='buttonLink')
    segment_mode: str = Field(default="COMMON", alias='segmentMode')
    segment_type: Optional[str] = Field(default="SPECIFIC_USERS", alias='segmentType')
    segment_query_joins: Optional[str] = Field(default=None, alias='segmentQueryJoins')
    segment_query_conditions: Optional[str] = Field(default=None, alias='segmentQueryConditions')
    client_type: Optional[str] = Field(default=None, alias='clientType')
    file_bytes: Optional[bytes] = Field(default=None, alias='fileBytes')
    start_date: Optional[date] = Field(default=None, alias='startDate')
    run_mode: str = Field(default="MANUAL", alias='runMode')
    exclude_wrong_details: bool = Field(default=False, alias='excludeWrongDetails')
    email_title: Optional[str] = Field(default=None, alias='emailTitle')
    email_text: Optional[str] = Field(default=None, alias='emailText')
    details: List[CompanyDetails] = Field(default_factory=create_default_details, alias='details')
    company_type: Optional[str] = Field(default=None, alias='companyType')
    department_code: Optional[str] = Field(default=None, alias='departmentCode')
    notification_type: str = Field(default="INFORM", alias='notificationType')


class CustomCampaign(DefaultCampaign):
    segment_type: str = Field(default="ALL_USERS", alias='segmentType')
    count_in_batch: int = Field(default=1, alias='countInBatch')
    details: Optional[List[CompanyDetails]] = Field(default_factory=lambda: None, alias='details')


class CampaignListList(RootModel):
    root: List[CampaignItem]
