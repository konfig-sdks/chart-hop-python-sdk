operation_parameter_map = {
    '/v1/org/{orgId}/access/entity/{type}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'id'
            },
            {
                'name': 'action'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'date'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/action-POST': {
        'parameters': [
            {
                'name': 'action'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'stepTaskConfigs'
            },
        ]
    },
    '/v1/org/{orgId}/action/{actionId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'actionId'
            },
        ]
    },
    '/v1/org/{orgId}/action/{actionId}/run-POST': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'eventCode'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'actionId'
            },
        ]
    },
    '/v1/org/{orgId}/action/{actionId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'actionId'
            },
        ]
    },
    '/v1/org/{orgId}/action-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/action/{actionId}-PATCH': {
        'parameters': [
            {
                'name': 'action'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'actionId'
            },
            {
                'name': 'stepTaskConfigs'
            },
        ]
    },
    '/v1/org/{orgId}/ai/form-response/summary-POST': {
        'parameters': [
            {
                'name': 'questionId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'assessmentId'
            },
        ]
    },
    '/v1/app-POST': {
        'parameters': [
            {
                'name': 'summary'
            },
            {
                'name': 'title'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'cronOrder'
            },
            {
                'name': 'minAccess'
            },
            {
                'name': 'type'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'redirectUris'
            },
            {
                'name': 'allowedIps'
            },
            {
                'name': 'configFields'
            },
            {
                'name': 'setupInstructions'
            },
            {
                'name': 'cronSchedule'
            },
            {
                'name': 'cronDayOfWeek'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'wordmarkImagePath'
            },
            {
                'name': 'poweredByImagePath'
            },
            {
                'name': 'status'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'eventNotifyUrl'
            },
            {
                'name': 'payload'
            },
            {
                'name': 'events'
            },
            {
                'name': 'bundle'
            },
            {
                'name': 'scopes'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/{appUserId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
        ]
    },
    '/v1/app/org/{orgId}/install-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'includeFormer'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/{appUserId}/token-POST': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
        ]
    },
    '/v1/app/org/{orgId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'q'
            },
            {
                'name': 'type'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/app/{appId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/v1/app/name/{appName}-GET': {
        'parameters': [
            {
                'name': 'appName'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/name/{appName}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appName'
            },
            {
                'name': 'includeInactive'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/{appUserId}/code-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/{appUserId}/token-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/{appUserId}/installdata/{installDataName}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
            {
                'name': 'installDataName'
            },
        ]
    },
    '/v1/app/org/{orgId}/install-POST': {
        'parameters': [
            {
                'name': 'orgs'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'status'
            },
            {
                'name': 'options'
            },
            {
                'name': 'internalOptions'
            },
            {
                'name': 'secrets'
            },
            {
                'name': 'emailSettings'
            },
        ]
    },
    '/v1/app-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/app/{appId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/{appUserId}/run-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
        ]
    },
    '/v1/app/notify-POST': {
        'parameters': [
            {
                'name': 'emailSubject'
            },
            {
                'name': 'emailContentHtml'
            },
            {
                'name': 'emailMarkdown'
            },
            {
                'name': 'chatMarkdown'
            },
            {
                'name': 'notifyType'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/{appUserId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
            {
                'name': 'keepEntityIds'
            },
        ]
    },
    '/v1/app/{appId}-PATCH': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'summary'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'redirectUris'
            },
            {
                'name': 'allowedIps'
            },
            {
                'name': 'configFields'
            },
            {
                'name': 'setupInstructions'
            },
            {
                'name': 'cronOrder'
            },
            {
                'name': 'cronSchedule'
            },
            {
                'name': 'cronDayOfWeek'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'wordmarkImagePath'
            },
            {
                'name': 'poweredByImagePath'
            },
            {
                'name': 'status'
            },
            {
                'name': 'minAccess'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'eventNotifyUrl'
            },
            {
                'name': 'payload'
            },
            {
                'name': 'events'
            },
            {
                'name': 'type'
            },
            {
                'name': 'bundle'
            },
            {
                'name': 'scopes'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/{appUserId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'orgs'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'status'
            },
            {
                'name': 'options'
            },
            {
                'name': 'internalOptions'
            },
            {
                'name': 'secrets'
            },
            {
                'name': 'emailSettings'
            },
            {
                'name': 'includeInactive'
            },
        ]
    },
    '/v1/app/org/{orgId}/install/validate-POST': {
        'parameters': [
            {
                'name': 'orgs'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'status'
            },
            {
                'name': 'options'
            },
            {
                'name': 'internalOptions'
            },
            {
                'name': 'secrets'
            },
            {
                'name': 'emailSettings'
            },
        ]
    },
    '/v1/app-config-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'fieldMappers'
            },
            {
                'name': 'customFieldMappers'
            },
            {
                'name': 'customOutboundFieldMappers'
            },
            {
                'name': 'disabledFieldMappers'
            },
            {
                'name': 'enabledOutboundFieldMappers'
            },
            {
                'name': 'templateMatchers'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/v1/app-config/{appId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/v1/app-config/{appId}/{userId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/v1/app-config/{appId}/{userId}-PATCH': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'fieldMappers'
            },
            {
                'name': 'customFieldMappers'
            },
            {
                'name': 'customOutboundFieldMappers'
            },
            {
                'name': 'disabledFieldMappers'
            },
            {
                'name': 'enabledOutboundFieldMappers'
            },
            {
                'name': 'templateMatchers'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'isPreview'
            },
            {
                'name': 'approvalNotifierUserIds'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'fallbackApproverJobId'
            },
            {
                'name': 'fallbackApproverJobError'
            },
            {
                'name': 'createDefaultStages'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/stage-POST': {
        'parameters': [
            {
                'name': 'rejectBehavior'
            },
            {
                'name': 'status'
            },
            {
                'name': 'approvalCommentRequired'
            },
            {
                'name': 'rejectionCommentRequired'
            },
            {
                'name': 'order'
            },
            {
                'name': 'groups'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'inclusionExpression'
            },
            {
                'name': 'inclusionBehavior'
            },
            {
                'name': 'expandExpression'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request-POST': {
        'parameters': [
            {
                'name': 'entityId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'dryRun'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/stage/{approvalChainStageId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'approvalChainStageId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'approvalRequestId'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/create-default-chain-POST': {
        'parameters': [
            {
                'name': 'entityType'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'entityIds'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/stage/{approvalChainStageId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'approvalChainStageId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/stage-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request/entity/comp-review-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'entityIds'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request/entity/scenario-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'entityIds'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}/reassign-approver-POST': {
        'parameters': [
            {
                'name': 'stageOrder'
            },
            {
                'name': 'initialJobId'
            },
            {
                'name': 'reassignJobId'
            },
            {
                'name': 'message'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'approvalRequestId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'approvalRequestId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}/send-reminder-POST': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'approvalRequestId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'isPreview'
            },
            {
                'name': 'fallbackApproverJobId'
            },
            {
                'name': 'fallbackApproverJobError'
            },
            {
                'name': 'approvalNotifierUserIds'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}-PATCH': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'approvalRequestId'
            },
            {
                'name': 'message'
            },
            {
                'name': 'previewJobId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-chain/{approvalChainId}/stage/{approvalChainStageId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'approvalChainStageId'
            },
            {
                'name': 'inclusionExpression'
            },
            {
                'name': 'inclusionBehavior'
            },
            {
                'name': 'expandExpression'
            },
            {
                'name': 'rejectBehavior'
            },
            {
                'name': 'status'
            },
            {
                'name': 'approvalCommentRequired'
            },
            {
                'name': 'rejectionCommentRequired'
            },
            {
                'name': 'order'
            },
            {
                'name': 'groups'
            },
        ]
    },
    '/v1/org/{orgId}/approval-request/entity/scenario-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'entityIds'
            },
            {
                'name': 'includeDeleted'
            },
        ]
    },
    '/v1/org/{orgId}/approval-request/scenario-job/{jobId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/org/{orgId}/approval-request/{approvalRequestId}/scenario-response-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'approvalRequestId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/bulk/delete-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/bulk/duplicate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/{assessmentId}/complete-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'type'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'color'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'doneAt'
            },
            {
                'name': 'taskCount'
            },
            {
                'name': 'taskDoneCount'
            },
            {
                'name': 'peopleIncludedCount'
            },
            {
                'name': 'query'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/{assessmentId}/form/{formId}/expire-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'formId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/{assessmentId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/{assessmentId}/reactivate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/{assessmentId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/bulk/move-POST': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'type'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/assessment/{assessmentId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'type'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'color'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'doneAt'
            },
            {
                'name': 'taskCount'
            },
            {
                'name': 'taskDoneCount'
            },
            {
                'name': 'peopleIncludedCount'
            },
            {
                'name': 'query'
            },
            {
                'name': 'silent'
            },
        ]
    },
    '/v1/org/{orgId}/band-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'color'
            },
            {
                'name': 'baseInterval'
            },
            {
                'name': 'jobLevel'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'baseCompMax'
            },
            {
                'name': 'baseCompMid'
            },
            {
                'name': 'baseCompMin'
            },
            {
                'name': 'baseSpread'
            },
            {
                'name': 'baseTargetPay'
            },
            {
                'name': 'baseTargetPayPercentile'
            },
            {
                'name': 'equityTargetShares'
            },
            {
                'name': 'equityTargetPercentOfBase'
            },
            {
                'name': 'equityTargetValue'
            },
            {
                'name': 'variableValue'
            },
            {
                'name': 'variablePercentOfBase'
            },
            {
                'name': 'jobTierOneField'
            },
            {
                'name': 'jobTierTwoField'
            },
            {
                'name': 'jobTierThreeField'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/band-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/band/reset-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/band/{bandId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'bandId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/band-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'includeDeleted'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/band/{bandId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'bandId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/band/{bandId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'bandId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'color'
            },
            {
                'name': 'baseCompMax'
            },
            {
                'name': 'baseCompMid'
            },
            {
                'name': 'baseCompMin'
            },
            {
                'name': 'baseSpread'
            },
            {
                'name': 'baseInterval'
            },
            {
                'name': 'baseTargetPay'
            },
            {
                'name': 'baseTargetPayPercentile'
            },
            {
                'name': 'equityTargetShares'
            },
            {
                'name': 'equityTargetPercentOfBase'
            },
            {
                'name': 'equityTargetValue'
            },
            {
                'name': 'variableValue'
            },
            {
                'name': 'variablePercentOfBase'
            },
            {
                'name': 'jobTierOneField'
            },
            {
                'name': 'jobTierTwoField'
            },
            {
                'name': 'jobTierThreeField'
            },
            {
                'name': 'jobLevel'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/customer/{customerId}/billing/cancel-POST': {
        'parameters': [
            {
                'name': 'otherComments'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'customerId'
            },
        ]
    },
    '/v1/customer/{customerId}/billing-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/v1/customer/{customerId}/billing/checkout-POST': {
        'parameters': [
            {
                'name': 'paymentMethod'
            },
            {
                'name': 'customerId'
            },
        ]
    },
    '/v1/org/{orgId}/budget-pool/{id}/calculate-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/budget-pool/{id}/preview-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v1/org/{orgId}/budget-pool-POST': {
        'parameters': [
            {
                'name': 'compReviewId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'appliedField'
            },
            {
                'name': 'sourceField'
            },
            {
                'name': 'basisType'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'participantsExpr'
            },
            {
                'name': 'fixedAmount'
            },
            {
                'name': 'fixedValue'
            },
            {
                'name': 'basisFieldMatrix'
            },
            {
                'name': 'fixedBudgetMap'
            },
            {
                'name': 'basisExpr'
            },
            {
                'name': 'defaultCurrency'
            },
        ]
    },
    '/v1/org/{orgId}/budget-pool/{id}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v1/org/{orgId}/budget-pool-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/budget-pool/{id}/guidelines-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v1/org/{orgId}/budget-pool/{id}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v1/org/{orgId}/budget-pool/{id}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'label'
            },
            {
                'name': 'participantsExpr'
            },
            {
                'name': 'appliedField'
            },
            {
                'name': 'sourceField'
            },
            {
                'name': 'basisType'
            },
            {
                'name': 'fixedAmount'
            },
            {
                'name': 'fixedValue'
            },
            {
                'name': 'basisFieldMatrix'
            },
            {
                'name': 'fixedBudgetMap'
            },
            {
                'name': 'basisExpr'
            },
            {
                'name': 'defaultCurrency'
            },
        ]
    },
    '/v1/org/{orgId}/calendar-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'type'
            },
            {
                'name': 'q'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v1/org/{orgId}/category-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'fieldIds'
            },
            {
                'name': 'nativeFields'
            },
        ]
    },
    '/v1/org/{orgId}/category-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'unsorted'
            },
        ]
    },
    '/v1/org/{orgId}/category/{categoryId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'categoryId'
            },
        ]
    },
    '/v1/org/{orgId}/category/{categoryId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'categoryId'
            },
        ]
    },
    '/v1/org/{orgId}/category/{categoryId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'fieldIds'
            },
            {
                'name': 'nativeFields'
            },
        ]
    },
    '/v1/org/{orgId}/category-sort-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'categoryIds'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/category-sort-PUT': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'categoryIds'
            },
        ]
    },
    '/v1/org/{orgId}/category-sort/upsert-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'categoryIds'
            },
        ]
    },
    '/v1/org/{orgId}/category-sort-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/category-sort-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/category-sort-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'categoryIds'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}/change/{changeId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'changeId'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'includeUpdatedFields'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v1/org/{orgId}/change/{changeId}/approve-POST': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'changeId'
            },
            {
                'name': 'approvalNote'
            },
            {
                'name': 'changeId'
            },
        ]
    },
    '/v1/org/{orgId}/change/bulkupdate-POST': {
        'parameters': [
            {
                'name': 'jobIds'
            },
            {
                'name': 'update'
            },
            {
                'name': 'date'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/v1/org/{orgId}/change/{changeId}/approver-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'changeId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/change/depart-rehire-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'otherJobId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'date'
            },
            {
                'name': 'announceDate'
            },
            {
                'name': 'departType'
            },
            {
                'name': 'departRegret'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'promotionType'
            },
            {
                'name': 'job'
            },
            {
                'name': 'update'
            },
            {
                'name': 'note'
            },
            {
                'name': 'startDate'
            },
        ]
    },
    '/v1/org/{orgId}/change/sync/{type}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'otherJobId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'date'
            },
            {
                'name': 'announceDate'
            },
            {
                'name': 'departType'
            },
            {
                'name': 'departRegret'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'promotionType'
            },
            {
                'name': 'job'
            },
            {
                'name': 'update'
            },
            {
                'name': 'note'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/change/{type}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'otherJobId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'date'
            },
            {
                'name': 'announceDate'
            },
            {
                'name': 'departType'
            },
            {
                'name': 'departRegret'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'promotionType'
            },
            {
                'name': 'job'
            },
            {
                'name': 'update'
            },
            {
                'name': 'note'
            },
            {
                'name': 'source'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/change/{changeId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'changeId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/change/scenario/{scenarioId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
            {
                'name': 'q'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/change/{changeId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'changeId'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/change/{changeId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'changeId'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v1/org/{orgId}/change-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'type'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'includeBackfill'
            },
            {
                'name': 'refs'
            },
            {
                'name': 'q'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'open'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'scenarioOnly'
            },
            {
                'name': 'parentOnly'
            },
            {
                'name': 'includeGrantSchedule'
            },
            {
                'name': 'excludeAtsRecruitingFields'
            },
            {
                'name': 'includeStruck'
            },
            {
                'name': 'status'
            },
            {
                'name': 'stripUpdates'
            },
            {
                'name': 'format'
            },
            {
                'name': 'fieldEntityTypes'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v2/org/{orgId}/change-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'status'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'fieldsChanged'
            },
            {
                'name': 'q'
            },
            {
                'name': 'open'
            },
            {
                'name': 'includeGrantSchedule'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'format'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}/change/{changeId}/status/{processId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'changeId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/change/bulkchange-POST': {
        'parameters': [
            {
                'name': 'changes'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/change/{changeId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'changeId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'announceDate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'departType'
            },
            {
                'name': 'departRegret'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'promotionType'
            },
            {
                'name': 'job'
            },
            {
                'name': 'update'
            },
            {
                'name': 'note'
            },
            {
                'name': 'approvalNote'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/change/{type}/validate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'otherJobId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'date'
            },
            {
                'name': 'announceDate'
            },
            {
                'name': 'departType'
            },
            {
                'name': 'departRegret'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'promotionType'
            },
            {
                'name': 'job'
            },
            {
                'name': 'update'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/v1/org/{orgId}/comment-POST': {
        'parameters': [
            {
                'name': 'entityId'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'content'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'parentEntityId'
            },
        ]
    },
    '/v1/org/{orgId}/comment/entity/{entityId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'desc'
            },
        ]
    },
    '/v1/org/{orgId}/comment/{commentId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'commentId'
            },
        ]
    },
    '/v1/org/{orgId}/comment/comp-review/{compReviewId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'approvalRequestId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'isPreview'
            },
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/org/{orgId}/comment/scenario/{scenarioId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'includeChangeComments'
            },
        ]
    },
    '/v1/org/{orgId}/comment/{commentId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'commentId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/conclude-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'isFullyApproved'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/bulk/duplicate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'config'
            },
            {
                'name': 'status'
            },
            {
                'name': 'shareAccess'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/visualizations-POST': {
        'parameters': [
            {
                'name': 'isCollabicientView'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'changeIds'
            },
            {
                'name': 'viewInCurrency'
            },
            {
                'name': 'includeCollaborators'
            },
            {
                'name': 'viewJobId'
            },
            {
                'name': 'preview'
            },
            {
                'name': 'includeAllRequests'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/bulk/delete-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/duplicate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/export/audit-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/export-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/export/comments-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/generate-POST': {
        'parameters': [
            {
                'name': 'isPreview'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/preview-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/in-cycle/changes/{changeId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'changeId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/in-cycle/changes-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'approvalRequestId'
            },
            {
                'name': 'isPreview'
            },
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/in-cycle/collabicient-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'scenariosOnly'
            },
            {
                'name': 'proposalOnly'
            },
            {
                'name': 'reviewsOnly'
            },
            {
                'name': 'columnsOnly'
            },
            {
                'name': 'isPreview'
            },
            {
                'name': 'collabicientJobId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/associated-entities-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/eligible-employees-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'filterScenarioIds'
            },
            {
                'name': 'ineligible'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/metadata-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/approval-requests-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'isPreview'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/in-cycle-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'scenariosOnly'
            },
            {
                'name': 'proposalOnly'
            },
            {
                'name': 'reviewsOnly'
            },
            {
                'name': 'columnsOnly'
            },
            {
                'name': 'isPreview'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'includeAllRequests'
            },
            {
                'name': 'includeFeatures'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/pause-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/send-reminder-email-POST': {
        'parameters': [
            {
                'name': 'approvalRequestId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}/approval-requests/{approvalRequestId}-PATCH': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'approvalRequestId'
            },
            {
                'name': 'message'
            },
            {
                'name': 'previewJobId'
            },
            {
                'name': 'isFinalApproval'
            },
            {
                'name': 'collaboratorSelectedReviewerJobId'
            },
        ]
    },
    '/v1/org/{orgId}/comp-review/{compReviewId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'config'
            },
            {
                'name': 'status'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'reviewerCount'
            },
            {
                'name': 'submittedCount'
            },
        ]
    },
    '/v1/org/{orgId}/content-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'parentContentId'
            },
            {
                'name': 'path'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'emoji'
            },
            {
                'name': 'coverImagePath'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/org/{orgId}/content/{contentId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'contentId'
            },
        ]
    },
    '/v1/org/{orgId}/content/path/{path}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'path'
            },
        ]
    },
    '/v1/org/{orgId}/content-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/content/{contentId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'contentId'
            },
        ]
    },
    '/v1/org/{orgId}/content/path/{path}/render-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'path'
            },
        ]
    },
    '/v1/org/{orgId}/content/homepage/render-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/content/homepage-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'parentContentId'
            },
            {
                'name': 'path'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'emoji'
            },
            {
                'name': 'coverImagePath'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/org/{orgId}/content/{contentId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'contentId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'parentContentId'
            },
            {
                'name': 'path'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'emoji'
            },
            {
                'name': 'coverImagePath'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/customer-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'billAddress'
            },
            {
                'name': 'industry'
            },
            {
                'name': 'source'
            },
            {
                'name': 'status'
            },
            {
                'name': 'salesforceAccountId'
            },
            {
                'name': 'products'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'nextInvoiceDate'
            },
            {
                'name': 'primaryHeadCountFilter'
            },
            {
                'name': 'secondaryHeadCountFilter'
            },
            {
                'name': 'arr'
            },
            {
                'name': 'projectedArr'
            },
            {
                'name': 'trialStartDate'
            },
            {
                'name': 'trialEndDate'
            },
            {
                'name': 'stripeSubscriptionSync'
            },
        ]
    },
    '/v1/customer/{customerId}/invoices-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/v1/customer/{customerId}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/v1/customer/{customerId}/subscription-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/v1/customer-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/customer/{customerId}-PATCH': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'billAddress'
            },
            {
                'name': 'industry'
            },
            {
                'name': 'source'
            },
            {
                'name': 'status'
            },
            {
                'name': 'salesforceAccountId'
            },
            {
                'name': 'products'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'nextInvoiceDate'
            },
            {
                'name': 'primaryHeadCountFilter'
            },
            {
                'name': 'secondaryHeadCountFilter'
            },
            {
                'name': 'arr'
            },
            {
                'name': 'projectedArr'
            },
            {
                'name': 'trialStartDate'
            },
            {
                'name': 'trialEndDate'
            },
            {
                'name': 'stripeSubscriptionSync'
            },
        ]
    },
    '/v1/customer/{customerId}/subscription-PATCH': {
        'parameters': [
            {
                'name': 'paymentMethod'
            },
            {
                'name': 'customerId'
            },
        ]
    },
    '/v1/org/{orgId}/data-view-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'type'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'columnWidths'
            },
            {
                'name': 'date'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'groupBy'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'sensitive'
            },
        ]
    },
    '/v1/org/{orgId}/data-view/{dataViewId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'dataViewId'
            },
        ]
    },
    '/v1/org/{orgId}/data-view-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'type'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/data-view/{dataViewId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'dataViewId'
            },
        ]
    },
    '/v1/org/{orgId}/data-view/{dataViewId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'dataViewId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'type'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'columnWidths'
            },
            {
                'name': 'date'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'groupBy'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'sensitive'
            },
        ]
    },
    '/v1/email-template-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'category'
            },
        ]
    },
    '/v1/email-template/non-essential-GET': {
        'parameters': [
        ]
    },
    '/v1/email-template/name/{name}-GET': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/v1/email-template/essential-GET': {
        'parameters': [
        ]
    },
    '/v1/email-template/{emailTemplateId}-PATCH': {
        'parameters': [
            {
                'name': 'emailTemplateId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'category'
            },
        ]
    },
    '/v1/org/{orgId}/event/notify/inbound/{appId}/{inboundId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'inboundId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/event/notify/outbound/app/{appId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/event/{eventId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'eventId'
            },
        ]
    },
    '/v1/org/{orgId}/event-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'parentEntityId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'processId'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'code'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/event/{eventId}/notify-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'eventId'
            },
            {
                'name': 'app'
            },
        ]
    },
    '/v1/org/{orgId}/exchange-rate/{date}/custom/bulkupdate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'addRates'
            },
        ]
    },
    '/v1/org/{orgId}/exchange-rate/{date}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'currencyCode'
            },
        ]
    },
    '/v1/org/{orgId}/exchange-rate/{date}/custom-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/exchange-rate/{date}/global-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/exchange-rate/{date}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/exchange-rate/{date}/history-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'toDate'
            },
        ]
    },
    '/v1/org/{orgId}/exchange-rate/{date}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'date'
            },
            {
                'name': 'rates'
            },
        ]
    },
    '/v1/org/{orgId}/export/csv/change-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/export/csv/fields-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/export/csv/scenario/{scenarioId}/comments-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/export/zip/file-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'field'
            },
            {
                'name': 'date'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'q'
            },
            {
                'name': 'size'
            },
        ]
    },
    '/v1/org/{orgId}/export/powerpoint/org-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/export/pdf/review/{assessmentId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
        ]
    },
    '/v1/org/{orgId}/export/powerpoint/report/{reportId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
        ]
    },
    '/v1/org/{orgId}/export/csv/snapshot-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/export/csv/scenario/{scenarioId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/export/csv/task/{reviewId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reviewId'
            },
        ]
    },
    '/v1/org/{orgId}/export/csv/users-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/cql/evaluate-POST': {
        'parameters': [
            {
                'name': 'expr'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/cql/validate-POST': {
        'parameters': [
            {
                'name': 'expressions'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/field-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'label'
            },
            {
                'name': 'type'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'isUnique'
            },
            {
                'name': 'isRequired'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'question'
            },
            {
                'name': 'inUse'
            },
            {
                'name': 'expr'
            },
            {
                'name': 'exprType'
            },
            {
                'name': 'plural'
            },
            {
                'name': 'values'
            },
            {
                'name': 'defaultValue'
            },
            {
                'name': 'options'
            },
            {
                'name': 'hideExpr'
            },
            {
                'name': 'expireDays'
            },
            {
                'name': 'status'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'tableRef'
            },
            {
                'name': 'isEffectiveDated'
            },
            {
                'name': 'dataFetchTypes'
            },
            {
                'name': 'aliases'
            },
            {
                'name': 'calc'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'classification'
            },
            {
                'name': 'places'
            },
            {
                'name': 'tableType'
            },
        ]
    },
    '/v1/org/{orgId}/field-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'table'
            },
            {
                'name': 'tableType'
            },
            {
                'name': 'form'
            },
            {
                'name': 'builtin'
            },
            {
                'name': 'includeTtst'
            },
        ]
    },
    '/v1/org/{orgId}/field/built-in-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/field/{fieldId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fieldId'
            },
        ]
    },
    '/v1/org/{orgId}/field/category/{categoryId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'categoryId'
            },
        ]
    },
    '/v1/org/{orgId}/field/category-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/field/delete-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/field/{fieldId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fieldId'
            },
        ]
    },
    '/v1/org/{orgId}/field/remove-overrides-POST': {
        'parameters': [
            {
                'name': 'fieldIds'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/field/remove-category-POST': {
        'parameters': [
            {
                'name': 'fieldIds'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/field/{fieldId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'label'
            },
            {
                'name': 'question'
            },
            {
                'name': 'inUse'
            },
            {
                'name': 'expr'
            },
            {
                'name': 'exprType'
            },
            {
                'name': 'type'
            },
            {
                'name': 'plural'
            },
            {
                'name': 'values'
            },
            {
                'name': 'defaultValue'
            },
            {
                'name': 'options'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'hideExpr'
            },
            {
                'name': 'expireDays'
            },
            {
                'name': 'status'
            },
            {
                'name': 'tableRef'
            },
            {
                'name': 'isUnique'
            },
            {
                'name': 'isRequired'
            },
            {
                'name': 'isEffectiveDated'
            },
            {
                'name': 'dataFetchTypes'
            },
            {
                'name': 'aliases'
            },
            {
                'name': 'calc'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'classification'
            },
            {
                'name': 'places'
            },
        ]
    },
    '/v1/org/{orgId}/field/{fieldId}/dryrun-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'label'
            },
            {
                'name': 'question'
            },
            {
                'name': 'inUse'
            },
            {
                'name': 'expr'
            },
            {
                'name': 'exprType'
            },
            {
                'name': 'type'
            },
            {
                'name': 'plural'
            },
            {
                'name': 'values'
            },
            {
                'name': 'defaultValue'
            },
            {
                'name': 'options'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'hideExpr'
            },
            {
                'name': 'expireDays'
            },
            {
                'name': 'status'
            },
            {
                'name': 'tableRef'
            },
            {
                'name': 'isUnique'
            },
            {
                'name': 'isRequired'
            },
            {
                'name': 'isEffectiveDated'
            },
            {
                'name': 'dataFetchTypes'
            },
            {
                'name': 'aliases'
            },
            {
                'name': 'calc'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'classification'
            },
            {
                'name': 'places'
            },
        ]
    },
    '/v1/org/{orgId}/field/status-POST': {
        'parameters': [
            {
                'name': 'updateStatus'
            },
            {
                'name': 'fieldIds'
            },
            {
                'name': 'reservedFieldNames'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/file-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/v1/org/{orgId}/file/{fileId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/v1/org/{orgId}/file/{fileId}/download-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/v1/org/{orgId}/file/{fileId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/v1/org/{orgId}/file-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'field'
            },
            {
                'name': 'sensitive'
            },
        ]
    },
    '/v1/org/{orgId}/form-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'status'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'type'
            },
            {
                'name': 'targetType'
            },
            {
                'name': 'targetFilter'
            },
            {
                'name': 'submitFilter'
            },
            {
                'name': 'responseReadFilter'
            },
            {
                'name': 'useFieldAccess'
            },
            {
                'name': 'approval'
            },
            {
                'name': 'authorSensitive'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
        ]
    },
    '/v1/org/{orgId}/form/delete-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/form/draft/{draftId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'draftId'
            },
        ]
    },
    '/v1/org/{orgId}/form/person/{personId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'personId'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'evalJobId'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}/draft-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'personId'
            },
        ]
    },
    '/v1/org/{orgId}/form/available-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'targetType'
            },
        ]
    },
    '/v1/org/{orgId}/form-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}/render-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'targetType'
            },
            {
                'name': 'formResponseId'
            },
            {
                'name': 'formResponseChangeId'
            },
            {
                'name': 'formVersionId'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}/rerender/question/{updateQuestionId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'updateQuestionId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'targetType'
            },
            {
                'name': 'formVersionId'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}/collect-POST': {
        'parameters': [
            {
                'name': 'preview'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'targetFilter'
            },
            {
                'name': 'submitFilter'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}/remind-POST': {
        'parameters': [
            {
                'name': 'preview'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'targetFilter'
            },
            {
                'name': 'submitFilter'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}/draft-POST': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'blocksData'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}/submit-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'targetType'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}/submit/draft-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'targetType'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}-POST': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'blocksData'
            },
        ]
    },
    '/v1/org/{orgId}/form/{formId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'label'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'targetType'
            },
            {
                'name': 'targetFilter'
            },
            {
                'name': 'submitFilter'
            },
            {
                'name': 'responseReadFilter'
            },
            {
                'name': 'useFieldAccess'
            },
            {
                'name': 'approval'
            },
            {
                'name': 'authorSensitive'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/v1/org/{orgId}/form/status-POST': {
        'parameters': [
            {
                'name': 'updateStatus'
            },
            {
                'name': 'formIds'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/form-response-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'submitPersonId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'returnAccess'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v1/org/{orgId}/form-response/{formResponseId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formResponseId'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v1/org/{orgId}/form-response/count-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'submitPersonId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'questionId'
            },
        ]
    },
    '/v1/org/{orgId}/form-response/{formResponseId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formResponseId'
            },
        ]
    },
    '/v1/org/{orgId}/form-response/{formResponseId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formResponseId'
            },
        ]
    },
    '/v1/org/{orgId}/form-response/{formResponseId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'formResponseId'
            },
            {
                'name': 'shareAccess'
            },
        ]
    },
    '/v2/org/{orgId}/group/{type}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/group/graph-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'start'
            },
            {
                'name': 'depth'
            },
            {
                'name': 'groupApproxLimit'
            },
            {
                'name': 'jobLimit'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'jobFilter'
            },
            {
                'name': 'groupFilter'
            },
            {
                'name': 'date'
            },
            {
                'name': 'groupFields'
            },
            {
                'name': 'jobFields'
            },
            {
                'name': 'positionFields'
            },
            {
                'name': 'kind'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/group/{type}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'jobFields'
            },
            {
                'name': 'positionFields'
            },
            {
                'name': 'includeAll'
            },
            {
                'name': 'search'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/group/orphaned-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'start'
            },
            {
                'name': 'groupLimit'
            },
            {
                'name': 'jobLimit'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'jobFilter'
            },
            {
                'name': 'groupFilter'
            },
            {
                'name': 'date'
            },
            {
                'name': 'groupFields'
            },
            {
                'name': 'jobFields'
            },
            {
                'name': 'positionFields'
            },
            {
                'name': 'kind'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/group/{type}/{groupId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'jobFields'
            },
            {
                'name': 'positionFields'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/group/count-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'groupFilter'
            },
            {
                'name': 'date'
            },
            {
                'name': 'kind'
            },
        ]
    },
    '/v2/org/{orgId}/group/{type}/import-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'file'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/group/{type}/bulk-delete-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v2/org/{orgId}/group/{type}/{groupId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/group/{type}/{groupId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/guideline-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'includeDeleted'
            },
        ]
    },
    '/v1/org/{orgId}/guideline/{id}/calculate-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v1/org/{orgId}/guideline-POST': {
        'parameters': [
            {
                'name': 'compReviewId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'appliedField'
            },
            {
                'name': 'sourceField'
            },
            {
                'name': 'calculationType'
            },
            {
                'name': 'flagMode'
            },
            {
                'name': 'enablePopulateValue'
            },
            {
                'name': 'basisType'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'budgetPoolId'
            },
            {
                'name': 'participantsExpr'
            },
            {
                'name': 'flagDeviationThreshold'
            },
            {
                'name': 'basisExpr'
            },
            {
                'name': 'basisFieldMatrix'
            },
            {
                'name': 'fixedAmountRange'
            },
            {
                'name': 'fixedValueRange'
            },
        ]
    },
    '/v1/org/{orgId}/guideline/{id}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v1/org/{orgId}/guideline/{id}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v1/org/{orgId}/guideline/{id}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'label'
            },
            {
                'name': 'budgetPoolId'
            },
            {
                'name': 'participantsExpr'
            },
            {
                'name': 'appliedField'
            },
            {
                'name': 'sourceField'
            },
            {
                'name': 'calculationType'
            },
            {
                'name': 'flagMode'
            },
            {
                'name': 'flagDeviationThreshold'
            },
            {
                'name': 'enablePopulateValue'
            },
            {
                'name': 'basisType'
            },
            {
                'name': 'basisExpr'
            },
            {
                'name': 'basisFieldMatrix'
            },
            {
                'name': 'fixedAmountRange'
            },
            {
                'name': 'fixedValueRange'
            },
        ]
    },
    '/v1/org/{orgId}/import/csv/data-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'skipErrors'
            },
            {
                'name': 'upsert'
            },
            {
                'name': 'createGroups'
            },
            {
                'name': 'disableSyncHireDate'
            },
            {
                'name': 'updateTypes'
            },
            {
                'name': 'notifyUserIds'
            },
            {
                'name': 'notifyAppName'
            },
            {
                'name': 'defaultChangeDate'
            },
            {
                'name': 'disableOverwritePerson'
            },
            {
                'name': 'importDryRun'
            },
            {
                'name': 'importAfterDryRun'
            },
            {
                'name': 'parentProcessId'
            },
            {
                'name': 'importSource'
            },
        ]
    },
    '/v1/org/{orgId}/import/csv/initialColumnMatch-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/v1/org/{orgId}/import/csv/columnMatch-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'skipErrors'
            },
            {
                'name': 'upsert'
            },
            {
                'name': 'createGroups'
            },
            {
                'name': 'disableSyncHireDate'
            },
            {
                'name': 'updateTypes'
            },
            {
                'name': 'notifyUserIds'
            },
            {
                'name': 'notifyAppName'
            },
            {
                'name': 'defaultChangeDate'
            },
            {
                'name': 'disableOverwritePerson'
            },
            {
                'name': 'importDryRun'
            },
            {
                'name': 'importAfterDryRun'
            },
            {
                'name': 'parentProcessId'
            },
            {
                'name': 'importSource'
            },
            {
                'name': 'syncImages'
            },
            {
                'name': 'file'
            },
            {
                'name': 'userDefinedFieldAliases'
            },
        ]
    },
    '/v1/org/{orgId}/import/csv/filepath-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'filePath'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'skipErrors'
            },
            {
                'name': 'upsert'
            },
            {
                'name': 'createGroups'
            },
            {
                'name': 'disableSyncHireDate'
            },
            {
                'name': 'updateTypes'
            },
            {
                'name': 'notifyUserIds'
            },
            {
                'name': 'notifyAppName'
            },
            {
                'name': 'defaultChangeDate'
            },
            {
                'name': 'disableOverwritePerson'
            },
            {
                'name': 'importDryRun'
            },
            {
                'name': 'importAfterDryRun'
            },
            {
                'name': 'parentProcessId'
            },
            {
                'name': 'importSource'
            },
        ]
    },
    '/v1/org/{orgId}/import/spreadsheet/validateFormat-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'maxRows'
            },
        ]
    },
    '/v2/org/{orgId}/job-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/job/{jobId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/job-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'compReviewId'
            },
            {
                'name': 'approvalChainId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'q'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'fieldsList'
            },
            {
                'name': 'format'
            },
            {
                'name': 'useScenarioChanges'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v2/org/{orgId}/job/count-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'q'
            },
        ]
    },
    '/v2/org/{orgId}/job/graph-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'start'
            },
            {
                'name': 'depth'
            },
            {
                'name': 'approxLimit'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'q'
            },
            {
                'name': 'date'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v2/org/{orgId}/job/graph-counts-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'q'
            },
        ]
    },
    '/v2/org/{orgId}/job/{jobId}/position-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'positionFields'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/job/bulkupdate-POST': {
        'parameters': [
            {
                'name': 'updates'
            },
            {
                'name': 'date'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/v2/org/{orgId}/job/{jobId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/job/{jobId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/job-level-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'code'
            },
            {
                'name': 'benchmarkType'
            },
            {
                'name': 'benchmarkLevel'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/job-level/{jobLevelId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobLevelId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/job-level-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'includeDeleted'
            },
        ]
    },
    '/v1/org/{orgId}/job-level/{jobLevelId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobLevelId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/job-level/{jobLevelId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobLevelId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'code'
            },
            {
                'name': 'benchmarkType'
            },
            {
                'name': 'benchmarkLevel'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/legaldoc-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'content'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/legaldoc/{name}-GET': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/v1/media/{mediaId}-GET': {
        'parameters': [
            {
                'name': 'mediaId'
            },
        ]
    },
    '/v1/org/{orgId}/media/{mediaId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'mediaId'
            },
        ]
    },
    '/v1/media-POST': {
        'parameters': [
            {
                'name': 'file'
            },
        ]
    },
    '/v1/org/{orgId}/media-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/v1/org/{orgId}/message-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'id'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'notificationType'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'content'
            },
            {
                'name': 'messageUrl'
            },
            {
                'name': 'key'
            },
            {
                'name': 'readAt'
            },
            {
                'name': 'seenAt'
            },
            {
                'name': 'createId'
            },
            {
                'name': 'createAt'
            },
        ]
    },
    '/v1/org/{orgId}/message/me-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'unreadOnly'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/message/{messageId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'messageId'
            },
        ]
    },
    '/v1/org/{orgId}/message/me/{messageKey}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'messageKey'
            },
        ]
    },
    '/v1/org/{orgId}/message/bulk/seen-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/message/bulk/read-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/message/{messageId}/read-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'messageId'
            },
        ]
    },
    '/v1/org/{orgId}/metric-POST': {
        'parameters': [
            {
                'name': 'metric'
            },
            {
                'name': 'value'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/multiplier-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'value'
            },
            {
                'name': 'expr'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'code'
            },
            {
                'name': 'category'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/multiplier/{multiplierId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'multiplierId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/multiplier/{multiplierId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'multiplierId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/multiplier-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'includeDeleted'
            },
        ]
    },
    '/v1/org/{orgId}/multiplier/{multiplierId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'multiplierId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'code'
            },
            {
                'name': 'value'
            },
            {
                'name': 'expr'
            },
            {
                'name': 'category'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/notification-POST': {
        'parameters': [
            {
                'name': 'templateName'
            },
            {
                'name': 'toUserIds'
            },
            {
                'name': 'jobData'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'atsName'
            },
            {
                'name': 'orgName'
            },
            {
                'name': 'userName'
            },
            {
                'name': 'syncSummary'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/oauth/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'code'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'refresh_token'
            },
        ]
    },
    '/oauth/sso/{idp}/access-token-GET': {
        'parameters': [
            {
                'name': 'idp'
            },
            {
                'name': 'authCode'
            },
        ]
    },
    '/oauth/token/sso/{type}-POST': {
        'parameters': [
            {
                'name': 'idToken'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'type'
            },
            {
                'name': 'fromToken'
            },
            {
                'name': 'createOrg'
            },
            {
                'name': 'signupSource'
            },
            {
                'name': 'utmParams'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/oauth/sso/{idp}/login-GET': {
        'parameters': [
            {
                'name': 'idp'
            },
        ]
    },
    '/oauth/app/{appName}-GET': {
        'parameters': [
            {
                'name': 'appName'
            },
            {
                'name': 'token'
            },
            {
                'name': 'state'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/oauth/token/view-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/oauth/token-DELETE': {
        'parameters': [
        ]
    },
    '/v1/org/{orgId}/onboard-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'getUncomplete'
            },
        ]
    },
    '/v1/org/{orgId}/onboard/{stepName}/skip-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'stepName'
            },
        ]
    },
    '/v1/org/{orgId}/agreement-POST': {
        'parameters': [
            {
                'name': 'action'
            },
            {
                'name': 'legalDocId'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/change-head-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'estEmployees'
            },
            {
                'name': 'status'
            },
            {
                'name': 'currencies'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'onboarding'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'industry'
            },
            {
                'name': 'estRevenue'
            },
            {
                'name': 'foundedYear'
            },
            {
                'name': 'address'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'email'
            },
            {
                'name': 'url'
            },
            {
                'name': 'domains'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'stock'
            },
            {
                'name': 'appTime'
            },
            {
                'name': 'zone'
            },
            {
                'name': 'fiscalStart'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'sensitiveFields'
            },
            {
                'name': 'options'
            },
            {
                'name': 'internalOptions'
            },
            {
                'name': 'onboardSteps'
            },
            {
                'name': 'selfServeImporting'
            },
            {
                'name': 'headCount'
            },
        ]
    },
    '/v1/org/{orgId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/slug/{slug}-GET': {
        'parameters': [
            {
                'name': 'slug'
            },
        ]
    },
    '/v1/org/{orgId}/data-user-person-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'personId'
            },
        ]
    },
    '/v1/org/{orgId}/data-user-person-count-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/data-users-persons-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'role'
            },
            {
                'name': 'status'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{org}/app-install-code-POST': {
        'parameters': [
            {
                'name': 'org'
            },
        ]
    },
    '/v1/org/{orgId}/access-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/org/{slug}-GET': {
        'parameters': [
            {
                'name': 'slug'
            },
        ]
    },
    '/v1/org/{orgId}/welcome-email-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'realOnly'
            },
            {
                'name': 'lastCreateAt'
            },
            {
                'name': 'lastActiveAt'
            },
            {
                'name': 'internalOptions'
            },
        ]
    },
    '/v1/org/{orgId}/test-email-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'welcomeEmailSubject'
            },
            {
                'name': 'welcomeEmailButtonLabel'
            },
            {
                'name': 'welcomeEmailBody'
            },
        ]
    },
    '/v1/org/{orgId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'type'
            },
            {
                'name': 'industry'
            },
            {
                'name': 'estEmployees'
            },
            {
                'name': 'estRevenue'
            },
            {
                'name': 'foundedYear'
            },
            {
                'name': 'address'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'email'
            },
            {
                'name': 'url'
            },
            {
                'name': 'domains'
            },
            {
                'name': 'status'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'currencies'
            },
            {
                'name': 'stock'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'appTime'
            },
            {
                'name': 'zone'
            },
            {
                'name': 'fiscalStart'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'sensitiveFields'
            },
            {
                'name': 'options'
            },
            {
                'name': 'internalOptions'
            },
            {
                'name': 'onboardSteps'
            },
            {
                'name': 'onboarding'
            },
            {
                'name': 'selfServeImporting'
            },
            {
                'name': 'headCount'
            },
        ]
    },
    '/v1/org/app-install-code/validate-POST': {
        'parameters': [
            {
                'name': 'authorizationCode'
            },
            {
                'name': 'issueAccessToken'
            },
        ]
    },
    '/v1/org/{orgId}/config-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'hiddenFieldIds'
            },
            {
                'name': 'builtinCategoryMap'
            },
            {
                'name': 'builtinFieldConfig'
            },
            {
                'name': 'compensationBandsConfig'
            },
            {
                'name': 'smartCurrencyOptions'
            },
            {
                'name': 'smartCurrencyDefault'
            },
            {
                'name': 'requiredJobFields'
            },
            {
                'name': 'scenarioApprovalChains'
            },
            {
                'name': 'isOpenJobRoleApprovalEnabled'
            },
            {
                'name': 'grantConfiguration'
            },
        ]
    },
    '/v1/org/{orgId}/config-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/config-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'hiddenFieldIds'
            },
            {
                'name': 'builtinCategoryMap'
            },
            {
                'name': 'builtinFieldConfig'
            },
            {
                'name': 'compensationBandsConfig'
            },
            {
                'name': 'smartCurrencyOptions'
            },
            {
                'name': 'smartCurrencyDefault'
            },
            {
                'name': 'requiredJobFields'
            },
            {
                'name': 'scenarioApprovalChains'
            },
            {
                'name': 'isOpenJobRoleApprovalEnabled'
            },
            {
                'name': 'grantConfiguration'
            },
        ]
    },
    '/v2/org/{orgId}/person-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/person-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'q'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'fieldsList'
            },
            {
                'name': 'includeAll'
            },
            {
                'name': 'format'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v2/org/{orgId}/person/{personId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/person/geocodes-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v2/org/{orgId}/person/{personId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'personId'
            },
        ]
    },
    '/v2/org/{orgId}/person/{personId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/policy/validate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'id'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'rules'
            },
            {
                'name': 'copiedFromId'
            },
            {
                'name': 'createId'
            },
            {
                'name': 'createAt'
            },
            {
                'name': 'updateId'
            },
            {
                'name': 'updateAt'
            },
            {
                'name': 'deleteId'
            },
            {
                'name': 'deleteAt'
            },
        ]
    },
    '/v1/org/{orgId}/policy/{policyId}/copy-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/v1/org/{orgId}/policy-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'rules'
            },
            {
                'name': 'copiedFromId'
            },
        ]
    },
    '/v1/org/{orgId}/policy/action-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/policy-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/v1/org/{orgId}/policy/{policyId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/v1/org/{orgId}/policy/{policyId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/v1/org/{orgId}/policy/{policyId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'policyId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'label'
            },
            {
                'name': 'rules'
            },
        ]
    },
    '/v2/org/{orgId}/position/{positionId}/job/{jobId}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'positionId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/position-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/position/{positionId}/purge-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'positionId'
            },
        ]
    },
    '/v2/org/{orgId}/position/{positionId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'positionId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/position/{positionId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'positionId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'includeDeleted'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/position/{positionId}/history-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'positionId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/position/import-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'importFromProcessId'
            },
            {
                'name': 'parentProcessId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/v2/org/{orgId}/position-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'includeDeleted'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v2/org/{orgId}/position/{positionId}/job/{jobId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'positionId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/org/{orgId}/position/{positionId}/job/{jobId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'positionId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'removeDate'
            },
            {
                'name': 'assigndate'
            },
        ]
    },
    '/v2/org/{orgId}/position/{positionId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'positionId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/preload-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
            {
                'name': 'showState'
            },
        ]
    },
    '/v1/org/{orgId}/process-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'type'
            },
            {
                'name': 'status'
            },
            {
                'name': 'runUserId'
            },
            {
                'name': 'options'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'filePath'
            },
            {
                'name': 'parentProcessId'
            },
            {
                'name': 'message'
            },
            {
                'name': 'progress'
            },
            {
                'name': 'internalError'
            },
            {
                'name': 'results'
            },
            {
                'name': 'logDataList'
            },
            {
                'name': 'state'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'uuid'
            },
        ]
    },
    '/v1/org/{orgId}/process/self-serve-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'maxRows'
            },
            {
                'name': 'minColumns'
            },
            {
                'name': 'isSync'
            },
            {
                'name': 'file'
            },
            {
                'name': 'state'
            },
        ]
    },
    '/v1/org/{orgId}/process/{createIdOverride}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'type'
            },
            {
                'name': 'status'
            },
            {
                'name': 'runUserId'
            },
            {
                'name': 'options'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'createIdOverride'
            },
            {
                'name': 'filePath'
            },
            {
                'name': 'parentProcessId'
            },
            {
                'name': 'message'
            },
            {
                'name': 'progress'
            },
            {
                'name': 'internalError'
            },
            {
                'name': 'results'
            },
            {
                'name': 'logDataList'
            },
            {
                'name': 'state'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'uuid'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/decrement-PUT': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/file-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/log-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/events-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/process/last-sync/{appUserId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'appUserId'
            },
        ]
    },
    '/v1/org/{orgId}/process-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'isAppProcess'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'parentProcessId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'completedAtStart'
            },
            {
                'name': 'completedAtEnd'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'isParentProcess'
            },
            {
                'name': 'processTypes'
            },
            {
                'name': 'searchValue'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'syncDirections'
            },
            {
                'name': 'syncCauses'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/increment-PUT': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/resume-PUT': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/resumeWithFile-PUT': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/state-PUT': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'filePath'
            },
            {
                'name': 'message'
            },
            {
                'name': 'progress'
            },
            {
                'name': 'internalError'
            },
            {
                'name': 'options'
            },
            {
                'name': 'results'
            },
            {
                'name': 'logDataList'
            },
            {
                'name': 'state'
            },
            {
                'name': 'appId'
            },
        ]
    },
    '/v1/org/{orgId}/process/{processId}/file-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'processId'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/v1/product-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'salesforceProductId'
            },
            {
                'name': 'stripeProductId'
            },
            {
                'name': 'features'
            },
            {
                'name': 'sku'
            },
            {
                'name': 'featureOptions'
            },
        ]
    },
    '/v1/product/{productId}-GET': {
        'parameters': [
            {
                'name': 'productId'
            },
        ]
    },
    '/v1/product-GET': {
        'parameters': [
        ]
    },
    '/v1/product/{productId}-PATCH': {
        'parameters': [
            {
                'name': 'productId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sku'
            },
            {
                'name': 'salesforceProductId'
            },
            {
                'name': 'stripeProductId'
            },
            {
                'name': 'features'
            },
            {
                'name': 'featureOptions'
            },
        ]
    },
    '/v1/org/{orgId}/profile-tab-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'status'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'targetFilter'
            },
            {
                'name': 'readFilter'
            },
        ]
    },
    '/v1/org/{orgId}/profile-tab/{profileTabId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'profileTabId'
            },
        ]
    },
    '/v1/org/{orgId}/profile-tab/job/{jobId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/org/{orgId}/profile-tab/{profileTabId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'profileTabId'
            },
        ]
    },
    '/v1/org/{orgId}/profile-tab/job/{jobId}/profile-tab/{tabId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'tabId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/profile-tab/person/{personId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/org/{orgId}/profile-tab-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/profile-tab/{profileTabId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'profileTabId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'status'
            },
            {
                'name': 'targetFilter'
            },
            {
                'name': 'readFilter'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/org/{orgId}/query/{queryToken}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'queryToken'
            },
        ]
    },
    '/v1/org/{orgId}/query/{queryToken}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'queryToken'
            },
            {
                'name': 'format'
            },
            {
                'name': 'mapper'
            },
        ]
    },
    '/v1/org/{orgId}/query-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'params'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/query-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/question-POST': {
        'parameters': [
            {
                'name': 'question'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'plural'
            },
            {
                'name': 'values'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/v1/org/{orgId}/question-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'ids'
            },
        ]
    },
    '/v1/org/{orgId}/question/{questionId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'questionId'
            },
        ]
    },
    '/v1/org/{orgId}/question/{questionId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'questionId'
            },
        ]
    },
    '/v1/org/{orgId}/question/{questionId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'questionId'
            },
            {
                'name': 'question'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'plural'
            },
            {
                'name': 'values'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/v1/org/{orgId}/report/bulk-delete-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}/clone-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
        ]
    },
    '/v1/org/{orgId}/report-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'share'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'chartIds'
            },
        ]
    },
    '/v1/org/{orgId}/report/bulk-duplicate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}/chart/{chartId}/export/csv-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'chartId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'interval'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'projectHires'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'changeGroupingType'
            },
            {
                'name': 'changeGroupingId'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
        ]
    },
    '/v1/org/{orgId}/report-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'fromId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}/query-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'interval'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'projectHires'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'changeGroupingType'
            },
            {
                'name': 'changeGroupingId'
            },
        ]
    },
    '/v1/org/{orgId}/report/count-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
        ]
    },
    '/v1/org/{orgId}/report/query-POST': {
        'parameters': [
            {
                'name': 'options'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'series'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'content'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'interval'
            },
            {
                'name': 'intervalDates'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'label'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'share'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'chartIds'
            },
            {
                'name': 'referencedReportUrl'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}/chart/{chartId}/clone-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'chartId'
            },
            {
                'name': 'chartLabel'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}/chart-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'type'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filterOverride'
            },
            {
                'name': 'isAdvancedQueryMode'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}/chart/{chartId}/data-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'chartId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'interval'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'projectHires'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}/chart-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
        ]
    },
    '/v1/org/{orgId}/report/chart/{chartId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'chartId'
            },
        ]
    },
    '/v1/org/{orgId}/report/{reportId}/chart/{chartId}/query-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'chartId'
            },
            {
                'name': 'providedQuery'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'interval'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'projectHires'
            },
            {
                'name': 'changeGroupingType'
            },
            {
                'name': 'changeGroupingId'
            },
        ]
    },
    '/v1/org/{orgId}/report/chart/{chartId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'chartId'
            },
        ]
    },
    '/v1/org/{orgId}/report/chart/{chartId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'chartId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'type'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filterOverride'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'isAdvancedQueryMode'
            },
        ]
    },
    '/v1/org/{orgId}/role/{roleId}/copy-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/v1/org/{orgId}/role-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'policyIds'
            },
        ]
    },
    '/v1/org/{orgId}/role-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/v1/org/{orgId}/role/{roleId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/v1/org/{orgId}/role/{roleId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/v1/org/{orgId}/role/{roleId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'label'
            },
            {
                'name': 'policyIds'
            },
        ]
    },
    '/saml/{org}/login-POST': {
        'parameters': [
            {
                'name': 'org'
            },
            {
                'name': 'idp'
            },
        ]
    },
    '/saml/sso/{org}-POST': {
        'parameters': [
            {
                'name': 'org'
            },
            {
                'name': 'token'
            },
            {
                'name': 'SAMLResponse'
            },
            {
                'name': 'RelayState'
            },
        ]
    },
    '/saml/org/{orgId}/xml-cert-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'idp'
            },
        ]
    },
    '/saml/org/{orgId}/xml-cert-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'idp'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}/dates-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'days'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/bulk/archive-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}/combine-POST': {
        'parameters': [
            {
                'name': 'scenarioIds'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'copyOnly'
            },
            {
                'name': 'useScenarioDateForChanges'
            },
        ]
    },
    '/v1/org/{orgId}/scenario-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'type'
            },
            {
                'name': 'startDateFixed'
            },
            {
                'name': 'query'
            },
            {
                'name': 'validJobIdSet'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'sharedViewConfig'
            },
            {
                'name': 'budget'
            },
            {
                'name': 'costCalc'
            },
            {
                'name': 'silent'
            },
            {
                'name': 'skipChangeCreation'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/bulk/delete-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/scenario-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'status'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}/recalculate-metadata-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}/merge-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'skipErrors'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/bulk/unarchive-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'shareAccess'
            },
            {
                'name': 'startDateFixed'
            },
            {
                'name': 'validJobIdSet'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'sharedViewConfig'
            },
            {
                'name': 'budget'
            },
            {
                'name': 'costCalc'
            },
            {
                'name': 'silent'
            },
        ]
    },
    '/v1/org/{orgId}/scenario/{scenarioId}/update-shared-view-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'customColumnNames'
            },
            {
                'name': 'columnWidths'
            },
            {
                'name': 'type'
            },
            {
                'name': 'updateId'
            },
            {
                'name': 'updateAt'
            },
        ]
    },
    '/v1/org/{orgId}/search-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'q'
            },
            {
                'name': 'entityTypes'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'includeFormer'
            },
            {
                'name': 'date'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'canAccess'
            },
            {
                'name': 'includeExternalRecruiter'
            },
        ]
    },
    '/v1/status-GET': {
        'parameters': [
        ]
    },
    '/v1/stock-GET': {
        'parameters': [
            {
                'name': 'symbol'
            },
            {
                'name': 'type'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/stock/{symbol}/{date}/{type}-GET': {
        'parameters': [
            {
                'name': 'symbol'
            },
            {
                'name': 'date'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/v1/stock/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/stock/{symbol}/{date}/{type}-PUT': {
        'parameters': [
            {
                'name': 'symbol'
            },
            {
                'name': 'date'
            },
            {
                'name': 'type'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'price'
            },
            {
                'name': 'total'
            },
        ]
    },
    '/v1/stripe/setup-intent-POST': {
        'parameters': [
        ]
    },
    '/v1/stripe/plan-GET': {
        'parameters': [
        ]
    },
    '/v1/stripe/product-GET': {
        'parameters': [
        ]
    },
    '/v1/stripe/product/{productId}-GET': {
        'parameters': [
            {
                'name': 'productId'
            },
        ]
    },
    '/v1/stripe/webhook-POST': {
        'parameters': [
            {
                'name': 'Stripe-Signature'
            },
        ]
    },
    '/v1/org/{orgId}/table-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'effectiveDated'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'label'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'shareAccess'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}/data/{keyColumn}/{keyValue}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'keyColumn'
            },
            {
                'name': 'keyValue'
            },
            {
                'name': 'date'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}/data/{keyColumn}/{keyValue}/purge-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'keyColumn'
            },
            {
                'name': 'keyValue'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}/export-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}/data-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}/data/{keyColumn}/{keyValue}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'keyColumn'
            },
            {
                'name': 'keyValue'
            },
            {
                'name': 'date'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}/import-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'date'
            },
            {
                'name': 'importFromProcessId'
            },
            {
                'name': 'parentProcessId'
            },
        ]
    },
    '/v1/org/{orgId}/table-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'includeBuiltIns'
            },
            {
                'name': 'names'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}/data/{keyColumn}/{keyValue}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'keyColumn'
            },
            {
                'name': 'keyValue'
            },
            {
                'name': 'date'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'label'
            },
            {
                'name': 'labelColumnId'
            },
            {
                'name': 'effectiveDated'
            },
            {
                'name': 'sensitive'
            },
            {
                'name': 'shareAccess'
            },
        ]
    },
    '/v1/org/{orgId}/table/{tableId}/data-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'scenarioId'
            },
        ]
    },
    '/v1/org/{orgId}/task/bulk-delete-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/task-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/task/summary/{assessmentId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
        ]
    },
    '/v1/org/{orgId}/task/me-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/task/{taskId}/skip-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'taskId'
            },
        ]
    },
    '/v1/org/{orgId}/task/task-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'format'
            },
            {
                'name': 'from'
            },
            {
                'name': 'returnAccess'
            },
            {
                'name': 'returnFormCompletionLinks'
            },
        ]
    },
    '/v1/org/{orgId}/task/{taskId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'taskId'
            },
        ]
    },
    '/v1/org/{orgId}/task/{assessmentId}/{formId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'formId'
            },
        ]
    },
    '/v1/org/{orgId}/task/remind-POST': {
        'parameters': [
            {
                'name': 'taskIds'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/v1/org/{orgId}/task/{taskId}/mark-done-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'taskId'
            },
        ]
    },
    '/v1/org/{orgId}/task-config-POST': {
        'parameters': [
            {
                'name': 'entityId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'pastDueAction'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'parentEntityId'
            },
            {
                'name': 'dueDate'
            },
            {
                'name': 'isSkippable'
            },
            {
                'name': 'label'
            },
            {
                'name': 'deleteId'
            },
            {
                'name': 'deleteAt'
            },
        ]
    },
    '/v1/org/{orgId}/task-config-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'parentEntityId'
            },
            {
                'name': 'assessmentId'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/task-config/{id}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v1/org/{orgId}/template/bulk/delete-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/template/bulk/duplicate-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/org/{orgId}/template/email-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'content'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'stylesheet'
            },
            {
                'name': 'type'
            },
            {
                'name': 'filename'
            },
        ]
    },
    '/v1/org/{orgId}/template-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'content'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'stylesheet'
            },
            {
                'name': 'type'
            },
            {
                'name': 'filename'
            },
        ]
    },
    '/v1/org/{orgId}/template/{templateId}/render-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'templateId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'format'
            },
            {
                'name': 'changeGroupingType'
            },
            {
                'name': 'changeGroupingId'
            },
            {
                'name': 'useScenarioChanges'
            },
        ]
    },
    '/v1/org/{orgId}/template/{templateId}/generate-POST': {
        'parameters': [
            {
                'name': 'saveToFiles'
            },
            {
                'name': 'sendToManagers'
            },
            {
                'name': 'sendToPersons'
            },
            {
                'name': 'useScenarioChanges'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'templateId'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'emailSubject'
            },
            {
                'name': 'emailMessage'
            },
            {
                'name': 'fileSensitive'
            },
            {
                'name': 'fileField'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'changeGroupingType'
            },
            {
                'name': 'changeGroupingId'
            },
        ]
    },
    '/v1/org/{orgId}/template/{templateId}/preview-POST': {
        'parameters': [
            {
                'name': 'content'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'stylesheet'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'scenarioId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'format'
            },
            {
                'name': 'changeGroupingType'
            },
            {
                'name': 'changeGroupingId'
            },
            {
                'name': 'useScenarioChanges'
            },
        ]
    },
    '/v1/org/{orgId}/template-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/org/{orgId}/template/{templateId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'templateId'
            },
        ]
    },
    '/v1/org/{orgId}/template/email/{templateName}-GET': {
        'parameters': [
            {
                'name': 'templateName'
            },
        ]
    },
    '/v1/org/{orgId}/template/{templateId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'templateId'
            },
        ]
    },
    '/v1/org/{orgId}/template/email/{templateName}-DELETE': {
        'parameters': [
            {
                'name': 'templateName'
            },
        ]
    },
    '/v1/org/{orgId}/template/email/{templateName}-PATCH': {
        'parameters': [
            {
                'name': 'templateName'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'content'
            },
            {
                'name': 'stylesheet'
            },
            {
                'name': 'type'
            },
            {
                'name': 'filename'
            },
        ]
    },
    '/v1/org/{orgId}/template/{templateId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'templateId'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'content'
            },
            {
                'name': 'stylesheet'
            },
            {
                'name': 'type'
            },
            {
                'name': 'filename'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff/{timeOffId}/approve-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'timeOffId'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff-POST': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'days'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'typeDescription'
            },
            {
                'name': 'note'
            },
            {
                'name': 'approval'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff/{timeOffId}-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'timeOffId'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'untilDate'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'returnAccess'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff/{timeOffId}/reject-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'timeOffId'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff/{timeOffId}-DELETE': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'timeOffId'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff/request-POST': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'typeDescription'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff/{timeOffId}-PATCH': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'timeOffId'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'days'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'typeDescription'
            },
            {
                'name': 'note'
            },
            {
                'name': 'approval'
            },
        ]
    },
    '/v1/org/{orgId}/timeoff/request/validate-POST': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'orgId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'typeDescription'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/v1/org/{orgId}/usage/{type}-POST': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'entityId'
            },
        ]
    },
    '/v1/user/assign-PATCH': {
        'parameters': [
        ]
    },
    '/v1/user/{userId}/password-POST': {
        'parameters': [
            {
                'name': 'newPassword'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'oldPassword'
            },
        ]
    },
    '/v1/user-POST': {
        'parameters': [
            {
                'name': 'orgs'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'status'
            },
            {
                'name': 'options'
            },
            {
                'name': 'internalOptions'
            },
            {
                'name': 'secrets'
            },
            {
                'name': 'emailSettings'
            },
        ]
    },
    '/v1/user-GET': {
        'parameters': [
            {
                'name': 'orgId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/user/me-GET': {
        'parameters': [
        ]
    },
    '/v1/user/email/{email}-GET': {
        'parameters': [
            {
                'name': 'email'
            },
        ]
    },
    '/v1/user/{userId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/v1/user/invite-POST': {
        'parameters': [
        ]
    },
    '/v1/user/person/{personId}-GET': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'orgId'
            },
        ]
    },
    '/v1/user/{userId}/token-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/v1/user/token-DELETE': {
        'parameters': [
        ]
    },
    '/v1/user/sendreset-POST': {
        'parameters': [
            {
                'name': 'email'
            },
        ]
    },
    '/v1/user/{userId}-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'orgs'
            },
            {
                'name': 'imagePath'
            },
            {
                'name': 'status'
            },
            {
                'name': 'options'
            },
            {
                'name': 'internalOptions'
            },
            {
                'name': 'secrets'
            },
            {
                'name': 'emailSettings'
            },
        ]
    },
    '/v1/user/me/view-GET': {
        'parameters': [
        ]
    },
    '/v1/webauthn/verify-GET': {
        'parameters': [
        ]
    },
    '/v1/webauthn/register/{emailBase64}-DELETE': {
        'parameters': [
            {
                'name': 'emailBase64'
            },
        ]
    },
    '/v1/webauthn/register-GET': {
        'parameters': [
        ]
    },
    '/v1/webauthn/register-POST': {
        'parameters': [
            {
                'name': 'requestId'
            },
            {
                'name': 'credentialResponse'
            },
        ]
    },
    '/v1/webauthn/verify-POST': {
        'parameters': [
            {
                'name': 'requestId'
            },
            {
                'name': 'credentialResponse'
            },
        ]
    },
};