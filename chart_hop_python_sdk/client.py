# coding: utf-8
"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

import typing
import inspect
from datetime import date, datetime
from chart_hop_python_sdk.client_custom import ClientCustom
from chart_hop_python_sdk.configuration import Configuration
from chart_hop_python_sdk.api_client import ApiClient
from chart_hop_python_sdk.type_util import copy_signature
from chart_hop_python_sdk.apis.tags.access_api import AccessApi
from chart_hop_python_sdk.apis.tags.action_api import ActionApi
from chart_hop_python_sdk.apis.tags.ai_api import AiApi
from chart_hop_python_sdk.apis.tags.app_api import AppApi
from chart_hop_python_sdk.apis.tags.app_config_api import AppConfigApi
from chart_hop_python_sdk.apis.tags.approval_api import ApprovalApi
from chart_hop_python_sdk.apis.tags.approval_request_api import ApprovalRequestApi
from chart_hop_python_sdk.apis.tags.assessment_api import AssessmentApi
from chart_hop_python_sdk.apis.tags.band_api import BandApi
from chart_hop_python_sdk.apis.tags.billing_api import BillingApi
from chart_hop_python_sdk.apis.tags.budget_pool_api import BudgetPoolApi
from chart_hop_python_sdk.apis.tags.calendar_api import CalendarApi
from chart_hop_python_sdk.apis.tags.category_api import CategoryApi
from chart_hop_python_sdk.apis.tags.category_sort_api import CategorySortApi
from chart_hop_python_sdk.apis.tags.change_api import ChangeApi
from chart_hop_python_sdk.apis.tags.comment_api import CommentApi
from chart_hop_python_sdk.apis.tags.comp_review_api import CompReviewApi
from chart_hop_python_sdk.apis.tags.content_api import ContentApi
from chart_hop_python_sdk.apis.tags.customer_api import CustomerApi
from chart_hop_python_sdk.apis.tags.data_view_api import DataViewApi
from chart_hop_python_sdk.apis.tags.email_template_api import EmailTemplateApi
from chart_hop_python_sdk.apis.tags.event_api import EventApi
from chart_hop_python_sdk.apis.tags.exchange_rate_api import ExchangeRateApi
from chart_hop_python_sdk.apis.tags.export_api import ExportApi
from chart_hop_python_sdk.apis.tags.expression_api import ExpressionApi
from chart_hop_python_sdk.apis.tags.field_api import FieldApi
from chart_hop_python_sdk.apis.tags.file_api import FileApi
from chart_hop_python_sdk.apis.tags.form_api import FormApi
from chart_hop_python_sdk.apis.tags.form_response_api import FormResponseApi
from chart_hop_python_sdk.apis.tags.group_api import GroupApi
from chart_hop_python_sdk.apis.tags.guideline_api import GuidelineApi
from chart_hop_python_sdk.apis.tags.model_import_api import ModelImportApi
from chart_hop_python_sdk.apis.tags.job_api import JobApi
from chart_hop_python_sdk.apis.tags.job_level_api import JobLevelApi
from chart_hop_python_sdk.apis.tags.legal_doc_api import LegalDocApi
from chart_hop_python_sdk.apis.tags.media_api import MediaApi
from chart_hop_python_sdk.apis.tags.message_api import MessageApi
from chart_hop_python_sdk.apis.tags.metric_api import MetricApi
from chart_hop_python_sdk.apis.tags.multiplier_api import MultiplierApi
from chart_hop_python_sdk.apis.tags.notification_api import NotificationApi
from chart_hop_python_sdk.apis.tags.oauth_api import OauthApi
from chart_hop_python_sdk.apis.tags.onboard_api import OnboardApi
from chart_hop_python_sdk.apis.tags.org_api import OrgApi
from chart_hop_python_sdk.apis.tags.org_config_api import OrgConfigApi
from chart_hop_python_sdk.apis.tags.person_api import PersonApi
from chart_hop_python_sdk.apis.tags.policy_api import PolicyApi
from chart_hop_python_sdk.apis.tags.position_api import PositionApi
from chart_hop_python_sdk.apis.tags.preload_api import PreloadApi
from chart_hop_python_sdk.apis.tags.process_api import ProcessApi
from chart_hop_python_sdk.apis.tags.product_api import ProductApi
from chart_hop_python_sdk.apis.tags.profile_tab_api import ProfileTabApi
from chart_hop_python_sdk.apis.tags.query_api import QueryApi
from chart_hop_python_sdk.apis.tags.question_api import QuestionApi
from chart_hop_python_sdk.apis.tags.report_api import ReportApi
from chart_hop_python_sdk.apis.tags.report_chart_api import ReportChartApi
from chart_hop_python_sdk.apis.tags.role_api import RoleApi
from chart_hop_python_sdk.apis.tags.saml_api import SamlApi
from chart_hop_python_sdk.apis.tags.scenario_api import ScenarioApi
from chart_hop_python_sdk.apis.tags.search_api import SearchApi
from chart_hop_python_sdk.apis.tags.status_api import StatusApi
from chart_hop_python_sdk.apis.tags.stock_api import StockApi
from chart_hop_python_sdk.apis.tags.stripe_api import StripeApi
from chart_hop_python_sdk.apis.tags.table_api import TableApi
from chart_hop_python_sdk.apis.tags.task_api import TaskApi
from chart_hop_python_sdk.apis.tags.task_config_api import TaskConfigApi
from chart_hop_python_sdk.apis.tags.template_api import TemplateApi
from chart_hop_python_sdk.apis.tags.timeoff_api import TimeoffApi
from chart_hop_python_sdk.apis.tags.usage_api import UsageApi
from chart_hop_python_sdk.apis.tags.user_api import UserApi
from chart_hop_python_sdk.apis.tags.webauthn_api import WebauthnApi



