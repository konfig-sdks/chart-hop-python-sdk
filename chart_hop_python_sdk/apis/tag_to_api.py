import typing_extensions

from chart_hop_python_sdk.apis.tags import TagValues
from chart_hop_python_sdk.apis.tags.comp_review_api import CompReviewApi
from chart_hop_python_sdk.apis.tags.app_api import AppApi
from chart_hop_python_sdk.apis.tags.approval_api import ApprovalApi
from chart_hop_python_sdk.apis.tags.form_api import FormApi
from chart_hop_python_sdk.apis.tags.change_api import ChangeApi
from chart_hop_python_sdk.apis.tags.org_api import OrgApi
from chart_hop_python_sdk.apis.tags.process_api import ProcessApi
from chart_hop_python_sdk.apis.tags.template_api import TemplateApi
from chart_hop_python_sdk.apis.tags.user_api import UserApi
from chart_hop_python_sdk.apis.tags.field_api import FieldApi
from chart_hop_python_sdk.apis.tags.scenario_api import ScenarioApi
from chart_hop_python_sdk.apis.tags.table_api import TableApi
from chart_hop_python_sdk.apis.tags.report_api import ReportApi
from chart_hop_python_sdk.apis.tags.assessment_api import AssessmentApi
from chart_hop_python_sdk.apis.tags.export_api import ExportApi
from chart_hop_python_sdk.apis.tags.position_api import PositionApi
from chart_hop_python_sdk.apis.tags.task_api import TaskApi
from chart_hop_python_sdk.apis.tags.group_api import GroupApi
from chart_hop_python_sdk.apis.tags.job_api import JobApi
from chart_hop_python_sdk.apis.tags.content_api import ContentApi
from chart_hop_python_sdk.apis.tags.timeoff_api import TimeoffApi
from chart_hop_python_sdk.apis.tags.budget_pool_api import BudgetPoolApi
from chart_hop_python_sdk.apis.tags.policy_api import PolicyApi
from chart_hop_python_sdk.apis.tags.profile_tab_api import ProfileTabApi
from chart_hop_python_sdk.apis.tags.report_chart_api import ReportChartApi
from chart_hop_python_sdk.apis.tags.band_api import BandApi
from chart_hop_python_sdk.apis.tags.customer_api import CustomerApi
from chart_hop_python_sdk.apis.tags.exchange_rate_api import ExchangeRateApi
from chart_hop_python_sdk.apis.tags.message_api import MessageApi
from chart_hop_python_sdk.apis.tags.oauth_api import OauthApi
from chart_hop_python_sdk.apis.tags.action_api import ActionApi
from chart_hop_python_sdk.apis.tags.category_sort_api import CategorySortApi
from chart_hop_python_sdk.apis.tags.comment_api import CommentApi
from chart_hop_python_sdk.apis.tags.form_response_api import FormResponseApi
from chart_hop_python_sdk.apis.tags.guideline_api import GuidelineApi
from chart_hop_python_sdk.apis.tags.role_api import RoleApi
from chart_hop_python_sdk.apis.tags.person_api import PersonApi
from chart_hop_python_sdk.apis.tags.category_api import CategoryApi
from chart_hop_python_sdk.apis.tags.data_view_api import DataViewApi
from chart_hop_python_sdk.apis.tags.email_template_api import EmailTemplateApi
from chart_hop_python_sdk.apis.tags.event_api import EventApi
from chart_hop_python_sdk.apis.tags.file_api import FileApi
from chart_hop_python_sdk.apis.tags.model_import_api import ModelImportApi
from chart_hop_python_sdk.apis.tags.job_level_api import JobLevelApi
from chart_hop_python_sdk.apis.tags.multiplier_api import MultiplierApi
from chart_hop_python_sdk.apis.tags.question_api import QuestionApi
from chart_hop_python_sdk.apis.tags.stripe_api import StripeApi
from chart_hop_python_sdk.apis.tags.webauthn_api import WebauthnApi
from chart_hop_python_sdk.apis.tags.app_config_api import AppConfigApi
from chart_hop_python_sdk.apis.tags.media_api import MediaApi
from chart_hop_python_sdk.apis.tags.product_api import ProductApi
from chart_hop_python_sdk.apis.tags.query_api import QueryApi
from chart_hop_python_sdk.apis.tags.saml_api import SamlApi
from chart_hop_python_sdk.apis.tags.stock_api import StockApi
from chart_hop_python_sdk.apis.tags.approval_request_api import ApprovalRequestApi
from chart_hop_python_sdk.apis.tags.billing_api import BillingApi
from chart_hop_python_sdk.apis.tags.org_config_api import OrgConfigApi
from chart_hop_python_sdk.apis.tags.task_config_api import TaskConfigApi
from chart_hop_python_sdk.apis.tags.expression_api import ExpressionApi
from chart_hop_python_sdk.apis.tags.legal_doc_api import LegalDocApi
from chart_hop_python_sdk.apis.tags.onboard_api import OnboardApi
from chart_hop_python_sdk.apis.tags.access_api import AccessApi
from chart_hop_python_sdk.apis.tags.ai_api import AiApi
from chart_hop_python_sdk.apis.tags.calendar_api import CalendarApi
from chart_hop_python_sdk.apis.tags.metric_api import MetricApi
from chart_hop_python_sdk.apis.tags.notification_api import NotificationApi
from chart_hop_python_sdk.apis.tags.preload_api import PreloadApi
from chart_hop_python_sdk.apis.tags.search_api import SearchApi
from chart_hop_python_sdk.apis.tags.status_api import StatusApi
from chart_hop_python_sdk.apis.tags.usage_api import UsageApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COMPREVIEW: CompReviewApi,
        TagValues.APP: AppApi,
        TagValues.APPROVAL: ApprovalApi,
        TagValues.FORM: FormApi,
        TagValues.CHANGE: ChangeApi,
        TagValues.ORG: OrgApi,
        TagValues.PROCESS: ProcessApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.USER: UserApi,
        TagValues.FIELD: FieldApi,
        TagValues.SCENARIO: ScenarioApi,
        TagValues.TABLE: TableApi,
        TagValues.REPORT: ReportApi,
        TagValues.ASSESSMENT: AssessmentApi,
        TagValues.EXPORT: ExportApi,
        TagValues.POSITION: PositionApi,
        TagValues.TASK: TaskApi,
        TagValues.GROUP: GroupApi,
        TagValues.JOB: JobApi,
        TagValues.CONTENT: ContentApi,
        TagValues.TIMEOFF: TimeoffApi,
        TagValues.BUDGETPOOL: BudgetPoolApi,
        TagValues.POLICY: PolicyApi,
        TagValues.PROFILETAB: ProfileTabApi,
        TagValues.REPORT_CHART: ReportChartApi,
        TagValues.BAND: BandApi,
        TagValues.CUSTOMER: CustomerApi,
        TagValues.EXCHANGERATE: ExchangeRateApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.OAUTH: OauthApi,
        TagValues.ACTION: ActionApi,
        TagValues.CATEGORYSORT: CategorySortApi,
        TagValues.COMMENT: CommentApi,
        TagValues.FORMRESPONSE: FormResponseApi,
        TagValues.GUIDELINE: GuidelineApi,
        TagValues.ROLE: RoleApi,
        TagValues.PERSON: PersonApi,
        TagValues.CATEGORY: CategoryApi,
        TagValues.DATAVIEW: DataViewApi,
        TagValues.EMAILTEMPLATE: EmailTemplateApi,
        TagValues.EVENT: EventApi,
        TagValues.FILE: FileApi,
        TagValues.IMPORT: ModelImportApi,
        TagValues.JOBLEVEL: JobLevelApi,
        TagValues.MULTIPLIER: MultiplierApi,
        TagValues.QUESTION: QuestionApi,
        TagValues.STRIPE: StripeApi,
        TagValues.WEBAUTHN: WebauthnApi,
        TagValues.APP_CONFIG: AppConfigApi,
        TagValues.MEDIA: MediaApi,
        TagValues.PRODUCT: ProductApi,
        TagValues.QUERY: QueryApi,
        TagValues.SAML: SamlApi,
        TagValues.STOCK: StockApi,
        TagValues.APPROVALREQUEST: ApprovalRequestApi,
        TagValues.BILLING: BillingApi,
        TagValues.ORGCONFIG: OrgConfigApi,
        TagValues.TASKCONFIG: TaskConfigApi,
        TagValues.EXPRESSION: ExpressionApi,
        TagValues.LEGAL_DOC: LegalDocApi,
        TagValues.ONBOARD: OnboardApi,
        TagValues.ACCESS: AccessApi,
        TagValues.AI: AiApi,
        TagValues.CALENDAR: CalendarApi,
        TagValues.METRIC: MetricApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.PRELOAD: PreloadApi,
        TagValues.SEARCH: SearchApi,
        TagValues.STATUS: StatusApi,
        TagValues.USAGE: UsageApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COMPREVIEW: CompReviewApi,
        TagValues.APP: AppApi,
        TagValues.APPROVAL: ApprovalApi,
        TagValues.FORM: FormApi,
        TagValues.CHANGE: ChangeApi,
        TagValues.ORG: OrgApi,
        TagValues.PROCESS: ProcessApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.USER: UserApi,
        TagValues.FIELD: FieldApi,
        TagValues.SCENARIO: ScenarioApi,
        TagValues.TABLE: TableApi,
        TagValues.REPORT: ReportApi,
        TagValues.ASSESSMENT: AssessmentApi,
        TagValues.EXPORT: ExportApi,
        TagValues.POSITION: PositionApi,
        TagValues.TASK: TaskApi,
        TagValues.GROUP: GroupApi,
        TagValues.JOB: JobApi,
        TagValues.CONTENT: ContentApi,
        TagValues.TIMEOFF: TimeoffApi,
        TagValues.BUDGETPOOL: BudgetPoolApi,
        TagValues.POLICY: PolicyApi,
        TagValues.PROFILETAB: ProfileTabApi,
        TagValues.REPORT_CHART: ReportChartApi,
        TagValues.BAND: BandApi,
        TagValues.CUSTOMER: CustomerApi,
        TagValues.EXCHANGERATE: ExchangeRateApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.OAUTH: OauthApi,
        TagValues.ACTION: ActionApi,
        TagValues.CATEGORYSORT: CategorySortApi,
        TagValues.COMMENT: CommentApi,
        TagValues.FORMRESPONSE: FormResponseApi,
        TagValues.GUIDELINE: GuidelineApi,
        TagValues.ROLE: RoleApi,
        TagValues.PERSON: PersonApi,
        TagValues.CATEGORY: CategoryApi,
        TagValues.DATAVIEW: DataViewApi,
        TagValues.EMAILTEMPLATE: EmailTemplateApi,
        TagValues.EVENT: EventApi,
        TagValues.FILE: FileApi,
        TagValues.IMPORT: ModelImportApi,
        TagValues.JOBLEVEL: JobLevelApi,
        TagValues.MULTIPLIER: MultiplierApi,
        TagValues.QUESTION: QuestionApi,
        TagValues.STRIPE: StripeApi,
        TagValues.WEBAUTHN: WebauthnApi,
        TagValues.APP_CONFIG: AppConfigApi,
        TagValues.MEDIA: MediaApi,
        TagValues.PRODUCT: ProductApi,
        TagValues.QUERY: QueryApi,
        TagValues.SAML: SamlApi,
        TagValues.STOCK: StockApi,
        TagValues.APPROVALREQUEST: ApprovalRequestApi,
        TagValues.BILLING: BillingApi,
        TagValues.ORGCONFIG: OrgConfigApi,
        TagValues.TASKCONFIG: TaskConfigApi,
        TagValues.EXPRESSION: ExpressionApi,
        TagValues.LEGAL_DOC: LegalDocApi,
        TagValues.ONBOARD: OnboardApi,
        TagValues.ACCESS: AccessApi,
        TagValues.AI: AiApi,
        TagValues.CALENDAR: CalendarApi,
        TagValues.METRIC: MetricApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.PRELOAD: PreloadApi,
        TagValues.SEARCH: SearchApi,
        TagValues.STATUS: StatusApi,
        TagValues.USAGE: UsageApi,
    }
)
