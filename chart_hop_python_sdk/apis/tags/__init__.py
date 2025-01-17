# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from chart_hop_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    COMPREVIEW = "comp-review"
    APP = "app"
    APPROVAL = "approval"
    FORM = "form"
    CHANGE = "change"
    ORG = "org"
    PROCESS = "process"
    TEMPLATE = "template"
    USER = "user"
    FIELD = "field"
    SCENARIO = "scenario"
    TABLE = "table"
    REPORT = "report"
    ASSESSMENT = "assessment"
    EXPORT = "export"
    POSITION = "position"
    TASK = "task"
    GROUP = "group"
    JOB = "job"
    CONTENT = "content"
    TIMEOFF = "timeoff"
    BUDGETPOOL = "budget-pool"
    POLICY = "policy"
    PROFILETAB = "profile-tab"
    REPORT_CHART = "reportChart"
    BAND = "band"
    CUSTOMER = "customer"
    EXCHANGERATE = "exchange-rate"
    MESSAGE = "message"
    OAUTH = "oauth"
    ACTION = "action"
    CATEGORYSORT = "category-sort"
    COMMENT = "comment"
    FORMRESPONSE = "form-response"
    GUIDELINE = "guideline"
    ROLE = "role"
    PERSON = "person"
    CATEGORY = "category"
    DATAVIEW = "data-view"
    EMAILTEMPLATE = "email-template"
    EVENT = "event"
    FILE = "file"
    IMPORT = "import"
    JOBLEVEL = "job-level"
    MULTIPLIER = "multiplier"
    QUESTION = "question"
    STRIPE = "stripe"
    WEBAUTHN = "webauthn"
    APP_CONFIG = "appConfig"
    MEDIA = "media"
    PRODUCT = "product"
    QUERY = "query"
    SAML = "saml"
    STOCK = "stock"
    APPROVALREQUEST = "approval-request"
    BILLING = "billing"
    ORGCONFIG = "org-config"
    TASKCONFIG = "task-config"
    EXPRESSION = "expression"
    LEGAL_DOC = "legalDoc"
    ONBOARD = "onboard"
    ACCESS = "access"
    AI = "ai"
    CALENDAR = "calendar"
    METRIC = "metric"
    NOTIFICATION = "notification"
    PRELOAD = "preload"
    SEARCH = "search"
    STATUS = "status"
    USAGE = "usage"