class ChartHop(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.access: AccessApi = AccessApi(api_client)
        self.action: ActionApi = ActionApi(api_client)
        self.ai: AiApi = AiApi(api_client)
        self.app: AppApi = AppApi(api_client)
        self.app_config: AppConfigApi = AppConfigApi(api_client)
        self.approval: ApprovalApi = ApprovalApi(api_client)
        self.approval_request: ApprovalRequestApi = ApprovalRequestApi(api_client)
        self.assessment: AssessmentApi = AssessmentApi(api_client)
        self.band: BandApi = BandApi(api_client)
        self.billing: BillingApi = BillingApi(api_client)
        self.budget_pool: BudgetPoolApi = BudgetPoolApi(api_client)
        self.calendar: CalendarApi = CalendarApi(api_client)
        self.category: CategoryApi = CategoryApi(api_client)
        self.category_sort: CategorySortApi = CategorySortApi(api_client)
        self.change: ChangeApi = ChangeApi(api_client)
        self.comment: CommentApi = CommentApi(api_client)
        self.comp_review: CompReviewApi = CompReviewApi(api_client)
        self.content: ContentApi = ContentApi(api_client)
        self.customer: CustomerApi = CustomerApi(api_client)
        self.data_view: DataViewApi = DataViewApi(api_client)
        self.email_template: EmailTemplateApi = EmailTemplateApi(api_client)
        self.event: EventApi = EventApi(api_client)
        self.exchange_rate: ExchangeRateApi = ExchangeRateApi(api_client)
        self.export: ExportApi = ExportApi(api_client)
        self.expression: ExpressionApi = ExpressionApi(api_client)
        self.field: FieldApi = FieldApi(api_client)
        self.file: FileApi = FileApi(api_client)
        self.form: FormApi = FormApi(api_client)
        self.form_response: FormResponseApi = FormResponseApi(api_client)
        self.group: GroupApi = GroupApi(api_client)
        self.guideline: GuidelineApi = GuidelineApi(api_client)
        self.import: ModelImportApi = ModelImportApi(api_client)
        self.job: JobApi = JobApi(api_client)
        self.job_level: JobLevelApi = JobLevelApi(api_client)
        self.legal_doc: LegalDocApi = LegalDocApi(api_client)
        self.media: MediaApi = MediaApi(api_client)
        self.message: MessageApi = MessageApi(api_client)
        self.metric: MetricApi = MetricApi(api_client)
        self.multiplier: MultiplierApi = MultiplierApi(api_client)
        self.notification: NotificationApi = NotificationApi(api_client)
        self.oauth: OauthApi = OauthApi(api_client)
        self.onboard: OnboardApi = OnboardApi(api_client)
        self.org: OrgApi = OrgApi(api_client)
        self.org_config: OrgConfigApi = OrgConfigApi(api_client)
        self.person: PersonApi = PersonApi(api_client)
        self.policy: PolicyApi = PolicyApi(api_client)
        self.position: PositionApi = PositionApi(api_client)
        self.preload: PreloadApi = PreloadApi(api_client)
        self.process: ProcessApi = ProcessApi(api_client)
        self.product: ProductApi = ProductApi(api_client)
        self.profile_tab: ProfileTabApi = ProfileTabApi(api_client)
        self.query: QueryApi = QueryApi(api_client)
        self.question: QuestionApi = QuestionApi(api_client)
        self.report: ReportApi = ReportApi(api_client)
        self.report_chart: ReportChartApi = ReportChartApi(api_client)
        self.role: RoleApi = RoleApi(api_client)
        self.saml: SamlApi = SamlApi(api_client)
        self.scenario: ScenarioApi = ScenarioApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
        self.status: StatusApi = StatusApi(api_client)
        self.stock: StockApi = StockApi(api_client)
        self.stripe: StripeApi = StripeApi(api_client)
        self.table: TableApi = TableApi(api_client)
        self.task: TaskApi = TaskApi(api_client)
        self.task_config: TaskConfigApi = TaskConfigApi(api_client)
        self.template: TemplateApi = TemplateApi(api_client)
        self.timeoff: TimeoffApi = TimeoffApi(api_client)
        self.usage: UsageApi = UsageApi(api_client)
        self.user: UserApi = UserApi(api_client)
        self.webauthn: WebauthnApi = WebauthnApi(api_client)
