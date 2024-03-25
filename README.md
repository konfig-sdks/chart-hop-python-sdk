<div align="center">

[![Visit Charthop](./header.png)](https://charthop.com)

# Charthop<a id="charthop"></a>

REST API for ChartHop


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`charthop.access.entity_actions`](#charthopaccessentity_actions)
  * [`charthop.action.create_new_action`](#charthopactioncreate_new_action)
  * [`charthop.action.delete_action_by_id`](#charthopactiondelete_action_by_id)
  * [`charthop.action.execute_action_for_testing`](#charthopactionexecute_action_for_testing)
  * [`charthop.action.get_action_by_id`](#charthopactionget_action_by_id)
  * [`charthop.action.get_all_paginated`](#charthopactionget_all_paginated)
  * [`charthop.action.update_existing_action_by_id`](#charthopactionupdate_existing_action_by_id)
  * [`charthop.ai.generate_text_summary`](#charthopaigenerate_text_summary)
  * [`charthop.app.create_new_app`](#charthopappcreate_new_app)
  * [`charthop.app.find_installed_app_users`](#charthopappfind_installed_app_users)
  * [`charthop.app.find_installed_app_users_0`](#charthopappfind_installed_app_users_0)
  * [`charthop.app.generate_or_regenerate_access_token`](#charthopappgenerate_or_regenerate_access_token)
  * [`charthop.app.get_active_apps_by_org`](#charthopappget_active_apps_by_org)
  * [`charthop.app.get_by_id`](#charthopappget_by_id)
  * [`charthop.app.get_by_name`](#charthopappget_by_name)
  * [`charthop.app.get_installed_app_by_name`](#charthopappget_installed_app_by_name)
  * [`charthop.app.get_oauth2_authorization_code`](#charthopappget_oauth2_authorization_code)
  * [`charthop.app.get_token_for_app`](#charthopappget_token_for_app)
  * [`charthop.app.get_token_for_app_0`](#charthopappget_token_for_app_0)
  * [`charthop.app.install_app_for_org`](#charthopappinstall_app_for_org)
  * [`charthop.app.list_public_global_apps`](#charthopapplist_public_global_apps)
  * [`charthop.app.remove_by_id`](#charthopappremove_by_id)
  * [`charthop.app.run_installed_app`](#charthopapprun_installed_app)
  * [`charthop.app.send_email_notification`](#charthopappsend_email_notification)
  * [`charthop.app.uninstall_app_by_user_id`](#charthopappuninstall_app_by_user_id)
  * [`charthop.app.update_existing_app`](#charthopappupdate_existing_app)
  * [`charthop.app.update_installed_app`](#charthopappupdate_installed_app)
  * [`charthop.app.validate_app_installation`](#charthopappvalidate_app_installation)
  * [`charthop.app_config.create_new_config`](#charthopapp_configcreate_new_config)
  * [`charthop.app_config.get_default_config_by_app`](#charthopapp_configget_default_config_by_app)
  * [`charthop.app_config.get_user_config_by_app_and_user`](#charthopapp_configget_user_config_by_app_and_user)
  * [`charthop.app_config.update_by_id`](#charthopapp_configupdate_by_id)
  * [`charthop.approval.create_chain`](#charthopapprovalcreate_chain)
  * [`charthop.approval.create_chain_stage`](#charthopapprovalcreate_chain_stage)
  * [`charthop.approval.create_request`](#charthopapprovalcreate_request)
  * [`charthop.approval.delete_approval_chain_stage`](#charthopapprovaldelete_approval_chain_stage)
  * [`charthop.approval.delete_chain_by_id`](#charthopapprovaldelete_chain_by_id)
  * [`charthop.approval.delete_request_approval`](#charthopapprovaldelete_request_approval)
  * [`charthop.approval.generate_default_chain_stages`](#charthopapprovalgenerate_default_chain_stages)
  * [`charthop.approval.get_all_approval_requests_for_approval_chain`](#charthopapprovalget_all_approval_requests_for_approval_chain)
  * [`charthop.approval.get_all_stages_for_chain`](#charthopapprovalget_all_stages_for_chain)
  * [`charthop.approval.get_approval_chain_by_id`](#charthopapprovalget_approval_chain_by_id)
  * [`charthop.approval.get_approval_chain_stages`](#charthopapprovalget_approval_chain_stages)
  * [`charthop.approval.get_approval_chains`](#charthopapprovalget_approval_chains)
  * [`charthop.approval.get_comp_review_responses_for_chain`](#charthopapprovalget_comp_review_responses_for_chain)
  * [`charthop.approval.get_scenario_responses`](#charthopapprovalget_scenario_responses)
  * [`charthop.approval.reassign_approver_at_stage`](#charthopapprovalreassign_approver_at_stage)
  * [`charthop.approval.request_approval_request`](#charthopapprovalrequest_approval_request)
  * [`charthop.approval.send_stage_reviewer_reminder`](#charthopapprovalsend_stage_reviewer_reminder)
  * [`charthop.approval.update_chain`](#charthopapprovalupdate_chain)
  * [`charthop.approval.update_existing_request`](#charthopapprovalupdate_existing_request)
  * [`charthop.approval.update_stage_by_id`](#charthopapprovalupdate_stage_by_id)
  * [`charthop.approval_request.get_all_approval_request_scenario_responses`](#charthopapproval_requestget_all_approval_request_scenario_responses)
  * [`charthop.approval_request.get_approval_request_scenario_response_by_job_id`](#charthopapproval_requestget_approval_request_scenario_response_by_job_id)
  * [`charthop.approval_request.get_scenario_response_by_id`](#charthopapproval_requestget_scenario_response_by_id)
  * [`charthop.assessment.bulk_delete`](#charthopassessmentbulk_delete)
  * [`charthop.assessment.bulk_duplicate_assessments`](#charthopassessmentbulk_duplicate_assessments)
  * [`charthop.assessment.complete_assessment`](#charthopassessmentcomplete_assessment)
  * [`charthop.assessment.create_new_assessment`](#charthopassessmentcreate_new_assessment)
  * [`charthop.assessment.expire_form_tasks`](#charthopassessmentexpire_form_tasks)
  * [`charthop.assessment.get_all_paginated`](#charthopassessmentget_all_paginated)
  * [`charthop.assessment.get_by_id`](#charthopassessmentget_by_id)
  * [`charthop.assessment.reactivate_assessment`](#charthopassessmentreactivate_assessment)
  * [`charthop.assessment.remove_by_id`](#charthopassessmentremove_by_id)
  * [`charthop.assessment.update_assessment_types`](#charthopassessmentupdate_assessment_types)
  * [`charthop.assessment.update_existing_assessment`](#charthopassessmentupdate_existing_assessment)
  * [`charthop.band.create_comp_band`](#charthopbandcreate_comp_band)
  * [`charthop.band.delete_comp_bands_on_date`](#charthopbanddelete_comp_bands_on_date)
  * [`charthop.band.delete_comp_bands_on_date_0`](#charthopbanddelete_comp_bands_on_date_0)
  * [`charthop.band.find_comp_bands_in_org`](#charthopbandfind_comp_bands_in_org)
  * [`charthop.band.find_comp_bands_in_org_0`](#charthopbandfind_comp_bands_in_org_0)
  * [`charthop.band.remove_comp_band`](#charthopbandremove_comp_band)
  * [`charthop.band.update_comp_band_by_id`](#charthopbandupdate_comp_band_by_id)
  * [`charthop.billing.cancel_subscription_for_customer`](#charthopbillingcancel_subscription_for_customer)
  * [`charthop.billing.customer_billing_info`](#charthopbillingcustomer_billing_info)
  * [`charthop.billing.upgrade_subscription`](#charthopbillingupgrade_subscription)
  * [`charthop.budget_pool.calculate_guideline`](#charthopbudget_poolcalculate_guideline)
  * [`charthop.budget_pool.calculate_guideline_0`](#charthopbudget_poolcalculate_guideline_0)
  * [`charthop.budget_pool.create_new_pool`](#charthopbudget_poolcreate_new_pool)
  * [`charthop.budget_pool.delete_budget_pool_by_id`](#charthopbudget_pooldelete_budget_pool_by_id)
  * [`charthop.budget_pool.get_all_for_org`](#charthopbudget_poolget_all_for_org)
  * [`charthop.budget_pool.get_guidelines_for_budget_pool`](#charthopbudget_poolget_guidelines_for_budget_pool)
  * [`charthop.budget_pool.get_specific_pool`](#charthopbudget_poolget_specific_pool)
  * [`charthop.budget_pool.update_budget_pool`](#charthopbudget_poolupdate_budget_pool)
  * [`charthop.calendar.get_entries_by_time_period`](#charthopcalendarget_entries_by_time_period)
  * [`charthop.category.create_new_category`](#charthopcategorycreate_new_category)
  * [`charthop.category.get_available`](#charthopcategoryget_available)
  * [`charthop.category.get_by_id`](#charthopcategoryget_by_id)
  * [`charthop.category.remove_by_id`](#charthopcategoryremove_by_id)
  * [`charthop.category.update_existing_category`](#charthopcategoryupdate_existing_category)
  * [`charthop.category_sort.create_if_not_exists`](#charthopcategory_sortcreate_if_not_exists)
  * [`charthop.category_sort.create_or_update_sort`](#charthopcategory_sortcreate_or_update_sort)
  * [`charthop.category_sort.create_or_update_sort_order`](#charthopcategory_sortcreate_or_update_sort_order)
  * [`charthop.category_sort.delete_sort_order`](#charthopcategory_sortdelete_sort_order)
  * [`charthop.category_sort.get_category_sort_order`](#charthopcategory_sortget_category_sort_order)
  * [`charthop.category_sort.update_existing_category_sort`](#charthopcategory_sortupdate_existing_category_sort)
  * [`charthop.change.amend_scenario_change`](#charthopchangeamend_scenario_change)
  * [`charthop.change.approve_or_reject`](#charthopchangeapprove_or_reject)
  * [`charthop.change.bulk_update_jobs`](#charthopchangebulk_update_jobs)
  * [`charthop.change.check_approver_eligibility`](#charthopchangecheck_approver_eligibility)
  * [`charthop.change.create_depart_rehire_pair`](#charthopchangecreate_depart_rehire_pair)
  * [`charthop.change.create_if_not_exists`](#charthopchangecreate_if_not_exists)
  * [`charthop.change.create_new_change`](#charthopchangecreate_new_change)
  * [`charthop.change.delete_previous_change`](#charthopchangedelete_previous_change)
  * [`charthop.change.find_scenario_changes`](#charthopchangefind_scenario_changes)
  * [`charthop.change.get_by_id`](#charthopchangeget_by_id)
  * [`charthop.change.get_by_id_0`](#charthopchangeget_by_id_0)
  * [`charthop.change.get_recent_changes`](#charthopchangeget_recent_changes)
  * [`charthop.change.get_recent_changes_for_org_or_person`](#charthopchangeget_recent_changes_for_org_or_person)
  * [`charthop.change.get_status`](#charthopchangeget_status)
  * [`charthop.change.perform_bulk_change`](#charthopchangeperform_bulk_change)
  * [`charthop.change.update_change_by_id`](#charthopchangeupdate_change_by_id)
  * [`charthop.change.validate_change_operation`](#charthopchangevalidate_change_operation)
  * [`charthop.comment.create_new_comment`](#charthopcommentcreate_new_comment)
  * [`charthop.comment.get_by_entity_id`](#charthopcommentget_by_entity_id)
  * [`charthop.comment.get_by_id`](#charthopcommentget_by_id)
  * [`charthop.comment.list_comments_on_comp_review`](#charthopcommentlist_comments_on_comp_review)
  * [`charthop.comment.list_comments_on_scenario_and_changes`](#charthopcommentlist_comments_on_scenario_and_changes)
  * [`charthop.comment.remove_by_id`](#charthopcommentremove_by_id)
  * [`charthop.comp_review.close_comp_review`](#charthopcomp_reviewclose_comp_review)
  * [`charthop.comp_review.create_bulk_duplicate`](#charthopcomp_reviewcreate_bulk_duplicate)
  * [`charthop.comp_review.create_comp_review`](#charthopcomp_reviewcreate_comp_review)
  * [`charthop.comp_review.create_visualization_data`](#charthopcomp_reviewcreate_visualization_data)
  * [`charthop.comp_review.delete_bulk_comp_reviews`](#charthopcomp_reviewdelete_bulk_comp_reviews)
  * [`charthop.comp_review.delete_comp_review`](#charthopcomp_reviewdelete_comp_review)
  * [`charthop.comp_review.duplicate_comp_review`](#charthopcomp_reviewduplicate_comp_review)
  * [`charthop.comp_review.export_audit_log`](#charthopcomp_reviewexport_audit_log)
  * [`charthop.comp_review.export_changes`](#charthopcomp_reviewexport_changes)
  * [`charthop.comp_review.export_comments`](#charthopcomp_reviewexport_comments)
  * [`charthop.comp_review.find_comp_review_by_id`](#charthopcomp_reviewfind_comp_review_by_id)
  * [`charthop.comp_review.find_comp_reviews`](#charthopcomp_reviewfind_comp_reviews)
  * [`charthop.comp_review.generate_comp_review`](#charthopcomp_reviewgenerate_comp_review)
  * [`charthop.comp_review.generate_tiering_preview`](#charthopcomp_reviewgenerate_tiering_preview)
  * [`charthop.comp_review.get_change_and_guideline_flags`](#charthopcomp_reviewget_change_and_guideline_flags)
  * [`charthop.comp_review.get_changes_in_cycle`](#charthopcomp_reviewget_changes_in_cycle)
  * [`charthop.comp_review.get_collabicient_in_cycle`](#charthopcomp_reviewget_collabicient_in_cycle)
  * [`charthop.comp_review.get_date_caches`](#charthopcomp_reviewget_date_caches)
  * [`charthop.comp_review.get_eligible_employees`](#charthopcomp_reviewget_eligible_employees)
  * [`charthop.comp_review.get_metadata_by_id`](#charthopcomp_reviewget_metadata_by_id)
  * [`charthop.comp_review.list_request_responses`](#charthopcomp_reviewlist_request_responses)
  * [`charthop.comp_review.overview_in_cycle_comp_review`](#charthopcomp_reviewoverview_in_cycle_comp_review)
  * [`charthop.comp_review.pause_review`](#charthopcomp_reviewpause_review)
  * [`charthop.comp_review.send_reminder_email`](#charthopcomp_reviewsend_reminder_email)
  * [`charthop.comp_review.update_approval_request_status`](#charthopcomp_reviewupdate_approval_request_status)
  * [`charthop.comp_review.update_comp_review`](#charthopcomp_reviewupdate_comp_review)
  * [`charthop.content.create_new_piece`](#charthopcontentcreate_new_piece)
  * [`charthop.content.get_by_id`](#charthopcontentget_by_id)
  * [`charthop.content.get_by_path`](#charthopcontentget_by_path)
  * [`charthop.content.get_paginated`](#charthopcontentget_paginated)
  * [`charthop.content.remove_by_id`](#charthopcontentremove_by_id)
  * [`charthop.content.render_by_path`](#charthopcontentrender_by_path)
  * [`charthop.content.render_homepage_contents`](#charthopcontentrender_homepage_contents)
  * [`charthop.content.update_homepage_content`](#charthopcontentupdate_homepage_content)
  * [`charthop.content.update_piece_by_id`](#charthopcontentupdate_piece_by_id)
  * [`charthop.customer.create_new_customer`](#charthopcustomercreate_new_customer)
  * [`charthop.customer.get_all_invoices_for_customer`](#charthopcustomerget_all_invoices_for_customer)
  * [`charthop.customer.get_by_id`](#charthopcustomerget_by_id)
  * [`charthop.customer.get_charthop_subscription`](#charthopcustomerget_charthop_subscription)
  * [`charthop.customer.list_visible_customers`](#charthopcustomerlist_visible_customers)
  * [`charthop.customer.update_existing_customer`](#charthopcustomerupdate_existing_customer)
  * [`charthop.customer.update_subscription`](#charthopcustomerupdate_subscription)
  * [`charthop.data_view.create_new_data_view`](#charthopdata_viewcreate_new_data_view)
  * [`charthop.data_view.delete_data_view`](#charthopdata_viewdelete_data_view)
  * [`charthop.data_view.get_all_paginated`](#charthopdata_viewget_all_paginated)
  * [`charthop.data_view.get_by_id`](#charthopdata_viewget_by_id)
  * [`charthop.data_view.update_existing_view`](#charthopdata_viewupdate_existing_view)
  * [`charthop.email_template.create_new_template`](#charthopemail_templatecreate_new_template)
  * [`charthop.email_template.get_all_non_essential`](#charthopemail_templateget_all_non_essential)
  * [`charthop.email_template.get_by_name`](#charthopemail_templateget_by_name)
  * [`charthop.email_template.list_essential_email_templates`](#charthopemail_templatelist_essential_email_templates)
  * [`charthop.email_template.update_existing_template`](#charthopemail_templateupdate_existing_template)
  * [`charthop.event.create_inbound_notification`](#charthopeventcreate_inbound_notification)
  * [`charthop.event.create_outbound_event`](#charthopeventcreate_outbound_event)
  * [`charthop.event.get_event_payload`](#charthopeventget_event_payload)
  * [`charthop.event.get_past_events`](#charthopeventget_past_events)
  * [`charthop.event.resend_associated_notifications`](#charthopeventresend_associated_notifications)
  * [`charthop.exchange_rate.bulk_update_custom_rates`](#charthopexchange_ratebulk_update_custom_rates)
  * [`charthop.exchange_rate.delete_custom_rate_on_date`](#charthopexchange_ratedelete_custom_rate_on_date)
  * [`charthop.exchange_rate.get_custom_exchange_rates`](#charthopexchange_rateget_custom_exchange_rates)
  * [`charthop.exchange_rate.get_global_by_date`](#charthopexchange_rateget_global_by_date)
  * [`charthop.exchange_rate.get_rates_on_date`](#charthopexchange_rateget_rates_on_date)
  * [`charthop.exchange_rate.org_custom_exchange_rates_history`](#charthopexchange_rateorg_custom_exchange_rates_history)
  * [`charthop.exchange_rate.update_usd_exchange_rates_for_date`](#charthopexchange_rateupdate_usd_exchange_rates_for_date)
  * [`charthop.export.changelog_to_csv`](#charthopexportchangelog_to_csv)
  * [`charthop.export.csv_custom_fields`](#charthopexportcsv_custom_fields)
  * [`charthop.export.csv_scenario_comments`](#charthopexportcsv_scenario_comments)
  * [`charthop.export.file_zip_download`](#charthopexportfile_zip_download)
  * [`charthop.export.org_chart_to_powerpoint`](#charthopexportorg_chart_to_powerpoint)
  * [`charthop.export.pdf_review`](#charthopexportpdf_review)
  * [`charthop.export.report_to_powerpoint`](#charthopexportreport_to_powerpoint)
  * [`charthop.export.roster_to_csv_snapshot`](#charthopexportroster_to_csv_snapshot)
  * [`charthop.export.scenario_csv`](#charthopexportscenario_csv)
  * [`charthop.export.task_to_csv`](#charthopexporttask_to_csv)
  * [`charthop.export.user_review_csv`](#charthopexportuser_review_csv)
  * [`charthop.expression.evaluate_carrot_expression`](#charthopexpressionevaluate_carrot_expression)
  * [`charthop.expression.validate_carrot_expression`](#charthopexpressionvalidate_carrot_expression)
  * [`charthop.field.create_new_field`](#charthopfieldcreate_new_field)
  * [`charthop.field.get_all_paginated`](#charthopfieldget_all_paginated)
  * [`charthop.field.get_built_in_fields`](#charthopfieldget_built_in_fields)
  * [`charthop.field.get_by_id`](#charthopfieldget_by_id)
  * [`charthop.field.get_fields_in_category`](#charthopfieldget_fields_in_category)
  * [`charthop.field.get_uncategorized_fields`](#charthopfieldget_uncategorized_fields)
  * [`charthop.field.remove`](#charthopfieldremove)
  * [`charthop.field.remove_by_id`](#charthopfieldremove_by_id)
  * [`charthop.field.remove_field_overrides`](#charthopfieldremove_field_overrides)
  * [`charthop.field.remove_from_categories`](#charthopfieldremove_from_categories)
  * [`charthop.field.update_existing_field`](#charthopfieldupdate_existing_field)
  * [`charthop.field.update_field_dry_run`](#charthopfieldupdate_field_dry_run)
  * [`charthop.field.update_status_for_existing_fields`](#charthopfieldupdate_status_for_existing_fields)
  * [`charthop.file.get_metadata`](#charthopfileget_metadata)
  * [`charthop.file.get_metadata_0`](#charthopfileget_metadata_0)
  * [`charthop.file.get_metadata_by_id`](#charthopfileget_metadata_by_id)
  * [`charthop.file.remove_file_by_id`](#charthopfileremove_file_by_id)
  * [`charthop.file.upload_new_file`](#charthopfileupload_new_file)
  * [`charthop.form.create_new_form`](#charthopformcreate_new_form)
  * [`charthop.form.delete_form_by_id`](#charthopformdelete_form_by_id)
  * [`charthop.form.delete_form_by_id_0`](#charthopformdelete_form_by_id_0)
  * [`charthop.form.delete_form_draft`](#charthopformdelete_form_draft)
  * [`charthop.form.get_applicable_forms_for_person`](#charthopformget_applicable_forms_for_person)
  * [`charthop.form.get_by_id`](#charthopformget_by_id)
  * [`charthop.form.get_current_state_of_draft_data`](#charthopformget_current_state_of_draft_data)
  * [`charthop.form.list_available_forms`](#charthopformlist_available_forms)
  * [`charthop.form.list_org_forms`](#charthopformlist_org_forms)
  * [`charthop.form.render_for_display`](#charthopformrender_for_display)
  * [`charthop.form.rerender_question_update`](#charthopformrerender_question_update)
  * [`charthop.form.send_emails_and_chat_notifications`](#charthopformsend_emails_and_chat_notifications)
  * [`charthop.form.send_reminder_notification`](#charthopformsend_reminder_notification)
  * [`charthop.form.submit_draft_data`](#charthopformsubmit_draft_data)
  * [`charthop.form.submit_form_data`](#charthopformsubmit_form_data)
  * [`charthop.form.submit_form_draft`](#charthopformsubmit_form_draft)
  * [`charthop.form.submit_form_response`](#charthopformsubmit_form_response)
  * [`charthop.form.update_existing_form`](#charthopformupdate_existing_form)
  * [`charthop.form.update_form_status`](#charthopformupdate_form_status)
  * [`charthop.form_response.get_by_form`](#charthopform_responseget_by_form)
  * [`charthop.form_response.get_by_id`](#charthopform_responseget_by_id)
  * [`charthop.form_response.get_form_response_count`](#charthopform_responseget_form_response_count)
  * [`charthop.form_response.remove_by_id`](#charthopform_responseremove_by_id)
  * [`charthop.form_response.update_answers_metadata`](#charthopform_responseupdate_answers_metadata)
  * [`charthop.form_response.update_metadata`](#charthopform_responseupdate_metadata)
  * [`charthop.group.create_new_group`](#charthopgroupcreate_new_group)
  * [`charthop.group.find_in_org_of_type`](#charthopgroupfind_in_org_of_type)
  * [`charthop.group.find_of_type`](#charthopgroupfind_of_type)
  * [`charthop.group.find_orphaned_groups`](#charthopgroupfind_orphaned_groups)
  * [`charthop.group.get_by_id`](#charthopgroupget_by_id)
  * [`charthop.group.get_organized_group_counts`](#charthopgroupget_organized_group_counts)
  * [`charthop.group.import_csv_data`](#charthopgroupimport_csv_data)
  * [`charthop.group.mark_multiple_as_deleted`](#charthopgroupmark_multiple_as_deleted)
  * [`charthop.group.remove_by_group_id`](#charthopgroupremove_by_group_id)
  * [`charthop.group.update_group_details`](#charthopgroupupdate_group_details)
  * [`charthop.guideline.all_for_comp_review`](#charthopguidelineall_for_comp_review)
  * [`charthop.guideline.calculate_matrix_values_for_specific_guideline`](#charthopguidelinecalculate_matrix_values_for_specific_guideline)
  * [`charthop.guideline.create_new_guideline`](#charthopguidelinecreate_new_guideline)
  * [`charthop.guideline.get_specific_guideline`](#charthopguidelineget_specific_guideline)
  * [`charthop.guideline.remove_by_id`](#charthopguidelineremove_by_id)
  * [`charthop.guideline.update_guideline`](#charthopguidelineupdate_guideline)
  * [`charthop.import.csv_data`](#charthopimportcsv_data)
  * [`charthop.import.csv_data_column_match`](#charthopimportcsv_data_column_match)
  * [`charthop.import.csv_data_with_column_match`](#charthopimportcsv_data_with_column_match)
  * [`charthop.import.csv_data_with_file_path`](#charthopimportcsv_data_with_file_path)
  * [`charthop.import.spreadsheet_validation`](#charthopimportspreadsheet_validation)
  * [`charthop.job.create_new_job`](#charthopjobcreate_new_job)
  * [`charthop.job.find_in_organization`](#charthopjobfind_in_organization)
  * [`charthop.job.find_in_organization_0`](#charthopjobfind_in_organization_0)
  * [`charthop.job.get_organization_job_count`](#charthopjobget_organization_job_count)
  * [`charthop.job.get_region_jobs_graph`](#charthopjobget_region_jobs_graph)
  * [`charthop.job.get_siblings_and_directs_map`](#charthopjobget_siblings_and_directs_map)
  * [`charthop.job.list_occupied_positions_by_job_and_date`](#charthopjoblist_occupied_positions_by_job_and_date)
  * [`charthop.job.perform_bulk_update`](#charthopjobperform_bulk_update)
  * [`charthop.job.remove_by_id`](#charthopjobremove_by_id)
  * [`charthop.job.update_job_details`](#charthopjobupdate_job_details)
  * [`charthop.job_level.create_new_job_level`](#charthopjob_levelcreate_new_job_level)
  * [`charthop.job_level.delete_job_level`](#charthopjob_leveldelete_job_level)
  * [`charthop.job_level.find_in_organization`](#charthopjob_levelfind_in_organization)
  * [`charthop.job_level.get_by_effective_date`](#charthopjob_levelget_by_effective_date)
  * [`charthop.job_level.update_job_level`](#charthopjob_levelupdate_job_level)
  * [`charthop.legal_doc.create_document`](#charthoplegal_doccreate_document)
  * [`charthop.legal_doc.get_by_name`](#charthoplegal_docget_by_name)
  * [`charthop.media.get_metadata`](#charthopmediaget_metadata)
  * [`charthop.media.get_metadata_0`](#charthopmediaget_metadata_0)
  * [`charthop.media.upload_new_media`](#charthopmediaupload_new_media)
  * [`charthop.media.upload_new_piece`](#charthopmediaupload_new_piece)
  * [`charthop.message.create_new_message`](#charthopmessagecreate_new_message)
  * [`charthop.message.get_all_for_user`](#charthopmessageget_all_for_user)
  * [`charthop.message.get_message_by_id`](#charthopmessageget_message_by_id)
  * [`charthop.message.get_message_by_key`](#charthopmessageget_message_by_key)
  * [`charthop.message.mark_bulk_as_seen`](#charthopmessagemark_bulk_as_seen)
  * [`charthop.message.mark_messages_as_read`](#charthopmessagemark_messages_as_read)
  * [`charthop.message.set_read_status`](#charthopmessageset_read_status)
  * [`charthop.metric.record_daily_metric`](#charthopmetricrecord_daily_metric)
  * [`charthop.multiplier.create_new_multiplier`](#charthopmultipliercreate_new_multiplier)
  * [`charthop.multiplier.delete_multiplier_by_id`](#charthopmultiplierdelete_multiplier_by_id)
  * [`charthop.multiplier.find_comp_band_multipliers_in_org`](#charthopmultiplierfind_comp_band_multipliers_in_org)
  * [`charthop.multiplier.find_comp_band_multipliers_in_org_0`](#charthopmultiplierfind_comp_band_multipliers_in_org_0)
  * [`charthop.multiplier.update_multipler_by_id`](#charthopmultiplierupdate_multipler_by_id)
  * [`charthop.notification.send_email_or_in_app_notification`](#charthopnotificationsend_email_or_in_app_notification)
  * [`charthop.oauth.authorize_user_token`](#charthopoauthauthorize_user_token)
  * [`charthop.oauth.exchange_idp_access_token_response`](#charthopoauthexchange_idp_access_token_response)
  * [`charthop.oauth.generate_bearer_token_from_sso`](#charthopoauthgenerate_bearer_token_from_sso)
  * [`charthop.oauth.login_via_idp`](#charthopoauthlogin_via_idp)
  * [`charthop.oauth.process_oauth_redirect_request`](#charthopoauthprocess_oauth_redirect_request)
  * [`charthop.oauth.return_view_token`](#charthopoauthreturn_view_token)
  * [`charthop.oauth.revoke_bearer_token`](#charthopoauthrevoke_bearer_token)
  * [`charthop.onboard.incomplete_steps`](#charthoponboardincomplete_steps)
  * [`charthop.onboard.mark_step_skipped`](#charthoponboardmark_step_skipped)
  * [`charthop.org.consent_terms_of_service`](#charthoporgconsent_terms_of_service)
  * [`charthop.org.create_new_job_placeholder`](#charthoporgcreate_new_job_placeholder)
  * [`charthop.org.create_new_org`](#charthoporgcreate_new_org)
  * [`charthop.org.get_by_id`](#charthoporgget_by_id)
  * [`charthop.org.get_by_slug`](#charthoporgget_by_slug)
  * [`charthop.org.get_data_user_person_by_id`](#charthoporgget_data_user_person_by_id)
  * [`charthop.org.get_data_user_person_count`](#charthoporgget_data_user_person_count)
  * [`charthop.org.get_data_users_persons`](#charthoporgget_data_users_persons)
  * [`charthop.org.get_oauth2_authorization_code`](#charthoporgget_oauth2_authorization_code)
  * [`charthop.org.get_user_access`](#charthoporgget_user_access)
  * [`charthop.org.get_validation_by_slug`](#charthoporgget_validation_by_slug)
  * [`charthop.org.get_welcome_email_settings`](#charthoporgget_welcome_email_settings)
  * [`charthop.org.list_visible_orgs`](#charthoporglist_visible_orgs)
  * [`charthop.org.send_test_email_to_oneself`](#charthoporgsend_test_email_to_oneself)
  * [`charthop.org.update_existing_org`](#charthoporgupdate_existing_org)
  * [`charthop.org.validate_app_install_authorization_code`](#charthoporgvalidate_app_install_authorization_code)
  * [`charthop.org_config.create_if_not_exists`](#charthoporg_configcreate_if_not_exists)
  * [`charthop.org_config.get_by_org_id`](#charthoporg_configget_by_org_id)
  * [`charthop.org_config.patch_existing_config`](#charthoporg_configpatch_existing_config)
  * [`charthop.person.create_new_person`](#charthoppersoncreate_new_person)
  * [`charthop.person.find_in_organization`](#charthoppersonfind_in_organization)
  * [`charthop.person.get_by_id`](#charthoppersonget_by_id)
  * [`charthop.person.get_geocodes_for_org`](#charthoppersonget_geocodes_for_org)
  * [`charthop.person.remove_by_id`](#charthoppersonremove_by_id)
  * [`charthop.person.update_by_id`](#charthoppersonupdate_by_id)
  * [`charthop.policy.check_validity_of`](#charthoppolicycheck_validity_of)
  * [`charthop.policy.copy_existing_policy`](#charthoppolicycopy_existing_policy)
  * [`charthop.policy.create_new_policy`](#charthoppolicycreate_new_policy)
  * [`charthop.policy.get_all_entity_action_maps`](#charthoppolicyget_all_entity_action_maps)
  * [`charthop.policy.get_all_policies`](#charthoppolicyget_all_policies)
  * [`charthop.policy.get_by_id`](#charthoppolicyget_by_id)
  * [`charthop.policy.remove_by_id`](#charthoppolicyremove_by_id)
  * [`charthop.policy.update_existing_policy`](#charthoppolicyupdate_existing_policy)
  * [`charthop.position.assign_job_to_position`](#charthoppositionassign_job_to_position)
  * [`charthop.position.create_new_position`](#charthoppositioncreate_new_position)
  * [`charthop.position.delete_and_purge`](#charthoppositiondelete_and_purge)
  * [`charthop.position.delete_position`](#charthoppositiondelete_position)
  * [`charthop.position.get_by_id`](#charthoppositionget_by_id)
  * [`charthop.position.get_history_by_id`](#charthoppositionget_history_by_id)
  * [`charthop.position.import_csv_data_with_file_path`](#charthoppositionimport_csv_data_with_file_path)
  * [`charthop.position.list`](#charthoppositionlist)
  * [`charthop.position.remove_job_from_position`](#charthoppositionremove_job_from_position)
  * [`charthop.position.update_job_dates_on_position`](#charthoppositionupdate_job_dates_on_position)
  * [`charthop.position.update_position_details`](#charthoppositionupdate_position_details)
  * [`charthop.preload.preloaded_data_retrieval`](#charthoppreloadpreloaded_data_retrieval)
  * [`charthop.process.check_process_status`](#charthopprocesscheck_process_status)
  * [`charthop.process.create_new_pending_process`](#charthopprocesscreate_new_pending_process)
  * [`charthop.process.create_pending_process`](#charthopprocesscreate_pending_process)
  * [`charthop.process.create_pending_process_with_user_id`](#charthopprocesscreate_pending_process_with_user_id)
  * [`charthop.process.decrement_step`](#charthopprocessdecrement_step)
  * [`charthop.process.download_file_by_id`](#charthopprocessdownload_file_by_id)
  * [`charthop.process.download_log`](#charthopprocessdownload_log)
  * [`charthop.process.get_events_by_process_id`](#charthopprocessget_events_by_process_id)
  * [`charthop.process.get_last_sync_for_app_user`](#charthopprocessget_last_sync_for_app_user)
  * [`charthop.process.get_previously_run_processes`](#charthopprocessget_previously_run_processes)
  * [`charthop.process.increment_process_step`](#charthopprocessincrement_process_step)
  * [`charthop.process.resume_process_with_user_id`](#charthopprocessresume_process_with_user_id)
  * [`charthop.process.resume_with_file`](#charthopprocessresume_with_file)
  * [`charthop.process.update_process_state`](#charthopprocessupdate_process_state)
  * [`charthop.process.update_status_of_process`](#charthopprocessupdate_status_of_process)
  * [`charthop.process.upload_file_and_mark_complete`](#charthopprocessupload_file_and_mark_complete)
  * [`charthop.product.create_new_product`](#charthopproductcreate_new_product)
  * [`charthop.product.get_by_id`](#charthopproductget_by_id)
  * [`charthop.product.list_all_products`](#charthopproductlist_all_products)
  * [`charthop.product.update_existing_product`](#charthopproductupdate_existing_product)
  * [`charthop.profile_tab.create_new_tab`](#charthopprofile_tabcreate_new_tab)
  * [`charthop.profile_tab.delete_profile_tab`](#charthopprofile_tabdelete_profile_tab)
  * [`charthop.profile_tab.find_tabs_for_job`](#charthopprofile_tabfind_tabs_for_job)
  * [`charthop.profile_tab.get_by_org_id_and_tab_id`](#charthopprofile_tabget_by_org_id_and_tab_id)
  * [`charthop.profile_tab.get_evaluate_profile_tab_content`](#charthopprofile_tabget_evaluate_profile_tab_content)
  * [`charthop.profile_tab.get_profile_tabs`](#charthopprofile_tabget_profile_tabs)
  * [`charthop.profile_tab.list_profile_tabs`](#charthopprofile_tablist_profile_tabs)
  * [`charthop.profile_tab.update_existing_tab`](#charthopprofile_tabupdate_existing_tab)
  * [`charthop.query.expire_live_query`](#charthopqueryexpire_live_query)
  * [`charthop.query.live_query_result`](#charthopquerylive_query_result)
  * [`charthop.query.live_query_token`](#charthopquerylive_query_token)
  * [`charthop.query.query_tokens`](#charthopqueryquery_tokens)
  * [`charthop.question.create`](#charthopquestioncreate)
  * [`charthop.question.get_all_in_org`](#charthopquestionget_all_in_org)
  * [`charthop.question.get_by_id`](#charthopquestionget_by_id)
  * [`charthop.question.remove`](#charthopquestionremove)
  * [`charthop.question.update_by_org_and_id`](#charthopquestionupdate_by_org_and_id)
  * [`charthop.report.bulk_delete`](#charthopreportbulk_delete)
  * [`charthop.report.create_exact_copy`](#charthopreportcreate_exact_copy)
  * [`charthop.report.create_new_report`](#charthopreportcreate_new_report)
  * [`charthop.report.duplicate_reports`](#charthopreportduplicate_reports)
  * [`charthop.report.export_chart_csv`](#charthopreportexport_chart_csv)
  * [`charthop.report.find_report_by_id`](#charthopreportfind_report_by_id)
  * [`charthop.report.get_all_paginated`](#charthopreportget_all_paginated)
  * [`charthop.report.get_all_report_charts`](#charthopreportget_all_report_charts)
  * [`charthop.report.get_count_of_reports_in_organization`](#charthopreportget_count_of_reports_in_organization)
  * [`charthop.report.remove_by_id`](#charthopreportremove_by_id)
  * [`charthop.report.timeseries_data_arbitrary_queries`](#charthopreporttimeseries_data_arbitrary_queries)
  * [`charthop.report.update_existing_report`](#charthopreportupdate_existing_report)
  * [`charthop.report_chart.clone_chart`](#charthopreport_chartclone_chart)
  * [`charthop.report_chart.create_new_chart`](#charthopreport_chartcreate_new_chart)
  * [`charthop.report_chart.export_data`](#charthopreport_chartexport_data)
  * [`charthop.report_chart.get_all`](#charthopreport_chartget_all)
  * [`charthop.report_chart.get_by_chart_id`](#charthopreport_chartget_by_chart_id)
  * [`charthop.report_chart.query_underlying_data_in_chart`](#charthopreport_chartquery_underlying_data_in_chart)
  * [`charthop.report_chart.remove_by_id`](#charthopreport_chartremove_by_id)
  * [`charthop.report_chart.update_existing_chart_data`](#charthopreport_chartupdate_existing_chart_data)
  * [`charthop.role.copy_existing_role`](#charthoprolecopy_existing_role)
  * [`charthop.role.create_new_role`](#charthoprolecreate_new_role)
  * [`charthop.role.get_all_in_org`](#charthoproleget_all_in_org)
  * [`charthop.role.get_role_by_id`](#charthoproleget_role_by_id)
  * [`charthop.role.remove_by_id`](#charthoproleremove_by_id)
  * [`charthop.role.update_existing`](#charthoproleupdate_existing)
  * [`charthop.saml.perform_sso_assertion`](#charthopsamlperform_sso_assertion)
  * [`charthop.saml.perform_sso_assertion_0`](#charthopsamlperform_sso_assertion_0)
  * [`charthop.saml.save_per_org_xml_cert_from_idp`](#charthopsamlsave_per_org_xml_cert_from_idp)
  * [`charthop.saml.save_per_org_xml_cert_from_idp_0`](#charthopsamlsave_per_org_xml_cert_from_idp_0)
  * [`charthop.scenario.adjust_dates`](#charthopscenarioadjust_dates)
  * [`charthop.scenario.bulk_archive_scenarios`](#charthopscenariobulk_archive_scenarios)
  * [`charthop.scenario.combine_scenarios`](#charthopscenariocombine_scenarios)
  * [`charthop.scenario.create_new`](#charthopscenariocreate_new)
  * [`charthop.scenario.delete_bulk_scenarios`](#charthopscenariodelete_bulk_scenarios)
  * [`charthop.scenario.get_by_id`](#charthopscenarioget_by_id)
  * [`charthop.scenario.list_paginated_scenarios`](#charthopscenariolist_paginated_scenarios)
  * [`charthop.scenario.manually_recalculate_metadata`](#charthopscenariomanually_recalculate_metadata)
  * [`charthop.scenario.merge_into_primary_timeline`](#charthopscenariomerge_into_primary_timeline)
  * [`charthop.scenario.remove_by_id`](#charthopscenarioremove_by_id)
  * [`charthop.scenario.unarchive_set_of_scenarios`](#charthopscenariounarchive_set_of_scenarios)
  * [`charthop.scenario.update_scenario_change`](#charthopscenarioupdate_scenario_change)
  * [`charthop.scenario.update_shared_view_config`](#charthopscenarioupdate_shared_view_config)
  * [`charthop.search.org_data_by_org_id_and_search_string`](#charthopsearchorg_data_by_org_id_and_search_string)
  * [`charthop.status.api_is_up_and_available`](#charthopstatusapi_is_up_and_available)
  * [`charthop.stock.get_history`](#charthopstockget_history)
  * [`charthop.stock.get_price_by_date_type`](#charthopstockget_price_by_date_type)
  * [`charthop.stock.remove_price`](#charthopstockremove_price)
  * [`charthop.stock.upsert_price_by_date_type`](#charthopstockupsert_price_by_date_type)
  * [`charthop.stripe.create_setup_intent_secret`](#charthopstripecreate_setup_intent_secret)
  * [`charthop.stripe.get_all_plans`](#charthopstripeget_all_plans)
  * [`charthop.stripe.get_all_products`](#charthopstripeget_all_products)
  * [`charthop.stripe.get_product_by_id`](#charthopstripeget_product_by_id)
  * [`charthop.stripe.process_webhook_events`](#charthopstripeprocess_webhook_events)
  * [`charthop.table.create_new_table`](#charthoptablecreate_new_table)
  * [`charthop.table.delete_row`](#charthoptabledelete_row)
  * [`charthop.table.delete_row_from_history`](#charthoptabledelete_row_from_history)
  * [`charthop.table.export_data_to_csv`](#charthoptableexport_data_to_csv)
  * [`charthop.table.get_all_rows`](#charthoptableget_all_rows)
  * [`charthop.table.get_row_by_column`](#charthoptableget_row_by_column)
  * [`charthop.table.get_table_by_id_or_name`](#charthoptableget_table_by_id_or_name)
  * [`charthop.table.import_data_from_csv_file`](#charthoptableimport_data_from_csv_file)
  * [`charthop.table.list_in_org_paginated`](#charthoptablelist_in_org_paginated)
  * [`charthop.table.remove_by_id`](#charthoptableremove_by_id)
  * [`charthop.table.update_existing_row_data`](#charthoptableupdate_existing_row_data)
  * [`charthop.table.update_existing_table`](#charthoptableupdate_existing_table)
  * [`charthop.table.upsert_row_data`](#charthoptableupsert_row_data)
  * [`charthop.task.delete_bulk_tasks`](#charthoptaskdelete_bulk_tasks)
  * [`charthop.task.get_all_tasks`](#charthoptaskget_all_tasks)
  * [`charthop.task.get_assessment_tasks_summary`](#charthoptaskget_assessment_tasks_summary)
  * [`charthop.task.get_current_user_tasks`](#charthoptaskget_current_user_tasks)
  * [`charthop.task.mark_as_skipped`](#charthoptaskmark_as_skipped)
  * [`charthop.task.query_assessment_tasks`](#charthoptaskquery_assessment_tasks)
  * [`charthop.task.remove_by_id`](#charthoptaskremove_by_id)
  * [`charthop.task.remove_form_from_assessment`](#charthoptaskremove_form_from_assessment)
  * [`charthop.task.send_reminder_notification`](#charthoptasksend_reminder_notification)
  * [`charthop.task.update_status`](#charthoptaskupdate_status)
  * [`charthop.task_config.create_new_config`](#charthoptask_configcreate_new_config)
  * [`charthop.task_config.get_all_configs`](#charthoptask_configget_all_configs)
  * [`charthop.task_config.get_specific_config`](#charthoptask_configget_specific_config)
  * [`charthop.template.bulk_delete`](#charthoptemplatebulk_delete)
  * [`charthop.template.create_bulk_duplicate`](#charthoptemplatecreate_bulk_duplicate)
  * [`charthop.template.create_email`](#charthoptemplatecreate_email)
  * [`charthop.template.create_new_template`](#charthoptemplatecreate_new_template)
  * [`charthop.template.evaluate_against_job`](#charthoptemplateevaluate_against_job)
  * [`charthop.template.generate_pdfs_and_emails`](#charthoptemplategenerate_pdfs_and_emails)
  * [`charthop.template.generate_template_preview`](#charthoptemplategenerate_template_preview)
  * [`charthop.template.get_all_in_orgs`](#charthoptemplateget_all_in_orgs)
  * [`charthop.template.get_by_id`](#charthoptemplateget_by_id)
  * [`charthop.template.get_by_name`](#charthoptemplateget_by_name)
  * [`charthop.template.remove_by_id`](#charthoptemplateremove_by_id)
  * [`charthop.template.remove_email`](#charthoptemplateremove_email)
  * [`charthop.template.update_email_template`](#charthoptemplateupdate_email_template)
  * [`charthop.template.update_existing`](#charthoptemplateupdate_existing)
  * [`charthop.timeoff.approve_pending_request`](#charthoptimeoffapprove_pending_request)
  * [`charthop.timeoff.create_entry`](#charthoptimeoffcreate_entry)
  * [`charthop.timeoff.find_time_off_by_id`](#charthoptimeofffind_time_off_by_id)
  * [`charthop.timeoff.get_time_off`](#charthoptimeoffget_time_off)
  * [`charthop.timeoff.reject_time_off_request`](#charthoptimeoffreject_time_off_request)
  * [`charthop.timeoff.remove_entry`](#charthoptimeoffremove_entry)
  * [`charthop.timeoff.submit_time_off_request`](#charthoptimeoffsubmit_time_off_request)
  * [`charthop.timeoff.update_time_off_entry`](#charthoptimeoffupdate_time_off_entry)
  * [`charthop.timeoff.validate_timeoff_request`](#charthoptimeoffvalidate_timeoff_request)
  * [`charthop.usage.record_product_feature_usage`](#charthopusagerecord_product_feature_usage)
  * [`charthop.user.assign_role_to_multiple`](#charthopuserassign_role_to_multiple)
  * [`charthop.user.change_password`](#charthopuserchange_password)
  * [`charthop.user.create_new_user`](#charthopusercreate_new_user)
  * [`charthop.user.get_all_users_within_orgs`](#charthopuserget_all_users_within_orgs)
  * [`charthop.user.get_current_user`](#charthopuserget_current_user)
  * [`charthop.user.get_user_by_email`](#charthopuserget_user_by_email)
  * [`charthop.user.get_user_by_id`](#charthopuserget_user_by_id)
  * [`charthop.user.invite_multiple_new_users`](#charthopuserinvite_multiple_new_users)
  * [`charthop.user.return_user_by_person_id`](#charthopuserreturn_user_by_person_id)
  * [`charthop.user.revoke_access_token`](#charthopuserrevoke_access_token)
  * [`charthop.user.revoke_access_tokens`](#charthopuserrevoke_access_tokens)
  * [`charthop.user.send_password_reset_email`](#charthopusersend_password_reset_email)
  * [`charthop.user.update_existing_user`](#charthopuserupdate_existing_user)
  * [`charthop.user.viewed_user_details`](#charthopuserviewed_user_details)
  * [`charthop.webauthn.check_existing_key`](#charthopwebauthncheck_existing_key)
  * [`charthop.webauthn.remove_registered_credentials_by_email`](#charthopwebauthnremove_registered_credentials_by_email)
  * [`charthop.webauthn.verify_physical_key_for_user`](#charthopwebauthnverify_physical_key_for_user)
  * [`charthop.webauthn.verify_physical_key_for_user_0`](#charthopwebauthnverify_physical_key_for_user_0)
  * [`charthop.webauthn.verify_physical_key_for_user_1`](#charthopwebauthnverify_physical_key_for_user_1)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=ChartHop&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from chart_hop_python_sdk import ChartHop, ApiException

charthop = ChartHop(
)

try:
    # Return the appropriate actions that can be performed on an entity or set of entities
    entity_actions_response = charthop.access.entity_actions(
        org_id="orgId_example",
        type="type_example",
        id="string_example",
        action="string_example",
        fields="string_example",
        date="1970-01-01",
        scenario_id="string_example",
    )
    print(entity_actions_response)
except ApiException as e:
    print("Exception when calling AccessApi.entity_actions: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from chart_hop_python_sdk import ChartHop, ApiException

charthop = ChartHop(
)

async def main():
    try:
        # Return the appropriate actions that can be performed on an entity or set of entities
        entity_actions_response = await charthop.access.aentity_actions(
            org_id="orgId_example",
            type="type_example",
            id="string_example",
            action="string_example",
            fields="string_example",
            date="1970-01-01",
            scenario_id="string_example",
        )
        print(entity_actions_response)
    except ApiException as e:
        print("Exception when calling AccessApi.entity_actions: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from chart_hop_python_sdk import ChartHop, ApiException

charthop = ChartHop(
)

try:
    # Return the appropriate actions that can be performed on an entity or set of entities
    entity_actions_response = charthop.access.raw.entity_actions(
        org_id="orgId_example",
        type="type_example",
        id="string_example",
        action="string_example",
        fields="string_example",
        date="1970-01-01",
        scenario_id="string_example",
    )
    pprint(entity_actions_response.body)
    pprint(entity_actions_response.body["access"])
    pprint(entity_actions_response.headers)
    pprint(entity_actions_response.status)
    pprint(entity_actions_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccessApi.entity_actions: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `charthop.access.entity_actions`<a id="charthopaccessentity_actions"></a>

Return the appropriate actions that can be performed on an entity or set of entities

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
entity_actions_response = charthop.access.entity_actions(
    org_id="orgId_example",
    type="type_example",
    id="string_example",
    action="string_example",
    fields="string_example",
    date="1970-01-01",
    scenario_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Entity type

##### id: `str`<a id="id-str"></a>

Entity ids

##### action: `str`<a id="action-str"></a>

Actions, defaults to update,delete

##### fields: `str`<a id="fields-str"></a>

Fields to check, defaults to all fields

##### date: `date`<a id="date-date"></a>

Date, defaults to today

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id, defaults to primary

#### 🔄 Return<a id="🔄-return"></a>

[`AccessResponse`](./chart_hop_python_sdk/pydantic/access_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/access/entity/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.action.create_new_action`<a id="charthopactioncreate_new_action"></a>

Create an action

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_action_response = charthop.action.create_new_action(
    action={
        "cron_schedule": "5 4 * * *",
        "steps": [
            {
                "step_id": "588f7ee98f138b19220041a7",
                "type": "FORM",
            }
        ],
        "status": "ACTIVE",
        "sensitive": True,
        "category": "ONBOARDING",
    },
    org_id="orgId_example",
    step_task_configs=[
        {
            "org_id": "588f7ee98f138b19220041a7",
            "assessment_id": "588f7ee98f138b19220041a7",
            "parent_entity_id": "588f7ee98f138b19220041a7",
            "entity_id": "588f7ee98f138b19220041a7",
            "type": "FORM_SUBMIT",
            "past_due_action": "NONE",
            "create_id": "588f7ee98f138b19220041a7",
            "create_at": "2017-01-24T13:57:52Z",
            "update_id": "588f7ee98f138b19220041a7",
            "update_at": "2017-01-24T13:57:52Z",
            "delete_id": "588f7ee98f138b19220041a7",
            "delete_at": "2017-01-24T13:57:52Z",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: [`CreateAction`](./chart_hop_python_sdk/type/create_action.py)<a id="action-createactionchart_hop_python_sdktypecreate_actionpy"></a>


##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### step_task_configs: List[`PartialTaskConfig`]<a id="step_task_configs-listpartialtaskconfig"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateActionBody`](./chart_hop_python_sdk/type/create_action_body.py)
Action data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Action`](./chart_hop_python_sdk/pydantic/action.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/action` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.action.delete_action_by_id`<a id="charthopactiondelete_action_by_id"></a>

Delete an action

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.action.delete_action_by_id(
    org_id="orgId_example",
    action_id="actionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### action_id: `str`<a id="action_id-str"></a>

Action id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/action/{actionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.action.execute_action_for_testing`<a id="charthopactionexecute_action_for_testing"></a>

Run an action - for testing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.action.execute_action_for_testing(
    job_id="string_example",
    event_code="string_example",
    org_id="orgId_example",
    action_id="actionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

##### event_code: `str`<a id="event_code-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### action_id: `str`<a id="action_id-str"></a>

Action id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ActionRunRequest`](./chart_hop_python_sdk/type/action_run_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/action/{actionId}/run` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.action.get_action_by_id`<a id="charthopactionget_action_by_id"></a>

Return a particular action by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_response = charthop.action.get_action_by_id(
    org_id="orgId_example",
    action_id="actionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### action_id: `str`<a id="action_id-str"></a>

Action id

#### 🔄 Return<a id="🔄-return"></a>

[`Action`](./chart_hop_python_sdk/pydantic/action.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/action/{actionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.action.get_all_paginated`<a id="charthopactionget_all_paginated"></a>

Return all actions in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_paginated_response = charthop.action.get_all_paginated(
    org_id="orgId_example",
    _from="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

Action id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsAction`](./chart_hop_python_sdk/pydantic/results_action.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/action` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.action.update_existing_action_by_id`<a id="charthopactionupdate_existing_action_by_id"></a>

Update an existing action

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.action.update_existing_action_by_id(
    action={
        "cron_schedule": "5 4 * * *",
        "status": "ACTIVE",
        "category": "ONBOARDING",
    },
    org_id="orgId_example",
    action_id="actionId_example",
    step_task_configs=[
        {
            "org_id": "588f7ee98f138b19220041a7",
            "assessment_id": "588f7ee98f138b19220041a7",
            "parent_entity_id": "588f7ee98f138b19220041a7",
            "entity_id": "588f7ee98f138b19220041a7",
            "type": "FORM_SUBMIT",
            "past_due_action": "NONE",
            "create_id": "588f7ee98f138b19220041a7",
            "create_at": "2017-01-24T13:57:52Z",
            "update_id": "588f7ee98f138b19220041a7",
            "update_at": "2017-01-24T13:57:52Z",
            "delete_id": "588f7ee98f138b19220041a7",
            "delete_at": "2017-01-24T13:57:52Z",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: [`UpdateAction`](./chart_hop_python_sdk/type/update_action.py)<a id="action-updateactionchart_hop_python_sdktypeupdate_actionpy"></a>


##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### action_id: `str`<a id="action_id-str"></a>

Action id

##### step_task_configs: List[`PartialTaskConfig`]<a id="step_task_configs-listpartialtaskconfig"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchActionBody`](./chart_hop_python_sdk/type/patch_action_body.py)
Action data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/action/{actionId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.ai.generate_text_summary`<a id="charthopaigenerate_text_summary"></a>

Use AI to generate a summary of text form responses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_text_summary_response = charthop.ai.generate_text_summary(
    question_id="string_example",
    org_id="orgId_example",
    form_id="string_example",
    assessment_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### question_id: `str`<a id="question_id-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

##### assessment_id: `str`<a id="assessment_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SummarizeFormResponsesRequest`](./chart_hop_python_sdk/type/summarize_form_responses_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SummarizeResponse`](./chart_hop_python_sdk/pydantic/summarize_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/ai/form-response/summary` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.create_new_app`<a id="charthopappcreate_new_app"></a>

Create a new app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_app_response = charthop.app.create_new_app(
    summary="The Slack app does X Y and Z",
    title="Slack",
    org_id="588f7ee98f138b19220041a7",
    name="slack-import",
    cron_order=1,
    min_access="NONE",
    type="APP",
    tags=[
        "string_example"
    ],
    description="The Slack app does X Y and Z",
    redirect_uris=[
        "string_example"
    ],
    allowed_ips=[
        "string_example"
    ],
    config_fields=[
        {
            "name": "name_example",
            "label": "label_example",
            "type": "STRING",
        }
    ],
    setup_instructions="To install the Slack, use your API key from X and Y",
    cron_schedule="DAILY",
    cron_day_of_week="MONDAY",
    image_path="/",
    wordmark_image_path="/",
    powered_by_image_path="/",
    status="GLOBAL",
    role_id="string_example",
    event_notify_url="string_example",
    payload={
        "key": "string_example",
    },
    events=[
        "string_example"
    ],
    bundle={
    },
    scopes=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### summary: `str`<a id="summary-str"></a>

short summary of app

##### title: `str`<a id="title-str"></a>

human-readable name of app

##### org_id: `str`<a id="org_id-str"></a>

organization id

##### name: `str`<a id="name-str"></a>

short unique name

##### cron_order: `int`<a id="cron_order-int"></a>

execution order of the cron (lower numbers execute earlier)

##### min_access: `str`<a id="min_access-str"></a>

minimum access level requested by app

##### type: `str`<a id="type-str"></a>

APP, BUNDLE, or INTERNAL

##### tags: [`CreateAppTags`](./chart_hop_python_sdk/type/create_app_tags.py)<a id="tags-createapptagschart_hop_python_sdktypecreate_app_tagspy"></a>

##### description: `str`<a id="description-str"></a>

full description of app, in Markdown

##### redirect_uris: [`CreateAppRedirectUris`](./chart_hop_python_sdk/type/create_app_redirect_uris.py)<a id="redirect_uris-createappredirecturischart_hop_python_sdktypecreate_app_redirect_urispy"></a>

##### allowed_ips: [`CreateAppAllowedIps`](./chart_hop_python_sdk/type/create_app_allowed_ips.py)<a id="allowed_ips-createappallowedipschart_hop_python_sdktypecreate_app_allowed_ipspy"></a>

##### config_fields: List[`AppConfigField`]<a id="config_fields-listappconfigfield"></a>

list of configuration fields

##### setup_instructions: `str`<a id="setup_instructions-str"></a>

setup instructions, in Markdown

##### cron_schedule: `str`<a id="cron_schedule-str"></a>

cron schedule

##### cron_day_of_week: `str`<a id="cron_day_of_week-str"></a>

Day of week if cronSchedule is WEEKLY

##### image_path: `str`<a id="image_path-str"></a>

path to avatar profile image, should be approximately square dimensions and show logo

##### wordmark_image_path: `str`<a id="wordmark_image_path-str"></a>

path to larger profile logo image containing brand wordmark, does not need to be square dimensions

##### powered_by_image_path: `str`<a id="powered_by_image_path-str"></a>

path to powered by image, should be approximately square dimensions and show logo

##### status: `str`<a id="status-str"></a>

current status of app

##### role_id: `str`<a id="role_id-str"></a>

roleId requested by app

##### event_notify_url: `str`<a id="event_notify_url-str"></a>

URL that should be notified on events

##### payload: [`CreateAppPayload`](./chart_hop_python_sdk/type/create_app_payload.py)<a id="payload-createapppayloadchart_hop_python_sdktypecreate_app_payloadpy"></a>

##### events: [`CreateAppEvents`](./chart_hop_python_sdk/type/create_app_events.py)<a id="events-createappeventschart_hop_python_sdktypecreate_app_eventspy"></a>

##### bundle: [`Bundle`](./chart_hop_python_sdk/type/bundle.py)<a id="bundle-bundlechart_hop_python_sdktypebundlepy"></a>


##### scopes: [`CreateAppScopes`](./chart_hop_python_sdk/type/create_app_scopes.py)<a id="scopes-createappscopeschart_hop_python_sdktypecreate_app_scopespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateApp`](./chart_hop_python_sdk/type/create_app.py)
App data to create

#### 🔄 Return<a id="🔄-return"></a>

[`App`](./chart_hop_python_sdk/pydantic/app.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.find_installed_app_users`<a id="charthopappfind_installed_app_users"></a>

Get an installed app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_installed_app_users_response = charthop.app.find_installed_app_users(
    org_id="orgId_example",
    app_user_id="appUserId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

App user id

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./chart_hop_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/{appUserId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.find_installed_app_users_0`<a id="charthopappfind_installed_app_users_0"></a>

Find installed app users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_installed_app_users_0_response = charthop.app.find_installed_app_users_0(
    org_id="orgId_example",
    type="string_example",
    tags="string_example",
    statuses="string_example",
    include_former=True,
    _from="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Filter by type (app, bundle)

##### tags: `str`<a id="tags-str"></a>

Filter by tag

##### statuses: `str`<a id="statuses-str"></a>

Filter by App User statuses, comma-separated. Accepted values: ['NORMAL', 'INACTIVE', 'UNINSTALLED']

##### include_former: `bool`<a id="include_former-bool"></a>

Whether to include app users with NONE access to orgs they pertain to.  Default is false

##### _from: `str`<a id="_from-str"></a>

App id to start from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsUser`](./chart_hop_python_sdk/pydantic/results_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.generate_or_regenerate_access_token`<a id="charthopappgenerate_or_regenerate_access_token"></a>

Generate or regenerate a long-lived access token for the app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_or_regenerate_access_token_response = charthop.app.generate_or_regenerate_access_token(
    scope="string_example",
    org_id="orgId_example",
    app_user_id="appUserId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

scope being requested

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

App user id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ScopeRequest`](./chart_hop_python_sdk/type/scope_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenResponse`](./chart_hop_python_sdk/pydantic/access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/{appUserId}/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.get_active_apps_by_org`<a id="charthopappget_active_apps_by_org"></a>

Return all active apps available for a particular org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_active_apps_by_org_response = charthop.app.get_active_apps_by_org(
    org_id="orgId_example",
    q="string_example",
    type="string_example",
    tags="string_example",
    _from="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### q: `str`<a id="q-str"></a>

Search query

##### type: `str`<a id="type-str"></a>

Filter by type (app, bundle)

##### tags: `str`<a id="tags-str"></a>

Filter by tags

##### _from: `str`<a id="_from-str"></a>

App id to start from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsApp`](./chart_hop_python_sdk/pydantic/results_app.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.get_by_id`<a id="charthopappget_by_id"></a>

Return a particular app by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.app.get_by_id(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

App id

#### 🔄 Return<a id="🔄-return"></a>

[`App`](./chart_hop_python_sdk/pydantic/app.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/{appId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.get_by_name`<a id="charthopappget_by_name"></a>

Return a particular app by name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_name_response = charthop.app.get_by_name(
    app_name="appName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_name: `str`<a id="app_name-str"></a>

App name

#### 🔄 Return<a id="🔄-return"></a>

[`App`](./chart_hop_python_sdk/pydantic/app.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/name/{appName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.get_installed_app_by_name`<a id="charthopappget_installed_app_by_name"></a>

Get an installed app by name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_installed_app_by_name_response = charthop.app.get_installed_app_by_name(
    org_id="orgId_example",
    app_name="appName_example",
    include_inactive=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_name: `str`<a id="app_name-str"></a>

App name

##### include_inactive: `bool`<a id="include_inactive-bool"></a>

If the installed appUser is inactive, load inactive instead

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./chart_hop_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/name/{appName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.get_oauth2_authorization_code`<a id="charthopappget_oauth2_authorization_code"></a>

Retrieve an Oauth2 authorization code for this app, which can be exchanged for an access token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_oauth2_authorization_code_response = charthop.app.get_oauth2_authorization_code(
    org_id="orgId_example",
    app_user_id="appUserId_example",
    scope="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

App user id

##### scope: `str`<a id="scope-str"></a>

Scopes

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenResponse`](./chart_hop_python_sdk/pydantic/access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/{appUserId}/code` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.get_token_for_app`<a id="charthopappget_token_for_app"></a>

Retrieve the current token for this app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_token_for_app_response = charthop.app.get_token_for_app(
    org_id="orgId_example",
    app_user_id="appUserId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

App user id

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenResponse`](./chart_hop_python_sdk/pydantic/access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/{appUserId}/token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.get_token_for_app_0`<a id="charthopappget_token_for_app_0"></a>

Retrieve the current token for this app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.app.get_token_for_app_0(
    org_id="orgId_example",
    app_user_id="appUserId_example",
    install_data_name="installDataName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

App user id

##### install_data_name: `str`<a id="install_data_name-str"></a>

Name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/{appUserId}/installdata/{installDataName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.install_app_for_org`<a id="charthopappinstall_app_for_org"></a>

Install an app for a particular org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.app.install_app_for_org(
    orgs=[
        {
            "org_id": "5887a7718f138b6a2a0041a7",
            "person_id": "5887a7718f138b6a2a0041a7",
            "access": "NONE",
            "role_id": "5887a7718f138b6a2a0041a7",
        }
    ],
    org_id="orgId_example",
    app_id="string_example",
    name={
        "first": "Jane",
        "middle": "Quidditch",
        "last": "Public",
        "pref": "JQ",
        "pref_last": "Smith",
    },
    email="bob@example.com",
    image_path="/",
    status="SUPERUSER",
    options={},
    internal_options={},
    secrets={},
    email_settings=[
        {
            "category": "ADMINISTRATIVE",
            "subscribed": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### orgs: List[`OrgAccess`]<a id="orgs-listorgaccess"></a>

list of member orgs with permission levels

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_id: `str`<a id="app_id-str"></a>

if the user is an app user, the id of the app

##### name: [`Name`](./chart_hop_python_sdk/type/name.py)<a id="name-namechart_hop_python_sdktypenamepy"></a>


##### email: `str`<a id="email-str"></a>

email address of user

##### image_path: `str`<a id="image_path-str"></a>

path to full-sized profile image in storage

##### status: `str`<a id="status-str"></a>

current status of user

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

for apps, options (specific options are specific to the particular app); for users, user-set preferences

##### internal_options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="internal_options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

internal (ChartHop controlled) options

##### secrets: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="secrets-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

write-only secrets; the content of these secrets are not retrievable via the external-facing API

##### email_settings: List[`UserEmailSetting`]<a id="email_settings-listuseremailsetting"></a>

Email settings for the user

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateUser`](./chart_hop_python_sdk/type/create_user.py)
App user data to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.list_public_global_apps`<a id="charthopapplist_public_global_apps"></a>

Return all publicly visible global apps

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_public_global_apps_response = charthop.app.list_public_global_apps(
    tag="string_example",
    _from="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag: `str`<a id="tag-str"></a>

Tag to filter by

##### _from: `str`<a id="_from-str"></a>

App id to start from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsApp`](./chart_hop_python_sdk/pydantic/results_app.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.remove_by_id`<a id="charthopappremove_by_id"></a>

Delete an app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.app.remove_by_id(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

App id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/{appId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.run_installed_app`<a id="charthopapprun_installed_app"></a>

Run an installed app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
run_installed_app_response = charthop.app.run_installed_app(
    org_id="orgId_example",
    app_user_id="appUserId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

App user id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/{appUserId}/run` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.send_email_notification`<a id="charthopappsend_email_notification"></a>

Send an email notification to the configured notify users, on behalf of an app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.app.send_email_notification(
    email_subject="string_example",
    email_content_html="string_example",
    email_markdown="string_example",
    chat_markdown="string_example",
    notify_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email_subject: `str`<a id="email_subject-str"></a>

email subject line

##### email_content_html: `str`<a id="email_content_html-str"></a>

email HTML content

##### email_markdown: `str`<a id="email_markdown-str"></a>

email Markdown content

##### chat_markdown: `str`<a id="chat_markdown-str"></a>

chat Markdown content, if chat message should be different/abbreviated

##### notify_type: `str`<a id="notify_type-str"></a>

Type of notification

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NotifyRequest`](./chart_hop_python_sdk/type/notify_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/notify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.uninstall_app_by_user_id`<a id="charthopappuninstall_app_by_user_id"></a>

Uninstall an app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.app.uninstall_app_by_user_id(
    org_id="orgId_example",
    app_user_id="appUserId_example",
    keep_entity_ids="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

App user id

##### keep_entity_ids: `str`<a id="keep_entity_ids-str"></a>

Comma-separated list of bundle-installed entities to delete -- if this parameter is omitted, all bundle-installed entities will be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/{appUserId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.update_existing_app`<a id="charthopappupdate_existing_app"></a>

Update an existing app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.app.update_existing_app(
    app_id="appId_example",
    tags=[
        "string_example"
    ],
    summary="The Slack app does X Y and Z",
    title="Slack",
    description="The Slack app does X Y and Z",
    name="slack-import",
    redirect_uris=[
        "string_example"
    ],
    allowed_ips=[
        "string_example"
    ],
    config_fields=[
        {
            "name": "name_example",
            "label": "label_example",
            "type": "STRING",
        }
    ],
    setup_instructions="To install the Slack, use your API key from X and Y",
    cron_order=1,
    cron_schedule="DAILY",
    cron_day_of_week="MONDAY",
    image_path="/",
    wordmark_image_path="/",
    powered_by_image_path="/",
    status="GLOBAL",
    min_access="NONE",
    role_id="string_example",
    event_notify_url="string_example",
    payload={
        "key": "string_example",
    },
    events=[
        "string_example"
    ],
    type="APP",
    bundle={
    },
    scopes=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

App id

##### tags: [`UpdateAppTags`](./chart_hop_python_sdk/type/update_app_tags.py)<a id="tags-updateapptagschart_hop_python_sdktypeupdate_app_tagspy"></a>

##### summary: `str`<a id="summary-str"></a>

short summary of app

##### title: `str`<a id="title-str"></a>

human-readable name of app

##### description: `str`<a id="description-str"></a>

full description of app, in Markdown

##### name: `str`<a id="name-str"></a>

short unique name

##### redirect_uris: [`UpdateAppRedirectUris`](./chart_hop_python_sdk/type/update_app_redirect_uris.py)<a id="redirect_uris-updateappredirecturischart_hop_python_sdktypeupdate_app_redirect_urispy"></a>

##### allowed_ips: [`UpdateAppAllowedIps`](./chart_hop_python_sdk/type/update_app_allowed_ips.py)<a id="allowed_ips-updateappallowedipschart_hop_python_sdktypeupdate_app_allowed_ipspy"></a>

##### config_fields: List[`AppConfigField`]<a id="config_fields-listappconfigfield"></a>

list of configuration fields

##### setup_instructions: `str`<a id="setup_instructions-str"></a>

setup instructions, in Markdown

##### cron_order: `int`<a id="cron_order-int"></a>

execution order of the cron (lower numbers execute earlier)

##### cron_schedule: `str`<a id="cron_schedule-str"></a>

cron schedule

##### cron_day_of_week: `str`<a id="cron_day_of_week-str"></a>

Day of week if cronSchedule is WEEKLY

##### image_path: `str`<a id="image_path-str"></a>

path to avatar profile image, should be approximately square dimensions and show logo

##### wordmark_image_path: `str`<a id="wordmark_image_path-str"></a>

path to larger profile logo image containing brand wordmark, does not need to be square dimensions

##### powered_by_image_path: `str`<a id="powered_by_image_path-str"></a>

path to powered by image, should be approximately square dimensions and show logo

##### status: `str`<a id="status-str"></a>

current status of app

##### min_access: `str`<a id="min_access-str"></a>

minimum access level requested by app

##### role_id: `str`<a id="role_id-str"></a>

roleId requested by app

##### event_notify_url: `str`<a id="event_notify_url-str"></a>

URL that should be notified on events

##### payload: [`UpdateAppPayload`](./chart_hop_python_sdk/type/update_app_payload.py)<a id="payload-updateapppayloadchart_hop_python_sdktypeupdate_app_payloadpy"></a>

##### events: [`UpdateAppEvents`](./chart_hop_python_sdk/type/update_app_events.py)<a id="events-updateappeventschart_hop_python_sdktypeupdate_app_eventspy"></a>

##### type: `str`<a id="type-str"></a>

APP, BUNDLE, or INTERNAL

##### bundle: [`Bundle`](./chart_hop_python_sdk/type/bundle.py)<a id="bundle-bundlechart_hop_python_sdktypebundlepy"></a>


##### scopes: [`UpdateAppScopes`](./chart_hop_python_sdk/type/update_app_scopes.py)<a id="scopes-updateappscopeschart_hop_python_sdktypeupdate_app_scopespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateApp`](./chart_hop_python_sdk/type/update_app.py)
App data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/{appId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.update_installed_app`<a id="charthopappupdate_installed_app"></a>

Update the settings of an installed app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.app.update_installed_app(
    org_id="orgId_example",
    app_user_id="appUserId_example",
    app_id="string_example",
    name={
        "first": "Jane",
        "middle": "Quidditch",
        "last": "Public",
        "pref": "JQ",
        "pref_last": "Smith",
    },
    email="bob@example.com",
    orgs=[
        {
            "org_id": "5887a7718f138b6a2a0041a7",
            "person_id": "5887a7718f138b6a2a0041a7",
            "access": "NONE",
            "role_id": "5887a7718f138b6a2a0041a7",
        }
    ],
    image_path="/",
    status="SUPERUSER",
    options={},
    internal_options={},
    secrets={},
    email_settings=[
        {
            "category": "ADMINISTRATIVE",
            "subscribed": True,
        }
    ],
    include_inactive=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

App user id

##### app_id: `str`<a id="app_id-str"></a>

if the user is an app user, the id of the app

##### name: [`Name`](./chart_hop_python_sdk/type/name.py)<a id="name-namechart_hop_python_sdktypenamepy"></a>


##### email: `str`<a id="email-str"></a>

email address of user

##### orgs: List[`OrgAccess`]<a id="orgs-listorgaccess"></a>

list of member orgs with permission levels

##### image_path: `str`<a id="image_path-str"></a>

path to full-sized profile image in storage

##### status: `str`<a id="status-str"></a>

current status of user

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

for apps, options (specific options are specific to the particular app); for users, user-set preferences

##### internal_options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="internal_options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

internal (ChartHop controlled) options

##### secrets: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="secrets-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

write-only secrets; the content of these secrets are not retrievable via the external-facing API

##### email_settings: List[`UserEmailSetting`]<a id="email_settings-listuseremailsetting"></a>

Email settings for the user

##### include_inactive: `bool`<a id="include_inactive-bool"></a>

If the installed appUser is inactive, load inactive instead

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateUser`](./chart_hop_python_sdk/type/update_user.py)
App user data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/{appUserId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app.validate_app_installation`<a id="charthopappvalidate_app_installation"></a>

Validate the installation of an app for a particular org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_app_installation_response = charthop.app.validate_app_installation(
    orgs=[
        {
            "org_id": "5887a7718f138b6a2a0041a7",
            "person_id": "5887a7718f138b6a2a0041a7",
            "access": "NONE",
            "role_id": "5887a7718f138b6a2a0041a7",
        }
    ],
    org_id="orgId_example",
    app_id="string_example",
    name={
        "first": "Jane",
        "middle": "Quidditch",
        "last": "Public",
        "pref": "JQ",
        "pref_last": "Smith",
    },
    email="bob@example.com",
    image_path="/",
    status="SUPERUSER",
    options={},
    internal_options={},
    secrets={},
    email_settings=[
        {
            "category": "ADMINISTRATIVE",
            "subscribed": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### orgs: List[`OrgAccess`]<a id="orgs-listorgaccess"></a>

list of member orgs with permission levels

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_id: `str`<a id="app_id-str"></a>

if the user is an app user, the id of the app

##### name: [`Name`](./chart_hop_python_sdk/type/name.py)<a id="name-namechart_hop_python_sdktypenamepy"></a>


##### email: `str`<a id="email-str"></a>

email address of user

##### image_path: `str`<a id="image_path-str"></a>

path to full-sized profile image in storage

##### status: `str`<a id="status-str"></a>

current status of user

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

for apps, options (specific options are specific to the particular app); for users, user-set preferences

##### internal_options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="internal_options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

internal (ChartHop controlled) options

##### secrets: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="secrets-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

write-only secrets; the content of these secrets are not retrievable via the external-facing API

##### email_settings: List[`UserEmailSetting`]<a id="email_settings-listuseremailsetting"></a>

Email settings for the user

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateUser`](./chart_hop_python_sdk/type/create_user.py)
App user data to create

#### 🔄 Return<a id="🔄-return"></a>

[`BundleInstallValidate`](./chart_hop_python_sdk/pydantic/bundle_install_validate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app/org/{orgId}/install/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app_config.create_new_config`<a id="charthopapp_configcreate_new_config"></a>

Create a new app config

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_config_response = charthop.app_config.create_new_config(
    app_id="588f7ee98f138b19220041a7",
    user_id="588f7ee98f138b19220041a7",
    org_id="588f7ee98f138b19220041a7",
    field_mappers=[
        {
            "charthop_fields": [
                "charthop_fields_example"
            ],
            "remote_fields": [
                "remote_fields_example"
            ],
            "type": "type_example",
        }
    ],
    custom_field_mappers=[
        {
            "charthop_fields": [
                "charthop_fields_example"
            ],
            "remote_fields": [
                "remote_fields_example"
            ],
            "type": "type_example",
        }
    ],
    custom_outbound_field_mappers=[
        {
            "description": "description_example",
            "namespace": "namespace_example",
            "value_mappers": [
                {
                    "charthop_side": {},
                    "external_side": "external_side_example",
                }
            ],
        }
    ],
    disabled_field_mappers=[
        "string_example"
    ],
    enabled_outbound_field_mappers=[
        "string_example"
    ],
    template_matchers=[
        {
            "key": "string_example",
        }
    ],
    options={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

app id

##### user_id: `str`<a id="user_id-str"></a>

user id, if this person corresponds with a user

##### org_id: `str`<a id="org_id-str"></a>

org id, if this app config corresponds with an org

##### field_mappers: List[`FieldMapper`]<a id="field_mappers-listfieldmapper"></a>

list of default field mappers

##### custom_field_mappers: List[`FieldMapper`]<a id="custom_field_mappers-listfieldmapper"></a>

list of custom field mappers by a user

##### custom_outbound_field_mappers: List[`OutboundFieldMapper`]<a id="custom_outbound_field_mappers-listoutboundfieldmapper"></a>

list of custom outbound field mappers

##### disabled_field_mappers: [`CreateAppConfigDisabledFieldMappers`](./chart_hop_python_sdk/type/create_app_config_disabled_field_mappers.py)<a id="disabled_field_mappers-createappconfigdisabledfieldmapperschart_hop_python_sdktypecreate_app_config_disabled_field_mapperspy"></a>

##### enabled_outbound_field_mappers: [`CreateAppConfigEnabledOutboundFieldMappers`](./chart_hop_python_sdk/type/create_app_config_enabled_outbound_field_mappers.py)<a id="enabled_outbound_field_mappers-createappconfigenabledoutboundfieldmapperschart_hop_python_sdktypecreate_app_config_enabled_outbound_field_mapperspy"></a>

##### template_matchers: [`CreateAppConfigTemplateMatchers`](./chart_hop_python_sdk/type/create_app_config_template_matchers.py)<a id="template_matchers-createappconfigtemplatematcherschart_hop_python_sdktypecreate_app_config_template_matcherspy"></a>

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

app specific options

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateAppConfig`](./chart_hop_python_sdk/type/create_app_config.py)
App config data to create

#### 🔄 Return<a id="🔄-return"></a>

[`AppConfig`](./chart_hop_python_sdk/pydantic/app_config.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app-config` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app_config.get_default_config_by_app`<a id="charthopapp_configget_default_config_by_app"></a>

Return default app configuration by app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_default_config_by_app_response = charthop.app_config.get_default_config_by_app(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

App id

#### 🔄 Return<a id="🔄-return"></a>

[`AppConfig`](./chart_hop_python_sdk/pydantic/app_config.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app-config/{appId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app_config.get_user_config_by_app_and_user`<a id="charthopapp_configget_user_config_by_app_and_user"></a>

Return user app configuration by app and user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_config_by_app_and_user_response = charthop.app_config.get_user_config_by_app_and_user(
    app_id="appId_example",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

App id

##### user_id: `str`<a id="user_id-str"></a>

User id

#### 🔄 Return<a id="🔄-return"></a>

[`AppConfig`](./chart_hop_python_sdk/pydantic/app_config.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app-config/{appId}/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.app_config.update_by_id`<a id="charthopapp_configupdate_by_id"></a>

Update an existing app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.app_config.update_by_id(
    app_id="appId_example",
    user_id="userId_example",
    field_mappers=[
        {
            "charthop_fields": [
                "charthop_fields_example"
            ],
            "remote_fields": [
                "remote_fields_example"
            ],
            "type": "type_example",
        }
    ],
    custom_field_mappers=[
        {
            "charthop_fields": [
                "charthop_fields_example"
            ],
            "remote_fields": [
                "remote_fields_example"
            ],
            "type": "type_example",
        }
    ],
    custom_outbound_field_mappers=[
        {
            "description": "description_example",
            "namespace": "namespace_example",
            "value_mappers": [
                {
                    "charthop_side": {},
                    "external_side": "external_side_example",
                }
            ],
        }
    ],
    disabled_field_mappers=[
        "string_example"
    ],
    enabled_outbound_field_mappers=[
        "string_example"
    ],
    template_matchers=[
        {
            "key": "string_example",
        }
    ],
    options={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

App id

##### user_id: `str`<a id="user_id-str"></a>

User id

##### field_mappers: List[`FieldMapper`]<a id="field_mappers-listfieldmapper"></a>

list of default field mappers

##### custom_field_mappers: List[`FieldMapper`]<a id="custom_field_mappers-listfieldmapper"></a>

list of custom field mappers by a user

##### custom_outbound_field_mappers: List[`OutboundFieldMapper`]<a id="custom_outbound_field_mappers-listoutboundfieldmapper"></a>

list of custom outbound field mappers

##### disabled_field_mappers: [`UpdateAppConfigDisabledFieldMappers`](./chart_hop_python_sdk/type/update_app_config_disabled_field_mappers.py)<a id="disabled_field_mappers-updateappconfigdisabledfieldmapperschart_hop_python_sdktypeupdate_app_config_disabled_field_mapperspy"></a>

##### enabled_outbound_field_mappers: [`UpdateAppConfigEnabledOutboundFieldMappers`](./chart_hop_python_sdk/type/update_app_config_enabled_outbound_field_mappers.py)<a id="enabled_outbound_field_mappers-updateappconfigenabledoutboundfieldmapperschart_hop_python_sdktypeupdate_app_config_enabled_outbound_field_mapperspy"></a>

##### template_matchers: [`UpdateAppConfigTemplateMatchers`](./chart_hop_python_sdk/type/update_app_config_template_matchers.py)<a id="template_matchers-updateappconfigtemplatematcherschart_hop_python_sdktypeupdate_app_config_template_matcherspy"></a>

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

app specific options

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateAppConfig`](./chart_hop_python_sdk/type/update_app_config.py)
App data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/app-config/{appId}/{userId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.create_chain`<a id="charthopapprovalcreate_chain"></a>

Create an approval chain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_chain_response = charthop.approval.create_chain(
    name="Comp Review 06/15/2022",
    is_preview=True,
    approval_notifier_user_ids=[
        "string_example"
    ],
    org_id="orgId_example",
    entity_id="588f7ee98f138b19220041a7",
    entity_type="SCENARIO",
    fallback_approver_job_id="588f7ee98f138b19220041a7",
    fallback_approver_job_error="string_example",
    create_default_stages=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

human-readable name of approval chain

##### is_preview: `bool`<a id="is_preview-bool"></a>

isPreview specifies that this is a preview for implementations that use it (e.g. Compensation Reviews)

##### approval_notifier_user_ids: [`CreateApprovalChainApprovalNotifierUserIds`](./chart_hop_python_sdk/type/create_approval_chain_approval_notifier_user_ids.py)<a id="approval_notifier_user_ids-createapprovalchainapprovalnotifieruseridschart_hop_python_sdktypecreate_approval_chain_approval_notifier_user_idspy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### entity_id: `str`<a id="entity_id-str"></a>

entity id

##### entity_type: `str`<a id="entity_type-str"></a>

entity type

##### fallback_approver_job_id: `str`<a id="fallback_approver_job_id-str"></a>

the jobId of the fallback approver

##### fallback_approver_job_error: `str`<a id="fallback_approver_job_error-str"></a>

most recent error for fallback approver

##### create_default_stages: `bool`<a id="create_default_stages-bool"></a>

Create default stages

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateApprovalChain`](./chart_hop_python_sdk/type/create_approval_chain.py)
ApprovalChain data to create

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalChain`](./chart_hop_python_sdk/pydantic/approval_chain.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.create_chain_stage`<a id="charthopapprovalcreate_chain_stage"></a>

Create an approval chain stage

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_chain_stage_response = charthop.approval.create_chain_stage(
    reject_behavior="BACK_TO_BEGINNING",
    status="CANCELED",
    approval_comment_required=True,
    rejection_comment_required=True,
    order=1,
    groups=[
        {
            "type": "REVIEWER",
            "approvers": [
                {
                    "job_id": "job_id_example",
                    "status": "PENDING",
                }
            ],
        }
    ],
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    inclusion_expression="string_example",
    inclusion_behavior="ONLY_INCLUDE_IF",
    expand_expression="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reject_behavior: `str`<a id="reject_behavior-str"></a>

determines which stage becomes active when a rejection event happens

##### status: `str`<a id="status-str"></a>

status of the stage

##### approval_comment_required: `bool`<a id="approval_comment_required-bool"></a>

requires a comment on an approval event

##### rejection_comment_required: `bool`<a id="rejection_comment_required-bool"></a>

requires a comment on an rejection event

##### order: `int`<a id="order-int"></a>

order of stage in approval chain

##### groups: List[`ApprovalGroup`]<a id="groups-listapprovalgroup"></a>

list of groups that are involved in this approval stage

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### inclusion_expression: `str`<a id="inclusion_expression-str"></a>

optional custom expression to determine stage inclusion behavior

##### inclusion_behavior: `str`<a id="inclusion_behavior-str"></a>

determines whether stage is conditional based on an expression

##### expand_expression: `str`<a id="expand_expression-str"></a>

optional custom expression to determine approval request tree

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateApprovalChainStage`](./chart_hop_python_sdk/type/create_approval_chain_stage.py)
Approval chain stage data to create

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalChainStage`](./chart_hop_python_sdk/pydantic/approval_chain_stage.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/stage` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.create_request`<a id="charthopapprovalcreate_request"></a>

Create an approval request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_request_response = charthop.approval.create_request(
    entity_id="string_example",
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    dry_run=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### entity_id: `str`<a id="entity_id-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### dry_run: `bool`<a id="dry_run-bool"></a>

Dry run without creating real request

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApprovalRequestCreateBody`](./chart_hop_python_sdk/type/approval_request_create_body.py)
Approval request data to create

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalRequest`](./chart_hop_python_sdk/pydantic/approval_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.delete_approval_chain_stage`<a id="charthopapprovaldelete_approval_chain_stage"></a>

Delete an approval chain stage

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.approval.delete_approval_chain_stage(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    approval_chain_stage_id="approvalChainStageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### approval_chain_stage_id: `str`<a id="approval_chain_stage_id-str"></a>

Approval chain stage id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/stage/{approvalChainStageId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.delete_chain_by_id`<a id="charthopapprovaldelete_chain_by_id"></a>

Delete a approval chain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.approval.delete_chain_by_id(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.delete_request_approval`<a id="charthopapprovaldelete_request_approval"></a>

Delete an approval request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.approval.delete_request_approval(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    approval_request_id="approvalRequestId_example",
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

Approval request id

##### message: `str`<a id="message-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApprovalRequestDeleteBody`](./chart_hop_python_sdk/type/approval_request_delete_body.py)
Body params for deletion

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.generate_default_chain_stages`<a id="charthopapprovalgenerate_default_chain_stages"></a>

Build a default approval chain based on entity type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_default_chain_stages_response = charthop.approval.generate_default_chain_stages(
    entity_type="COMP_REVIEW",
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### entity_type: `str`<a id="entity_type-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DefaultChainCreateBody`](./chart_hop_python_sdk/type/default_chain_create_body.py)
Approval request data to create

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalChainStage`](./chart_hop_python_sdk/pydantic/approval_chain_stage.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/create-default-chain` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.get_all_approval_requests_for_approval_chain`<a id="charthopapprovalget_all_approval_requests_for_approval_chain"></a>

Return all approval requests for an approval chain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_approval_requests_for_approval_chain_response = charthop.approval.get_all_approval_requests_for_approval_chain(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    limit=1,
    entity_type="COMP_REVIEW",
    entity_ids="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### entity_type: `str`<a id="entity_type-str"></a>

entity type to filter on

##### entity_ids: `str`<a id="entity_ids-str"></a>

entity ids to filter on

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsApprovalRequest`](./chart_hop_python_sdk/pydantic/results_approval_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.get_all_stages_for_chain`<a id="charthopapprovalget_all_stages_for_chain"></a>

Return all approval chain stages for an approval chain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_stages_for_chain_response = charthop.approval.get_all_stages_for_chain(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    approval_chain_stage_id="approvalChainStageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### approval_chain_stage_id: `str`<a id="approval_chain_stage_id-str"></a>

Approval chain stage id

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalChainStage`](./chart_hop_python_sdk/pydantic/approval_chain_stage.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/stage/{approvalChainStageId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.get_approval_chain_by_id`<a id="charthopapprovalget_approval_chain_by_id"></a>

Return a particular approval chain by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_approval_chain_by_id_response = charthop.approval.get_approval_chain_by_id(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalChain`](./chart_hop_python_sdk/pydantic/approval_chain.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.get_approval_chain_stages`<a id="charthopapprovalget_approval_chain_stages"></a>

Return all approval chain stages for an approval chain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_approval_chain_stages_response = charthop.approval.get_approval_chain_stages(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsApprovalChainStage`](./chart_hop_python_sdk/pydantic/results_approval_chain_stage.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/stage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.get_approval_chains`<a id="charthopapprovalget_approval_chains"></a>

Return approval chains

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_approval_chains_response = charthop.approval.get_approval_chains(
    org_id="orgId_example",
    entity_type="COMP_REVIEW",
    entity_id="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### entity_type: `str`<a id="entity_type-str"></a>

The type of entity

##### entity_id: `str`<a id="entity_id-str"></a>

the id of the entity

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsApprovalChain`](./chart_hop_python_sdk/pydantic/results_approval_chain.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.get_comp_review_responses_for_chain`<a id="charthopapprovalget_comp_review_responses_for_chain"></a>

Return all approval request comp review responses for an approval chain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comp_review_responses_for_chain_response = charthop.approval.get_comp_review_responses_for_chain(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    limit=1,
    entity_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### entity_ids: List[`str`]<a id="entity_ids-liststr"></a>

entity ids to filter on

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsApprovalRequestCompReviewResponse`](./chart_hop_python_sdk/pydantic/results_approval_request_comp_review_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request/entity/comp-review` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.get_scenario_responses`<a id="charthopapprovalget_scenario_responses"></a>

Return all approval request scenario responses for an approval chain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_scenario_responses_response = charthop.approval.get_scenario_responses(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    limit=1,
    entity_ids="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### entity_ids: `str`<a id="entity_ids-str"></a>

entity ids to filter on

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsApprovalRequestScenarioResponse`](./chart_hop_python_sdk/pydantic/results_approval_request_scenario_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request/entity/scenario` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.reassign_approver_at_stage`<a id="charthopapprovalreassign_approver_at_stage"></a>

Reassigning an approver at a stage

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.approval.reassign_approver_at_stage(
    stage_order=1,
    initial_job_id="string_example",
    reassign_job_id="string_example",
    message="string_example",
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    approval_request_id="approvalRequestId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### stage_order: `int`<a id="stage_order-int"></a>

##### initial_job_id: `str`<a id="initial_job_id-str"></a>

##### reassign_job_id: `str`<a id="reassign_job_id-str"></a>

##### message: `str`<a id="message-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

approval request id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReassignApproverPatchBody`](./chart_hop_python_sdk/type/reassign_approver_patch_body.py)
approval request data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}/reassign-approver` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.request_approval_request`<a id="charthopapprovalrequest_approval_request"></a>

Return an approval request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_approval_request_response = charthop.approval.request_approval_request(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    approval_request_id="approvalRequestId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

Approval request id

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalRequest`](./chart_hop_python_sdk/pydantic/approval_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.send_stage_reviewer_reminder`<a id="charthopapprovalsend_stage_reviewer_reminder"></a>

Send a reminder for a stage reviewer in an existing approval request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.approval.send_stage_reviewer_reminder(
    job_id="string_example",
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    approval_request_id="approvalRequestId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

approval request id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SendReminderBody`](./chart_hop_python_sdk/type/send_reminder_body.py)
reminder body

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}/send-reminder` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.update_chain`<a id="charthopapprovalupdate_chain"></a>

Update a approval chain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.approval.update_chain(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    name="Comp Review 06/15/2022",
    is_preview=True,
    fallback_approver_job_id="588f7ee98f138b19220041a7",
    fallback_approver_job_error="string_example",
    approval_notifier_user_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

approval chain id

##### name: `str`<a id="name-str"></a>

human-readable name of approval chain

##### is_preview: `bool`<a id="is_preview-bool"></a>

isPreview specifies that this is a preview for implementations that use it (e.g. Compensation Reviews)

##### fallback_approver_job_id: `str`<a id="fallback_approver_job_id-str"></a>

the jobId of the fallback approver

##### fallback_approver_job_error: `str`<a id="fallback_approver_job_error-str"></a>

most recent error for fallback approver

##### approval_notifier_user_ids: [`UpdateApprovalChainApprovalNotifierUserIds`](./chart_hop_python_sdk/type/update_approval_chain_approval_notifier_user_ids.py)<a id="approval_notifier_user_ids-updateapprovalchainapprovalnotifieruseridschart_hop_python_sdktypeupdate_approval_chain_approval_notifier_user_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateApprovalChain`](./chart_hop_python_sdk/type/update_approval_chain.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.update_existing_request`<a id="charthopapprovalupdate_existing_request"></a>

Update an existing approval request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.approval.update_existing_request(
    status="CANCELED",
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    approval_request_id="approvalRequestId_example",
    message="string_example",
    preview_job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

approval request id

##### message: `str`<a id="message-str"></a>

##### preview_job_id: `str`<a id="preview_job_id-str"></a>

preview-as job id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApprovalRequestPatchBody`](./chart_hop_python_sdk/type/approval_request_patch_body.py)
approval request data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/request/{approvalRequestId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval.update_stage_by_id`<a id="charthopapprovalupdate_stage_by_id"></a>

Update an existing approval chain stage

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.approval.update_stage_by_id(
    org_id="orgId_example",
    approval_chain_id="approvalChainId_example",
    approval_chain_stage_id="approvalChainStageId_example",
    inclusion_expression="string_example",
    inclusion_behavior="ONLY_INCLUDE_IF",
    expand_expression="string_example",
    reject_behavior="BACK_TO_BEGINNING",
    status="CANCELED",
    approval_comment_required=True,
    rejection_comment_required=True,
    order=1,
    groups=[
        {
            "type": "REVIEWER",
            "approvers": [
                {
                    "job_id": "job_id_example",
                    "status": "PENDING",
                }
            ],
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id

##### approval_chain_stage_id: `str`<a id="approval_chain_stage_id-str"></a>

approval chain stage id

##### inclusion_expression: `str`<a id="inclusion_expression-str"></a>

optional custom expression to determine stage inclusion behavior

##### inclusion_behavior: `str`<a id="inclusion_behavior-str"></a>

determines whether stage is conditional based on an expression

##### expand_expression: `str`<a id="expand_expression-str"></a>

optional custom expression to determine approval request tree

##### reject_behavior: `str`<a id="reject_behavior-str"></a>

determines which stage becomes active when a rejection event happens

##### status: `str`<a id="status-str"></a>

status of the stage

##### approval_comment_required: `bool`<a id="approval_comment_required-bool"></a>

requires a comment on an approval event

##### rejection_comment_required: `bool`<a id="rejection_comment_required-bool"></a>

requires a comment on an rejection event

##### order: `int`<a id="order-int"></a>

order of stage in approval chain

##### groups: List[`ApprovalGroup`]<a id="groups-listapprovalgroup"></a>

list of groups that are involved in this approval stage

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateApprovalChainStage`](./chart_hop_python_sdk/type/update_approval_chain_stage.py)
approval chain stage data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-chain/{approvalChainId}/stage/{approvalChainStageId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval_request.get_all_approval_request_scenario_responses`<a id="charthopapproval_requestget_all_approval_request_scenario_responses"></a>

Return all approval request scenario responses for an org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_approval_request_scenario_responses_response = charthop.approval_request.get_all_approval_request_scenario_responses(
    org_id="orgId_example",
    limit=1,
    entity_ids="string_example",
    include_deleted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### entity_ids: `str`<a id="entity_ids-str"></a>

entity ids to filter on

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

Include deleted approval requests

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsApprovalRequestScenarioResponse`](./chart_hop_python_sdk/pydantic/results_approval_request_scenario_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-request/entity/scenario` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval_request.get_approval_request_scenario_response_by_job_id`<a id="charthopapproval_requestget_approval_request_scenario_response_by_job_id"></a>

Return a particular approval request scenario response by jobId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_approval_request_scenario_response_by_job_id_response = charthop.approval_request.get_approval_request_scenario_response_by_job_id(
    org_id="orgId_example",
    job_id="jobId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_id: `str`<a id="job_id-str"></a>

Job id

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalRequestScenarioResponse`](./chart_hop_python_sdk/pydantic/approval_request_scenario_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-request/scenario-job/{jobId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.approval_request.get_scenario_response_by_id`<a id="charthopapproval_requestget_scenario_response_by_id"></a>

Return a particular approval request scenario response by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_scenario_response_by_id_response = charthop.approval_request.get_scenario_response_by_id(
    org_id="orgId_example",
    approval_request_id="approvalRequestId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

Approval request id

#### 🔄 Return<a id="🔄-return"></a>

[`ApprovalRequestScenarioResponse`](./chart_hop_python_sdk/pydantic/approval_request_scenario_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/approval-request/{approvalRequestId}/scenario-response` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.bulk_delete`<a id="charthopassessmentbulk_delete"></a>

Delete a set of assessments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_delete_response = charthop.assessment.bulk_delete(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`AssessmentBulkDeleteRequest`](./chart_hop_python_sdk/type/assessment_bulk_delete_request.py)<a id="requestbody-assessmentbulkdeleterequestchart_hop_python_sdktypeassessment_bulk_delete_requestpy"></a>

List of assessment ids to delete

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/bulk/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.bulk_duplicate_assessments`<a id="charthopassessmentbulk_duplicate_assessments"></a>

Duplicate a set of assessments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_duplicate_assessments_response = charthop.assessment.bulk_duplicate_assessments(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`AssessmentBulkDuplicateAssessmentsRequest`](./chart_hop_python_sdk/type/assessment_bulk_duplicate_assessments_request.py)<a id="requestbody-assessmentbulkduplicateassessmentsrequestchart_hop_python_sdktypeassessment_bulk_duplicate_assessments_requestpy"></a>

List of assessment ids to duplicate

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/bulk/duplicate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.complete_assessment`<a id="charthopassessmentcomplete_assessment"></a>

Complete a assessment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_assessment_response = charthop.assessment.complete_assessment(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

#### 🔄 Return<a id="🔄-return"></a>

[`Assessment`](./chart_hop_python_sdk/pydantic/assessment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/{assessmentId}/complete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.create_new_assessment`<a id="charthopassessmentcreate_new_assessment"></a>

Create a assessment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_assessment_response = charthop.assessment.create_new_assessment(
    label="Engineering Budget Q2 2019",
    type="REVIEW",
    org_id="orgId_example",
    slug="engineering-budget-q2-2019",
    fields={},
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    sensitive="GLOBAL",
    color="#bf3253",
    start_date="1970-01-01",
    end_date="1970-01-01",
    status="DRAFT",
    done_at="2017-01-24T13:57:52Z",
    task_count=12,
    task_done_count=3,
    people_included_count=12,
    query="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

human-readable label of assessment

##### type: `str`<a id="type-str"></a>

type of assessment

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### slug: `str`<a id="slug-str"></a>

unique slug of assessment

##### fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

assessment fields (description)

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who have been granted access to this assessment

##### sensitive: `str`<a id="sensitive-str"></a>

view sensitivity of this assessment

##### color: `str`<a id="color-str"></a>

color of assessment

##### start_date: `date`<a id="start_date-date"></a>

Date this assessment begins. In the context of REVIEW goals, the date the review cycle begins.

##### end_date: `date`<a id="end_date-date"></a>

Date this assessment ends, or is completed. In the context of REVIEW assessment, the date the review cycle ends.

##### status: `str`<a id="status-str"></a>

status of this assessment - DRAFT, ACTIVE, DONE

##### done_at: `str`<a id="done_at-str"></a>

timestamp when the status of this assessment was set to done

##### task_count: `int`<a id="task_count-int"></a>

number of tasks associated with this assessment

##### task_done_count: `int`<a id="task_done_count-int"></a>

number of tasks associated with this assessment that are done

##### people_included_count: `int`<a id="people_included_count-int"></a>

number of people included in this assessment

##### query: `str`<a id="query-str"></a>

Query for which people/jobs can be included in the review.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateAssessment`](./chart_hop_python_sdk/type/create_assessment.py)
Assessment data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Assessment`](./chart_hop_python_sdk/pydantic/assessment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.expire_form_tasks`<a id="charthopassessmentexpire_form_tasks"></a>

Expire all pending tasks for a form of an assessment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
expire_form_tasks_response = charthop.assessment.expire_form_tasks(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
    form_id="formId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

##### form_id: `str`<a id="form_id-str"></a>

Form id

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/{assessmentId}/form/{formId}/expire` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.get_all_paginated`<a id="charthopassessmentget_all_paginated"></a>

Return all assessments in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_paginated_response = charthop.assessment.get_all_paginated(
    org_id="orgId_example",
    type="REVIEW",
    _from="string_example",
    limit=1,
    ids="string_example",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Type of assessment to filter by

##### _from: `str`<a id="_from-str"></a>

Assessment id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### ids: `str`<a id="ids-str"></a>

List of ids to filter by

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsAssessment`](./chart_hop_python_sdk/pydantic/results_assessment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.get_by_id`<a id="charthopassessmentget_by_id"></a>

Return a particular assessment by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.assessment.get_by_id(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

#### 🔄 Return<a id="🔄-return"></a>

[`Assessment`](./chart_hop_python_sdk/pydantic/assessment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/{assessmentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.reactivate_assessment`<a id="charthopassessmentreactivate_assessment"></a>

Reactivate a assessment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reactivate_assessment_response = charthop.assessment.reactivate_assessment(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

#### 🔄 Return<a id="🔄-return"></a>

[`Assessment`](./chart_hop_python_sdk/pydantic/assessment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/{assessmentId}/reactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.remove_by_id`<a id="charthopassessmentremove_by_id"></a>

Delete a assessment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.assessment.remove_by_id(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/{assessmentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.update_assessment_types`<a id="charthopassessmentupdate_assessment_types"></a>

Update the types of a set of assessments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_assessment_types_response = charthop.assessment.update_assessment_types(
    ids=[
        "string_example"
    ],
    type="REVIEW",
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: [`BulkChangeAssessmentTypesBodyIds`](./chart_hop_python_sdk/type/bulk_change_assessment_types_body_ids.py)<a id="ids-bulkchangeassessmenttypesbodyidschart_hop_python_sdktypebulk_change_assessment_types_body_idspy"></a>

##### type: `str`<a id="type-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BulkChangeAssessmentTypesBody`](./chart_hop_python_sdk/type/bulk_change_assessment_types_body.py)
List of assessment ids to update and the new type

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/bulk/move` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.assessment.update_existing_assessment`<a id="charthopassessmentupdate_existing_assessment"></a>

Update an existing assessment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.assessment.update_existing_assessment(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
    label="Engineering Budget Q2 2019",
    slug="engineering-budget-q2-2019",
    type="REVIEW",
    fields={},
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    sensitive="GLOBAL",
    color="#bf3253",
    start_date="1970-01-01",
    end_date="1970-01-01",
    status="DRAFT",
    done_at="2017-01-24T13:57:52Z",
    task_count=12,
    task_done_count=3,
    people_included_count=12,
    query="string_example",
    silent=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

##### label: `str`<a id="label-str"></a>

human-readable label of assessment

##### slug: `str`<a id="slug-str"></a>

unique slug of assessment

##### type: `str`<a id="type-str"></a>

type of assessment

##### fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

assessment fields (description)

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who have been granted access to this assessment

##### sensitive: `str`<a id="sensitive-str"></a>

view sensitivity of this assessment

##### color: `str`<a id="color-str"></a>

color of assessment

##### start_date: `date`<a id="start_date-date"></a>

Date this assessment begins. In the context of REVIEW goals, the date the review cycle begins.

##### end_date: `date`<a id="end_date-date"></a>

Date this assessment ends, or is completed. In the context of REVIEW assessment, the date the review cycle ends.

##### status: `str`<a id="status-str"></a>

status of this assessment - DRAFT, ACTIVE, DONE

##### done_at: `str`<a id="done_at-str"></a>

timestamp when the status of this assessment was set to done

##### task_count: `int`<a id="task_count-int"></a>

number of tasks associated with this assessment

##### task_done_count: `int`<a id="task_done_count-int"></a>

number of tasks associated with this assessment that are done

##### people_included_count: `int`<a id="people_included_count-int"></a>

number of people included in this assessment

##### query: `str`<a id="query-str"></a>

Query for which people/jobs can be included in the review.

##### silent: `bool`<a id="silent-bool"></a>

Suppress notification emails

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateAssessment`](./chart_hop_python_sdk/type/update_assessment.py)
Assessment data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/assessment/{assessmentId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.band.create_comp_band`<a id="charthopbandcreate_comp_band"></a>

Create a comp band

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.band.create_comp_band(
    label="L15",
    color="#ffee4a",
    base_interval={
        "name": "name_example",
        "label": "label_example",
    },
    job_level="string_example",
    org_id="orgId_example",
    base_comp_max={
        "amount": 3.14,
        "currency": "currency_example",
    },
    base_comp_mid={
        "amount": 3.14,
        "currency": "currency_example",
    },
    base_comp_min={
        "amount": 3.14,
        "currency": "currency_example",
    },
    base_spread=3.14,
    base_target_pay={
        "amount": 3.14,
        "currency": "currency_example",
    },
    base_target_pay_percentile=3.14,
    equity_target_shares=3.14,
    equity_target_percent_of_base=3.14,
    equity_target_value=3.14,
    variable_value={
        "amount": 3.14,
        "currency": "currency_example",
    },
    variable_percent_of_base=3.14,
    job_tier_one_field="string_example",
    job_tier_two_field="string_example",
    job_tier_three_field="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

human-readable name of content

##### color: `str`<a id="color-str"></a>

hex color associated with the band level

##### base_interval: [`EnumValue`](./chart_hop_python_sdk/type/enum_value.py)<a id="base_interval-enumvaluechart_hop_python_sdktypeenum_valuepy"></a>


##### job_level: `str`<a id="job_level-str"></a>

job level associated with the comp band

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### base_comp_max: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="base_comp_max-moneychart_hop_python_sdktypemoneypy"></a>


##### base_comp_mid: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="base_comp_mid-moneychart_hop_python_sdktypemoneypy"></a>


##### base_comp_min: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="base_comp_min-moneychart_hop_python_sdktypemoneypy"></a>


##### base_spread: `Union[int, float]`<a id="base_spread-unionint-float"></a>

spread percent used to calculate base comp from the midpoint

##### base_target_pay: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="base_target_pay-moneychart_hop_python_sdktypemoneypy"></a>


##### base_target_pay_percentile: `Union[int, float]`<a id="base_target_pay_percentile-unionint-float"></a>

base target pay associated with open jobs at this band level, as a percentile

##### equity_target_shares: `Union[int, float]`<a id="equity_target_shares-unionint-float"></a>

target equity for the band, in shares

##### equity_target_percent_of_base: `Union[int, float]`<a id="equity_target_percent_of_base-unionint-float"></a>

target equity for the band, as a percentage of base

##### equity_target_value: `Union[int, float]`<a id="equity_target_value-unionint-float"></a>

target equity for the band, as a monetary value, in the same currency as the base

##### variable_value: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="variable_value-moneychart_hop_python_sdktypemoneypy"></a>


##### variable_percent_of_base: `Union[int, float]`<a id="variable_percent_of_base-unionint-float"></a>

variable compensation for the band, specified as a percentage of base

##### job_tier_one_field: `str`<a id="job_tier_one_field-str"></a>

first job tier associated with the comp band

##### job_tier_two_field: `str`<a id="job_tier_two_field-str"></a>

second job tier associated with the comp band

##### job_tier_three_field: `str`<a id="job_tier_three_field-str"></a>

third job tier associated with the comp band

##### date: `date`<a id="date-date"></a>

Effective date of band creation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCompBand`](./chart_hop_python_sdk/type/create_comp_band.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/band` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.band.delete_comp_bands_on_date`<a id="charthopbanddelete_comp_bands_on_date"></a>

Delete all comp bands on a date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_comp_bands_on_date_response = charthop.band.delete_comp_bands_on_date(
    org_id="orgId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Effective date of group update

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/band` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.band.delete_comp_bands_on_date_0`<a id="charthopbanddelete_comp_bands_on_date_0"></a>

Delete all comp band data on a date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_comp_bands_on_date_0_response = charthop.band.delete_comp_bands_on_date_0(
    org_id="orgId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Effective date of group update

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/band/reset` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.band.find_comp_bands_in_org`<a id="charthopbandfind_comp_bands_in_org"></a>

Return a particular comp band by id on an effective date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_comp_bands_in_org_response = charthop.band.find_comp_bands_in_org(
    org_id="orgId_example",
    band_id="bandId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### band_id: `str`<a id="band_id-str"></a>

Comp band id

##### date: `date`<a id="date-date"></a>

Date to search as of

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/band/{bandId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.band.find_comp_bands_in_org_0`<a id="charthopbandfind_comp_bands_in_org_0"></a>

Find comp bands in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_comp_bands_in_org_0_response = charthop.band.find_comp_bands_in_org_0(
    org_id="orgId_example",
    date="1970-01-01",
    _from="string_example",
    limit=1,
    include_deleted=True,
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to search as of

##### _from: `str`<a id="_from-str"></a>

Table id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

Include deleted bands

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/band` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.band.remove_comp_band`<a id="charthopbandremove_comp_band"></a>

Delete a comp band

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.band.remove_comp_band(
    org_id="orgId_example",
    band_id="bandId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### band_id: `str`<a id="band_id-str"></a>

Comp band id

##### date: `date`<a id="date-date"></a>

Effective date of group update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/band/{bandId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.band.update_comp_band_by_id`<a id="charthopbandupdate_comp_band_by_id"></a>

Update a comp band

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.band.update_comp_band_by_id(
    org_id="orgId_example",
    band_id="bandId_example",
    label="L15",
    color="#ffee4a",
    base_comp_max={
        "amount": 3.14,
        "currency": "currency_example",
    },
    base_comp_mid={
        "amount": 3.14,
        "currency": "currency_example",
    },
    base_comp_min={
        "amount": 3.14,
        "currency": "currency_example",
    },
    base_spread=3.14,
    base_interval={
        "name": "name_example",
        "label": "label_example",
    },
    base_target_pay={
        "amount": 3.14,
        "currency": "currency_example",
    },
    base_target_pay_percentile=3.14,
    equity_target_shares=3.14,
    equity_target_percent_of_base=3.14,
    equity_target_value=3.14,
    variable_value={
        "amount": 3.14,
        "currency": "currency_example",
    },
    variable_percent_of_base=3.14,
    job_tier_one_field={
        "value": "value_example",
    },
    job_tier_two_field={
        "value": "value_example",
    },
    job_tier_three_field={
        "value": "value_example",
    },
    job_level="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### band_id: `str`<a id="band_id-str"></a>

Band id

##### label: `str`<a id="label-str"></a>

human-readable name of content

##### color: `str`<a id="color-str"></a>

hex color associated with the band level

##### base_comp_max: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="base_comp_max-moneychart_hop_python_sdktypemoneypy"></a>


##### base_comp_mid: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="base_comp_mid-moneychart_hop_python_sdktypemoneypy"></a>


##### base_comp_min: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="base_comp_min-moneychart_hop_python_sdktypemoneypy"></a>


##### base_spread: `Union[int, float]`<a id="base_spread-unionint-float"></a>

spread percent used to calculate base comp from the midpoint

##### base_interval: [`EnumValue`](./chart_hop_python_sdk/type/enum_value.py)<a id="base_interval-enumvaluechart_hop_python_sdktypeenum_valuepy"></a>


##### base_target_pay: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="base_target_pay-moneychart_hop_python_sdktypemoneypy"></a>


##### base_target_pay_percentile: `Union[int, float]`<a id="base_target_pay_percentile-unionint-float"></a>

base target pay associated with open jobs at this band level, as a percentile

##### equity_target_shares: `Union[int, float]`<a id="equity_target_shares-unionint-float"></a>

target equity for the band, in shares

##### equity_target_percent_of_base: `Union[int, float]`<a id="equity_target_percent_of_base-unionint-float"></a>

target equity for the band, as a percentage of base

##### equity_target_value: `Union[int, float]`<a id="equity_target_value-unionint-float"></a>

target equity for the band, as a monetary value, in the same currency as the base

##### variable_value: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="variable_value-moneychart_hop_python_sdktypemoneypy"></a>


##### variable_percent_of_base: `Union[int, float]`<a id="variable_percent_of_base-unionint-float"></a>

variable compensation for the band, specified as a percentage of base

##### job_tier_one_field: [`JobTierField`](./chart_hop_python_sdk/type/job_tier_field.py)<a id="job_tier_one_field-jobtierfieldchart_hop_python_sdktypejob_tier_fieldpy"></a>


##### job_tier_two_field: [`JobTierField`](./chart_hop_python_sdk/type/job_tier_field.py)<a id="job_tier_two_field-jobtierfieldchart_hop_python_sdktypejob_tier_fieldpy"></a>


##### job_tier_three_field: [`JobTierField`](./chart_hop_python_sdk/type/job_tier_field.py)<a id="job_tier_three_field-jobtierfieldchart_hop_python_sdktypejob_tier_fieldpy"></a>


##### job_level: `str`<a id="job_level-str"></a>

job level associated with the comp band

##### date: `date`<a id="date-date"></a>

Effective date of band update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCompBand`](./chart_hop_python_sdk/type/update_comp_band.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/band/{bandId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.billing.cancel_subscription_for_customer`<a id="charthopbillingcancel_subscription_for_customer"></a>

Cancel a subscription for a customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.billing.cancel_subscription_for_customer(
    other_comments="string_example",
    reason="string_example",
    customer_id="customerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### other_comments: `str`<a id="other_comments-str"></a>

Any additional comments about ChartHop when cancelling their subscription

##### reason: `str`<a id="reason-str"></a>

Concatenated string of reasons why the customer unsubscribed from ChartHop

##### customer_id: `str`<a id="customer_id-str"></a>

Customer id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CancelSubscriptionSurveyAnswers`](./chart_hop_python_sdk/type/cancel_subscription_survey_answers.py)
Survey response

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer/{customerId}/billing/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.billing.customer_billing_info`<a id="charthopbillingcustomer_billing_info"></a>

Return billing information for a customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
customer_billing_info_response = charthop.billing.customer_billing_info(
    customer_id="customerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

Customer id

#### 🔄 Return<a id="🔄-return"></a>

[`Billing`](./chart_hop_python_sdk/pydantic/billing.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer/{customerId}/billing` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.billing.upgrade_subscription`<a id="charthopbillingupgrade_subscription"></a>

Checks out customer to upgrade to pay for their subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.billing.upgrade_subscription(
    payment_method="string_example",
    customer_id="customerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_method: `str`<a id="payment_method-str"></a>

Payment method to create; 'INVOICE' to make subscription paid by invoice, or the ID of the payment method if to make the subscription automatically charge a card

##### customer_id: `str`<a id="customer_id-str"></a>

Customer id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateSubscription`](./chart_hop_python_sdk/type/update_subscription.py)
Subscription data to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer/{customerId}/billing/checkout` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.budget_pool.calculate_guideline`<a id="charthopbudget_poolcalculate_guideline"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.budget_pool.calculate_guideline(
    org_id="orgId_example",
    id="id_example",
    scenario_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug

##### id: `str`<a id="id-str"></a>

ID of the desired budget pool

##### scenario_id: `str`<a id="scenario_id-str"></a>

ID of the scenario the budget will be calculated against

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/budget-pool/{id}/calculate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.budget_pool.calculate_guideline_0`<a id="charthopbudget_poolcalculate_guideline_0"></a>

Generate tiering & preview with the given budget calculated for the compensation review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calculate_guideline_0_response = charthop.budget_pool.calculate_guideline_0(
    org_id="orgId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug

##### id: `str`<a id="id-str"></a>

ID of the desired budget pool

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetTiersResponse`](./chart_hop_python_sdk/pydantic/budget_tiers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/budget-pool/{id}/preview` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.budget_pool.create_new_pool`<a id="charthopbudget_poolcreate_new_pool"></a>

Create a new budget pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.budget_pool.create_new_pool(
    comp_review_id="588f7ee98f138b19220041a7",
    label="Merit",
    applied_field="base",
    source_field="base",
    basis_type="CUSTOM",
    org_id="orgId_example",
    participants_expr="string_example",
    fixed_amount={
        "amount": 3.14,
        "currency": "currency_example",
    },
    fixed_value=3.14,
    basis_field_matrix={
        "included_fields": [
            "included_fields_example"
        ],
        "conditions": [
            {
                "condition_expr": "condition_expr_example",
            }
        ],
    },
    fixed_budget_map={
        "key": {
            "amount": 3.14,
            "currency": "currency_example",
        },
    },
    basis_expr="string_example",
    default_currency="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

the ID of the comp review this budget is for

##### label: `str`<a id="label-str"></a>

unique label

##### applied_field: `str`<a id="applied_field-str"></a>

the field this budget pool applies to

##### source_field: `str`<a id="source_field-str"></a>

the field this budget pool is calculated from

##### basis_type: `str`<a id="basis_type-str"></a>

the method for calculating the amount in the budget

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug

##### participants_expr: `str`<a id="participants_expr-str"></a>

expression that determines if a particular job is included in this budget pool

##### fixed_amount: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="fixed_amount-moneychart_hop_python_sdktypemoneypy"></a>


##### fixed_value: `Union[int, float]`<a id="fixed_value-unionint-float"></a>

a fixed amount for the budget (used with basisType=FIXED || basisType=PERCENTAGE)

##### basis_field_matrix: [`BasisFieldMatrix`](./chart_hop_python_sdk/type/basis_field_matrix.py)<a id="basis_field_matrix-basisfieldmatrixchart_hop_python_sdktypebasis_field_matrixpy"></a>


##### fixed_budget_map: [`CreateBudgetPoolFixedBudgetMap`](./chart_hop_python_sdk/type/create_budget_pool_fixed_budget_map.py)<a id="fixed_budget_map-createbudgetpoolfixedbudgetmapchart_hop_python_sdktypecreate_budget_pool_fixed_budget_mappy"></a>

##### basis_expr: `str`<a id="basis_expr-str"></a>

expression that calculates how much each job contributes to the budget (used with basisType=CUSTOM)

##### default_currency: `str`<a id="default_currency-str"></a>

Default currency used when calculating budget pool, falls back to org primary currency if not set

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateBudgetPool`](./chart_hop_python_sdk/type/create_budget_pool.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/budget-pool` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.budget_pool.delete_budget_pool_by_id`<a id="charthopbudget_pooldelete_budget_pool_by_id"></a>

Delete a budget pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.budget_pool.delete_budget_pool_by_id(
    org_id="orgId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug

##### id: `str`<a id="id-str"></a>

ID of the desired budget pool

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/budget-pool/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.budget_pool.get_all_for_org`<a id="charthopbudget_poolget_all_for_org"></a>

Get all budget pools for an org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_org_response = charthop.budget_pool.get_all_for_org(
    org_id="orgId_example",
    comp_review_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp Review Id to filter on

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/budget-pool` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.budget_pool.get_guidelines_for_budget_pool`<a id="charthopbudget_poolget_guidelines_for_budget_pool"></a>

Get the guidelines associated with a budget pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_guidelines_for_budget_pool_response = charthop.budget_pool.get_guidelines_for_budget_pool(
    org_id="orgId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### id: `str`<a id="id-str"></a>

ID of the desired budget pool

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsGuideline`](./chart_hop_python_sdk/pydantic/results_guideline.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/budget-pool/{id}/guidelines` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.budget_pool.get_specific_pool`<a id="charthopbudget_poolget_specific_pool"></a>

Get a specific budget pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_pool_response = charthop.budget_pool.get_specific_pool(
    org_id="orgId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### id: `str`<a id="id-str"></a>

ID of the desired budget pool

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetPool`](./chart_hop_python_sdk/pydantic/budget_pool.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/budget-pool/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.budget_pool.update_budget_pool`<a id="charthopbudget_poolupdate_budget_pool"></a>

Update a budget pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.budget_pool.update_budget_pool(
    org_id="orgId_example",
    id="id_example",
    label="Merit",
    participants_expr="string_example",
    applied_field="base",
    source_field="base",
    basis_type="CUSTOM",
    fixed_amount={
        "amount": 3.14,
        "currency": "currency_example",
    },
    fixed_value=3.14,
    basis_field_matrix={
        "included_fields": [
            "included_fields_example"
        ],
        "conditions": [
            {
                "condition_expr": "condition_expr_example",
            }
        ],
    },
    fixed_budget_map={
        "key": {
            "amount": 3.14,
            "currency": "currency_example",
        },
    },
    basis_expr="string_example",
    default_currency="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug

##### id: `str`<a id="id-str"></a>

ID of the desired budget pool

##### label: `str`<a id="label-str"></a>

unique label

##### participants_expr: `str`<a id="participants_expr-str"></a>

expression that determines if a particular job is included in this budget pool

##### applied_field: `str`<a id="applied_field-str"></a>

the field this budget pool applies to

##### source_field: `str`<a id="source_field-str"></a>

the field this budget pool is calculated from

##### basis_type: `str`<a id="basis_type-str"></a>

the method for calculating the amount in the budget

##### fixed_amount: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="fixed_amount-moneychart_hop_python_sdktypemoneypy"></a>


##### fixed_value: `Union[int, float]`<a id="fixed_value-unionint-float"></a>

a fixed amount for the budget (used with basisType=FIXED || basisType=PERCENTAGE)

##### basis_field_matrix: [`BasisFieldMatrix`](./chart_hop_python_sdk/type/basis_field_matrix.py)<a id="basis_field_matrix-basisfieldmatrixchart_hop_python_sdktypebasis_field_matrixpy"></a>


##### fixed_budget_map: [`UpdateBudgetPoolFixedBudgetMap`](./chart_hop_python_sdk/type/update_budget_pool_fixed_budget_map.py)<a id="fixed_budget_map-updatebudgetpoolfixedbudgetmapchart_hop_python_sdktypeupdate_budget_pool_fixed_budget_mappy"></a>

##### basis_expr: `str`<a id="basis_expr-str"></a>

expression that calculates how much each job contributes to the budget (used with basisType=CUSTOM)

##### default_currency: `str`<a id="default_currency-str"></a>

Default currency used when calculating budget pool, falls back to org primary currency if not set

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateBudgetPool`](./chart_hop_python_sdk/type/update_budget_pool.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/budget-pool/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.calendar.get_entries_by_time_period`<a id="charthopcalendarget_entries_by_time_period"></a>

Return calendar entries in a given time period

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.calendar.get_entries_by_time_period(
    org_id="orgId_example",
    start="string_example",
    end="string_example",
    type="string_example",
    q="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### start: `str`<a id="start-str"></a>

Start date

##### end: `str`<a id="end-str"></a>

End date

##### type: `str`<a id="type-str"></a>

Type of calendar entries to retrieve (timeoff, anniversary, birthday)

##### q: `str`<a id="q-str"></a>

Query filter to filter for part of the organization

##### format: `str`<a id="format-str"></a>

Format to return data in

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/calendar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category.create_new_category`<a id="charthopcategorycreate_new_category"></a>

Create a category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_category_response = charthop.category.create_new_category(
    label="Performance",
    org_id="orgId_example",
    org_id="588f7ee98f138b19220041a7",
    field_ids=[
        "string_example"
    ],
    native_fields=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CreateCategory`](./chart_hop_python_sdk/type/create_category.py)<a id="requestbody-createcategorychart_hop_python_sdktypecreate_categorypy"></a>

Category data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Category`](./chart_hop_python_sdk/pydantic/category.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category.get_available`<a id="charthopcategoryget_available"></a>

Return categories that are available to the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_response = charthop.category.get_available(
    org_id="orgId_example",
    type="string_example",
    unsorted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

(Optional) Return only built-in or custom categories

##### unsorted: `bool`<a id="unsorted-bool"></a>

(Optional) Return categories array unsorted

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsCategory`](./chart_hop_python_sdk/pydantic/results_category.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category.get_by_id`<a id="charthopcategoryget_by_id"></a>

Return a particular category by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.category.get_by_id(
    org_id="orgId_example",
    category_id="categoryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### category_id: `str`<a id="category_id-str"></a>

Category id

#### 🔄 Return<a id="🔄-return"></a>

[`Category`](./chart_hop_python_sdk/pydantic/category.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category/{categoryId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category.remove_by_id`<a id="charthopcategoryremove_by_id"></a>

Delete a category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.category.remove_by_id(
    org_id="orgId_example",
    category_id="categoryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### category_id: `str`<a id="category_id-str"></a>

Category id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category/{categoryId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category.update_existing_category`<a id="charthopcategoryupdate_existing_category"></a>

Update an existing category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.category.update_existing_category(
    org_id="orgId_example",
    category_id="categoryId_example",
    label="Performance",
    field_ids=[
        "string_example"
    ],
    native_fields=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### category_id: `str`<a id="category_id-str"></a>

Category id

##### label: `str`<a id="label-str"></a>

human-readable label of category

##### field_ids: [`UpdateCategoryFieldIds`](./chart_hop_python_sdk/type/update_category_field_ids.py)<a id="field_ids-updatecategoryfieldidschart_hop_python_sdktypeupdate_category_field_idspy"></a>

##### native_fields: [`UpdateCategoryNativeFields`](./chart_hop_python_sdk/type/update_category_native_fields.py)<a id="native_fields-updatecategorynativefieldschart_hop_python_sdktypeupdate_category_native_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCategory`](./chart_hop_python_sdk/type/update_category.py)
Category data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category/{categoryId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category_sort.create_if_not_exists`<a id="charthopcategory_sortcreate_if_not_exists"></a>

Create a category sort order if it doesn't exist

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_if_not_exists_response = charthop.category_sort.create_if_not_exists(
    org_id="588f7ee98f138b19220041a7",
    category_ids=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CreateCategorySort`](./chart_hop_python_sdk/type/create_category_sort.py)<a id="requestbody-createcategorysortchart_hop_python_sdktypecreate_category_sortpy"></a>

Sort data to create

#### 🔄 Return<a id="🔄-return"></a>

[`CategorySort`](./chart_hop_python_sdk/pydantic/category_sort.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category-sort` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category_sort.create_or_update_sort`<a id="charthopcategory_sortcreate_or_update_sort"></a>

Create or update category sort order for a given org and return the sort data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_or_update_sort_response = charthop.category_sort.create_or_update_sort(
    org_id="orgId_example",
    category_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### category_ids: [`UpdateCategorySortCategoryIds`](./chart_hop_python_sdk/type/update_category_sort_category_ids.py)<a id="category_ids-updatecategorysortcategoryidschart_hop_python_sdktypeupdate_category_sort_category_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCategorySort`](./chart_hop_python_sdk/type/update_category_sort.py)
Category Ids in sort order

#### 🔄 Return<a id="🔄-return"></a>

[`CategorySort`](./chart_hop_python_sdk/pydantic/category_sort.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category-sort` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category_sort.create_or_update_sort_order`<a id="charthopcategory_sortcreate_or_update_sort_order"></a>

Create or update category sort order for a given org and return the sort data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_or_update_sort_order_response = charthop.category_sort.create_or_update_sort_order(
    org_id="orgId_example",
    category_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### category_ids: [`UpdateCategorySortCategoryIds`](./chart_hop_python_sdk/type/update_category_sort_category_ids.py)<a id="category_ids-updatecategorysortcategoryidschart_hop_python_sdktypeupdate_category_sort_category_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCategorySort`](./chart_hop_python_sdk/type/update_category_sort.py)
Category Ids in sort order

#### 🔄 Return<a id="🔄-return"></a>

[`CategorySort`](./chart_hop_python_sdk/pydantic/category_sort.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category-sort/upsert` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category_sort.delete_sort_order`<a id="charthopcategory_sortdelete_sort_order"></a>

Delete a category sort order

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.category_sort.delete_sort_order(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category-sort` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category_sort.get_category_sort_order`<a id="charthopcategory_sortget_category_sort_order"></a>

Return category sort order

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_category_sort_order_response = charthop.category_sort.get_category_sort_order(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`CategorySort`](./chart_hop_python_sdk/pydantic/category_sort.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category-sort` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.category_sort.update_existing_category_sort`<a id="charthopcategory_sortupdate_existing_category_sort"></a>

Update an existing category sort order

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.category_sort.update_existing_category_sort(
    org_id="orgId_example",
    category_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### category_ids: [`UpdateCategorySortCategoryIds`](./chart_hop_python_sdk/type/update_category_sort_category_ids.py)<a id="category_ids-updatecategorysortcategoryidschart_hop_python_sdktypeupdate_category_sort_category_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCategorySort`](./chart_hop_python_sdk/type/update_category_sort.py)
Sort data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/category-sort` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.amend_scenario_change`<a id="charthopchangeamend_scenario_change"></a>

Amend a change within a scenario, and potentially return the updated data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
amend_scenario_change_response = charthop.change.amend_scenario_change(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    change_id="changeId_example",
    fields="string_example",
    include_updated_fields=True,
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### change_id: `str`<a id="change_id-str"></a>

Change id

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve

##### include_updated_fields: `bool`<a id="include_updated_fields-bool"></a>

Include all updated fields in the response, including change.after.fieldName for each updated field

##### format: `str`<a id="format-str"></a>

Data format to return; default is json, can also use json-extended or json-readable

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeAmendScenarioChangeRequest`](./chart_hop_python_sdk/type/change_amend_scenario_change_request.py)
Column and data to update (must contain only one entry)

#### 🔄 Return<a id="🔄-return"></a>

[`UpdateScenarioChangeResponse`](./chart_hop_python_sdk/pydantic/update_scenario_change_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}/change/{changeId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.approve_or_reject`<a id="charthopchangeapprove_or_reject"></a>

Approve or reject a change

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.change.approve_or_reject(
    status="ACTIVE",
    org_id="orgId_example",
    change_id="changeId_example",
    approval_note="string_example",
    change_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### change_id: `str`<a id="change_id-str"></a>

Change id

##### requestBody: [`ApproveChange`](./chart_hop_python_sdk/type/approve_change.py)<a id="requestbody-approvechangechart_hop_python_sdktypeapprove_changepy"></a>

Change approval details

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/{changeId}/approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.bulk_update_jobs`<a id="charthopchangebulk_update_jobs"></a>

Perform a bulk update on a number of jobs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_update_jobs_response = charthop.change.bulk_update_jobs(
    job_ids=[
        "string_example"
    ],
    update={
        "placement": "NORMAL",
        "employment": "FULL",
        "sensitive": "GLOBAL",
    },
    date="1970-01-01",
    org_id="orgId_example",
    scenario_id="string_example",
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_ids: [`BulkUpdateRequestJobIds`](./chart_hop_python_sdk/type/bulk_update_request_job_ids.py)<a id="job_ids-bulkupdaterequestjobidschart_hop_python_sdktypebulk_update_request_job_idspy"></a>

##### update: [`JobUpdate`](./chart_hop_python_sdk/type/job_update.py)<a id="update-jobupdatechart_hop_python_sdktypejob_updatepy"></a>


##### date: `date`<a id="date-date"></a>

date of update

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

scenario id

##### note: `str`<a id="note-str"></a>

note for update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BulkUpdateRequest`](./chart_hop_python_sdk/type/bulk_update_request.py)
Bulk update data

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/bulkupdate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.check_approver_eligibility`<a id="charthopchangecheck_approver_eligibility"></a>

Given a of change id, see if the person can approve/reject

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_approver_eligibility_response = charthop.change.check_approver_eligibility(
    org_id="orgId_example",
    change_id="changeId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### change_id: `str`<a id="change_id-str"></a>

Change Id

##### date: `date`<a id="date-date"></a>

Date to check the approval on

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/{changeId}/approver` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.create_depart_rehire_pair`<a id="charthopchangecreate_depart_rehire_pair"></a>

Create a depart-rehire pair of changes, for filling in historical data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_depart_rehire_pair_response = charthop.change.create_depart_rehire_pair(
    org_id="orgId_example",
    job_id="588f7ee98f138b19220041a7",
    org_id="588f7ee98f138b19220041a7",
    scenario_id="588f7ee98f138b19220041a7",
    person_id="string_example",
    other_job_id="588f7ee98f138b19220041a7",
    type="HIRE",
    date="1970-01-01",
    announce_date="1970-01-01",
    depart_type="VOLUNTARY",
    depart_regret="REGRET",
    reason="string_example",
    promotion_type="PROMOTION",
    job={
        "title": "Senior Engineer",
        "job_id": "588f7ee98f138b19220041a7",
        "org_id": "588f7ee98f138b19220041a7",
        "snapshot_id": "588f7ee98f138b19220041a7",
        "sensitive": "GLOBAL",
        "placement": "NORMAL",
        "employment": "FULL",
        "state": "OPEN",
        "person_id": "588f7ee98f138b19220041a7",
        "backfill_person_id": "588f7ee98f138b19220041a7",
        "backfill_by_job_id": "588f7ee98f138b19220041a7",
    },
    update={
        "placement": "NORMAL",
        "employment": "FULL",
        "sensitive": "GLOBAL",
    },
    note="string_example",
    start_date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### start_date: `date`<a id="start_date-date"></a>

Rehire start date

##### requestBody: [`CreateChange`](./chart_hop_python_sdk/type/create_change.py)<a id="requestbody-createchangechart_hop_python_sdktypecreate_changepy"></a>

Depart data

#### 🔄 Return<a id="🔄-return"></a>

[`Change`](./chart_hop_python_sdk/pydantic/change.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/depart-rehire` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.create_if_not_exists`<a id="charthopchangecreate_if_not_exists"></a>

Sync a change (create the change only if it does not already exist)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_if_not_exists_response = charthop.change.create_if_not_exists(
    org_id="orgId_example",
    type="type_example",
    job_id="588f7ee98f138b19220041a7",
    org_id="588f7ee98f138b19220041a7",
    scenario_id="588f7ee98f138b19220041a7",
    person_id="string_example",
    other_job_id="588f7ee98f138b19220041a7",
    type="HIRE",
    date="1970-01-01",
    announce_date="1970-01-01",
    depart_type="VOLUNTARY",
    depart_regret="REGRET",
    reason="string_example",
    promotion_type="PROMOTION",
    job={
        "title": "Senior Engineer",
        "job_id": "588f7ee98f138b19220041a7",
        "org_id": "588f7ee98f138b19220041a7",
        "snapshot_id": "588f7ee98f138b19220041a7",
        "sensitive": "GLOBAL",
        "placement": "NORMAL",
        "employment": "FULL",
        "state": "OPEN",
        "person_id": "588f7ee98f138b19220041a7",
        "backfill_person_id": "588f7ee98f138b19220041a7",
        "backfill_by_job_id": "588f7ee98f138b19220041a7",
    },
    update={
        "placement": "NORMAL",
        "employment": "FULL",
        "sensitive": "GLOBAL",
    },
    note="string_example",
    process_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Change type

##### process_id: `str`<a id="process_id-str"></a>

Process id of person creation

##### requestBody: [`CreateChange`](./chart_hop_python_sdk/type/create_change.py)<a id="requestbody-createchangechart_hop_python_sdktypecreate_changepy"></a>

Change data

#### 🔄 Return<a id="🔄-return"></a>

[`Change`](./chart_hop_python_sdk/pydantic/change.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/sync/{type}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.create_new_change`<a id="charthopchangecreate_new_change"></a>

Create a new change

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_change_response = charthop.change.create_new_change(
    org_id="orgId_example",
    type="type_example",
    job_id="588f7ee98f138b19220041a7",
    org_id="588f7ee98f138b19220041a7",
    scenario_id="588f7ee98f138b19220041a7",
    person_id="string_example",
    other_job_id="588f7ee98f138b19220041a7",
    type="HIRE",
    date="1970-01-01",
    announce_date="1970-01-01",
    depart_type="VOLUNTARY",
    depart_regret="REGRET",
    reason="string_example",
    promotion_type="PROMOTION",
    job={
        "title": "Senior Engineer",
        "job_id": "588f7ee98f138b19220041a7",
        "org_id": "588f7ee98f138b19220041a7",
        "snapshot_id": "588f7ee98f138b19220041a7",
        "sensitive": "GLOBAL",
        "placement": "NORMAL",
        "employment": "FULL",
        "state": "OPEN",
        "person_id": "588f7ee98f138b19220041a7",
        "backfill_person_id": "588f7ee98f138b19220041a7",
        "backfill_by_job_id": "588f7ee98f138b19220041a7",
    },
    update={
        "placement": "NORMAL",
        "employment": "FULL",
        "sensitive": "GLOBAL",
    },
    note="string_example",
    source="string_example",
    process_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Change type

##### source: `str`<a id="source-str"></a>

Source of change

##### process_id: `str`<a id="process_id-str"></a>

Process id of change creation

##### requestBody: [`CreateChange`](./chart_hop_python_sdk/type/create_change.py)<a id="requestbody-createchangechart_hop_python_sdktypecreate_changepy"></a>

Change data

#### 🔄 Return<a id="🔄-return"></a>

[`Change`](./chart_hop_python_sdk/pydantic/change.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/{type}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.delete_previous_change`<a id="charthopchangedelete_previous_change"></a>

Delete a previous change

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.change.delete_previous_change(
    org_id="orgId_example",
    change_id="changeId_example",
    process_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### change_id: `str`<a id="change_id-str"></a>

Change id

##### process_id: `str`<a id="process_id-str"></a>

Process id of person creation

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/{changeId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.find_scenario_changes`<a id="charthopchangefind_scenario_changes"></a>

Return all changes for a particular scenario, with before job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_scenario_changes_response = charthop.change.find_scenario_changes(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    fields="string_example",
    format="string_example",
    q="string_example",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### q: `str`<a id="q-str"></a>

Search query

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ScenarioChangesWithBudgetRollup`](./chart_hop_python_sdk/pydantic/scenario_changes_with_budget_rollup.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/scenario/{scenarioId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.get_by_id`<a id="charthopchangeget_by_id"></a>

Return a particular change by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.change.get_by_id(
    org_id="orgId_example",
    change_id="changeId_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### change_id: `str`<a id="change_id-str"></a>

Change id

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`Change`](./chart_hop_python_sdk/pydantic/change.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/{changeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.get_by_id_0`<a id="charthopchangeget_by_id_0"></a>

Return a particular change by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.change.get_by_id_0(
    org_id="orgId_example",
    change_id="changeId_example",
    fields="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### change_id: `str`<a id="change_id-str"></a>

Change id

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/change/{changeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.get_recent_changes`<a id="charthopchangeget_recent_changes"></a>

Return recent changes across an org, or for a particular person or job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_changes_response = charthop.change.get_recent_changes(
    org_id="orgId_example",
    scenario_id="string_example",
    date="1970-01-01",
    end_date="1970-01-01",
    type="string_example",
    fields="string_example",
    person_id="string_example",
    job_id="string_example",
    include_backfill=True,
    refs="string_example",
    q="string_example",
    _from="string_example",
    limit=1,
    open="FILLED",
    desc=True,
    scenario_only=True,
    parent_only=True,
    include_grant_schedule=True,
    exclude_ats_recruiting_fields=True,
    include_struck=True,
    status="string_example",
    strip_updates=True,
    format="string_example",
    field_entity_types="string_example",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### date: `date`<a id="date-date"></a>

Date to start from

##### end_date: `date`<a id="end_date-date"></a>

Date to get changes through (inclusive)

##### type: `str`<a id="type-str"></a>

Types of change to filter by

##### fields: `str`<a id="fields-str"></a>

Return changes that modify these fields

##### person_id: `str`<a id="person_id-str"></a>

Person id to filter by

##### job_id: `str`<a id="job_id-str"></a>

Job id to filter by

##### include_backfill: `bool`<a id="include_backfill-bool"></a>

Find and include first backfill if it exists

##### refs: `str`<a id="refs-str"></a>

References to filter by

##### q: `str`<a id="q-str"></a>

Query to filter against

##### _from: `str`<a id="_from-str"></a>

Change id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### open: `str`<a id="open-str"></a>

Whether the role is open or not

##### desc: `bool`<a id="desc-bool"></a>

Descending (default false)

##### scenario_only: `bool`<a id="scenario_only-bool"></a>

Scenario only (exclude primary changes)

##### parent_only: `bool`<a id="parent_only-bool"></a>

Parent changes only (exclude child changes)

##### include_grant_schedule: `bool`<a id="include_grant_schedule-bool"></a>

Whether to include full grant schedule when returning equity updates

##### exclude_ats_recruiting_fields: `bool`<a id="exclude_ats_recruiting_fields-bool"></a>

Whether to exclude ats recruiting fields. Only applies when fieldEntityTypeString is passed

##### include_struck: `bool`<a id="include_struck-bool"></a>

Deprecated parameter for backwards-compatibility (use statuses) - whether to include STRUCK and PROPOSED changes, or just ACTIVE changes

##### status: `str`<a id="status-str"></a>

Statuses to filter by

##### strip_updates: `bool`<a id="strip_updates-bool"></a>

Whether to strip returned update changes of update types that were not explicitly requested

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### field_entity_types: `str`<a id="field_entity_types-str"></a>

Only return changes which set fields with these entity types

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsChange`](./chart_hop_python_sdk/pydantic/results_change.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.get_recent_changes_for_org_or_person`<a id="charthopchangeget_recent_changes_for_org_or_person"></a>

Return recent changes across an org, or for a particular person or job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_changes_for_org_or_person_response = charthop.change.get_recent_changes_for_org_or_person(
    org_id="orgId_example",
    job_id="string_example",
    person_id="string_example",
    scenario_id="string_example",
    type="string_example",
    status="string_example",
    fields="string_example",
    fields_changed="string_example",
    q="string_example",
    open="FILLED",
    include_grant_schedule=True,
    from_date="1970-01-01",
    _from="string_example",
    limit=1,
    desc=True,
    format="string_example",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_id: `str`<a id="job_id-str"></a>

Job id to filter by

##### person_id: `str`<a id="person_id-str"></a>

Person id to filter by

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### type: `str`<a id="type-str"></a>

Types of change to filter by, comma-separated

##### status: `str`<a id="status-str"></a>

Statuses to filter by, comma-separated

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### fields_changed: `str`<a id="fields_changed-str"></a>

Changed fields to filter by, comma-separated

##### q: `str`<a id="q-str"></a>

Query to filter against

##### open: `str`<a id="open-str"></a>

Whether the role is open or not

##### include_grant_schedule: `bool`<a id="include_grant_schedule-bool"></a>

Whether to include full grant schedule when returning equity updates

##### from_date: `date`<a id="from_date-date"></a>

Date to start from

##### _from: `str`<a id="_from-str"></a>

Change id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### desc: `bool`<a id="desc-bool"></a>

Descending (default false)

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/change` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.get_status`<a id="charthopchangeget_status"></a>

Get the status of a running change within a scenario

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_response = charthop.change.get_status(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    change_id="changeId_example",
    process_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### change_id: `str`<a id="change_id-str"></a>

Change id

##### process_id: `int`<a id="process_id-int"></a>

Process id

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeStatusResponse`](./chart_hop_python_sdk/pydantic/change_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}/change/{changeId}/status/{processId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.perform_bulk_change`<a id="charthopchangeperform_bulk_change"></a>

Perform a series of changes at once

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_bulk_change_response = charthop.change.perform_bulk_change(
    changes=[
        {
            "job_id": "588f7ee98f138b19220041a7",
            "org_id": "588f7ee98f138b19220041a7",
            "scenario_id": "588f7ee98f138b19220041a7",
            "other_job_id": "588f7ee98f138b19220041a7",
            "type": "HIRE",
            "depart_type": "VOLUNTARY",
            "depart_regret": "REGRET",
            "promotion_type": "PROMOTION",
        }
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### changes: List[`CreateChange`]<a id="changes-listcreatechange"></a>

list of changes to create

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BulkChangeRequest`](./chart_hop_python_sdk/type/bulk_change_request.py)
Bulk change data

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/bulkchange` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.update_change_by_id`<a id="charthopchangeupdate_change_by_id"></a>

Make a change to a change

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.change.update_change_by_id(
    org_id="orgId_example",
    change_id="changeId_example",
    date="1970-01-01",
    announce_date="1970-01-01",
    status="ACTIVE",
    depart_type="VOLUNTARY",
    depart_regret="REGRET",
    reason="string_example",
    promotion_type="PROMOTION",
    job={
        "title": "Senior Engineer",
        "job_id": "588f7ee98f138b19220041a7",
        "org_id": "588f7ee98f138b19220041a7",
        "snapshot_id": "588f7ee98f138b19220041a7",
        "sensitive": "GLOBAL",
        "placement": "NORMAL",
        "employment": "FULL",
        "state": "OPEN",
        "person_id": "588f7ee98f138b19220041a7",
        "backfill_person_id": "588f7ee98f138b19220041a7",
        "backfill_by_job_id": "588f7ee98f138b19220041a7",
    },
    update={
        "placement": "NORMAL",
        "employment": "FULL",
        "sensitive": "GLOBAL",
    },
    note="string_example",
    approval_note="Not acceptable",
    process_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### change_id: `str`<a id="change_id-str"></a>

Change id

##### date: `date`<a id="date-date"></a>

date of change

##### announce_date: `date`<a id="announce_date-date"></a>

for HIRE and DEPART changes, the announce date, if the announce date is different from the date of change

##### status: `str`<a id="status-str"></a>

whether the change is active or not

##### depart_type: `str`<a id="depart_type-str"></a>

for DEPART changes, the type of departure

##### depart_regret: `str`<a id="depart_regret-str"></a>

for DEPART changes, whether the departure is regrettable

##### reason: `str`<a id="reason-str"></a>

the reason of the change

##### promotion_type: `str`<a id="promotion_type-str"></a>

if it's a promotion or a demotion

##### job: [`PartialJob`](./chart_hop_python_sdk/type/partial_job.py)<a id="job-partialjobchart_hop_python_sdktypepartial_jobpy"></a>


##### update: [`JobUpdate`](./chart_hop_python_sdk/type/job_update.py)<a id="update-jobupdatechart_hop_python_sdktypejob_updatepy"></a>


##### note: `str`<a id="note-str"></a>

note on the change

##### approval_note: `str`<a id="approval_note-str"></a>

approval/rejection note

##### process_id: `str`<a id="process_id-str"></a>

Process id of person creation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateChange`](./chart_hop_python_sdk/type/update_change.py)
Change data

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/{changeId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.change.validate_change_operation`<a id="charthopchangevalidate_change_operation"></a>

Validate a change

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_change_operation_response = charthop.change.validate_change_operation(
    org_id="orgId_example",
    type="type_example",
    job_id="588f7ee98f138b19220041a7",
    org_id="588f7ee98f138b19220041a7",
    scenario_id="588f7ee98f138b19220041a7",
    person_id="string_example",
    other_job_id="588f7ee98f138b19220041a7",
    type="HIRE",
    date="1970-01-01",
    announce_date="1970-01-01",
    depart_type="VOLUNTARY",
    depart_regret="REGRET",
    reason="string_example",
    promotion_type="PROMOTION",
    job={
        "title": "Senior Engineer",
        "job_id": "588f7ee98f138b19220041a7",
        "org_id": "588f7ee98f138b19220041a7",
        "snapshot_id": "588f7ee98f138b19220041a7",
        "sensitive": "GLOBAL",
        "placement": "NORMAL",
        "employment": "FULL",
        "state": "OPEN",
        "person_id": "588f7ee98f138b19220041a7",
        "backfill_person_id": "588f7ee98f138b19220041a7",
        "backfill_by_job_id": "588f7ee98f138b19220041a7",
    },
    update={
        "placement": "NORMAL",
        "employment": "FULL",
        "sensitive": "GLOBAL",
    },
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Change type

##### requestBody: [`CreateChange`](./chart_hop_python_sdk/type/create_change.py)<a id="requestbody-createchangechart_hop_python_sdktypecreate_changepy"></a>

Change data

#### 🔄 Return<a id="🔄-return"></a>

[`Change`](./chart_hop_python_sdk/pydantic/change.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change/{type}/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comment.create_new_comment`<a id="charthopcommentcreate_new_comment"></a>

Post a comment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_comment_response = charthop.comment.create_new_comment(
    entity_id="588f7ee98f138b19220041a7",
    entity_type="CHANGE",
    content={
        "type": "HTML",
        "value": "value_example",
    },
    org_id="orgId_example",
    parent_entity_id="588f7ee98f138b19220041a7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### entity_id: `str`<a id="entity_id-str"></a>

entity the comment was posted on

##### entity_type: `str`<a id="entity_type-str"></a>

type of entity the comment was posted on

##### content: [`Markup`](./chart_hop_python_sdk/type/markup.py)<a id="content-markupchart_hop_python_sdktypemarkuppy"></a>


##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### parent_entity_id: `str`<a id="parent_entity_id-str"></a>

parent entity id that this comment belongs to, should be used with entityId

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateComment`](./chart_hop_python_sdk/type/create_comment.py)
Comment data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Comment`](./chart_hop_python_sdk/pydantic/comment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comment.get_by_entity_id`<a id="charthopcommentget_by_entity_id"></a>

Return comments on a particular entity paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_entity_id_response = charthop.comment.get_by_entity_id(
    org_id="orgId_example",
    entity_id="entityId_example",
    _from="string_example",
    limit=1,
    desc=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### entity_id: `str`<a id="entity_id-str"></a>

Entity id

##### _from: `str`<a id="_from-str"></a>

Comment id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### desc: `bool`<a id="desc-bool"></a>

Descending (default false)

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsComment`](./chart_hop_python_sdk/pydantic/results_comment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comment/entity/{entityId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comment.get_by_id`<a id="charthopcommentget_by_id"></a>

Return a particular comment by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.comment.get_by_id(
    org_id="orgId_example",
    comment_id="commentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comment_id: `str`<a id="comment_id-str"></a>

Comment id

#### 🔄 Return<a id="🔄-return"></a>

[`Comment`](./chart_hop_python_sdk/pydantic/comment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comment/{commentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comment.list_comments_on_comp_review`<a id="charthopcommentlist_comments_on_comp_review"></a>

Return comments on changes within a comp review, paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_comments_on_comp_review_response = charthop.comment.list_comments_on_comp_review(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    approval_request_id="string_example",
    _from="string_example",
    limit=1,
    desc=True,
    is_preview=True,
    job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

Approval request id

##### _from: `str`<a id="_from-str"></a>

Comment id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### desc: `bool`<a id="desc-bool"></a>

Descending (default false)

##### is_preview: `bool`<a id="is_preview-bool"></a>

Whether comments are viewed in preview mode, defaults false

##### job_id: `str`<a id="job_id-str"></a>

Optional preview user jobId

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsComment`](./chart_hop_python_sdk/pydantic/results_comment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comment/comp-review/{compReviewId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comment.list_comments_on_scenario_and_changes`<a id="charthopcommentlist_comments_on_scenario_and_changes"></a>

Return comments on a scenario and the changes within, paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_comments_on_scenario_and_changes_response = charthop.comment.list_comments_on_scenario_and_changes(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    _from="string_example",
    limit=1,
    desc=True,
    include_change_comments=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### _from: `str`<a id="_from-str"></a>

Comment id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### desc: `bool`<a id="desc-bool"></a>

Descending (default false)

##### include_change_comments: `bool`<a id="include_change_comments-bool"></a>

Whether to also include comments on changes within the scenario (default false)

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsComment`](./chart_hop_python_sdk/pydantic/results_comment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comment/scenario/{scenarioId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comment.remove_by_id`<a id="charthopcommentremove_by_id"></a>

Delete a comment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.comment.remove_by_id(
    org_id="orgId_example",
    comment_id="commentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comment_id: `str`<a id="comment_id-str"></a>

Comment id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comment/{commentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.close_comp_review`<a id="charthopcomp_reviewclose_comp_review"></a>

Concludes (or closes) the compensation review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.comp_review.close_comp_review(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    is_fully_approved=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### is_fully_approved: `bool`<a id="is_fully_approved-bool"></a>

Whether is review fully approved on conclude (default false)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/conclude` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.create_bulk_duplicate`<a id="charthopcomp_reviewcreate_bulk_duplicate"></a>

Duplicate a set of comp reviews

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bulk_duplicate_response = charthop.comp_review.create_bulk_duplicate(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CompreviewCreateBulkDuplicateRequest`](./chart_hop_python_sdk/type/compreview_create_bulk_duplicate_request.py)<a id="requestbody-compreviewcreatebulkduplicaterequestchart_hop_python_sdktypecompreview_create_bulk_duplicate_requestpy"></a>

List of comp review ids to duplicate

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/bulk/duplicate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.create_comp_review`<a id="charthopcomp_reviewcreate_comp_review"></a>

Create a comp review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.comp_review.create_comp_review(
    label="Comp review H2 2022",
    org_id="orgId_example",
    config={
        "key_dates": {
            "cycle_begin_date": "1970-01-01",
            "levels_submit_by_date": "1970-01-01",
            "final_approval_date": "1970-01-01",
        },
        "eligible_employees": {
            "ineligibility_type": "NONE",
        },
        "reviewers_and_approvers": {
            "reviewers": "ALL_MANAGERS",
        },
        "collaborators": {
            "collaboration_type": "NONE",
            "collaborator_access": "READ",
            "job_to_collaborators_map": {
                "key": [
                    "string_example"
                ],
            },
        },
        "reviewer_workbook": {
            "columns": [
                {
                    "name": "name_example",
                    "label": "label_example",
                    "editable_for": "editable_for_example",
                    "visible_to": "visible_to_example",
                    "visible_to_groups": [
                        "588f7ee98f138b19220041a7"
                    ],
                    "visible_to_type": "EVERYONE",
                }
            ],
        },
    },
    status="PENDING",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

human-readable label of goal

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### config: [`CompReviewConfig`](./chart_hop_python_sdk/type/comp_review_config.py)<a id="config-compreviewconfigchart_hop_python_sdktypecomp_review_configpy"></a>


##### status: `str`<a id="status-str"></a>

Whether the compensation review has been approved by the final approvers

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who have been granted access to this comp review

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCompReview`](./chart_hop_python_sdk/type/create_comp_review.py)
Comp review data to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.create_visualization_data`<a id="charthopcomp_reviewcreate_visualization_data"></a>

Get data for visualizations for a comp review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_visualization_data_response = charthop.comp_review.create_visualization_data(
    is_collabicient_view=True,
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    change_ids=[
        "string_example"
    ],
    view_in_currency="string_example",
    include_collaborators=True,
    view_job_id="string_example",
    preview=True,
    include_all_requests=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### is_collabicient_view: `bool`<a id="is_collabicient_view-bool"></a>

Are the visualizations for a collaborating participant

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### change_ids: [`GetVisualizationsOptionsChangeIds`](./chart_hop_python_sdk/type/get_visualizations_options_change_ids.py)<a id="change_ids-getvisualizationsoptionschangeidschart_hop_python_sdktypeget_visualizations_options_change_idspy"></a>

##### view_in_currency: `str`<a id="view_in_currency-str"></a>

Currency to view budget visualizations

##### include_collaborators: `bool`<a id="include_collaborators-bool"></a>

Whether or not to include approval requests on which a user is collaborating when calculating budget amounts for that user

##### view_job_id: `str`<a id="view_job_id-str"></a>

The job you would like to view as

##### preview: `bool`<a id="preview-bool"></a>

Are the visualizations for a preview

##### include_all_requests: `bool`<a id="include_all_requests-bool"></a>

Allows users with multiple roles to request full access for owner or final approver roles

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetVisualizationsOptions`](./chart_hop_python_sdk/type/get_visualizations_options.py)
Options for visualizations

#### 🔄 Return<a id="🔄-return"></a>

[`CompReviewVisualizations`](./chart_hop_python_sdk/pydantic/comp_review_visualizations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/visualizations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.delete_bulk_comp_reviews`<a id="charthopcomp_reviewdelete_bulk_comp_reviews"></a>

Delete a set of comp reviews

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_bulk_comp_reviews_response = charthop.comp_review.delete_bulk_comp_reviews(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CompreviewDeleteBulkCompReviewsRequest`](./chart_hop_python_sdk/type/compreview_delete_bulk_comp_reviews_request.py)<a id="requestbody-compreviewdeletebulkcompreviewsrequestchart_hop_python_sdktypecompreview_delete_bulk_comp_reviews_requestpy"></a>

List of comp review ids to delete

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/bulk/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.delete_comp_review`<a id="charthopcomp_reviewdelete_comp_review"></a>

Delete a comp review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.comp_review.delete_comp_review(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.duplicate_comp_review`<a id="charthopcomp_reviewduplicate_comp_review"></a>

Duplicate a comp review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
duplicate_comp_review_response = charthop.comp_review.duplicate_comp_review(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### 🔄 Return<a id="🔄-return"></a>

[`CompReview`](./chart_hop_python_sdk/pydantic/comp_review.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/duplicate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.export_audit_log`<a id="charthopcomp_reviewexport_audit_log"></a>

Export a comp review's audit log

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
export_audit_log_response = charthop.comp_review.export_audit_log(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompreviewExportChangesRequest`](./chart_hop_python_sdk/type/compreview_export_changes_request.py)
Export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/export/audit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.export_changes`<a id="charthopcomp_reviewexport_changes"></a>

Export a comp review's changes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
export_changes_response = charthop.comp_review.export_changes(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompreviewExportChangesRequest`](./chart_hop_python_sdk/type/compreview_export_changes_request.py)
Export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/export` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.export_comments`<a id="charthopcomp_reviewexport_comments"></a>

Export a comp review's comments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
export_comments_response = charthop.comp_review.export_comments(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/export/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.find_comp_review_by_id`<a id="charthopcomp_reviewfind_comp_review_by_id"></a>

Return a particular comp review by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_comp_review_by_id_response = charthop.comp_review.find_comp_review_by_id(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### 🔄 Return<a id="🔄-return"></a>

[`CompReview`](./chart_hop_python_sdk/pydantic/comp_review.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.find_comp_reviews`<a id="charthopcomp_reviewfind_comp_reviews"></a>

Find comp reviews in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_comp_reviews_response = charthop.comp_review.find_comp_reviews(
    org_id="orgId_example",
    _from="string_example",
    limit=1,
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

Comp review ID to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsCompReview`](./chart_hop_python_sdk/pydantic/results_comp_review.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.generate_comp_review`<a id="charthopcomp_reviewgenerate_comp_review"></a>

Generate a compensation review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_comp_review_response = charthop.comp_review.generate_comp_review(
    is_preview=True,
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### is_preview: `bool`<a id="is_preview-bool"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GenerateCompReviewOptions`](./chart_hop_python_sdk/type/generate_comp_review_options.py)
Whether this should be generated as a preview

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/generate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.generate_tiering_preview`<a id="charthopcomp_reviewgenerate_tiering_preview"></a>

Generate tiering & preview for a compensation review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_tiering_preview_response = charthop.comp_review.generate_tiering_preview(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### 🔄 Return<a id="🔄-return"></a>

[`TiersResponse`](./chart_hop_python_sdk/pydantic/tiers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/preview` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.get_change_and_guideline_flags`<a id="charthopcomp_reviewget_change_and_guideline_flags"></a>

Get the change data and guideline flags associated with an in-cycle change

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_change_and_guideline_flags_response = charthop.comp_review.get_change_and_guideline_flags(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    change_id="changeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### change_id: `str`<a id="change_id-str"></a>

Change id

#### 🔄 Return<a id="🔄-return"></a>

[`InCycleChange`](./chart_hop_python_sdk/pydantic/in_cycle_change.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/in-cycle/changes/{changeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.get_changes_in_cycle`<a id="charthopcomp_reviewget_changes_in_cycle"></a>

Get the changes for a set of scenarios in an in-cycle comp-review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_changes_in_cycle_response = charthop.comp_review.get_changes_in_cycle(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    approval_request_id="string_example",
    is_preview=True,
    job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

Approval request id

##### is_preview: `bool`<a id="is_preview-bool"></a>

##### job_id: `str`<a id="job_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InCycleViewChanges`](./chart_hop_python_sdk/pydantic/in_cycle_view_changes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/in-cycle/changes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.get_collabicient_in_cycle`<a id="charthopcomp_reviewget_collabicient_in_cycle"></a>

Get a collaborator participant reviewer in-cycle comp-review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collabicient_in_cycle_response = charthop.comp_review.get_collabicient_in_cycle(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    scenarios_only=True,
    proposal_only=True,
    reviews_only=True,
    columns_only=True,
    is_preview=True,
    collabicient_job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### scenarios_only: `bool`<a id="scenarios_only-bool"></a>

##### proposal_only: `bool`<a id="proposal_only-bool"></a>

##### reviews_only: `bool`<a id="reviews_only-bool"></a>

##### columns_only: `bool`<a id="columns_only-bool"></a>

##### is_preview: `bool`<a id="is_preview-bool"></a>

##### collabicient_job_id: `str`<a id="collabicient_job_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InCycleViewResponse`](./chart_hop_python_sdk/pydantic/in_cycle_view_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/in-cycle/collabicient` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.get_date_caches`<a id="charthopcomp_reviewget_date_caches"></a>

Get the necessary caches on a specific date for a compensation review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_date_caches_response = charthop.comp_review.get_date_caches(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### 🔄 Return<a id="🔄-return"></a>

[`PartialAppEntities`](./chart_hop_python_sdk/pydantic/partial_app_entities.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/associated-entities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.get_eligible_employees`<a id="charthopcomp_reviewget_eligible_employees"></a>

Get a list of employees eligible for a given comp review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_eligible_employees_response = charthop.comp_review.get_eligible_employees(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    filter_scenario_ids="string_example",
    ineligible=True,
    _from="string_example",
    limit=1,
    fields="string_example",
    format="string_example",
    filter="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### filter_scenario_ids: `str`<a id="filter_scenario_ids-str"></a>

Find ineligible employees under specific comp scenario managers

##### ineligible: `bool`<a id="ineligible-bool"></a>

Whether to get eligible or ineligible employees (defaults to eligible)

##### _from: `str`<a id="_from-str"></a>

Job id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### fields: `str`<a id="fields-str"></a>

Table fields

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### filter: `str`<a id="filter-str"></a>

Optional CQL filter to apply to employees

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/eligible-employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.get_metadata_by_id`<a id="charthopcomp_reviewget_metadata_by_id"></a>

Return metadata for a particular comp review by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metadata_by_id_response = charthop.comp_review.get_metadata_by_id(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### 🔄 Return<a id="🔄-return"></a>

[`CompReviewMetadata`](./chart_hop_python_sdk/pydantic/comp_review_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/metadata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.list_request_responses`<a id="charthopcomp_reviewlist_request_responses"></a>

Get a list of approval request responses for a given comp review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_request_responses_response = charthop.comp_review.list_request_responses(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    is_preview=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### is_preview: `bool`<a id="is_preview-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CompreviewListRequestResponsesResponse`](./chart_hop_python_sdk/pydantic/compreview_list_request_responses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/approval-requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.overview_in_cycle_comp_review`<a id="charthopcomp_reviewoverview_in_cycle_comp_review"></a>

Get an overview for a given user in an in-cycle comp-review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
overview_in_cycle_comp_review_response = charthop.comp_review.overview_in_cycle_comp_review(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    scenarios_only=True,
    proposal_only=True,
    reviews_only=True,
    columns_only=True,
    is_preview=True,
    job_id="string_example",
    include_all_requests=True,
    include_features=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### scenarios_only: `bool`<a id="scenarios_only-bool"></a>

##### proposal_only: `bool`<a id="proposal_only-bool"></a>

##### reviews_only: `bool`<a id="reviews_only-bool"></a>

##### columns_only: `bool`<a id="columns_only-bool"></a>

##### is_preview: `bool`<a id="is_preview-bool"></a>

##### job_id: `str`<a id="job_id-str"></a>

##### include_all_requests: `bool`<a id="include_all_requests-bool"></a>

Allows users with multiple roles to request full access for owner or final approver roles

##### include_features: `bool`<a id="include_features-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InCycleViewResponse`](./chart_hop_python_sdk/pydantic/in_cycle_view_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/in-cycle` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.pause_review`<a id="charthopcomp_reviewpause_review"></a>

Pauses the compensation review to allow for editing by an admin

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.comp_review.pause_review(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/pause` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.send_reminder_email`<a id="charthopcomp_reviewsend_reminder_email"></a>

Send a reminder email to someone participating in a comp review 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.comp_review.send_reminder_email(
    approval_request_id="string_example",
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SendReminderEmailOptions`](./chart_hop_python_sdk/type/send_reminder_email_options.py)
Approval request ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/send-reminder-email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.update_approval_request_status`<a id="charthopcomp_reviewupdate_approval_request_status"></a>

Update approval request status, including any rollups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.comp_review.update_approval_request_status(
    status="CANCELED",
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    approval_request_id="approvalRequestId_example",
    message="string_example",
    preview_job_id="string_example",
    is_final_approval=True,
    collaborator_selected_reviewer_job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

Approval request id

##### message: `str`<a id="message-str"></a>

##### preview_job_id: `str`<a id="preview_job_id-str"></a>

Preview-as job id

##### is_final_approval: `bool`<a id="is_final_approval-bool"></a>

Updating the final stage status

##### collaborator_selected_reviewer_job_id: `str`<a id="collaborator_selected_reviewer_job_id-str"></a>

Reviewer job id a collaborator is working on

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApprovalRequestPatchBody`](./chart_hop_python_sdk/type/approval_request_patch_body.py)
Approval request data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}/approval-requests/{approvalRequestId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.comp_review.update_comp_review`<a id="charthopcomp_reviewupdate_comp_review"></a>

Update a comp review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_comp_review_response = charthop.comp_review.update_comp_review(
    org_id="orgId_example",
    comp_review_id="compReviewId_example",
    label="Comp review H2 2022",
    config={
        "key_dates": {
            "cycle_begin_date": "1970-01-01",
            "levels_submit_by_date": "1970-01-01",
            "final_approval_date": "1970-01-01",
        },
        "eligible_employees": {
            "ineligibility_type": "NONE",
        },
        "reviewers_and_approvers": {
            "reviewers": "ALL_MANAGERS",
        },
        "collaborators": {
            "collaboration_type": "NONE",
            "collaborator_access": "READ",
            "job_to_collaborators_map": {
                "key": [
                    "string_example"
                ],
            },
        },
        "reviewer_workbook": {
            "columns": [
                {
                    "name": "name_example",
                    "label": "label_example",
                    "editable_for": "editable_for_example",
                    "visible_to": "visible_to_example",
                    "visible_to_groups": [
                        "588f7ee98f138b19220041a7"
                    ],
                    "visible_to_type": "EVERYONE",
                }
            ],
        },
    },
    status="PENDING",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    reviewer_count=1,
    submitted_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Review id

##### label: `str`<a id="label-str"></a>

human-readable label of goal

##### config: [`CompReviewConfig`](./chart_hop_python_sdk/type/comp_review_config.py)<a id="config-compreviewconfigchart_hop_python_sdktypecomp_review_configpy"></a>


##### status: `str`<a id="status-str"></a>

Whether the compensation review has been approved by the final approvers

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who have been granted access to this comp review

##### reviewer_count: `int`<a id="reviewer_count-int"></a>

count of reviewers in the comp review

##### submitted_count: `int`<a id="submitted_count-int"></a>

count of reviews that have been submitted and approved

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCompReview`](./chart_hop_python_sdk/type/update_comp_review.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompReview`](./chart_hop_python_sdk/pydantic/comp_review.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/comp-review/{compReviewId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.create_new_piece`<a id="charthopcontentcreate_new_piece"></a>

Create a new piece of content

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_piece_response = charthop.content.create_new_piece(
    title="Benefits Policies",
    org_id="orgId_example",
    parent_content_id="588f7ee98f138b19220041a7",
    path="employee-info/benefits-policies",
    blocks=[
        {
            "content": "content_example",
        }
    ],
    image_path="path/to/image.jpg",
    emoji="💥",
    cover_image_path="path/to/image.jpg",
    sensitive="GLOBAL",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    status="DRAFT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

title of the content page

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### parent_content_id: `str`<a id="parent_content_id-str"></a>

parent content id in the hierarchy

##### path: `str`<a id="path-str"></a>

full path to the content, if not set, defaults to an id/slug generated URL

##### blocks: List[`ContentBlock`]<a id="blocks-listcontentblock"></a>

content blocks

##### image_path: `str`<a id="image_path-str"></a>

path to the image for the page

##### emoji: `str`<a id="emoji-str"></a>

emoji, if an emoji is used to represent the page

##### cover_image_path: `str`<a id="cover_image_path-str"></a>

path to the cover image for the content page

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level (ORG public, HIGHly sensitive, or PRIVATE)

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

list of users and groups who have the content shared with them

##### status: `str`<a id="status-str"></a>

current status of the content page

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContent`](./chart_hop_python_sdk/type/create_content.py)
Content data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Content`](./chart_hop_python_sdk/pydantic/content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.get_by_id`<a id="charthopcontentget_by_id"></a>

Return a particular content by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.content.get_by_id(
    org_id="orgId_example",
    content_id="contentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### content_id: `str`<a id="content_id-str"></a>

Content id

#### 🔄 Return<a id="🔄-return"></a>

[`Content`](./chart_hop_python_sdk/pydantic/content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content/{contentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.get_by_path`<a id="charthopcontentget_by_path"></a>

Return a particular content by path

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_path_response = charthop.content.get_by_path(
    org_id="orgId_example",
    path="jUR,rZ#UM/?R,Fp^l6$ARj",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### path: `str`<a id="path-str"></a>

Path

#### 🔄 Return<a id="🔄-return"></a>

[`Content`](./chart_hop_python_sdk/pydantic/content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content/path/{path}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.get_paginated`<a id="charthopcontentget_paginated"></a>

Return all content in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_paginated_response = charthop.content.get_paginated(
    org_id="orgId_example",
    _from="string_example",
    limit=1,
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

Content id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsContent`](./chart_hop_python_sdk/pydantic/results_content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.remove_by_id`<a id="charthopcontentremove_by_id"></a>

Delete a content

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.content.remove_by_id(
    org_id="orgId_example",
    content_id="contentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### content_id: `str`<a id="content_id-str"></a>

Content id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content/{contentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.render_by_path`<a id="charthopcontentrender_by_path"></a>

Return a particular content by path, and render its contents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
render_by_path_response = charthop.content.render_by_path(
    org_id="orgId_example",
    path="jUR,rZ#UM/?R,Fp^l6$ARj",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### path: `str`<a id="path-str"></a>

Path

#### 🔄 Return<a id="🔄-return"></a>

[`ContentRender`](./chart_hop_python_sdk/pydantic/content_render.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content/path/{path}/render` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.render_homepage_contents`<a id="charthopcontentrender_homepage_contents"></a>

Render the contents of the homepage

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
render_homepage_contents_response = charthop.content.render_homepage_contents(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`HomepageContentRender`](./chart_hop_python_sdk/pydantic/homepage_content_render.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content/homepage/render` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.update_homepage_content`<a id="charthopcontentupdate_homepage_content"></a>

Update the homepage content

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.content.update_homepage_content(
    org_id="orgId_example",
    title="Benefits Policies",
    parent_content_id="588f7ee98f138b19220041a7",
    path="employee-info/benefits-policies",
    blocks=[
        {
            "content": "content_example",
        }
    ],
    image_path="path/to/image.jpg",
    emoji="💥",
    cover_image_path="path/to/image.jpg",
    sensitive="GLOBAL",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    status="DRAFT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### title: `str`<a id="title-str"></a>

title of the content page

##### parent_content_id: `str`<a id="parent_content_id-str"></a>

parent content id in the hierarchy

##### path: `str`<a id="path-str"></a>

full path to the content, if not set, defaults to an id/slug generated URL

##### blocks: List[`ContentBlock`]<a id="blocks-listcontentblock"></a>

content blocks

##### image_path: `str`<a id="image_path-str"></a>

path to the image for the page

##### emoji: `str`<a id="emoji-str"></a>

emoji, if an emoji is used to represent the page

##### cover_image_path: `str`<a id="cover_image_path-str"></a>

path to the cover image for the content page

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level (ORG public, HIGHly sensitive, or PRIVATE)

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

list of users and groups who have the content shared with them

##### status: `str`<a id="status-str"></a>

current status of the content page

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateContent`](./chart_hop_python_sdk/type/update_content.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content/homepage` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.content.update_piece_by_id`<a id="charthopcontentupdate_piece_by_id"></a>

Update an existing piece of content

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.content.update_piece_by_id(
    org_id="orgId_example",
    content_id="contentId_example",
    title="Benefits Policies",
    parent_content_id="588f7ee98f138b19220041a7",
    path="employee-info/benefits-policies",
    blocks=[
        {
            "content": "content_example",
        }
    ],
    image_path="path/to/image.jpg",
    emoji="💥",
    cover_image_path="path/to/image.jpg",
    sensitive="GLOBAL",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    status="DRAFT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### content_id: `str`<a id="content_id-str"></a>

Content id

##### title: `str`<a id="title-str"></a>

title of the content page

##### parent_content_id: `str`<a id="parent_content_id-str"></a>

parent content id in the hierarchy

##### path: `str`<a id="path-str"></a>

full path to the content, if not set, defaults to an id/slug generated URL

##### blocks: List[`ContentBlock`]<a id="blocks-listcontentblock"></a>

content blocks

##### image_path: `str`<a id="image_path-str"></a>

path to the image for the page

##### emoji: `str`<a id="emoji-str"></a>

emoji, if an emoji is used to represent the page

##### cover_image_path: `str`<a id="cover_image_path-str"></a>

path to the cover image for the content page

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level (ORG public, HIGHly sensitive, or PRIVATE)

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

list of users and groups who have the content shared with them

##### status: `str`<a id="status-str"></a>

current status of the content page

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateContent`](./chart_hop_python_sdk/type/update_content.py)
Content data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/content/{contentId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.customer.create_new_customer`<a id="charthopcustomercreate_new_customer"></a>

Create a new customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_customer_response = charthop.customer.create_new_customer(
    name="string_example",
    email="string_example",
    start_date="1970-01-01",
    bill_address={
        "street1": "123 Anywhere Street",
        "street2": "Apt 6L",
        "street3": "Sixth Floor",
        "city": "New York",
        "state": "NY",
        "country": "NY",
        "postal": "10001",
    },
    industry="string_example",
    source="ADP_MARKETPLACE",
    status="ACTIVE",
    salesforce_account_id="Cu2LC4aWwWL9Y864DZ",
    products=[
        {
            "product_id": "product_id_example",
            "stripe_price_id": "stripe_price_id_example",
        }
    ],
    end_date="1970-01-01",
    next_invoice_date="1970-01-01",
    primary_head_count_filter="string_example",
    secondary_head_count_filter="string_example",
    arr=3.14,
    projected_arr=3.14,
    trial_start_date="1970-01-01",
    trial_end_date="1970-01-01",
    stripe_subscription_sync="SYNC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

name of customer

##### email: `str`<a id="email-str"></a>

email address for billing purposes

##### start_date: `date`<a id="start_date-date"></a>

initial date of billing

##### bill_address: [`Address`](./chart_hop_python_sdk/type/address.py)<a id="bill_address-addresschart_hop_python_sdktypeaddresspy"></a>


##### industry: `str`<a id="industry-str"></a>

industry that customer is in

##### source: `str`<a id="source-str"></a>

source of customer signup

##### status: `str`<a id="status-str"></a>

current status

##### salesforce_account_id: `str`<a id="salesforce_account_id-str"></a>

salesforce account id

##### products: List[`ProductItem`]<a id="products-listproductitem"></a>

products that this customer has purchased

##### end_date: `date`<a id="end_date-date"></a>

end of service date for churning customers -- on or after this date, service should be disabled

##### next_invoice_date: `date`<a id="next_invoice_date-date"></a>

date of next invoice

##### primary_head_count_filter: `str`<a id="primary_head_count_filter-str"></a>

primary headcount filter - used for billing purposes

##### secondary_head_count_filter: `str`<a id="secondary_head_count_filter-str"></a>

secondary headcount filter - used for billing purposes

##### arr: `Union[int, float]`<a id="arr-unionint-float"></a>

current ARR of the customer based on most recent invoice

##### projected_arr: `Union[int, float]`<a id="projected_arr-unionint-float"></a>

projected ARR of the customer for upcoming invoice, based on plan and headcount

##### trial_start_date: `date`<a id="trial_start_date-date"></a>

date this customer begins their trial period

##### trial_end_date: `date`<a id="trial_end_date-date"></a>

date this customer ends their trial period

##### stripe_subscription_sync: `str`<a id="stripe_subscription_sync-str"></a>

Stripe subscription settings

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCustomer`](./chart_hop_python_sdk/type/create_customer.py)
Customer data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Customer`](./chart_hop_python_sdk/pydantic/customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.customer.get_all_invoices_for_customer`<a id="charthopcustomerget_all_invoices_for_customer"></a>

Returns a list of all the invoices for the given customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_invoices_for_customer_response = charthop.customer.get_all_invoices_for_customer(
    customer_id="customerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

Customer id

#### 🔄 Return<a id="🔄-return"></a>

[`InvoiceResponse`](./chart_hop_python_sdk/pydantic/invoice_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer/{customerId}/invoices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.customer.get_by_id`<a id="charthopcustomerget_by_id"></a>

Return a particular customer by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.customer.get_by_id(
    customer_id="customerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

Customer id

#### 🔄 Return<a id="🔄-return"></a>

[`Customer`](./chart_hop_python_sdk/pydantic/customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer/{customerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.customer.get_charthop_subscription`<a id="charthopcustomerget_charthop_subscription"></a>

Returns information about the Charthop subscription for the given customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_charthop_subscription_response = charthop.customer.get_charthop_subscription(
    customer_id="customerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

Customer id

#### 🔄 Return<a id="🔄-return"></a>

[`Subscription`](./chart_hop_python_sdk/pydantic/subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer/{customerId}/subscription` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.customer.list_visible_customers`<a id="charthopcustomerlist_visible_customers"></a>

Return all visible customers, paginated by name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_visible_customers_response = charthop.customer.list_visible_customers(
    _from="string_example",
    limit=1,
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `str`<a id="_from-str"></a>

Customer id to start from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### status: `str`<a id="status-str"></a>

Customer.Status. (ACTIVE/INACTIVE/TRAIL)

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsCustomer`](./chart_hop_python_sdk/pydantic/results_customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.customer.update_existing_customer`<a id="charthopcustomerupdate_existing_customer"></a>

Update an existing customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.customer.update_existing_customer(
    customer_id="customerId_example",
    name="string_example",
    email="string_example",
    bill_address={
        "street1": "123 Anywhere Street",
        "street2": "Apt 6L",
        "street3": "Sixth Floor",
        "city": "New York",
        "state": "NY",
        "country": "NY",
        "postal": "10001",
    },
    industry="string_example",
    source="ADP_MARKETPLACE",
    status="ACTIVE",
    salesforce_account_id="Cu2LC4aWwWL9Y864DZ",
    products=[
        {
            "product_id": "product_id_example",
            "stripe_price_id": "stripe_price_id_example",
        }
    ],
    start_date="1970-01-01",
    end_date="1970-01-01",
    next_invoice_date="1970-01-01",
    primary_head_count_filter="string_example",
    secondary_head_count_filter="string_example",
    arr=3.14,
    projected_arr=3.14,
    trial_start_date="1970-01-01",
    trial_end_date="1970-01-01",
    stripe_subscription_sync="SYNC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

Customer id

##### name: `str`<a id="name-str"></a>

name of customer

##### email: `str`<a id="email-str"></a>

email address for billing purposes

##### bill_address: [`Address`](./chart_hop_python_sdk/type/address.py)<a id="bill_address-addresschart_hop_python_sdktypeaddresspy"></a>


##### industry: `str`<a id="industry-str"></a>

industry that customer is in

##### source: `str`<a id="source-str"></a>

source of customer signup

##### status: `str`<a id="status-str"></a>

current status

##### salesforce_account_id: `str`<a id="salesforce_account_id-str"></a>

salesforce account id

##### products: List[`ProductItem`]<a id="products-listproductitem"></a>

products that this customer has purchased

##### start_date: `date`<a id="start_date-date"></a>

initial date of billing

##### end_date: `date`<a id="end_date-date"></a>

end of service date for churning customers -- on or after this date, service should be disabled

##### next_invoice_date: `date`<a id="next_invoice_date-date"></a>

date of next invoice

##### primary_head_count_filter: `str`<a id="primary_head_count_filter-str"></a>

primary headcount filter - used for billing purposes

##### secondary_head_count_filter: `str`<a id="secondary_head_count_filter-str"></a>

secondary headcount filter - used for billing purposes

##### arr: `Union[int, float]`<a id="arr-unionint-float"></a>

current ARR of the customer based on most recent invoice

##### projected_arr: `Union[int, float]`<a id="projected_arr-unionint-float"></a>

projected ARR of the customer for upcoming invoice, based on plan and headcount

##### trial_start_date: `date`<a id="trial_start_date-date"></a>

date this customer begins their trial period

##### trial_end_date: `date`<a id="trial_end_date-date"></a>

date this customer ends their trial period

##### stripe_subscription_sync: `str`<a id="stripe_subscription_sync-str"></a>

Stripe subscription settings

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCustomer`](./chart_hop_python_sdk/type/update_customer.py)
Customer data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer/{customerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.customer.update_subscription`<a id="charthopcustomerupdate_subscription"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.customer.update_subscription(
    payment_method="string_example",
    customer_id="customerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_method: `str`<a id="payment_method-str"></a>

Payment method to create; 'INVOICE' to make subscription paid by invoice, or the ID of the payment method if to make the subscription automatically charge a card

##### customer_id: `str`<a id="customer_id-str"></a>

Customer id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateSubscription`](./chart_hop_python_sdk/type/update_subscription.py)
Subscription data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer/{customerId}/subscription` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.data_view.create_new_data_view`<a id="charthopdata_viewcreate_new_data_view"></a>

Create a data view

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_data_view_response = charthop.data_view.create_new_data_view(
    name="string_example",
    org_id="orgId_example",
    columns="image,name,title",
    type="ANY",
    entity_type="string_example",
    column_widths={
        "key": 3.14,
    },
    date="string_example",
    start_date="string_example",
    end_date="string_example",
    filter="managerCount:1",
    sort="name,title",
    group_by="title",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    sensitive="GLOBAL",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

data view name

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### columns: `str`<a id="columns-str"></a>

comma delimited list of columns

##### type: `str`<a id="type-str"></a>

type of data view

##### entity_type: `str`<a id="entity_type-str"></a>

entity type being viewed

##### column_widths: [`CreateDataViewColumnWidths`](./chart_hop_python_sdk/type/create_data_view_column_widths.py)<a id="column_widths-createdataviewcolumnwidthschart_hop_python_sdktypecreate_data_view_column_widthspy"></a>

##### date: `str`<a id="date-str"></a>

date of view, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today

##### start_date: `str`<a id="start_date-str"></a>

start date of view, if displaying a date range, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today

##### end_date: `str`<a id="end_date-str"></a>

end date of view, if displaying a date range, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today

##### filter: `str`<a id="filter-str"></a>

filter query

##### sort: `str`<a id="sort-str"></a>

comma delimited list of columns by which to sort

##### group_by: `str`<a id="group_by-str"></a>

column to group duplicates by

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who are specifically granted permission to view or edit this data view

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level of data view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDataView`](./chart_hop_python_sdk/type/create_data_view.py)
Data view data to create

#### 🔄 Return<a id="🔄-return"></a>

[`DataView`](./chart_hop_python_sdk/pydantic/data_view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/data-view` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.data_view.delete_data_view`<a id="charthopdata_viewdelete_data_view"></a>

Delete a data  view

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.data_view.delete_data_view(
    org_id="orgId_example",
    data_view_id="dataViewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### data_view_id: `str`<a id="data_view_id-str"></a>

Data view id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/data-view/{dataViewId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.data_view.get_all_paginated`<a id="charthopdata_viewget_all_paginated"></a>

Return all data views in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_paginated_response = charthop.data_view.get_all_paginated(
    org_id="orgId_example",
    _from="string_example",
    type="ANY",
    limit=1,
    ids="string_example",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

Data view id to start paginating from

##### type: `str`<a id="type-str"></a>

Data view type to filter by

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### ids: `str`<a id="ids-str"></a>

Comma delimited of ids to return

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsDataView`](./chart_hop_python_sdk/pydantic/results_data_view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/data-view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.data_view.get_by_id`<a id="charthopdata_viewget_by_id"></a>

Return a particular data view by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.data_view.get_by_id(
    org_id="orgId_example",
    data_view_id="dataViewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### data_view_id: `str`<a id="data_view_id-str"></a>

Data view id

#### 🔄 Return<a id="🔄-return"></a>

[`DataView`](./chart_hop_python_sdk/pydantic/data_view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/data-view/{dataViewId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.data_view.update_existing_view`<a id="charthopdata_viewupdate_existing_view"></a>

Update an existing data view

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_view_response = charthop.data_view.update_existing_view(
    org_id="orgId_example",
    data_view_id="dataViewId_example",
    name="string_example",
    columns="image,name,title",
    type="ANY",
    entity_type="string_example",
    column_widths={
        "key": 3.14,
    },
    date="string_example",
    start_date="string_example",
    end_date="string_example",
    filter="managerCount:1",
    sort="name,title",
    group_by="title",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    sensitive="GLOBAL",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### data_view_id: `str`<a id="data_view_id-str"></a>

Data view id

##### name: `str`<a id="name-str"></a>

data view name

##### columns: `str`<a id="columns-str"></a>

comma delimited list of columns

##### type: `str`<a id="type-str"></a>

type of data view

##### entity_type: `str`<a id="entity_type-str"></a>

entity type being viewed

##### column_widths: [`UpdateDataViewColumnWidths`](./chart_hop_python_sdk/type/update_data_view_column_widths.py)<a id="column_widths-updatedataviewcolumnwidthschart_hop_python_sdktypeupdate_data_view_column_widthspy"></a>

##### date: `str`<a id="date-str"></a>

date of view, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today

##### start_date: `str`<a id="start_date-str"></a>

start date of view, if displaying a date range, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today

##### end_date: `str`<a id="end_date-str"></a>

end date of view, if displaying a date range, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today

##### filter: `str`<a id="filter-str"></a>

filter query

##### sort: `str`<a id="sort-str"></a>

comma delimited list of columns by which to sort

##### group_by: `str`<a id="group_by-str"></a>

column to group duplicates by

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who are specifically granted permission to view or edit this data view

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level of data view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateDataView`](./chart_hop_python_sdk/type/update_data_view.py)
Data view data to update

#### 🔄 Return<a id="🔄-return"></a>

[`DataView`](./chart_hop_python_sdk/pydantic/data_view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/data-view/{dataViewId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.email_template.create_new_template`<a id="charthopemail_templatecreate_new_template"></a>

Create a new email template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_template_response = charthop.email_template.create_new_template(
    name="self_serve_welcome",
    category="ADMINISTRATIVE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

name of the email template

##### category: `str`<a id="category-str"></a>

email category

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEmailTemplate`](./chart_hop_python_sdk/type/create_email_template.py)
Email template to create

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplate`](./chart_hop_python_sdk/pydantic/email_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/email-template` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.email_template.get_all_non_essential`<a id="charthopemail_templateget_all_non_essential"></a>

Return all non-essential email templates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_non_essential_response = charthop.email_template.get_all_non_essential()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsEmailTemplate`](./chart_hop_python_sdk/pydantic/results_email_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/email-template/non-essential` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.email_template.get_by_name`<a id="charthopemail_templateget_by_name"></a>

Return the email template by name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_name_response = charthop.email_template.get_by_name(
    name="name_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Email template name

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplate`](./chart_hop_python_sdk/pydantic/email_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/email-template/name/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.email_template.list_essential_email_templates`<a id="charthopemail_templatelist_essential_email_templates"></a>

Return all essential email templates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_essential_email_templates_response = charthop.email_template.list_essential_email_templates()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsEmailTemplate`](./chart_hop_python_sdk/pydantic/results_email_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/email-template/essential` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.email_template.update_existing_template`<a id="charthopemail_templateupdate_existing_template"></a>

Update an existing email template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.email_template.update_existing_template(
    email_template_id="emailTemplateId_example",
    name="self_serve_welcome",
    category="ADMINISTRATIVE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email_template_id: `str`<a id="email_template_id-str"></a>

Email template id

##### name: `str`<a id="name-str"></a>

name of the email template

##### category: `str`<a id="category-str"></a>

email category

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmailTemplate`](./chart_hop_python_sdk/type/update_email_template.py)
Email template data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/email-template/{emailTemplateId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.event.create_inbound_notification`<a id="charthopeventcreate_inbound_notification"></a>

Create an inbound event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_inbound_notification_response = charthop.event.create_inbound_notification(
    org_id="orgId_example",
    app_id="appId_example",
    inbound_id="inboundId_example",
    process_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_id: `str`<a id="app_id-str"></a>

App id

##### inbound_id: `str`<a id="inbound_id-str"></a>

Inbound id

##### process_id: `str`<a id="process_id-str"></a>

Process id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EventCreateInboundNotificationRequest`](./chart_hop_python_sdk/type/event_create_inbound_notification_request.py)
Inbound body to create event

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/event/notify/inbound/{appId}/{inboundId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.event.create_outbound_event`<a id="charthopeventcreate_outbound_event"></a>

Create an outbound event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_outbound_event_response = charthop.event.create_outbound_event(
    org_id="orgId_example",
    app_id="appId_example",
    process_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_id: `str`<a id="app_id-str"></a>

App id

##### process_id: `str`<a id="process_id-str"></a>

Process id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EventCreateOutboundEventRequest`](./chart_hop_python_sdk/type/event_create_outbound_event_request.py)
Outbound body to create event

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/event/notify/outbound/app/{appId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.event.get_event_payload`<a id="charthopeventget_event_payload"></a>

Return individual event, including payload

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_payload_response = charthop.event.get_event_payload(
    org_id="orgId_example",
    event_id="eventId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### event_id: `str`<a id="event_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Event`](./chart_hop_python_sdk/pydantic/event.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/event/{eventId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.event.get_past_events`<a id="charthopeventget_past_events"></a>

Return past events, paginated, without payloads present

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_past_events_response = charthop.event.get_past_events(
    org_id="orgId_example",
    user_id="string_example",
    entity_id="string_example",
    entity_type="ACTION",
    parent_entity_id="string_example",
    scenario_id="string_example",
    process_id="string_example",
    fields="string_example",
    code="string_example",
    _from=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### user_id: `str`<a id="user_id-str"></a>

User id

##### entity_id: `str`<a id="entity_id-str"></a>

Entity id

##### entity_type: `str`<a id="entity_type-str"></a>

Entity type

##### parent_entity_id: `str`<a id="parent_entity_id-str"></a>

Parent entity id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### process_id: `str`<a id="process_id-str"></a>

Process id

##### fields: `str`<a id="fields-str"></a>

Fields that were modified

##### code: `str`<a id="code-str"></a>

Event code to search for

##### _from: `int`<a id="_from-int"></a>

Timestamp to start search at

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsEvent`](./chart_hop_python_sdk/pydantic/results_event.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/event` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.event.resend_associated_notifications`<a id="charthopeventresend_associated_notifications"></a>

Resend all associated notifications for a previous event (superusers only)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.event.resend_associated_notifications(
    org_id="orgId_example",
    event_id="eventId_example",
    app="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### event_id: `str`<a id="event_id-str"></a>

Event id

##### app: `str`<a id="app-str"></a>

App name to restrict notifications to

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/event/{eventId}/notify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.exchange_rate.bulk_update_custom_rates`<a id="charthopexchange_ratebulk_update_custom_rates"></a>

Bulk update custom currency rates in org custom exchange rates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.exchange_rate.bulk_update_custom_rates(
    body=[
        {
        }
    ],
    org_id="orgId_example",
    date="1970-01-01",
    add_rates=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to use

##### add_rates: `bool`<a id="add_rates-bool"></a>

Boolean to determine whether to add or remove rates from update

##### requestBody: [`ExchangerateBulkUpdateCustomRatesRequest`](./chart_hop_python_sdk/type/exchangerate_bulk_update_custom_rates_request.py)<a id="requestbody-exchangeratebulkupdatecustomratesrequestchart_hop_python_sdktypeexchangerate_bulk_update_custom_rates_requestpy"></a>

Update data

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/exchange-rate/{date}/custom/bulkupdate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.exchange_rate.delete_custom_rate_on_date`<a id="charthopexchange_ratedelete_custom_rate_on_date"></a>

Delete a custom exchange rate on a particular date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.exchange_rate.delete_custom_rate_on_date(
    org_id="orgId_example",
    date="1970-01-01",
    currency_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to use

##### currency_code: `str`<a id="currency_code-str"></a>

Currency code

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/exchange-rate/{date}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.exchange_rate.get_custom_exchange_rates`<a id="charthopexchange_rateget_custom_exchange_rates"></a>

Return org custom exchange rates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_exchange_rates_response = charthop.exchange_rate.get_custom_exchange_rates(
    org_id="orgId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to use

#### 🔄 Return<a id="🔄-return"></a>

[`ExchangeRate`](./chart_hop_python_sdk/pydantic/exchange_rate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/exchange-rate/{date}/custom` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.exchange_rate.get_global_by_date`<a id="charthopexchange_rateget_global_by_date"></a>

Return the global exchange rates based on USD for a particular date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_global_by_date_response = charthop.exchange_rate.get_global_by_date(
    org_id="orgId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to use

#### 🔄 Return<a id="🔄-return"></a>

[`ExchangeRate`](./chart_hop_python_sdk/pydantic/exchange_rate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/exchange-rate/{date}/global` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.exchange_rate.get_rates_on_date`<a id="charthopexchange_rateget_rates_on_date"></a>

Return the exchange rates on a particular date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rates_on_date_response = charthop.exchange_rate.get_rates_on_date(
    org_id="orgId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to use

#### 🔄 Return<a id="🔄-return"></a>

[`ExchangeRate`](./chart_hop_python_sdk/pydantic/exchange_rate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/exchange-rate/{date}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.exchange_rate.org_custom_exchange_rates_history`<a id="charthopexchange_rateorg_custom_exchange_rates_history"></a>

Return org custom exchange rates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
org_custom_exchange_rates_history_response = charthop.exchange_rate.org_custom_exchange_rates_history(
    org_id="orgId_example",
    date="1970-01-01",
    currency="string_example",
    from_date="1970-01-01",
    to_date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to use

##### currency: `str`<a id="currency-str"></a>

Currency to search for

##### from_date: `date`<a id="from_date-date"></a>

Start date for search

##### to_date: `date`<a id="to_date-date"></a>

End date for search

#### 🔄 Return<a id="🔄-return"></a>

[`ExchangerateOrgCustomExchangeRatesHistoryResponse`](./chart_hop_python_sdk/pydantic/exchangerate_org_custom_exchange_rates_history_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/exchange-rate/{date}/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.exchange_rate.update_usd_exchange_rates_for_date`<a id="charthopexchange_rateupdate_usd_exchange_rates_for_date"></a>

Update the USD-based exchange rates for a particular date. Must be the first of a month.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.exchange_rate.update_usd_exchange_rates_for_date(
    org_id="orgId_example",
    date="1970-01-01",
    date="1970-01-01",
    rates={
        "key": 3.14,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to use

##### requestBody: [`UpdateExchangeRate`](./chart_hop_python_sdk/type/update_exchange_rate.py)<a id="requestbody-updateexchangeratechart_hop_python_sdktypeupdate_exchange_ratepy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/exchange-rate/{date}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.changelog_to_csv`<a id="charthopexportchangelog_to_csv"></a>

Export a changelog to CSV format

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
changelog_to_csv_response = charthop.export.changelog_to_csv(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExportChangelogToCsvRequest`](./chart_hop_python_sdk/type/export_changelog_to_csv_request.py)
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/csv/change` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.csv_custom_fields`<a id="charthopexportcsv_custom_fields"></a>

Export a CSV of custom fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
csv_custom_fields_response = charthop.export.csv_custom_fields(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExportCsvCustomFieldsRequest`](./chart_hop_python_sdk/type/export_csv_custom_fields_request.py)
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/csv/fields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.csv_scenario_comments`<a id="charthopexportcsv_scenario_comments"></a>

Export a csv log of a scenario comments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
csv_scenario_comments_response = charthop.export.csv_scenario_comments(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/csv/scenario/{scenarioId}/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.file_zip_download`<a id="charthopexportfile_zip_download"></a>

Export a zipfile of files downloaded from some field

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_zip_download_response = charthop.export.file_zip_download(
    org_id="orgId_example",
    field="string_example",
    date="1970-01-01",
    scenario_id="string_example",
    q="string_example",
    size="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### field: `str`<a id="field-str"></a>

Field

##### date: `date`<a id="date-date"></a>

Date

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### q: `str`<a id="q-str"></a>

Query for jobs or people to match against

##### size: `str`<a id="size-str"></a>

Size of images to export, if image file (250x250, 50x50, defaults to original)

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/zip/file` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.org_chart_to_powerpoint`<a id="charthopexportorg_chart_to_powerpoint"></a>

Export org chart to Powerpoint

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
org_chart_to_powerpoint_response = charthop.export.org_chart_to_powerpoint(
    org_id="orgId_example",
    date="2016-12-25",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

date to export the data from

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/powerpoint/org` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.pdf_review`<a id="charthopexportpdf_review"></a>

Export reviews in PDF format

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
pdf_review_response = charthop.export.pdf_review(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExportChangelogToCsvRequest`](./chart_hop_python_sdk/type/export_changelog_to_csv_request.py)
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/pdf/review/{assessmentId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.report_to_powerpoint`<a id="charthopexportreport_to_powerpoint"></a>

Export report to Powerpoint

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
report_to_powerpoint_response = charthop.export.report_to_powerpoint(
    org_id="orgId_example",
    report_id="reportId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

report id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/powerpoint/report/{reportId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.roster_to_csv_snapshot`<a id="charthopexportroster_to_csv_snapshot"></a>

Export a snapshot of a current roster to CSV format

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
roster_to_csv_snapshot_response = charthop.export.roster_to_csv_snapshot(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExportChangelogToCsvRequest`](./chart_hop_python_sdk/type/export_changelog_to_csv_request.py)
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/csv/snapshot` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.scenario_csv`<a id="charthopexportscenario_csv"></a>

Export a CSV changelog of a scenario

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
scenario_csv_response = charthop.export.scenario_csv(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExportChangelogToCsvRequest`](./chart_hop_python_sdk/type/export_changelog_to_csv_request.py)
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/csv/scenario/{scenarioId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.task_to_csv`<a id="charthopexporttask_to_csv"></a>

Export tasks for a review to CSV format

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
task_to_csv_response = charthop.export.task_to_csv(
    org_id="orgId_example",
    review_id="reviewId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### review_id: `str`<a id="review_id-str"></a>

review id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExportChangelogToCsvRequest`](./chart_hop_python_sdk/type/export_changelog_to_csv_request.py)
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/csv/task/{reviewId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.export.user_review_csv`<a id="charthopexportuser_review_csv"></a>

Export users for a review to CSV format

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
user_review_csv_response = charthop.export.user_review_csv(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExportChangelogToCsvRequest`](./chart_hop_python_sdk/type/export_changelog_to_csv_request.py)
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/export/csv/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.expression.evaluate_carrot_expression`<a id="charthopexpressionevaluate_carrot_expression"></a>

Evaluate carrot expression

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
evaluate_carrot_expression_response = charthop.expression.evaluate_carrot_expression(
    expr="string_example",
    entity_type="ACTION",
    entity_id="string_example",
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expr: `str`<a id="expr-str"></a>

##### entity_type: `str`<a id="entity_type-str"></a>

##### entity_id: `str`<a id="entity_id-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EvaluateExpressionRequest`](./chart_hop_python_sdk/type/evaluate_expression_request.py)
Expression to be evaluated

#### 🔄 Return<a id="🔄-return"></a>

[`EvaluateExpressionResponse`](./chart_hop_python_sdk/pydantic/evaluate_expression_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/cql/evaluate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.expression.validate_carrot_expression`<a id="charthopexpressionvalidate_carrot_expression"></a>

Validate carrot expression(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_carrot_expression_response = charthop.expression.validate_carrot_expression(
    expressions=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expressions: [`ValidateExpressionRequestExpressions`](./chart_hop_python_sdk/type/validate_expression_request_expressions.py)<a id="expressions-validateexpressionrequestexpressionschart_hop_python_sdktypevalidate_expression_request_expressionspy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ValidateExpressionRequest`](./chart_hop_python_sdk/type/validate_expression_request.py)
Expression to be validated

#### 🔄 Return<a id="🔄-return"></a>

[`ValidateExpressionResponse`](./chart_hop_python_sdk/pydantic/validate_expression_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/cql/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.create_new_field`<a id="charthopfieldcreate_new_field"></a>

Create a field

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_field_response = charthop.field.create_new_field(
    name="summary",
    label="Job Summary",
    type="ADDRESS",
    entity_type="JOB",
    sensitive="GLOBAL",
    is_unique=True,
    is_required=True,
    org_id="orgId_example",
    description="This field tracks the most recent performance rating for an individual.",
    org_id="588f7ee98f138b19220041a7",
    question="What do you think of this placeholder question?",
    in_use=True,
    expr="(base + variable) / 12",
    expr_type="ADDRESS",
    plural="SINGLE",
    values=[
        {
            "name": "name_example",
            "label": "label_example",
        }
    ],
    default_value={},
    options={},
    hide_expr=True,
    expire_days=1,
    status="ACTIVE",
    table_id="string_example",
    table_ref={
        "table_id": "table_id_example",
        "table_name": "table_name_example",
    },
    is_effective_dated=True,
    data_fetch_types=[
        "string_example"
    ],
    aliases=[
        "string_example"
    ],
    calc="ADDRESS",
    category_id="string_example",
    classification="COMPOUND",
    places=1,
    table_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_type: `str`<a id="table_type-str"></a>

table type to add the field to

##### requestBody: [`CreateField`](./chart_hop_python_sdk/type/create_field.py)<a id="requestbody-createfieldchart_hop_python_sdktypecreate_fieldpy"></a>

Field data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Field`](./chart_hop_python_sdk/pydantic/field.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.get_all_paginated`<a id="charthopfieldget_all_paginated"></a>

Return all fields in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_paginated_response = charthop.field.get_all_paginated(
    org_id="orgId_example",
    _from="string_example",
    limit=1,
    ids="string_example",
    table="string_example",
    table_type="string_example",
    form="string_example",
    builtin="string_example",
    include_ttst=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

Field id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### ids: `str`<a id="ids-str"></a>

Comma separated Field Ids to find

##### table: `str`<a id="table-str"></a>

Retrieve fields from a particular table (id or name); if not passed, returns non-table fields

##### table_type: `str`<a id="table_type-str"></a>

Retrieve fields from a particular table type; ignored if table not passed

##### form: `str`<a id="form-str"></a>

Retrieve fields relating to a particular form

##### builtin: `str`<a id="builtin-str"></a>

Include built-in (builtin), custom (custom) or all fields - defaults to custom

##### include_ttst: `bool`<a id="include_ttst-bool"></a>

Include custom ttst fields - defaults to false

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsField`](./chart_hop_python_sdk/pydantic/results_field.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.get_built_in_fields`<a id="charthopfieldget_built_in_fields"></a>

Get built-in fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_built_in_fields_response = charthop.field.get_built_in_fields(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsPartialField`](./chart_hop_python_sdk/pydantic/results_partial_field.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/built-in` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.get_by_id`<a id="charthopfieldget_by_id"></a>

Return a particular field by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.field.get_by_id(
    org_id="orgId_example",
    field_id="fieldId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### field_id: `str`<a id="field_id-str"></a>

Field id

#### 🔄 Return<a id="🔄-return"></a>

[`Field`](./chart_hop_python_sdk/pydantic/field.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/{fieldId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.get_fields_in_category`<a id="charthopfieldget_fields_in_category"></a>

Return fields in a particular category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fields_in_category_response = charthop.field.get_fields_in_category(
    org_id="orgId_example",
    category_id="categoryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### category_id: `str`<a id="category_id-str"></a>

Category id

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsField`](./chart_hop_python_sdk/pydantic/results_field.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/category/{categoryId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.get_uncategorized_fields`<a id="charthopfieldget_uncategorized_fields"></a>

Return uncategorized fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_uncategorized_fields_response = charthop.field.get_uncategorized_fields(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsField`](./chart_hop_python_sdk/pydantic/results_field.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/category` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.remove`<a id="charthopfieldremove"></a>

Delete fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.field.remove(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`FieldRemoveRequest`](./chart_hop_python_sdk/type/field_remove_request.py)<a id="requestbody-fieldremoverequestchart_hop_python_sdktypefield_remove_requestpy"></a>

Field ids

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/delete` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.remove_by_id`<a id="charthopfieldremove_by_id"></a>

Delete a field

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.field.remove_by_id(
    org_id="orgId_example",
    field_id="fieldId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### field_id: `str`<a id="field_id-str"></a>

Field id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/{fieldId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.remove_field_overrides`<a id="charthopfieldremove_field_overrides"></a>

Remove overrides from fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.field.remove_field_overrides(
    field_ids=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_ids: [`FieldRemoveOverrideRequestFieldIds`](./chart_hop_python_sdk/type/field_remove_override_request_field_ids.py)<a id="field_ids-fieldremoveoverriderequestfieldidschart_hop_python_sdktypefield_remove_override_request_field_idspy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FieldRemoveOverrideRequest`](./chart_hop_python_sdk/type/field_remove_override_request.py)
Fields for which to remove overrides

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/remove-overrides` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.remove_from_categories`<a id="charthopfieldremove_from_categories"></a>

Remove field from all associated categories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.field.remove_from_categories(
    field_ids=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_ids: [`FieldRemoveCategoryRequestFieldIds`](./chart_hop_python_sdk/type/field_remove_category_request_field_ids.py)<a id="field_ids-fieldremovecategoryrequestfieldidschart_hop_python_sdktypefield_remove_category_request_field_idspy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FieldRemoveCategoryRequest`](./chart_hop_python_sdk/type/field_remove_category_request.py)
Fields to set as uncategorized

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/remove-category` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.update_existing_field`<a id="charthopfieldupdate_existing_field"></a>

Update an existing field

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.field.update_existing_field(
    org_id="orgId_example",
    field_id="fieldId_example",
    description="This field tracks the most recent performance rating for an individual.",
    name="summary",
    label="Job Summary",
    question="What do you think of this placeholder question?",
    in_use=True,
    expr="(base + variable) / 12",
    expr_type="ADDRESS",
    type="ADDRESS",
    plural="SINGLE",
    values=[
        {
            "name": "name_example",
            "label": "label_example",
        }
    ],
    default_value={},
    options={},
    sensitive="GLOBAL",
    hide_expr=True,
    expire_days=1,
    status="ACTIVE",
    table_ref={
        "table_id": "table_id_example",
        "table_name": "table_name_example",
    },
    is_unique=True,
    is_required=True,
    is_effective_dated=True,
    data_fetch_types=[
        "string_example"
    ],
    aliases=[
        "string_example"
    ],
    calc="ADDRESS",
    category_id="string_example",
    classification="COMPOUND",
    places=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### field_id: `str`<a id="field_id-str"></a>

Field id

##### description: `str`<a id="description-str"></a>

description of field

##### name: `str`<a id="name-str"></a>

short field name

##### label: `str`<a id="label-str"></a>

human-readable full name of field

##### question: `str`<a id="question-str"></a>

human-readable question associated with field

##### in_use: `bool`<a id="in_use-bool"></a>

disallow any updates to this Field (except for field.question string)

##### expr: `str`<a id="expr-str"></a>

calculated expression

##### expr_type: `str`<a id="expr_type-str"></a>

the expected type of the evaluated expression

##### type: `str`<a id="type-str"></a>

type of field

##### plural: `str`<a id="plural-str"></a>

plural type of the field (either SINGLE, LIST, or SET)

##### values: List[`EnumValue`]<a id="values-listenumvalue"></a>

possible values (enum type only)

##### default_value: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="default_value-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

default value if field is not set

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

validation options

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level of data

##### hide_expr: `bool`<a id="hide_expr-bool"></a>

hide expression-derived values from non-sensitive users

##### expire_days: `int`<a id="expire_days-int"></a>

number of days after which the data becomes invalid

##### status: `str`<a id="status-str"></a>

the status of the field

##### table_ref: [`TableRef`](./chart_hop_python_sdk/type/table_ref.py)<a id="table_ref-tablerefchart_hop_python_sdktypetable_refpy"></a>


##### is_unique: `bool`<a id="is_unique-bool"></a>

indicates that this field value is unique in conjunction with entityType PERSON or JOB

##### is_required: `bool`<a id="is_required-bool"></a>

indicates that this field value is required

##### is_effective_dated: `bool`<a id="is_effective_dated-bool"></a>

indicates that this field value is effective-dated

##### data_fetch_types: [`UpdateFieldDataFetchTypes`](./chart_hop_python_sdk/type/update_field_data_fetch_types.py)<a id="data_fetch_types-updatefielddatafetchtypeschart_hop_python_sdktypeupdate_field_data_fetch_typespy"></a>

##### aliases: [`UpdateFieldAliases`](./chart_hop_python_sdk/type/update_field_aliases.py)<a id="aliases-updatefieldaliaseschart_hop_python_sdktypeupdate_field_aliasespy"></a>

##### calc: `str`<a id="calc-str"></a>

unique ID for the function that runs to calculate the value of this field. For native fields only

##### category_id: `str`<a id="category_id-str"></a>

ID of the category to which this field belongs, if any

##### classification: `str`<a id="classification-str"></a>

indicates how this field is calculated (whether it's stored in the DB, evaluated through the expression service, or compound)

##### places: `int`<a id="places-int"></a>

number of decimal places for money values

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateField`](./chart_hop_python_sdk/type/update_field.py)
Field data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/{fieldId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.update_field_dry_run`<a id="charthopfieldupdate_field_dry_run"></a>

Perform a dry-run of an update to an existing field that will require migrations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.field.update_field_dry_run(
    org_id="orgId_example",
    field_id="fieldId_example",
    description="This field tracks the most recent performance rating for an individual.",
    name="summary",
    label="Job Summary",
    question="What do you think of this placeholder question?",
    in_use=True,
    expr="(base + variable) / 12",
    expr_type="ADDRESS",
    type="ADDRESS",
    plural="SINGLE",
    values=[
        {
            "name": "name_example",
            "label": "label_example",
        }
    ],
    default_value={},
    options={},
    sensitive="GLOBAL",
    hide_expr=True,
    expire_days=1,
    status="ACTIVE",
    table_ref={
        "table_id": "table_id_example",
        "table_name": "table_name_example",
    },
    is_unique=True,
    is_required=True,
    is_effective_dated=True,
    data_fetch_types=[
        "string_example"
    ],
    aliases=[
        "string_example"
    ],
    calc="ADDRESS",
    category_id="string_example",
    classification="COMPOUND",
    places=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### field_id: `str`<a id="field_id-str"></a>

Field id

##### description: `str`<a id="description-str"></a>

description of field

##### name: `str`<a id="name-str"></a>

short field name

##### label: `str`<a id="label-str"></a>

human-readable full name of field

##### question: `str`<a id="question-str"></a>

human-readable question associated with field

##### in_use: `bool`<a id="in_use-bool"></a>

disallow any updates to this Field (except for field.question string)

##### expr: `str`<a id="expr-str"></a>

calculated expression

##### expr_type: `str`<a id="expr_type-str"></a>

the expected type of the evaluated expression

##### type: `str`<a id="type-str"></a>

type of field

##### plural: `str`<a id="plural-str"></a>

plural type of the field (either SINGLE, LIST, or SET)

##### values: List[`EnumValue`]<a id="values-listenumvalue"></a>

possible values (enum type only)

##### default_value: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="default_value-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

default value if field is not set

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

validation options

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level of data

##### hide_expr: `bool`<a id="hide_expr-bool"></a>

hide expression-derived values from non-sensitive users

##### expire_days: `int`<a id="expire_days-int"></a>

number of days after which the data becomes invalid

##### status: `str`<a id="status-str"></a>

the status of the field

##### table_ref: [`TableRef`](./chart_hop_python_sdk/type/table_ref.py)<a id="table_ref-tablerefchart_hop_python_sdktypetable_refpy"></a>


##### is_unique: `bool`<a id="is_unique-bool"></a>

indicates that this field value is unique in conjunction with entityType PERSON or JOB

##### is_required: `bool`<a id="is_required-bool"></a>

indicates that this field value is required

##### is_effective_dated: `bool`<a id="is_effective_dated-bool"></a>

indicates that this field value is effective-dated

##### data_fetch_types: [`UpdateFieldDataFetchTypes`](./chart_hop_python_sdk/type/update_field_data_fetch_types.py)<a id="data_fetch_types-updatefielddatafetchtypeschart_hop_python_sdktypeupdate_field_data_fetch_typespy"></a>

##### aliases: [`UpdateFieldAliases`](./chart_hop_python_sdk/type/update_field_aliases.py)<a id="aliases-updatefieldaliaseschart_hop_python_sdktypeupdate_field_aliasespy"></a>

##### calc: `str`<a id="calc-str"></a>

unique ID for the function that runs to calculate the value of this field. For native fields only

##### category_id: `str`<a id="category_id-str"></a>

ID of the category to which this field belongs, if any

##### classification: `str`<a id="classification-str"></a>

indicates how this field is calculated (whether it's stored in the DB, evaluated through the expression service, or compound)

##### places: `int`<a id="places-int"></a>

number of decimal places for money values

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateField`](./chart_hop_python_sdk/type/update_field.py)
Field data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/{fieldId}/dryrun` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.field.update_status_for_existing_fields`<a id="charthopfieldupdate_status_for_existing_fields"></a>

Update status for existing fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.field.update_status_for_existing_fields(
    update_status="ACTIVE",
    field_ids=[
        "string_example"
    ],
    reserved_field_names=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### update_status: `str`<a id="update_status-str"></a>

New status to update

##### field_ids: [`FieldStatusUpdateRequestFieldIds`](./chart_hop_python_sdk/type/field_status_update_request_field_ids.py)<a id="field_ids-fieldstatusupdaterequestfieldidschart_hop_python_sdktypefield_status_update_request_field_idspy"></a>

##### reserved_field_names: [`FieldStatusUpdateRequestReservedFieldNames`](./chart_hop_python_sdk/type/field_status_update_request_reserved_field_names.py)<a id="reserved_field_names-fieldstatusupdaterequestreservedfieldnameschart_hop_python_sdktypefield_status_update_request_reserved_field_namespy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FieldStatusUpdateRequest`](./chart_hop_python_sdk/type/field_status_update_request.py)
Field data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/field/status` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.file.get_metadata`<a id="charthopfileget_metadata"></a>

Returns metadata about a file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metadata_response = charthop.file.get_metadata(
    org_id="orgId_example",
    entity_id="string_example",
    entity_type="string_example",
    limit=1,
    _from="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### entity_id: `str`<a id="entity_id-str"></a>

Entity id

##### entity_type: `str`<a id="entity_type-str"></a>

Entity type

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### _from: `str`<a id="_from-str"></a>

From result id

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsFileEntity`](./chart_hop_python_sdk/pydantic/results_file_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/file` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.file.get_metadata_0`<a id="charthopfileget_metadata_0"></a>

Returns metadata about a file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metadata_0_response = charthop.file.get_metadata_0(
    org_id="orgId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file_id: `str`<a id="file_id-str"></a>

File id

#### 🔄 Return<a id="🔄-return"></a>

[`FileEntity`](./chart_hop_python_sdk/pydantic/file_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/file/{fileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.file.get_metadata_by_id`<a id="charthopfileget_metadata_by_id"></a>

Download a file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.file.get_metadata_by_id(
    org_id="orgId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file_id: `str`<a id="file_id-str"></a>

File id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/file/{fileId}/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.file.remove_file_by_id`<a id="charthopfileremove_file_by_id"></a>

Delete a file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.file.remove_file_by_id(
    org_id="orgId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file_id: `str`<a id="file_id-str"></a>

File id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/file/{fileId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.file.upload_new_file`<a id="charthopfileupload_new_file"></a>

Upload a new file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_new_file_response = charthop.file.upload_new_file(
    org_id="orgId_example",
    file=open('/path/to/file', 'rb'),
    entity_id="string_example",
    entity_type="string_example",
    field="string_example",
    sensitive="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file: `IO`<a id="file-io"></a>

##### entity_id: `str`<a id="entity_id-str"></a>

entity id (if not passed, defaults to user id)

##### entity_type: `str`<a id="entity_type-str"></a>

entity type (if not passed, defaults to user)

##### field: `str`<a id="field-str"></a>

field name - can leave blank for a general upload

##### sensitive: `str`<a id="sensitive-str"></a>

file sensitivity level - defaults to PERSONAL

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileEntity`](./chart_hop_python_sdk/pydantic/file_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/file` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.create_new_form`<a id="charthopformcreate_new_form"></a>

Create a form

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_form_response = charthop.form.create_new_form(
    label="Health Index: Q2",
    fields=[
        {
            "field_id": "field_id_example",
            "label": "label_example",
            "required": True,
            "long_label": True,
        }
    ],
    blocks=[
        {
            "type": "QUESTION",
        }
    ],
    status="ACTIVE",
    org_id="orgId_example",
    description="The Engineering department, where engineers develop new technology and products.",
    type="BUILT_IN",
    target_type="NONE",
    target_filter="string_example",
    submit_filter="string_example",
    response_read_filter="string_example",
    use_field_access=True,
    approval="MANAGER",
    author_sensitive="ANONYMOUS",
    options={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

human-readable full name of form

##### fields: List[`FormField`]<a id="fields-listformfield"></a>

ordered list of fields being collected in this form

##### blocks: List[`FormBlock`]<a id="blocks-listformblock"></a>

ordered list of blocks being collected in this form

##### status: `str`<a id="status-str"></a>

status of the form

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### description: `str`<a id="description-str"></a>

description of form

##### type: `str`<a id="type-str"></a>

type of the form

##### target_type: `str`<a id="target_type-str"></a>

target type that the form can be filled out about (null defaults to PERSON for backwards compatibility)

##### target_filter: `str`<a id="target_filter-str"></a>

filter that controls on which profiles this tab will appear

##### submit_filter: `str`<a id="submit_filter-str"></a>

filter that controls which respondents can submit this form. The form:submit permission, if present, overrides this filter

##### response_read_filter: `str`<a id="response_read_filter-str"></a>

filter that controls who can read the form responses. The formResponse:read permission, if present, overrides this filter

##### use_field_access: `bool`<a id="use_field_access-bool"></a>

if this option is on, then form response answers will use field permissions to determine access to those responses

##### approval: `str`<a id="approval-str"></a>

approval needed, if any approval is required

##### author_sensitive: `str`<a id="author_sensitive-str"></a>

view sensitivity for the author of this form - the level of view access required to view the createId and updateId fields. If null, the author's identity is always visible as long as the viewer can read the form response. If set to PRIVATE, the author's identity is stored in ChartHop, but protected such that even users with sensitive access cannot access the data. If set to ANONYMOUS, the author's identity is not stored in ChartHop at all.

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

options, such as notification settings

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateForm`](./chart_hop_python_sdk/type/create_form.py)
Form data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./chart_hop_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.delete_form_by_id`<a id="charthopformdelete_form_by_id"></a>

Delete a form

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form.delete_form_by_id(
    org_id="orgId_example",
    form_id="formId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.delete_form_by_id_0`<a id="charthopformdelete_form_by_id_0"></a>

Delete forms

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form.delete_form_by_id_0(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`FormDeleteFormByIdRequest`](./chart_hop_python_sdk/type/form_delete_form_by_id_request.py)<a id="requestbody-formdeleteformbyidrequestchart_hop_python_sdktypeform_delete_form_by_id_requestpy"></a>

Form ids

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/delete` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.delete_form_draft`<a id="charthopformdelete_form_draft"></a>

Delete the given form draft

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_form_draft_response = charthop.form.delete_form_draft(
    org_id="orgId_example",
    draft_id="draftId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### draft_id: `str`<a id="draft_id-str"></a>

Form Draft id

#### 🔄 Return<a id="🔄-return"></a>

[`FormDraft`](./chart_hop_python_sdk/pydantic/form_draft.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/draft/{draftId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.get_applicable_forms_for_person`<a id="charthopformget_applicable_forms_for_person"></a>

Return all active forms applicable to a particular person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_applicable_forms_for_person_response = charthop.form.get_applicable_forms_for_person(
    org_id="orgId_example",
    person_id="personId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### person_id: `str`<a id="person_id-str"></a>

Person id

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsForm`](./chart_hop_python_sdk/pydantic/results_form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/person/{personId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.get_by_id`<a id="charthopformget_by_id"></a>

Return a particular form by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.form.get_by_id(
    org_id="orgId_example",
    form_id="formId_example",
    eval_job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### eval_job_id: `str`<a id="eval_job_id-str"></a>

Evaluate any expressions inside the form relative to a particular job

#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./chart_hop_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.get_current_state_of_draft_data`<a id="charthopformget_current_state_of_draft_data"></a>

Get the current state of form draft data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_state_of_draft_data_response = charthop.form.get_current_state_of_draft_data(
    org_id="orgId_example",
    form_id="formId_example",
    person_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### person_id: `str`<a id="person_id-str"></a>

Person id

#### 🔄 Return<a id="🔄-return"></a>

[`FormDraft`](./chart_hop_python_sdk/pydantic/form_draft.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}/draft` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.list_available_forms`<a id="charthopformlist_available_forms"></a>

Return all active forms applicable to a particular entity

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_available_forms_response = charthop.form.list_available_forms(
    org_id="orgId_example",
    target_id="string_example",
    target_type="NONE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### target_id: `str`<a id="target_id-str"></a>

Target id

##### target_type: `str`<a id="target_type-str"></a>

Target type

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsFormSummary`](./chart_hop_python_sdk/pydantic/results_form_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/available` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.list_org_forms`<a id="charthopformlist_org_forms"></a>

Return all forms in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_org_forms_response = charthop.form.list_org_forms(
    org_id="orgId_example",
    status="ACTIVE",
    _from="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### status: `str`<a id="status-str"></a>

Status to filter by

##### _from: `str`<a id="_from-str"></a>

Form id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsForm`](./chart_hop_python_sdk/pydantic/results_form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.render_for_display`<a id="charthopformrender_for_display"></a>

Render a form for display

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
render_for_display_response = charthop.form.render_for_display(
    org_id="orgId_example",
    form_id="formId_example",
    target_id="string_example",
    target_type="NONE",
    form_response_id="string_example",
    form_response_change_id="string_example",
    form_version_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### target_id: `str`<a id="target_id-str"></a>

Target id

##### target_type: `str`<a id="target_type-str"></a>

Target type

##### form_response_id: `str`<a id="form_response_id-str"></a>

Form response id, if editing a prior form response (unsupported)

##### form_response_change_id: `str`<a id="form_response_change_id-str"></a>

Form response change id, if editing a prior form response (deprecated)

##### form_version_id: `str`<a id="form_version_id-str"></a>

Form version id, if rendering a previous version of the form

#### 🔄 Return<a id="🔄-return"></a>

[`FormRender`](./chart_hop_python_sdk/pydantic/form_render.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}/render` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.rerender_question_update`<a id="charthopformrerender_question_update"></a>

Re-render form blocks based on changes to the form values

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rerender_question_update_response = charthop.form.rerender_question_update(
    org_id="orgId_example",
    form_id="formId_example",
    update_question_id="updateQuestionId_example",
    target_id="string_example",
    target_type="NONE",
    form_version_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### update_question_id: `str`<a id="update_question_id-str"></a>

The question id that is being updated to trigger the re-render

##### target_id: `str`<a id="target_id-str"></a>

Target id

##### target_type: `str`<a id="target_type-str"></a>

Target type

##### form_version_id: `str`<a id="form_version_id-str"></a>

Form version id, if rendering a previous version of the form

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormSubmitFormDraftRequest`](./chart_hop_python_sdk/type/form_submit_form_draft_request.py)
Form data to submit

#### 🔄 Return<a id="🔄-return"></a>

[`FormRerender`](./chart_hop_python_sdk/pydantic/form_rerender.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}/rerender/question/{updateQuestionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.send_emails_and_chat_notifications`<a id="charthopformsend_emails_and_chat_notifications"></a>

Collect data for an existing form, sending emails and chat notifications to people being requested

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_emails_and_chat_notifications_response = charthop.form.send_emails_and_chat_notifications(
    preview=True,
    org_id="orgId_example",
    form_id="formId_example",
    assessment_id="string_example",
    target_filter="string_example",
    submit_filter="string_example",
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### preview: `bool`<a id="preview-bool"></a>

Is this a preview?

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### assessment_id: `str`<a id="assessment_id-str"></a>

the assessment id that this form collection request aligns to (for example a performance review cycle)

##### target_filter: `str`<a id="target_filter-str"></a>

filter query to apply on who should receive the form collection request

##### submit_filter: `str`<a id="submit_filter-str"></a>

Filter to for jobs/person that match via relationship

##### message: `str`<a id="message-str"></a>

message to include in notification

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormCollectRequest`](./chart_hop_python_sdk/type/form_collect_request.py)
Details on the data collection

#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./chart_hop_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}/collect` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.send_reminder_notification`<a id="charthopformsend_reminder_notification"></a>

Sends reminder for a form with existing tasks, sending emails/chat notifications to people being requested

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_reminder_notification_response = charthop.form.send_reminder_notification(
    preview=True,
    org_id="orgId_example",
    form_id="formId_example",
    assessment_id="string_example",
    target_filter="string_example",
    submit_filter="string_example",
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### preview: `bool`<a id="preview-bool"></a>

Is this a preview?

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### assessment_id: `str`<a id="assessment_id-str"></a>

the assessment id that this form collection request aligns to (for example a performance review cycle)

##### target_filter: `str`<a id="target_filter-str"></a>

filter query to apply on who should receive the form collection request

##### submit_filter: `str`<a id="submit_filter-str"></a>

Filter to for jobs/person that match via relationship

##### message: `str`<a id="message-str"></a>

message to include in notification

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormCollectRequest`](./chart_hop_python_sdk/type/form_collect_request.py)
Details on the data collection

#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./chart_hop_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}/remind` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.submit_draft_data`<a id="charthopformsubmit_draft_data"></a>

Submit draft data from a form

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_draft_data_response = charthop.form.submit_draft_data(
    person_id="string_example",
    data={
        "key": {},
    },
    org_id="orgId_example",
    form_id="formId_example",
    blocks_data={
        "key": {},
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

person data is being filled out on behalf of

##### data: [`FormSubmitRequestData`](./chart_hop_python_sdk/type/form_submit_request_data.py)<a id="data-formsubmitrequestdatachart_hop_python_sdktypeform_submit_request_datapy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Org id

##### blocks_data: [`FormSubmitRequestBlocksData`](./chart_hop_python_sdk/type/form_submit_request_blocks_data.py)<a id="blocks_data-formsubmitrequestblocksdatachart_hop_python_sdktypeform_submit_request_blocks_datapy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormSubmitRequest`](./chart_hop_python_sdk/type/form_submit_request.py)
Form data to submit

#### 🔄 Return<a id="🔄-return"></a>

[`FormDraft`](./chart_hop_python_sdk/pydantic/form_draft.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}/draft` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.submit_form_data`<a id="charthopformsubmit_form_data"></a>

Submit data from a form

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form.submit_form_data(
    org_id="orgId_example",
    form_id="formId_example",
    target_id="string_example",
    target_type="NONE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### target_id: `str`<a id="target_id-str"></a>

Target id

##### target_type: `str`<a id="target_type-str"></a>

Target type

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormSubmitFormDraftRequest`](./chart_hop_python_sdk/type/form_submit_form_draft_request.py)
Form data to submit

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}/submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.submit_form_draft`<a id="charthopformsubmit_form_draft"></a>

Submit data from a form draft

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_form_draft_response = charthop.form.submit_form_draft(
    org_id="orgId_example",
    form_id="formId_example",
    target_id="string_example",
    target_type="NONE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### target_id: `str`<a id="target_id-str"></a>

Target id

##### target_type: `str`<a id="target_type-str"></a>

Target type

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormSubmitFormDraftRequest`](./chart_hop_python_sdk/type/form_submit_form_draft_request.py)
Form data to submit

#### 🔄 Return<a id="🔄-return"></a>

[`FormDraft`](./chart_hop_python_sdk/pydantic/form_draft.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}/submit/draft` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.submit_form_response`<a id="charthopformsubmit_form_response"></a>

Submit data from a form

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form.submit_form_response(
    person_id="string_example",
    data={
        "key": {},
    },
    org_id="orgId_example",
    form_id="formId_example",
    blocks_data={
        "key": {},
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

person data is being filled out on behalf of

##### data: [`FormSubmitRequestData`](./chart_hop_python_sdk/type/form_submit_request_data.py)<a id="data-formsubmitrequestdatachart_hop_python_sdktypeform_submit_request_datapy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Org id

##### blocks_data: [`FormSubmitRequestBlocksData`](./chart_hop_python_sdk/type/form_submit_request_blocks_data.py)<a id="blocks_data-formsubmitrequestblocksdatachart_hop_python_sdktypeform_submit_request_blocks_datapy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormSubmitRequest`](./chart_hop_python_sdk/type/form_submit_request.py)
Form data to submit

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.update_existing_form`<a id="charthopformupdate_existing_form"></a>

Update an existing form

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form.update_existing_form(
    org_id="orgId_example",
    form_id="formId_example",
    description="The Engineering department, where engineers develop new technology and products.",
    label="Health Index: Q2",
    fields=[
        {
            "field_id": "field_id_example",
            "label": "label_example",
            "required": True,
            "long_label": True,
        }
    ],
    blocks=[
        {
            "type": "QUESTION",
        }
    ],
    status="ACTIVE",
    type="BUILT_IN",
    target_type="NONE",
    target_filter="string_example",
    submit_filter="string_example",
    response_read_filter="string_example",
    use_field_access=True,
    approval="MANAGER",
    author_sensitive="ANONYMOUS",
    options={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id

##### description: `str`<a id="description-str"></a>

description of form

##### label: `str`<a id="label-str"></a>

human-readable full name of form

##### fields: List[`FormField`]<a id="fields-listformfield"></a>

ordered list of fields being collected in this form

##### blocks: List[`FormBlock`]<a id="blocks-listformblock"></a>

ordered list of blocks being collected in this form

##### status: `str`<a id="status-str"></a>

status of the form

##### type: `str`<a id="type-str"></a>

type of the form

##### target_type: `str`<a id="target_type-str"></a>

target type that the form can be filled out about (null defaults to PERSON for backwards compatibility)

##### target_filter: `str`<a id="target_filter-str"></a>

filter that controls on which profiles this tab will appear

##### submit_filter: `str`<a id="submit_filter-str"></a>

filter that controls which respondents can submit this form. The form:submit permission, if present, overrides this filter

##### response_read_filter: `str`<a id="response_read_filter-str"></a>

filter that controls who can read the form responses. The formResponse:read permission, if present, overrides this filter

##### use_field_access: `bool`<a id="use_field_access-bool"></a>

if this option is on, then form response answers will use field permissions to determine access to those responses

##### approval: `str`<a id="approval-str"></a>

approval needed, if any approval is required

##### author_sensitive: `str`<a id="author_sensitive-str"></a>

view sensitivity for the author of this form - the level of view access required to view the createId and updateId fields. If null, the author's identity is always visible as long as the viewer can read the form response. If set to PRIVATE, the author's identity is stored in ChartHop, but protected such that even users with sensitive access cannot access the data. If set to ANONYMOUS, the author's identity is not stored in ChartHop at all.

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

options, such as notification settings

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateForm`](./chart_hop_python_sdk/type/update_form.py)
Form data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/{formId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form.update_form_status`<a id="charthopformupdate_form_status"></a>

Update status for existing forms

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form.update_form_status(
    update_status="ACTIVE",
    form_ids=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### update_status: `str`<a id="update_status-str"></a>

New status to update

##### form_ids: [`FormStatusUpdateRequestFormIds`](./chart_hop_python_sdk/type/form_status_update_request_form_ids.py)<a id="form_ids-formstatusupdaterequestformidschart_hop_python_sdktypeform_status_update_request_form_idspy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormStatusUpdateRequest`](./chart_hop_python_sdk/type/form_status_update_request.py)
Form data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form/status` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form_response.get_by_form`<a id="charthopform_responseget_by_form"></a>

Return form responses by form

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form_response.get_by_form(
    org_id="orgId_example",
    form_id="string_example",
    assessment_id="string_example",
    submit_person_id="string_example",
    target_id="string_example",
    _from="string_example",
    limit=1,
    return_access="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id to filter by

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id to filter by

##### submit_person_id: `str`<a id="submit_person_id-str"></a>

Person id to filter by (person who submitted the form)

##### target_id: `str`<a id="target_id-str"></a>

Target id to filter by

##### _from: `str`<a id="_from-str"></a>

FormResponse id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form-response` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form_response.get_by_id`<a id="charthopform_responseget_by_id"></a>

Return a particular form response by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.form_response.get_by_id(
    org_id="orgId_example",
    form_response_id="formResponseId_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_response_id: `str`<a id="form_response_id-str"></a>

FormResponse id

##### format: `str`<a id="format-str"></a>

Data format to use for answers; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`FormResponse`](./chart_hop_python_sdk/pydantic/form_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form-response/{formResponseId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form_response.get_form_response_count`<a id="charthopform_responseget_form_response_count"></a>

Return the total count of form responses by form

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_form_response_count_response = charthop.form_response.get_form_response_count(
    org_id="orgId_example",
    form_id="string_example",
    assessment_id="string_example",
    submit_person_id="string_example",
    target_id="string_example",
    question_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_id: `str`<a id="form_id-str"></a>

Form id to filter by

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id to filter by

##### submit_person_id: `str`<a id="submit_person_id-str"></a>

Person id to filter by (person who submitted the form)

##### target_id: `str`<a id="target_id-str"></a>

Target id to filter by

##### question_id: `str`<a id="question_id-str"></a>

Question id to filter by

#### 🔄 Return<a id="🔄-return"></a>

[`FormResponseCount`](./chart_hop_python_sdk/pydantic/form_response_count.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form-response/count` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form_response.remove_by_id`<a id="charthopform_responseremove_by_id"></a>

Delete a form response

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form_response.remove_by_id(
    org_id="orgId_example",
    form_response_id="formResponseId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_response_id: `str`<a id="form_response_id-str"></a>

FormResponse id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form-response/{formResponseId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form_response.update_answers_metadata`<a id="charthopform_responseupdate_answers_metadata"></a>

Re-submit (update) an existing form response's answers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form_response.update_answers_metadata(
    org_id="orgId_example",
    form_response_id="formResponseId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_response_id: `str`<a id="form_response_id-str"></a>

FormResponse id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormresponseUpdateAnswersMetadataRequest`](./chart_hop_python_sdk/type/formresponse_update_answers_metadata_request.py)
FormResponse data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form-response/{formResponseId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.form_response.update_metadata`<a id="charthopform_responseupdate_metadata"></a>

Update an existing form response's metadata, such as shareAccess information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.form_response.update_metadata(
    org_id="orgId_example",
    form_response_id="formResponseId_example",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### form_response_id: `str`<a id="form_response_id-str"></a>

FormResponse id

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

list of share access, if the form response has been shared with anyone

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateFormResponse`](./chart_hop_python_sdk/type/update_form_response.py)
FormResponse data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/form-response/{formResponseId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.create_new_group`<a id="charthopgroupcreate_new_group"></a>

Create a group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.group.create_new_group(
    org_id="orgId_example",
    type="type_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Group type

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to create the group in

##### date: `date`<a id="date-date"></a>

Effective date of group creation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/{type}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.find_in_org_of_type`<a id="charthopgroupfind_in_org_of_type"></a>

Find groups in the organization of a certain type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_in_org_of_type_response = charthop.group.find_in_org_of_type(
    org_id="orgId_example",
    start="string_example",
    depth=1,
    group_approx_limit=1,
    job_limit=1,
    scenario_id="string_example",
    job_filter="string_example",
    group_filter="string_example",
    date="1970-01-01",
    group_fields="string_example",
    job_fields="string_example",
    position_fields="string_example",
    kind="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### start: `str`<a id="start-str"></a>

group id to use as the starting point

##### depth: `int`<a id="depth-int"></a>

number of levels down

##### group_approx_limit: `int`<a id="group_approx_limit-int"></a>

limit number of groups

##### job_limit: `int`<a id="job_limit-int"></a>

limit number of jobs

##### scenario_id: `str`<a id="scenario_id-str"></a>

scenario id to query

##### job_filter: `str`<a id="job_filter-str"></a>

query string to filter jobs by

##### group_filter: `str`<a id="group_filter-str"></a>

query string to filter group by

##### date: `date`<a id="date-date"></a>

date to search as of

##### group_fields: `str`<a id="group_fields-str"></a>

group fields to return

##### job_fields: `str`<a id="job_fields-str"></a>

job/person fields to return

##### position_fields: `str`<a id="position_fields-str"></a>

position fields to return

##### kind: `str`<a id="kind-str"></a>

kind of group to query (legacy/tracked)

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`GroupGraphResults`](./chart_hop_python_sdk/pydantic/group_graph_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/graph` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.find_of_type`<a id="charthopgroupfind_of_type"></a>

Find groups in the organization of a certain type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_of_type_response = charthop.group.find_of_type(
    org_id="orgId_example",
    type="type_example",
    scenario_id="string_example",
    date="1970-01-01",
    _from="string_example",
    limit=1,
    fields="string_example",
    job_fields="string_example",
    position_fields="string_example",
    include_all=True,
    search="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Group type

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date to search as of

##### _from: `str`<a id="_from-str"></a>

Group id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### job_fields: `str`<a id="job_fields-str"></a>

job fields to return, comma-separated

##### position_fields: `str`<a id="position_fields-str"></a>

position fields to return, comma-separated

##### include_all: `bool`<a id="include_all-bool"></a>

Include all groups, including deleted groups

##### search: `str`<a id="search-str"></a>

Search string to filter on code & name

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.find_orphaned_groups`<a id="charthopgroupfind_orphaned_groups"></a>

Find groups in the organization that have no child groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_orphaned_groups_response = charthop.group.find_orphaned_groups(
    org_id="orgId_example",
    start="string_example",
    group_limit=1,
    job_limit=1,
    scenario_id="string_example",
    job_filter="string_example",
    group_filter="string_example",
    date="1970-01-01",
    group_fields="string_example",
    job_fields="string_example",
    position_fields="string_example",
    kind="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### start: `str`<a id="start-str"></a>

group id to use as the starting point

##### group_limit: `int`<a id="group_limit-int"></a>

limit number of groups

##### job_limit: `int`<a id="job_limit-int"></a>

limit number of jobs

##### scenario_id: `str`<a id="scenario_id-str"></a>

scenario id to query

##### job_filter: `str`<a id="job_filter-str"></a>

query string to filter jobs by

##### group_filter: `str`<a id="group_filter-str"></a>

query string to filter group by

##### date: `date`<a id="date-date"></a>

date to search as of

##### group_fields: `str`<a id="group_fields-str"></a>

group fields to return

##### job_fields: `str`<a id="job_fields-str"></a>

job/person fields to return

##### position_fields: `str`<a id="position_fields-str"></a>

position fields to return

##### kind: `str`<a id="kind-str"></a>

kind of group to query (legacy/tracked)

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`GroupGraphResults`](./chart_hop_python_sdk/pydantic/group_graph_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/orphaned` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.get_by_id`<a id="charthopgroupget_by_id"></a>

Return a particular group by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.group.get_by_id(
    org_id="orgId_example",
    type="type_example",
    group_id="groupId_example",
    scenario_id="string_example",
    date="1970-01-01",
    fields="string_example",
    job_fields="string_example",
    position_fields="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Group type

##### group_id: `str`<a id="group_id-str"></a>

Group identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### job_fields: `str`<a id="job_fields-str"></a>

job fields to return, comma-separated

##### position_fields: `str`<a id="position_fields-str"></a>

position fields to return, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`GroupGetByIdResponse`](./chart_hop_python_sdk/pydantic/group_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/{type}/{groupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.get_organized_group_counts`<a id="charthopgroupget_organized_group_counts"></a>

Get organized group counts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_organized_group_counts_response = charthop.group.get_organized_group_counts(
    org_id="orgId_example",
    scenario_id="string_example",
    group_filter="string_example",
    date="1970-01-01",
    kind="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

scenario id to query

##### group_filter: `str`<a id="group_filter-str"></a>

query string to filter group by

##### date: `date`<a id="date-date"></a>

date to search as of

##### kind: `str`<a id="kind-str"></a>

kind of group to query (legacy/tracked)

#### 🔄 Return<a id="🔄-return"></a>

[`GroupCount`](./chart_hop_python_sdk/pydantic/group_count.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/count` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.import_csv_data`<a id="charthopgroupimport_csv_data"></a>

Import data from CSV file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_csv_data_response = charthop.group.import_csv_data(
    org_id="orgId_example",
    type="type_example",
    file=open('/path/to/file', 'rb'),
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Group type

##### file: `IO`<a id="file-io"></a>

##### date: `date`<a id="date-date"></a>

Date to update as of

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/{type}/import` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.mark_multiple_as_deleted`<a id="charthopgroupmark_multiple_as_deleted"></a>

Mark multiple groups as deleted

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mark_multiple_as_deleted_response = charthop.group.mark_multiple_as_deleted(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
    type="type_example",
    scenario_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Group type

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update the group in

##### requestBody: [`GroupMarkMultipleAsDeletedRequest`](./chart_hop_python_sdk/type/group_mark_multiple_as_deleted_request.py)<a id="requestbody-groupmarkmultipleasdeletedrequestchart_hop_python_sdktypegroup_mark_multiple_as_deleted_requestpy"></a>

Group ids of groups to bulk delete

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/{type}/bulk-delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.remove_by_group_id`<a id="charthopgroupremove_by_group_id"></a>

Delete a group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.group.remove_by_group_id(
    org_id="orgId_example",
    type="type_example",
    group_id="groupId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Group type

##### group_id: `str`<a id="group_id-str"></a>

Group id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update the group in

##### date: `date`<a id="date-date"></a>

Date to update as of

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/{type}/{groupId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.group.update_group_details`<a id="charthopgroupupdate_group_details"></a>

Update a group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.group.update_group_details(
    org_id="orgId_example",
    type="type_example",
    group_id="groupId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Group type

##### group_id: `str`<a id="group_id-str"></a>

Group id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update the group in

##### date: `date`<a id="date-date"></a>

Effective date of group update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/group/{type}/{groupId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.guideline.all_for_comp_review`<a id="charthopguidelineall_for_comp_review"></a>

Get all guidelines for a given comp review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
all_for_comp_review_response = charthop.guideline.all_for_comp_review(
    org_id="orgId_example",
    comp_review_id="string_example",
    include_deleted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

comp review id

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

include deleted guidelines

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsGuideline`](./chart_hop_python_sdk/pydantic/results_guideline.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/guideline` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.guideline.calculate_matrix_values_for_specific_guideline`<a id="charthopguidelinecalculate_matrix_values_for_specific_guideline"></a>

Calculate the matrix values for a specific guideline (which may apply to multiple scenarios in the comp review)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calculate_matrix_values_for_specific_guideline_response = charthop.guideline.calculate_matrix_values_for_specific_guideline(
    org_id="orgId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### id: `str`<a id="id-str"></a>

ID of the desired guideline

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsGuidelineCalculation`](./chart_hop_python_sdk/pydantic/results_guideline_calculation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/guideline/{id}/calculate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.guideline.create_new_guideline`<a id="charthopguidelinecreate_new_guideline"></a>

Create a new guideline

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.guideline.create_new_guideline(
    comp_review_id="588f7ee98f138b19220041a7",
    label="Merit Guideline",
    applied_field='base' or 'grantShares',
    source_field='base' or 'grantShares',
    calculation_type="TARGET",
    flag_mode="NONE",
    enable_populate_value=False,
    basis_type="CUSTOM",
    org_id="orgId_example",
    budget_pool_id="588f7ee98f138b19220041a7",
    participants_expr="is:person and tenure>=12",
    flag_deviation_threshold=0.75,
    basis_expr="tenure>12 ? (base * 0.04) : (base * 0.02)",
    basis_field_matrix={
        "included_fields": [
            "included_fields_example"
        ],
        "conditions": [
            {
                "condition_expr": "condition_expr_example",
            }
        ],
    },
    fixed_amount_range={
    },
    fixed_value_range={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

comp review id

##### label: `str`<a id="label-str"></a>

guideline name

##### applied_field: `str`<a id="applied_field-str"></a>

the field the guideline applies to

##### source_field: `str`<a id="source_field-str"></a>

the field the guideline is calculated from

##### calculation_type: `str`<a id="calculation_type-str"></a>

how does the guideline calculate the target value? e.g. is there a range (min/max) or only a target

##### flag_mode: `str`<a id="flag_mode-str"></a>

how does the guideline indicate deviations from the target amount

##### enable_populate_value: `bool`<a id="enable_populate_value-bool"></a>

whether or not the target values from the guidelines are pre-populated in the given columns

##### basis_type: `str`<a id="basis_type-str"></a>

how an individual guideline value itself is calculated, e.g. percentage of the appliedField, fixed amount, or custom CQL

##### org_id: `str`<a id="org_id-str"></a>

##### budget_pool_id: `str`<a id="budget_pool_id-str"></a>

the budget pool the guideline is allocated from

##### participants_expr: `str`<a id="participants_expr-str"></a>

CQL filter to determine which employees the guideline applies to

##### flag_deviation_threshold: `Union[int, float]`<a id="flag_deviation_threshold-unionint-float"></a>

the threshold (percent) against which deviations from the guideline are flagged

##### basis_expr: `str`<a id="basis_expr-str"></a>

if basisType.CUSTOM, the custom CQL expression used to generate the guideline value

##### basis_field_matrix: [`BasisFieldMatrix`](./chart_hop_python_sdk/type/basis_field_matrix.py)<a id="basis_field_matrix-basisfieldmatrixchart_hop_python_sdktypebasis_field_matrixpy"></a>


##### fixed_amount_range: [`MoneyRange`](./chart_hop_python_sdk/type/money_range.py)<a id="fixed_amount_range-moneyrangechart_hop_python_sdktypemoney_rangepy"></a>


##### fixed_value_range: [`ValueRange`](./chart_hop_python_sdk/type/value_range.py)<a id="fixed_value_range-valuerangechart_hop_python_sdktypevalue_rangepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateGuideline`](./chart_hop_python_sdk/type/create_guideline.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/guideline` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.guideline.get_specific_guideline`<a id="charthopguidelineget_specific_guideline"></a>

Get a specific guideline

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_guideline_response = charthop.guideline.get_specific_guideline(
    org_id="orgId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### id: `str`<a id="id-str"></a>

ID of the desired guideline

#### 🔄 Return<a id="🔄-return"></a>

[`Guideline`](./chart_hop_python_sdk/pydantic/guideline.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/guideline/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.guideline.remove_by_id`<a id="charthopguidelineremove_by_id"></a>

Delete a guideline

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.guideline.remove_by_id(
    org_id="orgId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/guideline/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.guideline.update_guideline`<a id="charthopguidelineupdate_guideline"></a>

Update a guideline

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.guideline.update_guideline(
    org_id="orgId_example",
    id="id_example",
    label="Merit Guideline",
    budget_pool_id="588f7ee98f138b19220041a7",
    participants_expr="is:person and tenure>=12",
    applied_field='base' or 'grantShares',
    source_field='base' or 'grantShares',
    calculation_type="TARGET",
    flag_mode="NONE",
    flag_deviation_threshold=0.75,
    enable_populate_value=False,
    basis_type="CUSTOM",
    basis_expr="tenure>12 ? (base * 0.04) : (base * 0.02)",
    basis_field_matrix={
        "included_fields": [
            "included_fields_example"
        ],
        "conditions": [
            {
                "condition_expr": "condition_expr_example",
            }
        ],
    },
    fixed_amount_range={
    },
    fixed_value_range={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

##### id: `str`<a id="id-str"></a>

##### label: `str`<a id="label-str"></a>

guideline name

##### budget_pool_id: `str`<a id="budget_pool_id-str"></a>

the budget pool the guideline is allocated from

##### participants_expr: `str`<a id="participants_expr-str"></a>

CQL filter to determine which employees the guideline applies to

##### applied_field: `str`<a id="applied_field-str"></a>

the field the guideline applies to

##### source_field: `str`<a id="source_field-str"></a>

the field the guideline is calculated from

##### calculation_type: `str`<a id="calculation_type-str"></a>

how does the guideline calculate the target value? e.g. is there a range (min/max) or only a target

##### flag_mode: `str`<a id="flag_mode-str"></a>

how does the guideline indicate deviations from the target amount

##### flag_deviation_threshold: `Union[int, float]`<a id="flag_deviation_threshold-unionint-float"></a>

the threshold (percent) against which deviations from the guideline are flagged

##### enable_populate_value: `bool`<a id="enable_populate_value-bool"></a>

whether or not the target values from the guidelines are pre-populated in the given columns

##### basis_type: `str`<a id="basis_type-str"></a>

how an individual guideline value itself is calculated, e.g. percentage of the appliedField, fixed amount, or custom CQL

##### basis_expr: `str`<a id="basis_expr-str"></a>

if basisType.CUSTOM, the custom CQL expression used to generate the guideline value

##### basis_field_matrix: [`BasisFieldMatrix`](./chart_hop_python_sdk/type/basis_field_matrix.py)<a id="basis_field_matrix-basisfieldmatrixchart_hop_python_sdktypebasis_field_matrixpy"></a>


##### fixed_amount_range: [`MoneyRange`](./chart_hop_python_sdk/type/money_range.py)<a id="fixed_amount_range-moneyrangechart_hop_python_sdktypemoney_rangepy"></a>


##### fixed_value_range: [`ValueRange`](./chart_hop_python_sdk/type/value_range.py)<a id="fixed_value_range-valuerangechart_hop_python_sdktypevalue_rangepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateGuideline`](./chart_hop_python_sdk/type/update_guideline.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/guideline/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.import.csv_data`<a id="charthopimportcsv_data"></a>

Import data from CSV file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
csv_data_response = charthop.import.csv_data(
    org_id="orgId_example",
    file=open('/path/to/file', 'rb'),
    scenario_id="string_example",
    skip_errors=True,
    upsert=True,
    create_groups=True,
    disable_sync_hire_date=True,
    update_types="string_example",
    notify_user_ids="string_example",
    notify_app_name="string_example",
    default_change_date="1970-01-01",
    disable_overwrite_person=True,
    import_dry_run=True,
    import_after_dry_run=True,
    parent_process_id="string_example",
    import_source="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file: `IO`<a id="file-io"></a>

##### scenario_id: `str`<a id="scenario_id-str"></a>

scenario id to import into

##### skip_errors: `bool`<a id="skip_errors-bool"></a>

whether to skip erroneous rows, or reject the entire upload if any are invalid (default)

##### upsert: `bool`<a id="upsert-bool"></a>

whether to create persons/jobs that are not matched

##### create_groups: `bool`<a id="create_groups-bool"></a>

whether to create groups that are not matched

##### disable_sync_hire_date: `bool`<a id="disable_sync_hire_date-bool"></a>

whether to disable adjusting dates of hires in cases where the start dates differ

##### update_types: `str`<a id="update_types-str"></a>

types of updates to apply (default all: title,comp,group,relationship,data,other)

##### notify_user_ids: `str`<a id="notify_user_ids-str"></a>

comma-separated list of user ids who should be notified when the import is complete

##### notify_app_name: `str`<a id="notify_app_name-str"></a>

name of the app that should be listed in the notify

##### default_change_date: `date`<a id="default_change_date-date"></a>

date of the changes - if not presented on the csv file

##### disable_overwrite_person: `bool`<a id="disable_overwrite_person-bool"></a>

disable overwriting changes to persons' data -- only update data if the person field is null

##### import_dry_run: `bool`<a id="import_dry_run-bool"></a>

import dry run

##### import_after_dry_run: `bool`<a id="import_after_dry_run-bool"></a>

whether to automatically import if dry run succeeds

##### parent_process_id: `str`<a id="parent_process_id-str"></a>

process id of parent process

##### import_source: `str`<a id="import_source-str"></a>

self identified source caller into this method

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/import/csv/data` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.import.csv_data_column_match`<a id="charthopimportcsv_data_column_match"></a>

Parse a CSV file in preparation for column matching as part of spreadsheet import process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.import.csv_data_column_match(
    org_id="orgId_example",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/import/csv/initialColumnMatch` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.import.csv_data_with_column_match`<a id="charthopimportcsv_data_with_column_match"></a>

Import data from CSV file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
csv_data_with_column_match_response = charthop.import.csv_data_with_column_match(
    org_id="orgId_example",
    scenario_id="string_example",
    skip_errors=True,
    upsert=True,
    create_groups=True,
    disable_sync_hire_date=True,
    update_types="string_example",
    notify_user_ids="string_example",
    notify_app_name="string_example",
    default_change_date="1970-01-01",
    disable_overwrite_person=True,
    import_dry_run=True,
    import_after_dry_run=True,
    parent_process_id="string_example",
    import_source="string_example",
    sync_images=True,
    file=open('/path/to/file', 'rb'),
    user_defined_field_aliases={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

scenario id to import into

##### skip_errors: `bool`<a id="skip_errors-bool"></a>

whether to skip erroneous rows, or reject the entire upload if any are invalid (default)

##### upsert: `bool`<a id="upsert-bool"></a>

whether to create persons/jobs that are not matched

##### create_groups: `bool`<a id="create_groups-bool"></a>

whether to create groups that are not matched

##### disable_sync_hire_date: `bool`<a id="disable_sync_hire_date-bool"></a>

whether to disable adjusting dates of hires in cases where the start dates differ

##### update_types: `str`<a id="update_types-str"></a>

types of updates to apply (default all: title,comp,group,relationship,data,other)

##### notify_user_ids: `str`<a id="notify_user_ids-str"></a>

comma-separated list of user ids who should be notified when the import is complete

##### notify_app_name: `str`<a id="notify_app_name-str"></a>

name of the app that should be listed in the notify

##### default_change_date: `date`<a id="default_change_date-date"></a>

date of the changes - if not presented on the csv file

##### disable_overwrite_person: `bool`<a id="disable_overwrite_person-bool"></a>

disable overwriting changes to persons' data -- only update data if the person field is null

##### import_dry_run: `bool`<a id="import_dry_run-bool"></a>

import dry run

##### import_after_dry_run: `bool`<a id="import_after_dry_run-bool"></a>

whether to automatically import if dry run succeeds

##### parent_process_id: `str`<a id="parent_process_id-str"></a>

process id of parent process

##### import_source: `str`<a id="import_source-str"></a>

self identified source caller into this method

##### sync_images: `bool`<a id="sync_images-bool"></a>

import images from csv

##### file: `IO`<a id="file-io"></a>

##### user_defined_field_aliases: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="user_defined_field_aliases-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

user defined field aliases for column matching

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportCsvDataWithColumnMatchRequest`](./chart_hop_python_sdk/type/import_csv_data_with_column_match_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/import/csv/columnMatch` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.import.csv_data_with_file_path`<a id="charthopimportcsv_data_with_file_path"></a>

Import data from CSV file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
csv_data_with_file_path_response = charthop.import.csv_data_with_file_path(
    org_id="orgId_example",
    file_path="string_example",
    scenario_id="string_example",
    skip_errors=True,
    upsert=True,
    create_groups=True,
    disable_sync_hire_date=True,
    update_types="string_example",
    notify_user_ids="string_example",
    notify_app_name="string_example",
    default_change_date="1970-01-01",
    disable_overwrite_person=True,
    import_dry_run=True,
    import_after_dry_run=True,
    parent_process_id="string_example",
    import_source="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file_path: `str`<a id="file_path-str"></a>

filePath

##### scenario_id: `str`<a id="scenario_id-str"></a>

scenario id to import into

##### skip_errors: `bool`<a id="skip_errors-bool"></a>

whether to skip erroneous rows, or reject the entire upload if any are invalid (default)

##### upsert: `bool`<a id="upsert-bool"></a>

whether to create persons/jobs that are not matched

##### create_groups: `bool`<a id="create_groups-bool"></a>

whether to create groups that are not matched

##### disable_sync_hire_date: `bool`<a id="disable_sync_hire_date-bool"></a>

whether to disable adjusting dates of hires in cases where the start dates differ

##### update_types: `str`<a id="update_types-str"></a>

types of updates to apply (default all: title,comp,group,relationship,data,other)

##### notify_user_ids: `str`<a id="notify_user_ids-str"></a>

comma-separated list of user ids who should be notified when the import is complete

##### notify_app_name: `str`<a id="notify_app_name-str"></a>

name of the app that should be listed in the notify

##### default_change_date: `date`<a id="default_change_date-date"></a>

date of the changes - if not presented on the csv file

##### disable_overwrite_person: `bool`<a id="disable_overwrite_person-bool"></a>

disable overwriting changes to persons' data -- only update data if the person field is null

##### import_dry_run: `bool`<a id="import_dry_run-bool"></a>

import dry run

##### import_after_dry_run: `bool`<a id="import_after_dry_run-bool"></a>

whether to automatically import if dry run succeeds

##### parent_process_id: `str`<a id="parent_process_id-str"></a>

process id of parent process

##### import_source: `str`<a id="import_source-str"></a>

self identified source caller into this method

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/import/csv/filepath` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.import.spreadsheet_validation`<a id="charthopimportspreadsheet_validation"></a>

Check if a spreadsheet file is valid to be imported

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.import.spreadsheet_validation(
    org_id="orgId_example",
    file=open('/path/to/file', 'rb'),
    max_rows=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file: `IO`<a id="file-io"></a>

##### max_rows: `int`<a id="max_rows-int"></a>

Max rows allowed in an imported spreadsheet file

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/import/spreadsheet/validateFormat` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.create_new_job`<a id="charthopjobcreate_new_job"></a>

Create a job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_job_response = charthop.job.create_new_job(
    org_id="orgId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to create the job in

##### date: `date`<a id="date-date"></a>

Effective date of job creation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.find_in_organization`<a id="charthopjobfind_in_organization"></a>

Return a particular job by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_in_organization_response = charthop.job.find_in_organization(
    org_id="orgId_example",
    job_id="jobId_example",
    scenario_id="string_example",
    date="1970-01-01",
    fields="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job/{jobId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.find_in_organization_0`<a id="charthopjobfind_in_organization_0"></a>

Find jobs in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_in_organization_0_response = charthop.job.find_in_organization_0(
    org_id="orgId_example",
    scenario_id="string_example",
    comp_review_id="string_example",
    approval_chain_id="string_example",
    date="1970-01-01",
    q="string_example",
    _from="string_example",
    limit=1,
    fields="string_example",
    fields_list=[
        "string_example"
    ],
    format="string_example",
    use_scenario_changes=True,
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### comp_review_id: `str`<a id="comp_review_id-str"></a>

Comp review id to query

##### approval_chain_id: `str`<a id="approval_chain_id-str"></a>

Approval chain id to query; only relevant when there is a comp review id

##### date: `date`<a id="date-date"></a>

Date to search as of

##### q: `str`<a id="q-str"></a>

Search query

##### _from: `str`<a id="_from-str"></a>

Job id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### fields_list: List[`str`]<a id="fields_list-liststr"></a>

Fields to retrieve, list syntax

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### use_scenario_changes: `bool`<a id="use_scenario_changes-bool"></a>

Find jobs only based on the changes that are in the scenario. This option also allows you to reference the change within the filter, which is otherwise not allowed

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.get_organization_job_count`<a id="charthopjobget_organization_job_count"></a>

Count jobs or people in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_organization_job_count_response = charthop.job.get_organization_job_count(
    org_id="orgId_example",
    scenario_id="string_example",
    date="1970-01-01",
    q="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date to search as of

##### q: `str`<a id="q-str"></a>

Search query

#### 🔄 Return<a id="🔄-return"></a>

[`OrgCount`](./chart_hop_python_sdk/pydantic/org_count.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job/count` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.get_region_jobs_graph`<a id="charthopjobget_region_jobs_graph"></a>

Retrieve jobs from a region of the job graph

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_region_jobs_graph_response = charthop.job.get_region_jobs_graph(
    org_id="orgId_example",
    start="string_example",
    depth=1,
    approx_limit=1,
    scenario_id="string_example",
    q="string_example",
    date="1970-01-01",
    fields="string_example",
    format="string_example",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### start: `str`<a id="start-str"></a>

Job id to use as the starting point for the search

##### depth: `int`<a id="depth-int"></a>

Number of levels down to search

##### approx_limit: `int`<a id="approx_limit-int"></a>

Number of results to return, approximately

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### q: `str`<a id="q-str"></a>

Query string to filter by

##### date: `date`<a id="date-date"></a>

Date to search as of

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job/graph` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.get_siblings_and_directs_map`<a id="charthopjobget_siblings_and_directs_map"></a>

Returns a map of jobId to their sibling and direct counts and the corresponding ids

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_siblings_and_directs_map_response = charthop.job.get_siblings_and_directs_map(
    org_id="orgId_example",
    scenario_id="string_example",
    date="1970-01-01",
    q="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date to search as of

##### q: `str`<a id="q-str"></a>

Query string to filter by

#### 🔄 Return<a id="🔄-return"></a>

[`GraphCountsResponse`](./chart_hop_python_sdk/pydantic/graph_counts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job/graph-counts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.list_occupied_positions_by_job_and_date`<a id="charthopjoblist_occupied_positions_by_job_and_date"></a>

Get a list of positions occupied by a job on specific date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_occupied_positions_by_job_and_date_response = charthop.job.list_occupied_positions_by_job_and_date(
    org_id="orgId_example",
    job_id="jobId_example",
    scenario_id="string_example",
    date="1970-01-01",
    _from="string_example",
    limit=1,
    position_fields="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update the job in

##### date: `date`<a id="date-date"></a>

Effective date of un-assignment

##### _from: `str`<a id="_from-str"></a>

Position id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### position_fields: `str`<a id="position_fields-str"></a>

Position fields to retrieve, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job/{jobId}/position` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.perform_bulk_update`<a id="charthopjobperform_bulk_update"></a>

Perform a bulk update on a number of jobs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_bulk_update_response = charthop.job.perform_bulk_update(
    updates=[
        {
            "job_id": "job_id_example",
            "update": {
                "key": {},
            },
        }
    ],
    date="1970-01-01",
    org_id="orgId_example",
    scenario_id="string_example",
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### updates: List[`UpdateOperation`]<a id="updates-listupdateoperation"></a>

list of update operations to perform

##### date: `date`<a id="date-date"></a>

date of update

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

scenario id

##### note: `str`<a id="note-str"></a>

note for update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BulkJobUpdateRequest`](./chart_hop_python_sdk/type/bulk_job_update_request.py)
Bulk update data

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job/bulkupdate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.remove_by_id`<a id="charthopjobremove_by_id"></a>

Delete a job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.job.remove_by_id(
    org_id="orgId_example",
    job_id="jobId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update the job in

##### date: `date`<a id="date-date"></a>

Effective date of job update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job/{jobId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job.update_job_details`<a id="charthopjobupdate_job_details"></a>

Update a job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.job.update_job_details(
    org_id="orgId_example",
    job_id="jobId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update the job in

##### date: `date`<a id="date-date"></a>

Effective date of job update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/job/{jobId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job_level.create_new_job_level`<a id="charthopjob_levelcreate_new_job_level"></a>

Create a job level

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.job_level.create_new_job_level(
    label="Associate",
    org_id="orgId_example",
    code="BF01",
    benchmark_type={
        "name": "name_example",
        "label": "label_example",
    },
    benchmark_level={
        "name": "name_example",
        "label": "label_example",
    },
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

human-readable name of job level

##### org_id: `str`<a id="org_id-str"></a>

org identifier (either id or slug)

##### code: `str`<a id="code-str"></a>

job level code

##### benchmark_type: [`EnumValue`](./chart_hop_python_sdk/type/enum_value.py)<a id="benchmark_type-enumvaluechart_hop_python_sdktypeenum_valuepy"></a>


##### benchmark_level: [`EnumValue`](./chart_hop_python_sdk/type/enum_value.py)<a id="benchmark_level-enumvaluechart_hop_python_sdktypeenum_valuepy"></a>


##### date: `date`<a id="date-date"></a>

Effective date of job level creation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateJobLevel`](./chart_hop_python_sdk/type/create_job_level.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/job-level` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job_level.delete_job_level`<a id="charthopjob_leveldelete_job_level"></a>

Delete a job level

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.job_level.delete_job_level(
    org_id="orgId_example",
    job_level_id="jobLevelId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_level_id: `str`<a id="job_level_id-str"></a>

Job level id

##### date: `date`<a id="date-date"></a>

Effective date of group update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/job-level/{jobLevelId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job_level.find_in_organization`<a id="charthopjob_levelfind_in_organization"></a>

Find job levels in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_in_organization_response = charthop.job_level.find_in_organization(
    org_id="orgId_example",
    date="1970-01-01",
    _from="string_example",
    limit=1,
    include_deleted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to search as of

##### _from: `str`<a id="_from-str"></a>

Job level id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

Include deleted job levels

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/job-level` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job_level.get_by_effective_date`<a id="charthopjob_levelget_by_effective_date"></a>

Return a particular job level by id on an effective date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_effective_date_response = charthop.job_level.get_by_effective_date(
    org_id="orgId_example",
    job_level_id="jobLevelId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_level_id: `str`<a id="job_level_id-str"></a>

Job level id

##### date: `date`<a id="date-date"></a>

Date to search as of

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/job-level/{jobLevelId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.job_level.update_job_level`<a id="charthopjob_levelupdate_job_level"></a>

Update a job level

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.job_level.update_job_level(
    org_id="orgId_example",
    job_level_id="jobLevelId_example",
    label="Associate",
    code="BF01",
    benchmark_type={
        "name": "name_example",
        "label": "label_example",
    },
    benchmark_level={
        "name": "name_example",
        "label": "label_example",
    },
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_level_id: `str`<a id="job_level_id-str"></a>

Job level id

##### label: `str`<a id="label-str"></a>

human-readable name of job level

##### code: `str`<a id="code-str"></a>

job level code

##### benchmark_type: [`EnumValue`](./chart_hop_python_sdk/type/enum_value.py)<a id="benchmark_type-enumvaluechart_hop_python_sdktypeenum_valuepy"></a>


##### benchmark_level: [`EnumValue`](./chart_hop_python_sdk/type/enum_value.py)<a id="benchmark_level-enumvaluechart_hop_python_sdktypeenum_valuepy"></a>


##### date: `date`<a id="date-date"></a>

Effective date of jobLevel update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateJobLevel`](./chart_hop_python_sdk/type/update_job_level.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/job-level/{jobLevelId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.legal_doc.create_document`<a id="charthoplegal_doccreate_document"></a>

Create a legal doc

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.legal_doc.create_document(
    name="ChartHop Service Agreement",
    content="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

human-readable full name of form

##### content: `str`<a id="content-str"></a>

legal doc content

##### date: `date`<a id="date-date"></a>

content by date

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateLegalDoc`](./chart_hop_python_sdk/type/create_legal_doc.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legaldoc` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.legal_doc.get_by_name`<a id="charthoplegal_docget_by_name"></a>

Retrieve the legal doc by name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_name_response = charthop.legal_doc.get_by_name(
    name="name_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

name

#### 🔄 Return<a id="🔄-return"></a>

[`LegalDoc`](./chart_hop_python_sdk/pydantic/legal_doc.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legaldoc/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.media.get_metadata`<a id="charthopmediaget_metadata"></a>

Returns metadata about a piece of media

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metadata_response = charthop.media.get_metadata(
    media_id="mediaId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### media_id: `str`<a id="media_id-str"></a>

Media id

#### 🔄 Return<a id="🔄-return"></a>

[`Media`](./chart_hop_python_sdk/pydantic/media.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/media/{mediaId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.media.get_metadata_0`<a id="charthopmediaget_metadata_0"></a>

Returns metadata about a piece of media

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metadata_0_response = charthop.media.get_metadata_0(
    org_id="orgId_example",
    media_id="mediaId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### media_id: `str`<a id="media_id-str"></a>

Media id

#### 🔄 Return<a id="🔄-return"></a>

[`Media`](./chart_hop_python_sdk/pydantic/media.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/media/{mediaId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.media.upload_new_media`<a id="charthopmediaupload_new_media"></a>

Upload a new piece of media

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_new_media_response = charthop.media.upload_new_media(
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Media`](./chart_hop_python_sdk/pydantic/media.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/media` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.media.upload_new_piece`<a id="charthopmediaupload_new_piece"></a>

Upload a new piece of media

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_new_piece_response = charthop.media.upload_new_piece(
    org_id="orgId_example",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Media`](./chart_hop_python_sdk/pydantic/media.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/media` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.message.create_new_message`<a id="charthopmessagecreate_new_message"></a>

Create a new message

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_message_response = charthop.message.create_new_message(
    org_id="orgId_example",
    title="string_example",
    id="588f7ee98f138b19220041a7",
    org_id="588f7ee98f138b19220041a7",
    type="CHAT",
    notification_type="SUCCESS",
    user_id="588f7ee98f138b19220041a7",
    content="string_example",
    message_url="string_example",
    key="string_example",
    read_at="2017-01-24T13:57:52Z",
    seen_at="2017-01-24T13:57:52Z",
    create_id="588f7ee98f138b19220041a7",
    create_at="2017-01-24T13:57:52Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`PartialMessage`](./chart_hop_python_sdk/type/partial_message.py)<a id="requestbody-partialmessagechart_hop_python_sdktypepartial_messagepy"></a>

Message data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./chart_hop_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/message` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.message.get_all_for_user`<a id="charthopmessageget_all_for_user"></a>

Return all messages for a particular user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_user_response = charthop.message.get_all_for_user(
    org_id="orgId_example",
    type="string_example",
    unread_only=True,
    _from="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Message \"type\" (WEB, CHAT, or EMAIL)

##### unread_only: `bool`<a id="unread_only-bool"></a>

Message \"status\" (read or unread)

##### _from: `str`<a id="_from-str"></a>

MessageId to start paginating from

##### limit: `int`<a id="limit-int"></a>

Limit

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsMessage`](./chart_hop_python_sdk/pydantic/results_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/message/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.message.get_message_by_id`<a id="charthopmessageget_message_by_id"></a>

Return a particular message by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_message_by_id_response = charthop.message.get_message_by_id(
    org_id="orgId_example",
    message_id="messageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### message_id: `str`<a id="message_id-str"></a>

Message id

#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./chart_hop_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/message/{messageId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.message.get_message_by_key`<a id="charthopmessageget_message_by_key"></a>

Return a particular message by key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_message_by_key_response = charthop.message.get_message_by_key(
    org_id="orgId_example",
    message_key="messageKey_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### message_key: `str`<a id="message_key-str"></a>

Message key

#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./chart_hop_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/message/me/{messageKey}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.message.mark_bulk_as_seen`<a id="charthopmessagemark_bulk_as_seen"></a>

Marks each message as `seen`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.message.mark_bulk_as_seen(
    body=[
        {
            "id": "588f7ee98f138b19220041a7",
            "org_id": "588f7ee98f138b19220041a7",
            "type": "CHAT",
            "notification_type": "SUCCESS",
            "user_id": "588f7ee98f138b19220041a7",
            "read_at": "2017-01-24T13:57:52Z",
            "seen_at": "2017-01-24T13:57:52Z",
            "create_id": "588f7ee98f138b19220041a7",
            "create_at": "2017-01-24T13:57:52Z",
        }
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`MessageMarkMessagesAsReadRequest`](./chart_hop_python_sdk/type/message_mark_messages_as_read_request.py)<a id="requestbody-messagemarkmessagesasreadrequestchart_hop_python_sdktypemessage_mark_messages_as_read_requestpy"></a>

Messages to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/message/bulk/seen` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.message.mark_messages_as_read`<a id="charthopmessagemark_messages_as_read"></a>

Sets each of the designated message's `readAt` property

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.message.mark_messages_as_read(
    body=[
        {
            "id": "588f7ee98f138b19220041a7",
            "org_id": "588f7ee98f138b19220041a7",
            "type": "CHAT",
            "notification_type": "SUCCESS",
            "user_id": "588f7ee98f138b19220041a7",
            "read_at": "2017-01-24T13:57:52Z",
            "seen_at": "2017-01-24T13:57:52Z",
            "create_id": "588f7ee98f138b19220041a7",
            "create_at": "2017-01-24T13:57:52Z",
        }
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`MessageMarkMessagesAsReadRequest`](./chart_hop_python_sdk/type/message_mark_messages_as_read_request.py)<a id="requestbody-messagemarkmessagesasreadrequestchart_hop_python_sdktypemessage_mark_messages_as_read_requestpy"></a>

Messages to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/message/bulk/read` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.message.set_read_status`<a id="charthopmessageset_read_status"></a>

Sets the designated message's `readAt` property

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.message.set_read_status(
    org_id="orgId_example",
    message_id="messageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### message_id: `str`<a id="message_id-str"></a>

Message id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/message/{messageId}/read` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.metric.record_daily_metric`<a id="charthopmetricrecord_daily_metric"></a>

Record a daily metric

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.metric.record_daily_metric(
    metric="string_example",
    value=3.14,
    org_id="orgId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### metric: `str`<a id="metric-str"></a>

the name of the metric, for example kpi.revenue.arr

##### value: `Union[int, float]`<a id="value-unionint-float"></a>

the numeric value of the metric

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

the date that the metric applies to (if blank, will default to today)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RecordMetricRequest`](./chart_hop_python_sdk/type/record_metric_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/metric` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.multiplier.create_new_multiplier`<a id="charthopmultipliercreate_new_multiplier"></a>

Create a multiplier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.multiplier.create_new_multiplier(
    label="Non-technical",
    value=0.75,
    expr="department!=\"Engineering\"",
    org_id="orgId_example",
    code="string_example",
    category="Location",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

human-readable name of multiplier

##### value: `Union[int, float]`<a id="value-unionint-float"></a>

amount to multiply the initial value by

##### expr: `str`<a id="expr-str"></a>

calculated expression to match against the job

##### org_id: `str`<a id="org_id-str"></a>

org identifier (either id or slug)

##### code: `str`<a id="code-str"></a>

##### category: `str`<a id="category-str"></a>

tag to group multipliers together by

##### date: `date`<a id="date-date"></a>

Effective date of multiplier creation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateMultiplier`](./chart_hop_python_sdk/type/create_multiplier.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/multiplier` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.multiplier.delete_multiplier_by_id`<a id="charthopmultiplierdelete_multiplier_by_id"></a>

Delete a multiplier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.multiplier.delete_multiplier_by_id(
    org_id="orgId_example",
    multiplier_id="multiplierId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### multiplier_id: `str`<a id="multiplier_id-str"></a>

Multiplier id

##### date: `date`<a id="date-date"></a>

Effective date of group update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/multiplier/{multiplierId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.multiplier.find_comp_band_multipliers_in_org`<a id="charthopmultiplierfind_comp_band_multipliers_in_org"></a>

Return a particular comp band multiplier by id on an effective date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_comp_band_multipliers_in_org_response = charthop.multiplier.find_comp_band_multipliers_in_org(
    org_id="orgId_example",
    multiplier_id="multiplierId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### multiplier_id: `str`<a id="multiplier_id-str"></a>

Comp band multiplier id

##### date: `date`<a id="date-date"></a>

Date to search as of

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/multiplier/{multiplierId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.multiplier.find_comp_band_multipliers_in_org_0`<a id="charthopmultiplierfind_comp_band_multipliers_in_org_0"></a>

Find comp band multipliers in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_comp_band_multipliers_in_org_0_response = charthop.multiplier.find_comp_band_multipliers_in_org_0(
    org_id="orgId_example",
    date="1970-01-01",
    _from="string_example",
    limit=1,
    include_deleted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### date: `date`<a id="date-date"></a>

Date to search as of

##### _from: `str`<a id="_from-str"></a>

Multiplier id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

Include deleted multipliers

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/multiplier` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.multiplier.update_multipler_by_id`<a id="charthopmultiplierupdate_multipler_by_id"></a>

Update a multiplier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.multiplier.update_multipler_by_id(
    org_id="orgId_example",
    multiplier_id="multiplierId_example",
    label="Non-technical",
    code="string_example",
    value=0.75,
    expr="department!=\"Engineering\"",
    category="Location",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### multiplier_id: `str`<a id="multiplier_id-str"></a>

Multiplier id

##### label: `str`<a id="label-str"></a>

human-readable name of multiplier

##### code: `str`<a id="code-str"></a>

##### value: `Union[int, float]`<a id="value-unionint-float"></a>

amount to multiply the initial value by

##### expr: `str`<a id="expr-str"></a>

calculated expression to match against the job

##### category: `str`<a id="category-str"></a>

tag to group multipliers together by

##### date: `date`<a id="date-date"></a>

Effective date of multiplier update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateMultiplier`](./chart_hop_python_sdk/type/update_multiplier.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/multiplier/{multiplierId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.notification.send_email_or_in_app_notification`<a id="charthopnotificationsend_email_or_in_app_notification"></a>

Send a email or in-app notification

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.notification.send_email_or_in_app_notification(
    template_name="string_example",
    to_user_ids=[
        "string_example"
    ],
    job_data={
    },
    org_id="orgId_example",
    ats_name="string_example",
    org_name="string_example",
    user_name="string_example",
    sync_summary="string_example",
    process_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_name: `str`<a id="template_name-str"></a>

name of message template

##### to_user_ids: [`NotificationRequestToUserIds`](./chart_hop_python_sdk/type/notification_request_to_user_ids.py)<a id="to_user_ids-notificationrequesttouseridschart_hop_python_sdktypenotification_request_to_user_idspy"></a>

##### job_data: [`NotificationJobData`](./chart_hop_python_sdk/type/notification_job_data.py)<a id="job_data-notificationjobdatachart_hop_python_sdktypenotification_job_datapy"></a>


##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### ats_name: `str`<a id="ats_name-str"></a>

name of the ATS system

##### org_name: `str`<a id="org_name-str"></a>

name of the organization

##### user_name: `str`<a id="user_name-str"></a>

preferred name of the user

##### sync_summary: `str`<a id="sync_summary-str"></a>

summary of reason for email

##### process_id: `str`<a id="process_id-str"></a>

id of the sync history process

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NotificationRequest`](./chart_hop_python_sdk/type/notification_request.py)
Notification request

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/notification` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.oauth.authorize_user_token`<a id="charthopoauthauthorize_user_token"></a>

Return an Oauth2 Authorization bearer token, given a username and password

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
authorize_user_token_response = charthop.oauth.authorize_user_token(
    grant_type="string_example",
    username="string_example",
    password="string_example",
    scope="string_example",
    code="string_example",
    redirect_uri="string_example",
    client_id="string_example",
    refresh_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

Type of grant; 'password', 'refresh_token', 'authorization_code' supported

##### username: `str`<a id="username-str"></a>

Username to authenticate

##### password: `str`<a id="password-str"></a>

Password to authenticate

##### scope: `str`<a id="scope-str"></a>

Requested access scope or scopes (space separated)

##### code: `str`<a id="code-str"></a>

Authorization code

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

Redirect URI

##### client_id: `str`<a id="client_id-str"></a>

Client id

##### refresh_token: `str`<a id="refresh_token-str"></a>

Refresh token

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OauthAuthorizeUserTokenRequest`](./chart_hop_python_sdk/type/oauth_authorize_user_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenResponse`](./chart_hop_python_sdk/pydantic/access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.oauth.exchange_idp_access_token_response`<a id="charthopoauthexchange_idp_access_token_response"></a>

Exchange a one-time use Auth Code for the IDP access token response

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
exchange_idp_access_token_response_response = charthop.oauth.exchange_idp_access_token_response(
    idp="idp_example",
    auth_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp: `str`<a id="idp-str"></a>

Identity provider of SSO login (e.g. adp)

##### auth_code: `str`<a id="auth_code-str"></a>

A one-time use Auth Code

#### 🔄 Return<a id="🔄-return"></a>

[`IdpAccessTokenResponse`](./chart_hop_python_sdk/pydantic/idp_access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/sso/{idp}/access-token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.oauth.generate_bearer_token_from_sso`<a id="charthopoauthgenerate_bearer_token_from_sso"></a>

Return an Oauth2 Authorization bearer token, given a SSO id token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_bearer_token_from_sso_response = charthop.oauth.generate_bearer_token_from_sso(
    id_token="string_example",
    scope="string_example",
    type="type_example",
    from_token="string_example",
    create_org=True,
    signup_source="ADP_MARKETPLACE",
    utm_params="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_token: `str`<a id="id_token-str"></a>

id token

##### scope: `str`<a id="scope-str"></a>

scope being requested

##### type: `str`<a id="type-str"></a>

type of SSO request (google or microsoft)

##### from_token: `str`<a id="from_token-str"></a>

an existing token

##### create_org: `bool`<a id="create_org-bool"></a>

automatically create org if possible to do so

##### signup_source: `str`<a id="signup_source-str"></a>

sign up source (self-serve, connect, or sequoia)

##### utm_params: `str`<a id="utm_params-str"></a>

utm params (used in salesforce for lead tracking)

##### email: `str`<a id="email-str"></a>

sign up email address

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessTokenRequest`](./chart_hop_python_sdk/type/access_token_request.py)
access token request

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenResponse`](./chart_hop_python_sdk/pydantic/access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/token/sso/{type}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.oauth.login_via_idp`<a id="charthopoauthlogin_via_idp"></a>

Login via the auth endpoint

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.oauth.login_via_idp(
    idp="idp_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp: `str`<a id="idp-str"></a>

Identity provider of SSO login (e.g. adp)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/sso/{idp}/login` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.oauth.process_oauth_redirect_request`<a id="charthopoauthprocess_oauth_redirect_request"></a>

Process an Oauth2 redirect request from an access request for an app installation, storing the accessToken and refreshToken as secrets for the app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.oauth.process_oauth_redirect_request(
    app_name="appName_example",
    token="string_example",
    state="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_name: `str`<a id="app_name-str"></a>

App name

##### token: `str`<a id="token-str"></a>

##### state: `str`<a id="state-str"></a>

State, containing orgId and appUserId

##### code: `str`<a id="code-str"></a>

Temporary authorization code

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/app/{appName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.oauth.return_view_token`<a id="charthopoauthreturn_view_token"></a>

Return a view-as token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
return_view_token_response = charthop.oauth.return_view_token(
    org_id="string_example",
    scope="string_example",
    person_id="string_example",
    user_id="string_example",
    role_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

org id

##### scope: `str`<a id="scope-str"></a>

scope being requested

##### person_id: `str`<a id="person_id-str"></a>

person id

##### user_id: `str`<a id="user_id-str"></a>

user id

##### role_id: `str`<a id="role_id-str"></a>

role id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewAsRequest`](./chart_hop_python_sdk/type/view_as_request.py)
request on whom to view as

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenResponse`](./chart_hop_python_sdk/pydantic/access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/token/view` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.oauth.revoke_bearer_token`<a id="charthopoauthrevoke_bearer_token"></a>

Delete the current Oauth2 bearer token (for signout)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.oauth.revoke_bearer_token()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/token` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.onboard.incomplete_steps`<a id="charthoponboardincomplete_steps"></a>

Returns all the onboarding steps the organization has not completed

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
incomplete_steps_response = charthop.onboard.incomplete_steps(
    org_id="orgId_example",
    get_uncomplete=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### get_uncomplete: `bool`<a id="get_uncomplete-bool"></a>

Return only uncompleted steps, or all steps?

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsOnboardStep`](./chart_hop_python_sdk/pydantic/results_onboard_step.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/onboard` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.onboard.mark_step_skipped`<a id="charthoponboardmark_step_skipped"></a>

Marks the given onboard step as 'skipped' for the given customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.onboard.mark_step_skipped(
    org_id="orgId_example",
    step_name="stepName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### step_name: `str`<a id="step_name-str"></a>

Step name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/onboard/{stepName}/skip` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.consent_terms_of_service`<a id="charthoporgconsent_terms_of_service"></a>

Consent on Terms of Service agreement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.org.consent_terms_of_service(
    action="string_example",
    legal_doc_id="string_example",
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: `str`<a id="action-str"></a>

action taken

##### legal_doc_id: `str`<a id="legal_doc_id-str"></a>

legal document entity id

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AgreementRequest`](./chart_hop_python_sdk/type/agreement_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/agreement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.create_new_job_placeholder`<a id="charthoporgcreate_new_job_placeholder"></a>

Create a new org head in the history, by creating an empty job placeholder above the current head

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.org.create_new_job_placeholder(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/change-head` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.create_new_org`<a id="charthoporgcreate_new_org"></a>

Create a new org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_org_response = charthop.org.create_new_org(
    name="Acme Corp",
    type="PRIVATE",
    est_employees=1,
    status="ACTIVE",
    currencies=[
        "string_example"
    ],
    timezone="America/New_York",
    onboarding=True,
    customer_id="588f7ee98f138b19220041a7",
    slug="acme-corp",
    industry="Software and Internet",
    est_revenue=1,
    founded_year=1998,
    address={
        "street1": "123 Anywhere Street",
        "street2": "Apt 6L",
        "street3": "Sixth Floor",
        "city": "New York",
        "state": "NY",
        "country": "NY",
        "postal": "10001",
    },
    phone="+907288",
    email="bob@example.com",
    url="string_example",
    domains=[
        {
            "domain": "domain_example",
            "aliases": [
                "aliases_example"
            ],
        }
    ],
    image_path="/",
    stock="GOOG",
    app_time="09:00",
    zone=2,
    fiscal_start=1,
    start_date="string_example",
    sensitive_fields={},
    options={},
    internal_options={},
    onboard_steps=[
        {
            "name": "name_example",
            "status": "COMPLETE",
        }
    ],
    self_serve_importing=True,
    head_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

name of organization

##### type: `str`<a id="type-str"></a>

type of organization

##### est_employees: `int`<a id="est_employees-int"></a>

approximate number of employees

##### status: `str`<a id="status-str"></a>

current status of organization

##### currencies: [`CreateOrgCurrencies`](./chart_hop_python_sdk/type/create_org_currencies.py)<a id="currencies-createorgcurrencieschart_hop_python_sdktypecreate_org_currenciespy"></a>

##### timezone: `str`<a id="timezone-str"></a>

timezone in use

##### onboarding: `bool`<a id="onboarding-bool"></a>

current onboarding status of an organization, allowing clearing of org

##### customer_id: `str`<a id="customer_id-str"></a>

customer for billing processing

##### slug: `str`<a id="slug-str"></a>

unique slug of organization

##### industry: `str`<a id="industry-str"></a>

industry

##### est_revenue: `int`<a id="est_revenue-int"></a>

approximate amount of revenue

##### founded_year: `int`<a id="founded_year-int"></a>

year of founding

##### address: [`Address`](./chart_hop_python_sdk/type/address.py)<a id="address-addresschart_hop_python_sdktypeaddresspy"></a>


##### phone: `str`<a id="phone-str"></a>

company phone number in E.164 format

##### email: `str`<a id="email-str"></a>

primary contact email

##### url: `str`<a id="url-str"></a>

website URL

##### domains: List[`OrgDomain`]<a id="domains-listorgdomain"></a>

domains used by this org

##### image_path: `str`<a id="image_path-str"></a>

path to full-sized profile image in storage

##### stock: `str`<a id="stock-str"></a>

stock symbol

##### app_time: `str`<a id="app_time-str"></a>

approximate time of day for daily app syncs to run (defaults to 9am Eastern time)

##### zone: `int`<a id="zone-int"></a>

infrastructure zone

##### fiscal_start: `int`<a id="fiscal_start-int"></a>

number of months into the calendar year that the fiscal year starts (1 = February, 2 = March)

##### start_date: `str`<a id="start_date-str"></a>

start date of history

##### sensitive_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="sensitive_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

map of sensitive field defaults

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

org-public options

##### internal_options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="internal_options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

internal (ChartHop controlled) options

##### onboard_steps: List[`OnboardStepResult`]<a id="onboard_steps-listonboardstepresult"></a>

list of onboard steps that this Org has completed (or skipped)

##### self_serve_importing: `bool`<a id="self_serve_importing-bool"></a>

completion status of initial import for orgs signed up via self serve

##### head_count: `int`<a id="head_count-int"></a>

number of total headcount currently in the org

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateOrg`](./chart_hop_python_sdk/type/create_org.py)
Org data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Org`](./chart_hop_python_sdk/pydantic/org.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_by_id`<a id="charthoporgget_by_id"></a>

Return a particular org by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.org.get_by_id(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`Org`](./chart_hop_python_sdk/pydantic/org.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_by_slug`<a id="charthoporgget_by_slug"></a>

Return a particular org by slug

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_slug_response = charthop.org.get_by_slug(
    slug="slug_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### slug: `str`<a id="slug-str"></a>

Org slug

#### 🔄 Return<a id="🔄-return"></a>

[`Org`](./chart_hop_python_sdk/pydantic/org.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/slug/{slug}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_data_user_person_by_id`<a id="charthoporgget_data_user_person_by_id"></a>

Gets a user or person by id. If both are provided, userId takes precedence

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_user_person_by_id_response = charthop.org.get_data_user_person_by_id(
    org_id="orgId_example",
    user_id="string_example",
    person_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### user_id: `str`<a id="user_id-str"></a>

userId

##### person_id: `str`<a id="person_id-str"></a>

personId

#### 🔄 Return<a id="🔄-return"></a>

[`OrgUsersPersonsResponse`](./chart_hop_python_sdk/pydantic/org_users_persons_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/data-user-person` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_data_user_person_count`<a id="charthoporgget_data_user_person_count"></a>

Gets the count of joined users, invited users, and org members who are not yet invited

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_user_person_count_response = charthop.org.get_data_user_person_count(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`OrgUsersPersonsCountResponse`](./chart_hop_python_sdk/pydantic/org_users_persons_count_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/data-user-person-count` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_data_users_persons`<a id="charthoporgget_data_users_persons"></a>

Gets a list of org users (joined or invited) and org members (not yet invited)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_users_persons_response = charthop.org.get_data_users_persons(
    org_id="orgId_example",
    limit=1,
    offset=1,
    sort="name, email, role, expr, invite, active",
    role="Owner, Technical Owner, Employee, etc...",
    status="joined, invited, not-invited",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### limit: `int`<a id="limit-int"></a>

limit

##### offset: `int`<a id="offset-int"></a>

offset

##### sort: `str`<a id="sort-str"></a>

Sort by

##### role: `str`<a id="role-str"></a>

Filter by user role label

##### status: `str`<a id="status-str"></a>

Filter by status

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`OrgUsersPersonsResponse`](./chart_hop_python_sdk/pydantic/org_users_persons_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/data-users-persons` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_oauth2_authorization_code`<a id="charthoporgget_oauth2_authorization_code"></a>

Retrieve an Oauth2 authorization code to install an app at this org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_oauth2_authorization_code_response = charthop.org.get_oauth2_authorization_code(
    org="org_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org: `str`<a id="org-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenResponse`](./chart_hop_python_sdk/pydantic/access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{org}/app-install-code` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_user_access`<a id="charthoporgget_user_access"></a>

Return information on current user's access

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.org.get_user_access(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/access` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_validation_by_slug`<a id="charthoporgget_validation_by_slug"></a>

Return validation for a org by slug

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.org.get_validation_by_slug(
    slug="slug_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### slug: `str`<a id="slug-str"></a>

Org slug

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/org/{slug}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.get_welcome_email_settings`<a id="charthoporgget_welcome_email_settings"></a>

Gets the custom setting or default for the welcome email's subject, body, cta button label

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_welcome_email_settings_response = charthop.org.get_welcome_email_settings(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`WelcomeEmailSettings`](./chart_hop_python_sdk/pydantic/welcome_email_settings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/welcome-email` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.list_visible_orgs`<a id="charthoporglist_visible_orgs"></a>

Return all visible orgs, paginated by name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_visible_orgs_response = charthop.org.list_visible_orgs(
    _from="string_example",
    q="string_example",
    limit=1,
    customer_id="string_example",
    real_only=True,
    last_create_at=1,
    last_active_at=1,
    internal_options="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `str`<a id="_from-str"></a>

Org id to start from

##### q: `str`<a id="q-str"></a>

Search query

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### customer_id: `str`<a id="customer_id-str"></a>

Find orgs belonging to a particular customer id

##### real_only: `bool`<a id="real_only-bool"></a>

Include only orgs where type is REAL?

##### last_create_at: `int`<a id="last_create_at-int"></a>

Only include orgs whose last createAt occurred after the date

##### last_active_at: `int`<a id="last_active_at-int"></a>

Only include orgs whose last activeAt occurred after the date

##### internal_options: `str`<a id="internal_options-str"></a>

Filter orgs by internal option key-value pair

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsOrg`](./chart_hop_python_sdk/pydantic/results_org.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.send_test_email_to_oneself`<a id="charthoporgsend_test_email_to_oneself"></a>

Send a test welcome email to oneself

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.org.send_test_email_to_oneself(
    org_id="orgId_example",
    welcome_email_subject="string_example",
    welcome_email_button_label="string_example",
    welcome_email_body="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### welcome_email_subject: `str`<a id="welcome_email_subject-str"></a>

##### welcome_email_button_label: `str`<a id="welcome_email_button_label-str"></a>

##### welcome_email_body: `str`<a id="welcome_email_body-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TestEmailRequest`](./chart_hop_python_sdk/type/test_email_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/test-email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.update_existing_org`<a id="charthoporgupdate_existing_org"></a>

Update an existing org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.org.update_existing_org(
    org_id="orgId_example",
    customer_id="588f7ee98f138b19220041a7",
    name="Acme Corp",
    slug="acme-corp",
    type="PRIVATE",
    industry="Software and Internet",
    est_employees=1,
    est_revenue=1,
    founded_year=1998,
    address={
        "street1": "123 Anywhere Street",
        "street2": "Apt 6L",
        "street3": "Sixth Floor",
        "city": "New York",
        "state": "NY",
        "country": "NY",
        "postal": "10001",
    },
    phone="+907288",
    email="bob@example.com",
    url="string_example",
    domains=[
        {
            "domain": "domain_example",
            "aliases": [
                "aliases_example"
            ],
        }
    ],
    status="ACTIVE",
    image_path="/",
    currencies=[
        "string_example"
    ],
    stock="GOOG",
    timezone="America/New_York",
    app_time="09:00",
    zone=2,
    fiscal_start=1,
    start_date="string_example",
    sensitive_fields={},
    options={},
    internal_options={},
    onboard_steps=[
        {
            "name": "name_example",
            "status": "COMPLETE",
        }
    ],
    onboarding=True,
    self_serve_importing=True,
    head_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### customer_id: `str`<a id="customer_id-str"></a>

customer for billing processing

##### name: `str`<a id="name-str"></a>

name of organization

##### slug: `str`<a id="slug-str"></a>

unique slug of organization

##### type: `str`<a id="type-str"></a>

type of organization

##### industry: `str`<a id="industry-str"></a>

industry

##### est_employees: `int`<a id="est_employees-int"></a>

approximate number of employees

##### est_revenue: `int`<a id="est_revenue-int"></a>

approximate amount of revenue

##### founded_year: `int`<a id="founded_year-int"></a>

year of founding

##### address: [`Address`](./chart_hop_python_sdk/type/address.py)<a id="address-addresschart_hop_python_sdktypeaddresspy"></a>


##### phone: `str`<a id="phone-str"></a>

company phone number in E.164 format

##### email: `str`<a id="email-str"></a>

primary contact email

##### url: `str`<a id="url-str"></a>

website URL

##### domains: List[`OrgDomain`]<a id="domains-listorgdomain"></a>

domains used by this org

##### status: `str`<a id="status-str"></a>

current status of organization

##### image_path: `str`<a id="image_path-str"></a>

path to full-sized profile image in storage

##### currencies: [`UpdateOrgCurrencies`](./chart_hop_python_sdk/type/update_org_currencies.py)<a id="currencies-updateorgcurrencieschart_hop_python_sdktypeupdate_org_currenciespy"></a>

##### stock: `str`<a id="stock-str"></a>

stock symbol

##### timezone: `str`<a id="timezone-str"></a>

timezone in use

##### app_time: `str`<a id="app_time-str"></a>

approximate time of day for daily app syncs to run (defaults to 9am Eastern time)

##### zone: `int`<a id="zone-int"></a>

infrastructure zone

##### fiscal_start: `int`<a id="fiscal_start-int"></a>

number of months into the calendar year that the fiscal year starts (1 = February, 2 = March)

##### start_date: `str`<a id="start_date-str"></a>

start date of history

##### sensitive_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="sensitive_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

map of sensitive field defaults

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

org-public options

##### internal_options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="internal_options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

internal (ChartHop controlled) options

##### onboard_steps: List[`OnboardStepResult`]<a id="onboard_steps-listonboardstepresult"></a>

list of onboard steps that this Org has completed (or skipped)

##### onboarding: `bool`<a id="onboarding-bool"></a>

current onboarding status of an organization, allowing clearing of org

##### self_serve_importing: `bool`<a id="self_serve_importing-bool"></a>

completion status of initial import for orgs signed up via self serve

##### head_count: `int`<a id="head_count-int"></a>

number of total headcount currently in the org

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateOrg`](./chart_hop_python_sdk/type/update_org.py)
Org data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org.validate_app_install_authorization_code`<a id="charthoporgvalidate_app_install_authorization_code"></a>

Validate authorization code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_app_install_authorization_code_response = charthop.org.validate_app_install_authorization_code(
    authorization_code="string_example",
    issue_access_token=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization_code: `str`<a id="authorization_code-str"></a>

authorization code token value

##### issue_access_token: `bool`<a id="issue_access_token-bool"></a>

flag indicating if authorization code should be exchanged for an access token

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppInstallCodeValidateRequest`](./chart_hop_python_sdk/type/app_install_code_validate_request.py)
Authorization code to validate

#### 🔄 Return<a id="🔄-return"></a>

[`AppInstallCodeValidateResponse`](./chart_hop_python_sdk/pydantic/app_install_code_validate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/app-install-code/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org_config.create_if_not_exists`<a id="charthoporg_configcreate_if_not_exists"></a>

Create an org config if it doesn't exist

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_if_not_exists_response = charthop.org_config.create_if_not_exists(
    org_id="588f7ee98f138b19220041a7",
    org_id="orgId_example",
    hidden_field_ids=[
        "string_example"
    ],
    builtin_category_map=[
        {
            "category_id": "category_id_example",
            "field_ids": [
                "588f7ee98f138b19220041a7"
            ],
        }
    ],
    builtin_field_config=[
        {
            "name": "name_example",
            "hidden": True,
        }
    ],
    compensation_bands_config={
        "annualized_salaries": True,
        "hourly_salaries": True,
        "hours_per_week": 3.14,
        "weeks_per_year": 3.14,
        "has_target_salary": True,
        "has_location_multiplier": True,
        "currency_rounding": [
            {
                "amount": 3.14,
                "currency": "currency_example",
            }
        ],
    },
    smart_currency_options=[
        {
            "name": "PERSON_HOME_ADDRESS_COUNTRY",
            "enabled": True,
        }
    ],
    smart_currency_default="USD",
    required_job_fields=[
        "string_example"
    ],
    scenario_approval_chains={
        "key": "588f7ee98f138b19220041a7",
    },
    is_open_job_role_approval_enabled=True,
    grant_configuration=[
        {
            "grant_type": "ISO",
            "enabled": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CreateOrgConfig`](./chart_hop_python_sdk/type/create_org_config.py)<a id="requestbody-createorgconfigchart_hop_python_sdktypecreate_org_configpy"></a>

Org config to create

#### 🔄 Return<a id="🔄-return"></a>

[`OrgConfig`](./chart_hop_python_sdk/pydantic/org_config.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/config` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org_config.get_by_org_id`<a id="charthoporg_configget_by_org_id"></a>

Return config for a given org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_org_id_response = charthop.org_config.get_by_org_id(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`OrgConfig`](./chart_hop_python_sdk/pydantic/org_config.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/config` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.org_config.patch_existing_config`<a id="charthoporg_configpatch_existing_config"></a>

Update an existing org config

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.org_config.patch_existing_config(
    org_id="orgId_example",
    hidden_field_ids=[
        "string_example"
    ],
    builtin_category_map=[
        {
            "category_id": "category_id_example",
            "field_ids": [
                "588f7ee98f138b19220041a7"
            ],
        }
    ],
    builtin_field_config=[
        {
            "name": "name_example",
            "hidden": True,
        }
    ],
    compensation_bands_config={
        "annualized_salaries": True,
        "hourly_salaries": True,
        "hours_per_week": 3.14,
        "weeks_per_year": 3.14,
        "has_target_salary": True,
        "has_location_multiplier": True,
        "currency_rounding": [
            {
                "amount": 3.14,
                "currency": "currency_example",
            }
        ],
    },
    smart_currency_options=[
        {
            "name": "PERSON_HOME_ADDRESS_COUNTRY",
            "enabled": True,
        }
    ],
    smart_currency_default="USD",
    required_job_fields=[
        "string_example"
    ],
    scenario_approval_chains={
        "key": "588f7ee98f138b19220041a7",
    },
    is_open_job_role_approval_enabled=True,
    grant_configuration=[
        {
            "grant_type": "ISO",
            "enabled": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### hidden_field_ids: [`UpdateOrgConfigHiddenFieldIds`](./chart_hop_python_sdk/type/update_org_config_hidden_field_ids.py)<a id="hidden_field_ids-updateorgconfighiddenfieldidschart_hop_python_sdktypeupdate_org_config_hidden_field_idspy"></a>

##### builtin_category_map: List[`BuiltInCategoryMap`]<a id="builtin_category_map-listbuiltincategorymap"></a>

set of maps of the custom fields that belongs to a built-in category

##### builtin_field_config: List[`BuiltInFieldConfig`]<a id="builtin_field_config-listbuiltinfieldconfig"></a>

Org configuration for built-in fields

##### compensation_bands_config: [`CompensationBandsConfig`](./chart_hop_python_sdk/type/compensation_bands_config.py)<a id="compensation_bands_config-compensationbandsconfigchart_hop_python_sdktypecompensation_bands_configpy"></a>


##### smart_currency_options: List[`SmartCurrencyOption`]<a id="smart_currency_options-listsmartcurrencyoption"></a>

Options for where to source a currency to use when currency is unknown. order specific

##### smart_currency_default: `str`<a id="smart_currency_default-str"></a>

The default currency to use when currency is unknown and there are no options set in smartCurrencyOptions

##### required_job_fields: [`UpdateOrgConfigRequiredJobFields`](./chart_hop_python_sdk/type/update_org_config_required_job_fields.py)<a id="required_job_fields-updateorgconfigrequiredjobfieldschart_hop_python_sdktypeupdate_org_config_required_job_fieldspy"></a>

##### scenario_approval_chains: [`UpdateOrgConfigScenarioApprovalChains`](./chart_hop_python_sdk/type/update_org_config_scenario_approval_chains.py)<a id="scenario_approval_chains-updateorgconfigscenarioapprovalchainschart_hop_python_sdktypeupdate_org_config_scenario_approval_chainspy"></a>

##### is_open_job_role_approval_enabled: `bool`<a id="is_open_job_role_approval_enabled-bool"></a>

Whether to show open job approval on Open Job Profile page

##### grant_configuration: List[`GrantAlias`]<a id="grant_configuration-listgrantalias"></a>

Org Grant Configuration

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateOrgConfig`](./chart_hop_python_sdk/type/update_org_config.py)
Sort data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/config` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.person.create_new_person`<a id="charthoppersoncreate_new_person"></a>

Create a person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_person_response = charthop.person.create_new_person(
    org_id="orgId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to create the person in

##### date: `date`<a id="date-date"></a>

Effective date of person creation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/person` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.person.find_in_organization`<a id="charthoppersonfind_in_organization"></a>

Find persons in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_in_organization_response = charthop.person.find_in_organization(
    org_id="orgId_example",
    scenario_id="string_example",
    date="1970-01-01",
    start_date="1970-01-01",
    end_date="1970-01-01",
    q="string_example",
    _from="string_example",
    limit=1,
    fields="string_example",
    fields_list=[
        "string_example"
    ],
    include_all=True,
    format="string_example",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date to search as of

##### start_date: `date`<a id="start_date-date"></a>

Start date, if retrieving persons employed between two dates (inclusive)

##### end_date: `date`<a id="end_date-date"></a>

End date, if retrieving persons employed between two dates (inclusive)

##### q: `str`<a id="q-str"></a>

Search query

##### _from: `str`<a id="_from-str"></a>

Person id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### fields_list: List[`str`]<a id="fields_list-liststr"></a>

Fields to retrieve, list syntax

##### include_all: `bool`<a id="include_all-bool"></a>

Include all persons in the system, including ex-employees or persons who were never in jobs

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/person` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.person.get_by_id`<a id="charthoppersonget_by_id"></a>

Return a particular person by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.person.get_by_id(
    org_id="orgId_example",
    person_id="personId_example",
    scenario_id="string_example",
    date="1970-01-01",
    fields="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### person_id: `str`<a id="person_id-str"></a>

Person id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/person/{personId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.person.get_geocodes_for_org`<a id="charthoppersonget_geocodes_for_org"></a>

Return all geocodes for persons in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_geocodes_for_org_response = charthop.person.get_geocodes_for_org(
    org_id="orgId_example",
    fields="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetGeocodesForOrgResponse`](./chart_hop_python_sdk/pydantic/person_get_geocodes_for_org_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/person/geocodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.person.remove_by_id`<a id="charthoppersonremove_by_id"></a>

Delete a person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.person.remove_by_id(
    org_id="orgId_example",
    person_id="personId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### person_id: `str`<a id="person_id-str"></a>

Person id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/person/{personId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.person.update_by_id`<a id="charthoppersonupdate_by_id"></a>

Update a person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.person.update_by_id(
    org_id="orgId_example",
    person_id="personId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### person_id: `str`<a id="person_id-str"></a>

Person id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update the person in

##### date: `date`<a id="date-date"></a>

Effective date of person update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/person/{personId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.policy.check_validity_of`<a id="charthoppolicycheck_validity_of"></a>

Return if a policy is valid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.policy.check_validity_of(
    org_id="orgId_example",
    description="This policy allows compensation to be viewed.",
    id="588f7ee98f138b19220041a7",
    org_id="588f7ee98f138b19220041a7",
    label="View Compensation",
    rules=[
        {
            "allow": [
                "['job:read', 'person.read']"
            ],
            "deny": [
                "['job:read', 'person.read']"
            ],
            "categories": [
                "['Compensation', 'Stock Grants']"
            ],
            "fields": [
                "['base']"
            ],
            "filter": "department:engineering and under:me",
        }
    ],
    copied_from_id="588f7ee98f138b19220041a7",
    create_id="588f7ee98f138b19220041a7",
    create_at="2017-01-24T13:57:52Z",
    update_id="588f7ee98f138b19220041a7",
    update_at="2017-01-24T13:57:52Z",
    delete_id="588f7ee98f138b19220041a7",
    delete_at="2017-01-24T13:57:52Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`PartialPolicy`](./chart_hop_python_sdk/type/partial_policy.py)<a id="requestbody-partialpolicychart_hop_python_sdktypepartial_policypy"></a>

Policy data to verify

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/policy/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.policy.copy_existing_policy`<a id="charthoppolicycopy_existing_policy"></a>

Copy an existing policy

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
copy_existing_policy_response = charthop.policy.copy_existing_policy(
    org_id="orgId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### policy_id: `str`<a id="policy_id-str"></a>

Policy id

#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./chart_hop_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/policy/{policyId}/copy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.policy.create_new_policy`<a id="charthoppolicycreate_new_policy"></a>

Create a policy

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_policy_response = charthop.policy.create_new_policy(
    label="View Compensation",
    org_id="orgId_example",
    description="This policy allows compensation to be viewed.",
    org_id="588f7ee98f138b19220041a7",
    rules=[
        {
            "allow": [
                "['job:read', 'person.read']"
            ],
            "deny": [
                "['job:read', 'person.read']"
            ],
            "categories": [
                "['Compensation', 'Stock Grants']"
            ],
            "fields": [
                "['base']"
            ],
            "filter": "department:engineering and under:me",
        }
    ],
    copied_from_id="588f7ee98f138b19220041a7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CreatePolicy`](./chart_hop_python_sdk/type/create_policy.py)<a id="requestbody-createpolicychart_hop_python_sdktypecreate_policypy"></a>

Policy data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./chart_hop_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/policy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.policy.get_all_entity_action_maps`<a id="charthoppolicyget_all_entity_action_maps"></a>

Return all entity:action maps allowed on a policy rule

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_entity_action_maps_response = charthop.policy.get_all_entity_action_maps(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`EntityAction`](./chart_hop_python_sdk/pydantic/entity_action.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/policy/action` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.policy.get_all_policies`<a id="charthoppolicyget_all_policies"></a>

Return all or a set of policies in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_policies_response = charthop.policy.get_all_policies(
    org_id="orgId_example",
    ids="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### ids: `str`<a id="ids-str"></a>

(Optional) Comma separated Policy Ids to find

##### type: `str`<a id="type-str"></a>

(Optional) Return only default or custom policies

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsPolicy`](./chart_hop_python_sdk/pydantic/results_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/policy` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.policy.get_by_id`<a id="charthoppolicyget_by_id"></a>

Return a particular policy by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.policy.get_by_id(
    org_id="orgId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### policy_id: `str`<a id="policy_id-str"></a>

Policy id

#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./chart_hop_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/policy/{policyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.policy.remove_by_id`<a id="charthoppolicyremove_by_id"></a>

Delete a policy

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.policy.remove_by_id(
    org_id="orgId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### policy_id: `str`<a id="policy_id-str"></a>

Policy id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/policy/{policyId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.policy.update_existing_policy`<a id="charthoppolicyupdate_existing_policy"></a>

Update an existing policy

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.policy.update_existing_policy(
    org_id="orgId_example",
    policy_id="policyId_example",
    description="This policy allows compensation to be viewed.",
    label="View Compensation",
    rules=[
        {
            "allow": [
                "['job:read', 'person.read']"
            ],
            "deny": [
                "['job:read', 'person.read']"
            ],
            "categories": [
                "['Compensation', 'Stock Grants']"
            ],
            "fields": [
                "['base']"
            ],
            "filter": "department:engineering and under:me",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### policy_id: `str`<a id="policy_id-str"></a>

Policy id

##### description: `str`<a id="description-str"></a>

description of policy

##### label: `str`<a id="label-str"></a>

human-readable full name of policy

##### rules: List[`PolicyRule`]<a id="rules-listpolicyrule"></a>

the rules that define the policy

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdatePolicy`](./chart_hop_python_sdk/type/update_policy.py)
Policy data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/policy/{policyId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.assign_job_to_position`<a id="charthoppositionassign_job_to_position"></a>

Assign a job to a position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_job_to_position_response = charthop.position.assign_job_to_position(
    org_id="orgId_example",
    position_id="positionId_example",
    job_id="jobId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### position_id: `str`<a id="position_id-str"></a>

Position id

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to assign the job in

##### date: `date`<a id="date-date"></a>

Effective date of assignment

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/{positionId}/job/{jobId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.create_new_position`<a id="charthoppositioncreate_new_position"></a>

Create a position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_position_response = charthop.position.create_new_position(
    org_id="orgId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to create the position in

##### date: `date`<a id="date-date"></a>

Effective date of position creation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.delete_and_purge`<a id="charthoppositiondelete_and_purge"></a>

Delete a position and purge it from all history

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_and_purge_response = charthop.position.delete_and_purge(
    org_id="orgId_example",
    position_id="positionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### position_id: `str`<a id="position_id-str"></a>

Position id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/{positionId}/purge` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.delete_position`<a id="charthoppositiondelete_position"></a>

Delete a position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_position_response = charthop.position.delete_position(
    org_id="orgId_example",
    position_id="positionId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### position_id: `str`<a id="position_id-str"></a>

Position id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to delete the position in

##### date: `date`<a id="date-date"></a>

Effective date of position deletion

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/{positionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.get_by_id`<a id="charthoppositionget_by_id"></a>

Return a particular position by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.position.get_by_id(
    org_id="orgId_example",
    position_id="positionId_example",
    scenario_id="string_example",
    date="1970-01-01",
    fields="string_example",
    include_deleted=True,
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### position_id: `str`<a id="position_id-str"></a>

Position identifier

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

Include deleted positions in the result

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`PositionGetByIdResponse`](./chart_hop_python_sdk/pydantic/position_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/{positionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.get_history_by_id`<a id="charthoppositionget_history_by_id"></a>

Return the history of a particular position by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_history_by_id_response = charthop.position.get_history_by_id(
    org_id="orgId_example",
    position_id="positionId_example",
    scenario_id="string_example",
    date="1970-01-01",
    fields="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### position_id: `str`<a id="position_id-str"></a>

Position identifier

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`PositionGetHistoryByIdResponse`](./chart_hop_python_sdk/pydantic/position_get_history_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/{positionId}/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.import_csv_data_with_file_path`<a id="charthoppositionimport_csv_data_with_file_path"></a>

Import positions as a CSV

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_csv_data_with_file_path_response = charthop.position.import_csv_data_with_file_path(
    org_id="orgId_example",
    import_from_process_id="string_example",
    parent_process_id="string_example",
    date="1970-01-01",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### import_from_process_id: `str`<a id="import_from_process_id-str"></a>

Import a file from another process, instead of directly uploading it

##### parent_process_id: `str`<a id="parent_process_id-str"></a>

Parent process id to attach to

##### date: `date`<a id="date-date"></a>

Effective date to import positions as of, if date column not provided

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PositionImportCsvDataWithFilePathRequest`](./chart_hop_python_sdk/type/position_import_csv_data_with_file_path_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/import` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.list`<a id="charthoppositionlist"></a>

Return a list of positions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = charthop.position.list(
    org_id="orgId_example",
    scenario_id="string_example",
    group_id="string_example",
    date="1970-01-01",
    _from="string_example",
    limit=1,
    fields="string_example",
    include_deleted=True,
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### group_id: `str`<a id="group_id-str"></a>

Group id to query

##### date: `date`<a id="date-date"></a>

Date

##### _from: `str`<a id="_from-str"></a>

Position id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

Include deleted positions in the result

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

#### 🔄 Return<a id="🔄-return"></a>

[`PositionListResponse`](./chart_hop_python_sdk/pydantic/position_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.remove_job_from_position`<a id="charthoppositionremove_job_from_position"></a>

Remove a job from a position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_job_from_position_response = charthop.position.remove_job_from_position(
    org_id="orgId_example",
    position_id="positionId_example",
    job_id="jobId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### position_id: `str`<a id="position_id-str"></a>

Position id

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to remove the job in

##### date: `date`<a id="date-date"></a>

Effective date of removal

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/{positionId}/job/{jobId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.update_job_dates_on_position`<a id="charthoppositionupdate_job_dates_on_position"></a>

Update assign or remove date of a job for a position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_dates_on_position_response = charthop.position.update_job_dates_on_position(
    org_id="orgId_example",
    position_id="positionId_example",
    job_id="jobId_example",
    scenario_id="string_example",
    remove_date="1970-01-01",
    assigndate="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### position_id: `str`<a id="position_id-str"></a>

Position id

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to remove the job in

##### remove_date: `date`<a id="remove_date-date"></a>

Effective date of removal

##### assigndate: `date`<a id="assigndate-date"></a>

Effective date of assignment

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/{positionId}/job/{jobId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.position.update_position_details`<a id="charthoppositionupdate_position_details"></a>

Update a position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_position_details_response = charthop.position.update_position_details(
    org_id="orgId_example",
    position_id="positionId_example",
    scenario_id="string_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### position_id: `str`<a id="position_id-str"></a>

Position id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update the position in

##### date: `date`<a id="date-date"></a>

Effective date of position update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/org/{orgId}/position/{positionId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.preload.preloaded_data_retrieval`<a id="charthoppreloadpreloaded_data_retrieval"></a>

Return a set of pre-loaded data required by the web app

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preloaded_data_retrieval_response = charthop.preload.preloaded_data_retrieval(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`PreloadResponse`](./chart_hop_python_sdk/pydantic/preload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/preload` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.check_process_status`<a id="charthopprocesscheck_process_status"></a>

Check the status of a particular process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_process_status_response = charthop.process.check_process_status(
    org_id="orgId_example",
    process_id="processId_example",
    show_state=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

##### show_state: `bool`<a id="show_state-bool"></a>

showState

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.create_new_pending_process`<a id="charthopprocesscreate_new_pending_process"></a>

Creates a new process in the pending state

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_pending_process_response = charthop.process.create_new_pending_process(
    org_id="588f7ee98f138b19220041a7",
    label="string_example",
    type="string_example",
    status="PENDING",
    run_user_id="588f7ee98f138b19220041a7",
    options={},
    org_id="orgId_example",
    file_path="string_example",
    parent_process_id="588f7ee98f138b19220041a7",
    message="string_example",
    progress=3.14,
    internal_error="string_example",
    results={
        "key": {},
    },
    log_data_list=[
        {
            "level": "INFO",
            "at": "2017-01-24T13:57:52Z",
            "data": {
                "key": {},
            },
        }
    ],
    state={},
    app_id="588f7ee98f138b19220041a7",
    uuid="84db3c6e-0877-4436-8af1-768c06b29586",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CreateProcess`](./chart_hop_python_sdk/type/create_process.py)<a id="requestbody-createprocesschart_hop_python_sdktypecreate_processpy"></a>

Process data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.create_pending_process`<a id="charthopprocesscreate_pending_process"></a>

Creates a new process in the pending state

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.create_pending_process(
    org_id="orgId_example",
    type="string_example",
    max_rows=1,
    min_columns=1,
    is_sync=True,
    file=open('/path/to/file', 'rb'),
    state={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Process type

##### max_rows: `int`<a id="max_rows-int"></a>

Max rows allowed in an imported spreadsheet file

##### min_columns: `int`<a id="min_columns-int"></a>

Min columns required in an imported spreadsheet file

##### is_sync: `bool`<a id="is_sync-bool"></a>

Whether the created process is sync flow or manual flow

##### file: `IO`<a id="file-io"></a>

##### state: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="state-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProcessCreatePendingProcessRequest`](./chart_hop_python_sdk/type/process_create_pending_process_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/self-serve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.create_pending_process_with_user_id`<a id="charthopprocesscreate_pending_process_with_user_id"></a>

Creates a new process with a specified createId in the pending state

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_pending_process_with_user_id_response = charthop.process.create_pending_process_with_user_id(
    org_id="588f7ee98f138b19220041a7",
    label="string_example",
    type="string_example",
    status="PENDING",
    run_user_id="588f7ee98f138b19220041a7",
    options={},
    org_id="orgId_example",
    create_id_override="createIdOverride_example",
    file_path="string_example",
    parent_process_id="588f7ee98f138b19220041a7",
    message="string_example",
    progress=3.14,
    internal_error="string_example",
    results={
        "key": {},
    },
    log_data_list=[
        {
            "level": "INFO",
            "at": "2017-01-24T13:57:52Z",
            "data": {
                "key": {},
            },
        }
    ],
    state={},
    app_id="588f7ee98f138b19220041a7",
    uuid="84db3c6e-0877-4436-8af1-768c06b29586",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### create_id_override: `str`<a id="create_id_override-str"></a>

created user id override

##### requestBody: [`CreateProcess`](./chart_hop_python_sdk/type/create_process.py)<a id="requestbody-createprocesschart_hop_python_sdktypecreate_processpy"></a>

Process data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{createIdOverride}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.decrement_step`<a id="charthopprocessdecrement_step"></a>

Decrement the step of an asynchronous process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.decrement_step(
    org_id="orgId_example",
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/decrement` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.download_file_by_id`<a id="charthopprocessdownload_file_by_id"></a>

Download the file associated with a particular process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.download_file_by_id(
    org_id="orgId_example",
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/file` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.download_log`<a id="charthopprocessdownload_log"></a>

Download the newline-delimited JSON log associated with a particular process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.download_log(
    org_id="orgId_example",
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/log` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.get_events_by_process_id`<a id="charthopprocessget_events_by_process_id"></a>

Get events associated to a particular process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_events_by_process_id_response = charthop.process.get_events_by_process_id(
    org_id="orgId_example",
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

#### 🔄 Return<a id="🔄-return"></a>

[`ProcessEventResponse`](./chart_hop_python_sdk/pydantic/process_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.get_last_sync_for_app_user`<a id="charthopprocessget_last_sync_for_app_user"></a>

Get last success sync and last sync for given appUserId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_last_sync_for_app_user_response = charthop.process.get_last_sync_for_app_user(
    org_id="orgId_example",
    app_user_id="appUserId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### app_user_id: `str`<a id="app_user_id-str"></a>

app user id

#### 🔄 Return<a id="🔄-return"></a>

[`AppProcessStatus`](./chart_hop_python_sdk/pydantic/app_process_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/last-sync/{appUserId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.get_previously_run_processes`<a id="charthopprocessget_previously_run_processes"></a>

Retrieve a number of previously run processes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_previously_run_processes_response = charthop.process.get_previously_run_processes(
    org_id="orgId_example",
    is_app_process=True,
    app_id="string_example",
    parent_process_id="string_example",
    type="string_example",
    completed_at_start=1,
    completed_at_end=1,
    statuses="string_example",
    is_parent_process=True,
    process_types="string_example",
    search_value="string_example",
    _from="string_example",
    limit=1,
    sync_directions="string_example",
    sync_causes="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### is_app_process: `bool`<a id="is_app_process-bool"></a>

Boolean if an app process

##### app_id: `str`<a id="app_id-str"></a>

App ID to filter by

##### parent_process_id: `str`<a id="parent_process_id-str"></a>

Parent process ID to search for children

##### type: `str`<a id="type-str"></a>

Type to filter by. Accepted values: ['auto', 'manual']

##### completed_at_start: `int`<a id="completed_at_start-int"></a>

completed at start

##### completed_at_end: `int`<a id="completed_at_end-int"></a>

completed at end

##### statuses: `str`<a id="statuses-str"></a>

Statuses to filter by, comma-separated. Accepted values: ['DONE', 'ERROR', 'PENDING', 'RUNNING', 'DONE_WITH_ERRORS']

##### is_parent_process: `bool`<a id="is_parent_process-bool"></a>

Boolean if a parent process

##### process_types: `str`<a id="process_types-str"></a>

Process types to filter by, comma-separated.

##### search_value: `str`<a id="search_value-str"></a>

Search term for general filtering

##### _from: `str`<a id="_from-str"></a>

from id

##### limit: `int`<a id="limit-int"></a>

limit

##### sync_directions: `str`<a id="sync_directions-str"></a>

direction

##### sync_causes: `str`<a id="sync_causes-str"></a>

V2 Causes to filter by, comma-separated. Accepted values: ['MANUAL', 'AUTO', 'EVENT_BASED]

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsProcess`](./chart_hop_python_sdk/pydantic/results_process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.increment_process_step`<a id="charthopprocessincrement_process_step"></a>

Increment the step of an asynchronous process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.increment_process_step(
    org_id="orgId_example",
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/increment` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.resume_process_with_user_id`<a id="charthopprocessresume_process_with_user_id"></a>

Resume an asynchronous process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.resume_process_with_user_id(
    org_id="orgId_example",
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProcessResumeProcessWithUserIdRequest`](./chart_hop_python_sdk/type/process_resume_process_with_user_id_request.py)
data to process

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/resume` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.resume_with_file`<a id="charthopprocessresume_with_file"></a>

Resume an asynchronous process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.resume_with_file(
    org_id="orgId_example",
    process_id="processId_example",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/resumeWithFile` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.update_process_state`<a id="charthopprocessupdate_process_state"></a>

Update process state

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.update_process_state(
    org_id="orgId_example",
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProcessUpdateProcessStateRequest`](./chart_hop_python_sdk/type/process_update_process_state_request.py)
state

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/state` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.update_status_of_process`<a id="charthopprocessupdate_status_of_process"></a>

Update the status of a process, marking its progress or setting status to DONE or ERROR

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.update_status_of_process(
    org_id="orgId_example",
    process_id="processId_example",
    status="PENDING",
    file_path="string_example",
    message="string_example",
    progress=3.14,
    internal_error="string_example",
    options={},
    results={
        "key": {},
    },
    log_data_list=[
        {
            "level": "INFO",
            "at": "2017-01-24T13:57:52Z",
            "data": {
                "key": {},
            },
        }
    ],
    state={},
    app_id="588f7ee98f138b19220041a7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

##### status: `str`<a id="status-str"></a>

current status of process

##### file_path: `str`<a id="file_path-str"></a>

data file path

##### message: `str`<a id="message-str"></a>

status or error message

##### progress: `Union[int, float]`<a id="progress-unionint-float"></a>

percent progress so far

##### internal_error: `str`<a id="internal_error-str"></a>

internal-only error message

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

options passed to the process

##### results: [`UpdateProcessResults`](./chart_hop_python_sdk/type/update_process_results.py)<a id="results-updateprocessresultschart_hop_python_sdktypeupdate_process_resultspy"></a>

##### log_data_list: List[`LogData`]<a id="log_data_list-listlogdata"></a>

list of log data that occurred during running of this process

##### state: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="state-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

process-specific state data

##### app_id: `str`<a id="app_id-str"></a>

app id of the process

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateProcess`](./chart_hop_python_sdk/type/update_process.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.process.upload_file_and_mark_complete`<a id="charthopprocessupload_file_and_mark_complete"></a>

Upload a file to be attached to a process, and mark the process as complete

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.process.upload_file_and_mark_complete(
    org_id="orgId_example",
    process_id="processId_example",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### process_id: `str`<a id="process_id-str"></a>

process id

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/process/{processId}/file` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.product.create_new_product`<a id="charthopproductcreate_new_product"></a>

Create a new product

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_product_response = charthop.product.create_new_product(
    name="Compensation Reviews",
    salesforce_product_id="01t4T000000RpgKQAS",
    stripe_product_id="prod_12345ABC",
    features=[
        "string_example"
    ],
    sku="compensation-reviews",
    feature_options={
        "key": [
            {
                "name": "smart_fields",
                "type": "LIMIT",
            }
        ],
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

name of product

##### salesforce_product_id: `str`<a id="salesforce_product_id-str"></a>

corresponding product id in salesforce

##### stripe_product_id: `str`<a id="stripe_product_id-str"></a>

corresponding product id in stripe

##### features: [`CreateProductFeatures`](./chart_hop_python_sdk/type/create_product_features.py)<a id="features-createproductfeatureschart_hop_python_sdktypecreate_product_featurespy"></a>

##### sku: `str`<a id="sku-str"></a>

unique sku of product

##### feature_options: [`CreateProductFeatureOptions`](./chart_hop_python_sdk/type/create_product_feature_options.py)<a id="feature_options-createproductfeatureoptionschart_hop_python_sdktypecreate_product_feature_optionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateProduct`](./chart_hop_python_sdk/type/create_product.py)
Product data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Product`](./chart_hop_python_sdk/pydantic/product.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/product` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.product.get_by_id`<a id="charthopproductget_by_id"></a>

Return a particular product by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.product.get_by_id(
    product_id="productId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_id: `str`<a id="product_id-str"></a>

Product id

#### 🔄 Return<a id="🔄-return"></a>

[`Product`](./chart_hop_python_sdk/pydantic/product.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/product/{productId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.product.list_all_products`<a id="charthopproductlist_all_products"></a>

Return all products

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_products_response = charthop.product.list_all_products()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsProduct`](./chart_hop_python_sdk/pydantic/results_product.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/product` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.product.update_existing_product`<a id="charthopproductupdate_existing_product"></a>

Update an existing product

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.product.update_existing_product(
    product_id="productId_example",
    name="Compensation Reviews",
    sku="compensation-reviews",
    salesforce_product_id="01t4T000000RpgKQAS",
    stripe_product_id="prod_12345ABC",
    features=[
        "string_example"
    ],
    feature_options={
        "key": [
            {
                "name": "smart_fields",
                "type": "LIMIT",
            }
        ],
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_id: `str`<a id="product_id-str"></a>

Product id

##### name: `str`<a id="name-str"></a>

name of product

##### sku: `str`<a id="sku-str"></a>

unique sku of product

##### salesforce_product_id: `str`<a id="salesforce_product_id-str"></a>

corresponding product id in salesforce

##### stripe_product_id: `str`<a id="stripe_product_id-str"></a>

corresponding product id in stripe

##### features: [`UpdateProductFeatures`](./chart_hop_python_sdk/type/update_product_features.py)<a id="features-updateproductfeatureschart_hop_python_sdktypeupdate_product_featurespy"></a>

##### feature_options: [`UpdateProductFeatureOptions`](./chart_hop_python_sdk/type/update_product_feature_options.py)<a id="feature_options-updateproductfeatureoptionschart_hop_python_sdktypeupdate_product_feature_optionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateProduct`](./chart_hop_python_sdk/type/update_product.py)
Product data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/product/{productId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.profile_tab.create_new_tab`<a id="charthopprofile_tabcreate_new_tab"></a>

Create a profile tab

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_tab_response = charthop.profile_tab.create_new_tab(
    label="Performance",
    blocks=[
        {
        }
    ],
    status="ACTIVE",
    sort=1,
    org_id="orgId_example",
    target_filter="string_example",
    read_filter="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

human-readable name of profile tab

##### blocks: List[`Block`]<a id="blocks-listblock"></a>

ordered list of blocks contained by profile tab

##### status: `str`<a id="status-str"></a>

status of the profile tab

##### sort: `int`<a id="sort-int"></a>

sort order

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### target_filter: `str`<a id="target_filter-str"></a>

filter that controls on which profiles this tab will appear

##### read_filter: `str`<a id="read_filter-str"></a>

filter that controls which viewers can read this profile tab. The profileTab:read permission, if present, overrides this filter

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateProfileTab`](./chart_hop_python_sdk/type/create_profile_tab.py)
Profile tab data to create

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileTab`](./chart_hop_python_sdk/pydantic/profile_tab.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/profile-tab` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.profile_tab.delete_profile_tab`<a id="charthopprofile_tabdelete_profile_tab"></a>

Delete a profile tab

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.profile_tab.delete_profile_tab(
    org_id="orgId_example",
    profile_tab_id="profileTabId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### profile_tab_id: `str`<a id="profile_tab_id-str"></a>

Profile tab id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/profile-tab/{profileTabId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.profile_tab.find_tabs_for_job`<a id="charthopprofile_tabfind_tabs_for_job"></a>

Return all profile tabs applicable to a particular job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_tabs_for_job_response = charthop.profile_tab.find_tabs_for_job(
    org_id="orgId_example",
    job_id="jobId_example",
    date="1970-01-01",
    fields="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### date: `date`<a id="date-date"></a>

Date

##### fields: `str`<a id="fields-str"></a>

Return profile tabs that contain particular fields (comma-separated)

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsProfileTabSummary`](./chart_hop_python_sdk/pydantic/results_profile_tab_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/profile-tab/job/{jobId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.profile_tab.get_by_org_id_and_tab_id`<a id="charthopprofile_tabget_by_org_id_and_tab_id"></a>

Return a particular profile tab by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_org_id_and_tab_id_response = charthop.profile_tab.get_by_org_id_and_tab_id(
    org_id="orgId_example",
    profile_tab_id="profileTabId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### profile_tab_id: `str`<a id="profile_tab_id-str"></a>

Content id

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileTab`](./chart_hop_python_sdk/pydantic/profile_tab.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/profile-tab/{profileTabId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.profile_tab.get_evaluate_profile_tab_content`<a id="charthopprofile_tabget_evaluate_profile_tab_content"></a>

Fetch and evaluate the content of a particular profile tab id, relative to a particular job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_evaluate_profile_tab_content_response = charthop.profile_tab.get_evaluate_profile_tab_content(
    org_id="orgId_example",
    job_id="jobId_example",
    tab_id="tabId_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### tab_id: `str`<a id="tab_id-str"></a>

Profile tab id

##### date: `date`<a id="date-date"></a>

Date

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileTabSummary`](./chart_hop_python_sdk/pydantic/profile_tab_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/profile-tab/job/{jobId}/profile-tab/{tabId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.profile_tab.get_profile_tabs`<a id="charthopprofile_tabget_profile_tabs"></a>

Return all profile tabs applicable to a particular person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_profile_tabs_response = charthop.profile_tab.get_profile_tabs(
    org_id="orgId_example",
    person_id="personId_example",
    date="1970-01-01",
    fields="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### person_id: `str`<a id="person_id-str"></a>

Person id

##### date: `date`<a id="date-date"></a>

Date

##### fields: `str`<a id="fields-str"></a>

Return profile tabs that contain particular fields (comma-separated)

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsProfileTabSummary`](./chart_hop_python_sdk/pydantic/results_profile_tab_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/profile-tab/person/{personId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.profile_tab.list_profile_tabs`<a id="charthopprofile_tablist_profile_tabs"></a>

Return all profile tabs in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_profile_tabs_response = charthop.profile_tab.list_profile_tabs(
    org_id="orgId_example",
    status="ACTIVE",
    _from="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### status: `str`<a id="status-str"></a>

Status to filter by

##### _from: `str`<a id="_from-str"></a>

Content id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsProfileTab`](./chart_hop_python_sdk/pydantic/results_profile_tab.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/profile-tab` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.profile_tab.update_existing_tab`<a id="charthopprofile_tabupdate_existing_tab"></a>

Update an existing profile tab

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.profile_tab.update_existing_tab(
    org_id="orgId_example",
    profile_tab_id="profileTabId_example",
    label="Performance",
    blocks=[
        {
        }
    ],
    status="ACTIVE",
    target_filter="string_example",
    read_filter="string_example",
    sort=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### profile_tab_id: `str`<a id="profile_tab_id-str"></a>

Profile tab id

##### label: `str`<a id="label-str"></a>

human-readable name of profile tab

##### blocks: List[`Block`]<a id="blocks-listblock"></a>

ordered list of blocks contained by profile tab

##### status: `str`<a id="status-str"></a>

status of the profile tab

##### target_filter: `str`<a id="target_filter-str"></a>

filter that controls on which profiles this tab will appear

##### read_filter: `str`<a id="read_filter-str"></a>

filter that controls which viewers can read this profile tab. The profileTab:read permission, if present, overrides this filter

##### sort: `int`<a id="sort-int"></a>

sort order

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateProfileTab`](./chart_hop_python_sdk/type/update_profile_tab.py)
Profile tab data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/profile-tab/{profileTabId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.query.expire_live_query`<a id="charthopqueryexpire_live_query"></a>

Expire a previously created live query immediately

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.query.expire_live_query(
    org_id="orgId_example",
    query_token="queryToken_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### query_token: `str`<a id="query_token-str"></a>

Query token (either id or token string)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/query/{queryToken}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.query.live_query_result`<a id="charthopquerylive_query_result"></a>

Return the results of a previously created live query

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.query.live_query_result(
    org_id="orgId_example",
    query_token="queryToken_example",
    format="string_example",
    mapper="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### query_token: `str`<a id="query_token-str"></a>

Query token

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### mapper: `str`<a id="mapper-str"></a>

Deprecated parameter for backwards-compatibility

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/query/{queryToken}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.query.live_query_token`<a id="charthopquerylive_query_token"></a>

Create a live query token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
live_query_token_response = charthop.query.live_query_token(
    type="string_example",
    params={},
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

query type

##### params: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="params-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

query params

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateQueryToken`](./chart_hop_python_sdk/type/create_query_token.py)
#### 🔄 Return<a id="🔄-return"></a>

[`QueryToken`](./chart_hop_python_sdk/pydantic/query_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/query` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.query.query_tokens`<a id="charthopqueryquery_tokens"></a>

Get a list of query tokens

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_tokens_response = charthop.query.query_tokens(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug

#### 🔄 Return<a id="🔄-return"></a>

[`QueryQueryTokensResponse`](./chart_hop_python_sdk/pydantic/query_query_tokens_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/query` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.question.create`<a id="charthopquestioncreate"></a>

Create a question

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = charthop.question.create(
    question="What is your favorite color?",
    org_id="orgId_example",
    org_id="588f7ee98f138b19220041a7",
    field_id="string_example",
    type="ADDRESS",
    plural="SINGLE",
    values=[
        {
            "name": "name_example",
            "label": "label_example",
        }
    ],
    options={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CreateQuestion`](./chart_hop_python_sdk/type/create_question.py)<a id="requestbody-createquestionchart_hop_python_sdktypecreate_questionpy"></a>

Question data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Question`](./chart_hop_python_sdk/pydantic/question.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/question` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.question.get_all_in_org`<a id="charthopquestionget_all_in_org"></a>

Return all questions in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_in_org_response = charthop.question.get_all_in_org(
    org_id="orgId_example",
    _from="string_example",
    limit=1,
    ids="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

Question id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### ids: `str`<a id="ids-str"></a>

Comma separated Question Ids to find

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsQuestion`](./chart_hop_python_sdk/pydantic/results_question.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/question` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.question.get_by_id`<a id="charthopquestionget_by_id"></a>

Return a particular question by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.question.get_by_id(
    org_id="orgId_example",
    question_id="questionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### question_id: `str`<a id="question_id-str"></a>

Question id

#### 🔄 Return<a id="🔄-return"></a>

[`Question`](./chart_hop_python_sdk/pydantic/question.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/question/{questionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.question.remove`<a id="charthopquestionremove"></a>

Delete a question

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.question.remove(
    org_id="orgId_example",
    question_id="questionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### question_id: `str`<a id="question_id-str"></a>

Question id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/question/{questionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.question.update_by_org_and_id`<a id="charthopquestionupdate_by_org_and_id"></a>

Update an existing question

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.question.update_by_org_and_id(
    org_id="orgId_example",
    question_id="questionId_example",
    question="What is your favorite color?",
    field_id="string_example",
    type="ADDRESS",
    plural="SINGLE",
    values=[
        {
            "name": "name_example",
            "label": "label_example",
        }
    ],
    options={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### question_id: `str`<a id="question_id-str"></a>

Question id

##### question: `str`<a id="question-str"></a>

text of the question

##### field_id: `str`<a id="field_id-str"></a>

if the question is linked to a field, the id of that field. Any question responses will be automatically saved to the field

##### type: `str`<a id="type-str"></a>

datatype of the question

##### plural: `str`<a id="plural-str"></a>

plural type of the question datatype (either SINGLE, LIST, or SET)

##### values: List[`EnumValue`]<a id="values-listenumvalue"></a>

possible values (enum type only)

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

validation options

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateQuestion`](./chart_hop_python_sdk/type/update_question.py)
Question data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/question/{questionId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.bulk_delete`<a id="charthopreportbulk_delete"></a>

Delete a set of reports

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_delete_response = charthop.report.bulk_delete(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`ReportBulkDeleteRequest`](./chart_hop_python_sdk/type/report_bulk_delete_request.py)<a id="requestbody-reportbulkdeleterequestchart_hop_python_sdktypereport_bulk_delete_requestpy"></a>

List of report ids to delete

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/bulk-delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.create_exact_copy`<a id="charthopreportcreate_exact_copy"></a>

Create an exact copy of an existing report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_exact_copy_response = charthop.report.create_exact_copy(
    org_id="orgId_example",
    report_id="reportId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

#### 🔄 Return<a id="🔄-return"></a>

[`Report`](./chart_hop_python_sdk/pydantic/report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}/clone` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.create_new_report`<a id="charthopreportcreate_new_report"></a>

Create a report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_report_response = charthop.report.create_new_report(
    label="Headcount Report",
    org_id="orgId_example",
    description="This is a report on headcount etd",
    filter="department:engineering",
    share="NORMAL",
    sensitive="GLOBAL",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    chart_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

report label

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### description: `str`<a id="description-str"></a>

report description

##### filter: `str`<a id="filter-str"></a>

filter automatically applied to every chart in this report

##### share: `str`<a id="share-str"></a>

sharing settings of report

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level of report

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who are specifically granted permission to view or edit this report

##### chart_ids: [`CreateReportChartIds`](./chart_hop_python_sdk/type/create_report_chart_ids.py)<a id="chart_ids-createreportchartidschart_hop_python_sdktypecreate_report_chart_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateReport`](./chart_hop_python_sdk/type/create_report.py)
Report data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Report`](./chart_hop_python_sdk/pydantic/report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.duplicate_reports`<a id="charthopreportduplicate_reports"></a>

Duplicate a set of reports

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
duplicate_reports_response = charthop.report.duplicate_reports(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`ReportDuplicateReportsRequest`](./chart_hop_python_sdk/type/report_duplicate_reports_request.py)<a id="requestbody-reportduplicatereportsrequestchart_hop_python_sdktypereport_duplicate_reports_requestpy"></a>

List of report ids to duplicate

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/bulk-duplicate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.export_chart_csv`<a id="charthopreportexport_chart_csv"></a>

Export a particular chart in a report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
export_chart_csv_response = charthop.report.export_chart_csv(
    org_id="orgId_example",
    report_id="reportId_example",
    chart_id="chartId_example",
    start_date="string_example",
    end_date="string_example",
    interval="DAY",
    scenario_id="string_example",
    project_hires=True,
    filter="string_example",
    change_grouping_type="PRIMARY",
    change_grouping_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

##### chart_id: `str`<a id="chart_id-str"></a>

Chart id

##### start_date: `str`<a id="start_date-str"></a>

Start date, inclusive

##### end_date: `str`<a id="end_date-str"></a>

End date, exclusive

##### interval: `str`<a id="interval-str"></a>

Interval

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### project_hires: `bool`<a id="project_hires-bool"></a>

Project future hires

##### filter: `str`<a id="filter-str"></a>

Additional filter to apply

##### change_grouping_type: `str`<a id="change_grouping_type-str"></a>

Type of change grouping

##### change_grouping_id: `str`<a id="change_grouping_id-str"></a>

Change grouping id to query (null for primary)

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}/chart/{chartId}/export/csv` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.find_report_by_id`<a id="charthopreportfind_report_by_id"></a>

Return a particular report by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_report_by_id_response = charthop.report.find_report_by_id(
    org_id="orgId_example",
    report_id="reportId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

#### 🔄 Return<a id="🔄-return"></a>

[`Report`](./chart_hop_python_sdk/pydantic/report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.get_all_paginated`<a id="charthopreportget_all_paginated"></a>

Return all reports in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_paginated_response = charthop.report.get_all_paginated(
    org_id="orgId_example",
    from_id="string_example",
    limit=1,
    sort="string_example",
    filter="string_example",
    fields="string_example",
    format="string_example",
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### from_id: `str`<a id="from_id-str"></a>

Offset

##### limit: `int`<a id="limit-int"></a>

Limit

##### sort: `str`<a id="sort-str"></a>

Sort

##### filter: `str`<a id="filter-str"></a>

Filter

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ReportDataStreamResults`](./chart_hop_python_sdk/pydantic/report_data_stream_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.get_all_report_charts`<a id="charthopreportget_all_report_charts"></a>

Query all the charts in a report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_report_charts_response = charthop.report.get_all_report_charts(
    org_id="orgId_example",
    report_id="reportId_example",
    start_date="string_example",
    end_date="string_example",
    interval="DAY",
    scenario_id="string_example",
    project_hires=True,
    filter="string_example",
    change_grouping_type="PRIMARY",
    change_grouping_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

##### start_date: `str`<a id="start_date-str"></a>

Start date, inclusive

##### end_date: `str`<a id="end_date-str"></a>

End date, exclusive

##### interval: `str`<a id="interval-str"></a>

Interval

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### project_hires: `bool`<a id="project_hires-bool"></a>

Project future hires

##### filter: `str`<a id="filter-str"></a>

Filter to apply to all results

##### change_grouping_type: `str`<a id="change_grouping_type-str"></a>

Type of change grouping

##### change_grouping_id: `str`<a id="change_grouping_id-str"></a>

Change grouping id to query (null for primary)

#### 🔄 Return<a id="🔄-return"></a>

[`ReportGetAllReportChartsResponse`](./chart_hop_python_sdk/pydantic/report_get_all_report_charts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}/query` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.get_count_of_reports_in_organization`<a id="charthopreportget_count_of_reports_in_organization"></a>

Return count of reports in an organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_count_of_reports_in_organization_response = charthop.report.get_count_of_reports_in_organization(
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

#### 🔄 Return<a id="🔄-return"></a>

[`ReportCount`](./chart_hop_python_sdk/pydantic/report_count.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/count` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.remove_by_id`<a id="charthopreportremove_by_id"></a>

Delete a report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.report.remove_by_id(
    org_id="orgId_example",
    report_id="reportId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.timeseries_data_arbitrary_queries`<a id="charthopreporttimeseries_data_arbitrary_queries"></a>

Return timeseries data from arbitrary queries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
timeseries_data_arbitrary_queries_response = charthop.report.timeseries_data_arbitrary_queries(
    options={},
    org_id="orgId_example",
    series=[
        {
            "label": "label_example",
            "color": "color_example",
            "y": "sum{headcount, gender:f} / sum{headcount}",
            "x": "sum{headcount, gender:f} / sum{headcount}",
            "options": {},
        }
    ],
    filters=[
        {
            "label": "label_example",
            "filter": "filter_example",
        }
    ],
    content="string_example",
    start_date="string_example",
    end_date="string_example",
    interval="DAY",
    interval_dates=[
        "1970-01-01"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

options, including format, scenarioId, projectHires

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### series: List[`ReportSeriesQuery`]<a id="series-listreportseriesquery"></a>

series to evaluate

##### filters: List[`ReportFilter`]<a id="filters-listreportfilter"></a>

filters to crosstab all results by (deprecated in reports V2, should use groupBy instead)

##### content: `str`<a id="content-str"></a>

content block to evaluate as a Carrot Template, as an alternative to using series

##### start_date: `str`<a id="start_date-str"></a>

start date, in either relative (-7d) or exact (YYYY-MM-DD) format

##### end_date: `str`<a id="end_date-str"></a>

end date, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today

##### interval: `str`<a id="interval-str"></a>

interval, if the query is a timeseries; if no interval, query is crosstabbed

##### interval_dates: [`ReportQueryIntervalDates`](./chart_hop_python_sdk/type/report_query_interval_dates.py)<a id="interval_dates-reportqueryintervaldateschart_hop_python_sdktypereport_query_interval_datespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReportQuery`](./chart_hop_python_sdk/type/report_query.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ReportTimeseriesDataArbitraryQueriesResponse`](./chart_hop_python_sdk/pydantic/report_timeseries_data_arbitrary_queries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/query` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report.update_existing_report`<a id="charthopreportupdate_existing_report"></a>

Update an existing report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.report.update_existing_report(
    org_id="orgId_example",
    report_id="reportId_example",
    description="This is a report on headcount etd",
    label="Headcount Report",
    filter="department:engineering",
    share="NORMAL",
    sensitive="GLOBAL",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    chart_ids=[
        "string_example"
    ],
    referenced_report_url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

##### description: `str`<a id="description-str"></a>

report description

##### label: `str`<a id="label-str"></a>

report label

##### filter: `str`<a id="filter-str"></a>

filter automatically applied to every chart in this report

##### share: `str`<a id="share-str"></a>

sharing settings of report

##### sensitive: `str`<a id="sensitive-str"></a>

sensitivity level of report

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who are specifically granted permission to view or edit this report

##### chart_ids: [`UpdateReportChartIds`](./chart_hop_python_sdk/type/update_report_chart_ids.py)<a id="chart_ids-updatereportchartidschart_hop_python_sdktypeupdate_report_chart_idspy"></a>

##### referenced_report_url: `str`<a id="referenced_report_url-str"></a>

Displayed report url

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateReport`](./chart_hop_python_sdk/type/update_report.py)
Report data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report_chart.clone_chart`<a id="charthopreport_chartclone_chart"></a>

Clone a chart in a report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
clone_chart_response = charthop.report_chart.clone_chart(
    org_id="orgId_example",
    report_id="reportId_example",
    chart_id="chartId_example",
    chart_label="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

##### chart_id: `str`<a id="chart_id-str"></a>

Chart id

##### chart_label: `str`<a id="chart_label-str"></a>

New label

#### 🔄 Return<a id="🔄-return"></a>

[`ReportChart`](./chart_hop_python_sdk/pydantic/report_chart.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}/chart/{chartId}/clone` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report_chart.create_new_chart`<a id="charthopreport_chartcreate_new_chart"></a>

Create a new chart in a report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_chart_response = charthop.report_chart.create_new_chart(
    label="Headcount Report",
    type="LINE",
    query={
        "interval": "DAY",
        "options": {},
    },
    sort=1,
    org_id="orgId_example",
    report_id="reportId_example",
    filter="department='Engineering'",
    filter_override=True,
    is_advanced_query_mode=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

chart label

##### type: `str`<a id="type-str"></a>

chart type

##### query: [`ReportQuery`](./chart_hop_python_sdk/type/report_query.py)<a id="query-reportquerychart_hop_python_sdktypereport_querypy"></a>


##### sort: `int`<a id="sort-int"></a>

sort order

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

##### filter: `str`<a id="filter-str"></a>

filter that applies to this chart

##### filter_override: `bool`<a id="filter_override-bool"></a>

whether the chart filter overrides the global filter

##### is_advanced_query_mode: `bool`<a id="is_advanced_query_mode-bool"></a>

whether the chart configuration is using advanced mode

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateReportChart`](./chart_hop_python_sdk/type/create_report_chart.py)
Report chart data to create

#### 🔄 Return<a id="🔄-return"></a>

[`ReportChart`](./chart_hop_python_sdk/pydantic/report_chart.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}/chart` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report_chart.export_data`<a id="charthopreport_chartexport_data"></a>

Export a particular chart's data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.report_chart.export_data(
    org_id="orgId_example",
    report_id="reportId_example",
    chart_id="chartId_example",
    start_date="string_example",
    end_date="string_example",
    interval="DAY",
    scenario_id="string_example",
    project_hires=True,
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

##### chart_id: `str`<a id="chart_id-str"></a>

Chart id

##### start_date: `str`<a id="start_date-str"></a>

Start date, inclusive

##### end_date: `str`<a id="end_date-str"></a>

End date, exclusive

##### interval: `str`<a id="interval-str"></a>

Interval

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### project_hires: `bool`<a id="project_hires-bool"></a>

Project future hires

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use html

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}/chart/{chartId}/data` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report_chart.get_all`<a id="charthopreport_chartget_all"></a>

Return all of the charts for a particular report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = charthop.report_chart.get_all(
    org_id="orgId_example",
    report_id="reportId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsReportChart`](./chart_hop_python_sdk/pydantic/results_report_chart.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}/chart` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report_chart.get_by_chart_id`<a id="charthopreport_chartget_by_chart_id"></a>

Return a particular report chart by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_chart_id_response = charthop.report_chart.get_by_chart_id(
    org_id="orgId_example",
    chart_id="chartId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### chart_id: `str`<a id="chart_id-str"></a>

Chart id

#### 🔄 Return<a id="🔄-return"></a>

[`ReportChart`](./chart_hop_python_sdk/pydantic/report_chart.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/chart/{chartId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report_chart.query_underlying_data_in_chart`<a id="charthopreport_chartquery_underlying_data_in_chart"></a>

Query for the underlying data in a chart

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_underlying_data_in_chart_response = charthop.report_chart.query_underlying_data_in_chart(
    org_id="orgId_example",
    report_id="reportId_example",
    chart_id="chartId_example",
    provided_query="string_example",
    start_date="string_example",
    end_date="string_example",
    interval="DAY",
    scenario_id="string_example",
    project_hires=True,
    change_grouping_type="PRIMARY",
    change_grouping_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### report_id: `str`<a id="report_id-str"></a>

Report id

##### chart_id: `str`<a id="chart_id-str"></a>

Chart id

##### provided_query: `str`<a id="provided_query-str"></a>

Query to run

##### start_date: `str`<a id="start_date-str"></a>

Start date, inclusive

##### end_date: `str`<a id="end_date-str"></a>

End date, exclusive

##### interval: `str`<a id="interval-str"></a>

Interval

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### project_hires: `bool`<a id="project_hires-bool"></a>

Project future hires

##### change_grouping_type: `str`<a id="change_grouping_type-str"></a>

Type of change grouping

##### change_grouping_id: `str`<a id="change_grouping_id-str"></a>

Change grouping id to query (null for primary)

#### 🔄 Return<a id="🔄-return"></a>

[`ReportMetricsReturnType`](./chart_hop_python_sdk/pydantic/report_metrics_return_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/{reportId}/chart/{chartId}/query` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report_chart.remove_by_id`<a id="charthopreport_chartremove_by_id"></a>

Delete a chart from a report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.report_chart.remove_by_id(
    org_id="orgId_example",
    chart_id="chartId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### chart_id: `str`<a id="chart_id-str"></a>

Chart id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/chart/{chartId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.report_chart.update_existing_chart_data`<a id="charthopreport_chartupdate_existing_chart_data"></a>

Update an existing report chart

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.report_chart.update_existing_chart_data(
    org_id="orgId_example",
    chart_id="chartId_example",
    label="Headcount Report",
    type="LINE",
    filter="department='Engineering'",
    filter_override=True,
    query={
        "interval": "DAY",
        "options": {},
    },
    sort=1,
    is_advanced_query_mode=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### chart_id: `str`<a id="chart_id-str"></a>

Chart id

##### label: `str`<a id="label-str"></a>

chart label

##### type: `str`<a id="type-str"></a>

chart type

##### filter: `str`<a id="filter-str"></a>

filter that applies to this chart

##### filter_override: `bool`<a id="filter_override-bool"></a>

whether the chart filter overrides the global filter

##### query: [`ReportQuery`](./chart_hop_python_sdk/type/report_query.py)<a id="query-reportquerychart_hop_python_sdktypereport_querypy"></a>


##### sort: `int`<a id="sort-int"></a>

sort order

##### is_advanced_query_mode: `bool`<a id="is_advanced_query_mode-bool"></a>

whether the chart configuration is using advanced mode

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateReportChart`](./chart_hop_python_sdk/type/update_report_chart.py)
Chart data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/report/chart/{chartId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.role.copy_existing_role`<a id="charthoprolecopy_existing_role"></a>

Copy an existing role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.role.copy_existing_role(
    org_id="orgId_example",
    role_id="roleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### role_id: `str`<a id="role_id-str"></a>

Role id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/role/{roleId}/copy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.role.create_new_role`<a id="charthoprolecreate_new_role"></a>

Create a role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_role_response = charthop.role.create_new_role(
    label="Engineering People Manager",
    org_id="orgId_example",
    description="This role is able to create and update new job data for the engineering department.",
    org_id="588f7ee98f138b19220041a7",
    policy_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`CreateRole`](./chart_hop_python_sdk/type/create_role.py)<a id="requestbody-createrolechart_hop_python_sdktypecreate_rolepy"></a>

Role data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Role`](./chart_hop_python_sdk/pydantic/role.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/role` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.role.get_all_in_org`<a id="charthoproleget_all_in_org"></a>

Return all or a set of roles in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_in_org_response = charthop.role.get_all_in_org(
    org_id="orgId_example",
    ids="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### ids: `str`<a id="ids-str"></a>

(Optional) Comma separated Role Ids to find

##### type: `str`<a id="type-str"></a>

(Optional) Return only default or custom roles

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsRole`](./chart_hop_python_sdk/pydantic/results_role.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/role` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.role.get_role_by_id`<a id="charthoproleget_role_by_id"></a>

Return a particular role by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_role_by_id_response = charthop.role.get_role_by_id(
    org_id="orgId_example",
    role_id="roleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### role_id: `str`<a id="role_id-str"></a>

Role id

#### 🔄 Return<a id="🔄-return"></a>

[`Role`](./chart_hop_python_sdk/pydantic/role.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/role/{roleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.role.remove_by_id`<a id="charthoproleremove_by_id"></a>

Delete a role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.role.remove_by_id(
    org_id="orgId_example",
    role_id="roleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### role_id: `str`<a id="role_id-str"></a>

Role id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/role/{roleId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.role.update_existing`<a id="charthoproleupdate_existing"></a>

Update an existing role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.role.update_existing(
    org_id="orgId_example",
    role_id="roleId_example",
    description="This role is able to create and update new job data for the engineering department.",
    label="Engineering People Manager",
    policy_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### role_id: `str`<a id="role_id-str"></a>

Role id

##### description: `str`<a id="description-str"></a>

description of role

##### label: `str`<a id="label-str"></a>

human-readable full name of role

##### policy_ids: [`UpdateRolePolicyIds`](./chart_hop_python_sdk/type/update_role_policy_ids.py)<a id="policy_ids-updaterolepolicyidschart_hop_python_sdktypeupdate_role_policy_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateRole`](./chart_hop_python_sdk/type/update_role.py)
Role data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/role/{roleId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.saml.perform_sso_assertion`<a id="charthopsamlperform_sso_assertion"></a>

Return an redirect to the designated Idp, given an identity provider

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.saml.perform_sso_assertion(
    org="org_example",
    idp="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org: `str`<a id="org-str"></a>

Org slug

##### idp: `str`<a id="idp-str"></a>

Identifier Provider

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saml/{org}/login` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.saml.perform_sso_assertion_0`<a id="charthopsamlperform_sso_assertion_0"></a>

Single sign on URL, where SAML assertion is perform

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.saml.perform_sso_assertion_0(
    org="org_example",
    token="string_example",
    saml_response="string_example",
    relay_state="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org: `str`<a id="org-str"></a>

Org slug

##### token: `str`<a id="token-str"></a>

##### saml_response: `str`<a id="saml_response-str"></a>

SAML Response

##### relay_state: `str`<a id="relay_state-str"></a>

Relay State

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SamlPerformSsoAssertionRequest`](./chart_hop_python_sdk/type/saml_perform_sso_assertion_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saml/sso/{org}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.saml.save_per_org_xml_cert_from_idp`<a id="charthopsamlsave_per_org_xml_cert_from_idp"></a>

Save per org Xml Cert from IDP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.saml.save_per_org_xml_cert_from_idp(
    org_id="orgId_example",
    idp="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### idp: `str`<a id="idp-str"></a>

Identifier Provider

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saml/org/{orgId}/xml-cert` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.saml.save_per_org_xml_cert_from_idp_0`<a id="charthopsamlsave_per_org_xml_cert_from_idp_0"></a>

Save per org Xml Cert from IDP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.saml.save_per_org_xml_cert_from_idp_0(
    org_id="orgId_example",
    file=open('/path/to/file', 'rb'),
    idp="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### file: `IO`<a id="file-io"></a>

##### idp: `str`<a id="idp-str"></a>

Identifier Provider

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saml/org/{orgId}/xml-cert` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.adjust_dates`<a id="charthopscenarioadjust_dates"></a>

Adjust the dates of the changes in a scenario

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
adjust_dates_response = charthop.scenario.adjust_dates(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    date="1970-01-01",
    days=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### date: `date`<a id="date-date"></a>

date to use as new start date

##### days: `int`<a id="days-int"></a>

number of days to adjust forward

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AdjustScenarioDateRequest`](./chart_hop_python_sdk/type/adjust_scenario_date_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}/dates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.bulk_archive_scenarios`<a id="charthopscenariobulk_archive_scenarios"></a>

Archive a set of scenarios

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_archive_scenarios_response = charthop.scenario.bulk_archive_scenarios(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`ScenarioBulkArchiveScenariosRequest`](./chart_hop_python_sdk/type/scenario_bulk_archive_scenarios_request.py)<a id="requestbody-scenariobulkarchivescenariosrequestchart_hop_python_sdktypescenario_bulk_archive_scenarios_requestpy"></a>

List of scenario ids to archive

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/bulk/archive` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.combine_scenarios`<a id="charthopscenariocombine_scenarios"></a>

Combine multiple scenarios into another scenario

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
combine_scenarios_response = charthop.scenario.combine_scenarios(
    scenario_ids=[
        "string_example"
    ],
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    copy_only=True,
    use_scenario_date_for_changes=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scenario_ids: [`CombineScenarioRequestScenarioIds`](./chart_hop_python_sdk/type/combine_scenario_request_scenario_ids.py)<a id="scenario_ids-combinescenariorequestscenarioidschart_hop_python_sdktypecombine_scenario_request_scenario_idspy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to combine the other scenarios into

##### copy_only: `bool`<a id="copy_only-bool"></a>

##### use_scenario_date_for_changes: `bool`<a id="use_scenario_date_for_changes-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CombineScenarioRequest`](./chart_hop_python_sdk/type/combine_scenario_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}/combine` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.create_new`<a id="charthopscenariocreate_new"></a>

Create a scenario

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = charthop.scenario.create_new(
    name="Q4 Conservative Plan",
    org_id="orgId_example",
    description="Q4 Conservative Plan",
    start_date="2017-01-15",
    status="OPEN",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    type="GENERAL",
    start_date_fixed="FIXED",
    query="string_example",
    valid_job_id_set=[
        "string_example"
    ],
    entity_id="string_example",
    entity_type="COMP_REVIEW",
    shared_view_config=[
        {
            "type": "ALL_CHANGES_GROUPED",
        }
    ],
    budget={
        "amount": 3.14,
        "currency": "currency_example",
    },
    cost_calc="string_example",
    silent=True,
    skip_change_creation=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

scenario name

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### description: `str`<a id="description-str"></a>

scenario description

##### start_date: `str`<a id="start_date-str"></a>

date that this scenario diverges from primary

##### status: `str`<a id="status-str"></a>

status of scenario

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who are specifically granted permission to this scenario

##### type: `str`<a id="type-str"></a>

Type of scenario to be created

##### start_date_fixed: `str`<a id="start_date_fixed-str"></a>

whether or not the start date should stay fixed in time, or update to today's date as time passes

##### query: `str`<a id="query-str"></a>

Query for selecting which people/jobs are initially included in the scenario (only applies to promotion scenarios)

##### valid_job_id_set: [`CreateScenarioValidJobIdSet`](./chart_hop_python_sdk/type/create_scenario_valid_job_id_set.py)<a id="valid_job_id_set-createscenariovalidjobidsetchart_hop_python_sdktypecreate_scenario_valid_job_id_setpy"></a>

##### entity_id: `str`<a id="entity_id-str"></a>

The entity this scenario is associated with

##### entity_type: `str`<a id="entity_type-str"></a>

The type of entity associated with this scenario

##### shared_view_config: List[`ScenarioSharedViewConfig`]<a id="shared_view_config-listscenariosharedviewconfig"></a>

View configurations associated with this scenario

##### budget: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="budget-moneychart_hop_python_sdktypemoneypy"></a>


##### cost_calc: `str`<a id="cost_calc-str"></a>

CQL used to calculate the budget allocation in the scenario

##### silent: `bool`<a id="silent-bool"></a>

Suppress notification emails

##### skip_change_creation: `bool`<a id="skip_change_creation-bool"></a>

Skip over change creation for PROMOTION scenarios

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateScenario`](./chart_hop_python_sdk/type/create_scenario.py)
Scenario data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Scenario`](./chart_hop_python_sdk/pydantic/scenario.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.delete_bulk_scenarios`<a id="charthopscenariodelete_bulk_scenarios"></a>

Delete a set of scenarios

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_bulk_scenarios_response = charthop.scenario.delete_bulk_scenarios(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`ScenarioDeleteBulkScenariosRequest`](./chart_hop_python_sdk/type/scenario_delete_bulk_scenarios_request.py)<a id="requestbody-scenariodeletebulkscenariosrequestchart_hop_python_sdktypescenario_delete_bulk_scenarios_requestpy"></a>

List of scenario ids to delete

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/bulk/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.get_by_id`<a id="charthopscenarioget_by_id"></a>

Return a particular scenario by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.scenario.get_by_id(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

#### 🔄 Return<a id="🔄-return"></a>

[`Scenario`](./chart_hop_python_sdk/pydantic/scenario.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.list_paginated_scenarios`<a id="charthopscenariolist_paginated_scenarios"></a>

Return all scenarios in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_paginated_scenarios_response = charthop.scenario.list_paginated_scenarios(
    org_id="orgId_example",
    _from="string_example",
    status="OPEN",
    limit=1,
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

Scenario id to start paginating from

##### status: `str`<a id="status-str"></a>

Scenario status to filter by

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsScenario`](./chart_hop_python_sdk/pydantic/results_scenario.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.manually_recalculate_metadata`<a id="charthopscenariomanually_recalculate_metadata"></a>

Manually recalculate a scenario's metadata

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
manually_recalculate_metadata_response = charthop.scenario.manually_recalculate_metadata(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

#### 🔄 Return<a id="🔄-return"></a>

[`ScenarioMetadata`](./chart_hop_python_sdk/pydantic/scenario_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}/recalculate-metadata` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.merge_into_primary_timeline`<a id="charthopscenariomerge_into_primary_timeline"></a>

Merge a scenario into the primary timeline

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
merge_into_primary_timeline_response = charthop.scenario.merge_into_primary_timeline(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    skip_errors=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to merge

##### skip_errors: `bool`<a id="skip_errors-bool"></a>

If passed, will skip any changes that fail validation

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}/merge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.remove_by_id`<a id="charthopscenarioremove_by_id"></a>

Delete a scenario

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.scenario.remove_by_id(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.unarchive_set_of_scenarios`<a id="charthopscenariounarchive_set_of_scenarios"></a>

Unarchive a set of scenarios

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unarchive_set_of_scenarios_response = charthop.scenario.unarchive_set_of_scenarios(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`ScenarioUnarchiveSetOfScenariosRequest`](./chart_hop_python_sdk/type/scenario_unarchive_set_of_scenarios_request.py)<a id="requestbody-scenariounarchivesetofscenariosrequestchart_hop_python_sdktypescenario_unarchive_set_of_scenarios_requestpy"></a>

List of scenario ids to unarchive

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/bulk/unarchive` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.update_scenario_change`<a id="charthopscenarioupdate_scenario_change"></a>

Update an existing scenario

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.scenario.update_scenario_change(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    description="Q4 Conservative Plan",
    name="Q4 Conservative Plan",
    start_date="2017-01-15",
    status="OPEN",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
    start_date_fixed="FIXED",
    valid_job_id_set=[
        "string_example"
    ],
    entity_id="string_example",
    entity_type="COMP_REVIEW",
    shared_view_config=[
        {
            "type": "ALL_CHANGES_GROUPED",
        }
    ],
    budget={
        "amount": 3.14,
        "currency": "currency_example",
    },
    cost_calc="string_example",
    silent=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### description: `str`<a id="description-str"></a>

scenario description

##### name: `str`<a id="name-str"></a>

scenario name

##### start_date: `str`<a id="start_date-str"></a>

date that this scenario diverges from primary

##### status: `str`<a id="status-str"></a>

status of scenario

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who are specifically granted permission to this scenario

##### start_date_fixed: `str`<a id="start_date_fixed-str"></a>

whether or not the start date should stay fixed in time, or update to today's date as time passes

##### valid_job_id_set: [`UpdateScenarioValidJobIdSet`](./chart_hop_python_sdk/type/update_scenario_valid_job_id_set.py)<a id="valid_job_id_set-updatescenariovalidjobidsetchart_hop_python_sdktypeupdate_scenario_valid_job_id_setpy"></a>

##### entity_id: `str`<a id="entity_id-str"></a>

The entity this scenario is associated with

##### entity_type: `str`<a id="entity_type-str"></a>

The type of entity associated with this scenario

##### shared_view_config: List[`ScenarioSharedViewConfig`]<a id="shared_view_config-listscenariosharedviewconfig"></a>

View configurations associated with this scenario

##### budget: [`Money`](./chart_hop_python_sdk/type/money.py)<a id="budget-moneychart_hop_python_sdktypemoneypy"></a>


##### cost_calc: `str`<a id="cost_calc-str"></a>

CQL used to calculate the budget allocation in the scenario

##### silent: `bool`<a id="silent-bool"></a>

Suppress notification emails

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateScenario`](./chart_hop_python_sdk/type/update_scenario.py)
Scenario data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.scenario.update_shared_view_config`<a id="charthopscenarioupdate_shared_view_config"></a>

Update a scenario view config

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.scenario.update_shared_view_config(
    org_id="orgId_example",
    scenario_id="scenarioId_example",
    custom_column_names=[
        "string_example"
    ],
    column_widths={
        "key": 1,
    },
    type="ALL_CHANGES_GROUPED",
    update_id="string_example",
    update_at=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id

##### custom_column_names: [`ScenarioSharedViewConfigCustomColumnNames`](./chart_hop_python_sdk/type/scenario_shared_view_config_custom_column_names.py)<a id="custom_column_names-scenariosharedviewconfigcustomcolumnnameschart_hop_python_sdktypescenario_shared_view_config_custom_column_namespy"></a>

##### column_widths: [`ScenarioSharedViewConfigColumnWidths`](./chart_hop_python_sdk/type/scenario_shared_view_config_column_widths.py)<a id="column_widths-scenariosharedviewconfigcolumnwidthschart_hop_python_sdktypescenario_shared_view_config_column_widthspy"></a>

##### type: `str`<a id="type-str"></a>

type of view

##### update_id: `str`<a id="update_id-str"></a>

update id

##### update_at: `int`<a id="update_at-int"></a>

update at

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ScenarioSharedViewConfig`](./chart_hop_python_sdk/type/scenario_shared_view_config.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/scenario/{scenarioId}/update-shared-view` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.search.org_data_by_org_id_and_search_string`<a id="charthopsearchorg_data_by_org_id_and_search_string"></a>

Return people, job, group, and field data for a particular org that match a provided search string

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
org_data_by_org_id_and_search_string_response = charthop.search.org_data_by_org_id_and_search_string(
    org_id="orgId_example",
    q="string_example",
    entity_types="string_example",
    limit=1,
    include_former=True,
    date="1970-01-01",
    scenario_id="string_example",
    can_access="string_example",
    include_external_recruiter=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### q: `str`<a id="q-str"></a>

Query search term

##### entity_types: `str`<a id="entity_types-str"></a>

Entity types

##### limit: `int`<a id="limit-int"></a>

Limit

##### include_former: `bool`<a id="include_former-bool"></a>

Include former users or persons

##### date: `date`<a id="date-date"></a>

Date

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario Id

##### can_access: `str`<a id="can_access-str"></a>

entity action pairs that can be accessed

##### include_external_recruiter: `bool`<a id="include_external_recruiter-bool"></a>

Include External Recruiter

#### 🔄 Return<a id="🔄-return"></a>

[`SearchResultResponse`](./chart_hop_python_sdk/pydantic/search_result_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.status.api_is_up_and_available`<a id="charthopstatusapi_is_up_and_available"></a>

Returns true if the API is up and available

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
api_is_up_and_available_response = charthop.status.api_is_up_and_available()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OkResponse`](./chart_hop_python_sdk/pydantic/ok_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stock.get_history`<a id="charthopstockget_history"></a>

Return the history of stock prices

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_history_response = charthop.stock.get_history(
    symbol="string_example",
    type="string_example",
    _from="1970-01-01",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### symbol: `str`<a id="symbol-str"></a>

Symbol to query

##### type: `str`<a id="type-str"></a>

Types of valuations to retrieve

##### _from: `date`<a id="_from-date"></a>

Date to start from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsStockPrice`](./chart_hop_python_sdk/pydantic/results_stock_price.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stock` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stock.get_price_by_date_type`<a id="charthopstockget_price_by_date_type"></a>

Get a stock price as of a particular date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_price_by_date_type_response = charthop.stock.get_price_by_date_type(
    symbol="symbol_example",
    date="1970-01-01",
    type="type_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### symbol: `str`<a id="symbol-str"></a>

Stock symbol

##### date: `date`<a id="date-date"></a>

Date to update information for

##### type: `str`<a id="type-str"></a>

Type of stock price to retrieve (for example 'public')

#### 🔄 Return<a id="🔄-return"></a>

[`StockPrice`](./chart_hop_python_sdk/pydantic/stock_price.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stock/{symbol}/{date}/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stock.remove_price`<a id="charthopstockremove_price"></a>

Delete a stock price

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.stock.remove_price(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Stock entry id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stock/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stock.upsert_price_by_date_type`<a id="charthopstockupsert_price_by_date_type"></a>

Upsert a stock price

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upsert_price_by_date_type_response = charthop.stock.upsert_price_by_date_type(
    symbol="symbol_example",
    date="1970-01-01",
    type="type_example",
    org_id="588f7ee98f138b19220041a7",
    price=3.14,
    total=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### symbol: `str`<a id="symbol-str"></a>

Stock symbol

##### date: `date`<a id="date-date"></a>

Date to update information for

##### type: `str`<a id="type-str"></a>

Type of stock price to upsert

##### org_id: `str`<a id="org_id-str"></a>

org id that this stock price derives from

##### price: `Union[int, float]`<a id="price-unionint-float"></a>

price per share

##### total: `int`<a id="total-int"></a>

total shares outstanding

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateStockPrice`](./chart_hop_python_sdk/type/update_stock_price.py)
Stock price data to create

#### 🔄 Return<a id="🔄-return"></a>

[`StockPrice`](./chart_hop_python_sdk/pydantic/stock_price.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stock/{symbol}/{date}/{type}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stripe.create_setup_intent_secret`<a id="charthopstripecreate_setup_intent_secret"></a>

Creates a Stripe setupIntent object and returns the secret for that object

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_setup_intent_secret_response = charthop.stripe.create_setup_intent_secret()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SetupIntent`](./chart_hop_python_sdk/pydantic/setup_intent.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stripe/setup-intent` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stripe.get_all_plans`<a id="charthopstripeget_all_plans"></a>

Return all billing plans directly from Stripe (staff only)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_plans_response = charthop.stripe.get_all_plans()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsPlan`](./chart_hop_python_sdk/pydantic/results_plan.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stripe/plan` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stripe.get_all_products`<a id="charthopstripeget_all_products"></a>

Return all products directly from Stripe (staff only)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_products_response = charthop.stripe.get_all_products()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsStripeProduct`](./chart_hop_python_sdk/pydantic/results_stripe_product.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stripe/product` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stripe.get_product_by_id`<a id="charthopstripeget_product_by_id"></a>

Return a particular product by its Stripe id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_product_by_id_response = charthop.stripe.get_product_by_id(
    product_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_id: `str`<a id="product_id-str"></a>

Stripe product id

#### 🔄 Return<a id="🔄-return"></a>

[`StripeProduct`](./chart_hop_python_sdk/pydantic/stripe_product.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stripe/product/{productId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.stripe.process_webhook_events`<a id="charthopstripeprocess_webhook_events"></a>

Process webhook events from Stripe

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.stripe.process_webhook_events(
    body="string_example",
    stripe_signature="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### stripe_signature: `str`<a id="stripe_signature-str"></a>

##### requestBody: `str`<a id="requestbody-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/stripe/webhook` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.create_new_table`<a id="charthoptablecreate_new_table"></a>

Create a table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_table_response = charthop.table.create_new_table(
    name="budget-data",
    effective_dated=True,
    org_id="orgId_example",
    label="Budget Data",
    sensitive="GLOBAL",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

name of table

##### effective_dated: `bool`<a id="effective_dated-bool"></a>

whether or not the table is time tracked with effective dates (allows time travel or not). If false, then the values set in the table will be the same across all dates.

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### label: `str`<a id="label-str"></a>

human readable label for the table

##### sensitive: `str`<a id="sensitive-str"></a>

base sensitivity of this table and entities in it -- should be either ORG or HIGH

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who are specifically granted permission to this table

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTable`](./chart_hop_python_sdk/type/create_table.py)
Table data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Table`](./chart_hop_python_sdk/pydantic/table.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.delete_row`<a id="charthoptabledelete_row"></a>

Delete an existing row

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_row_response = charthop.table.delete_row(
    org_id="orgId_example",
    table_id="tableId_example",
    key_column="keyColumn_example",
    key_value="keyValue_example",
    date="1970-01-01",
    scenario_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or unique name to update

##### key_column: `str`<a id="key_column-str"></a>

Column name to look up the row by (for example: id)

##### key_value: `str`<a id="key_value-str"></a>

Value of the key column

##### date: `date`<a id="date-date"></a>

Date to delete as of

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to delete from

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}/data/{keyColumn}/{keyValue}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.delete_row_from_history`<a id="charthoptabledelete_row_from_history"></a>

Delete an existing row, purging from history entirely

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_row_from_history_response = charthop.table.delete_row_from_history(
    org_id="orgId_example",
    table_id="tableId_example",
    key_column="keyColumn_example",
    key_value="keyValue_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or unique name to update

##### key_column: `str`<a id="key_column-str"></a>

Column name to look up the row by (for example: id)

##### key_value: `str`<a id="key_value-str"></a>

Value of the key column

##### date: `date`<a id="date-date"></a>

Date to look up as of

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}/data/{keyColumn}/{keyValue}/purge` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.export_data_to_csv`<a id="charthoptableexport_data_to_csv"></a>

Export table data to CSV file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
export_data_to_csv_response = charthop.table.export_data_to_csv(
    org_id="orgId_example",
    table_id="tableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or unique name to update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExportChangelogToCsvRequest`](./chart_hop_python_sdk/type/export_changelog_to_csv_request.py)
export options

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}/export` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.get_all_rows`<a id="charthoptableget_all_rows"></a>

Retrieve all rows from the table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_rows_response = charthop.table.get_all_rows(
    org_id="orgId_example",
    table_id="tableId_example",
    date="1970-01-01",
    scenario_id="string_example",
    columns="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or unique name to retrieve

##### date: `date`<a id="date-date"></a>

Date to search as of

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to retrieve from

##### columns: `str`<a id="columns-str"></a>

Columns to retrieve, comma-separated (defaults to all columns)

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended, json-readable, or csv

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}/data` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.get_row_by_column`<a id="charthoptableget_row_by_column"></a>

Retrieve a particular row

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_row_by_column_response = charthop.table.get_row_by_column(
    org_id="orgId_example",
    table_id="tableId_example",
    key_column="keyColumn_example",
    key_value="keyValue_example",
    date="1970-01-01",
    scenario_id="string_example",
    columns="string_example",
    format="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or unique name to retrieve

##### key_column: `str`<a id="key_column-str"></a>

Column name to look up the row by (for example: id)

##### key_value: `str`<a id="key_value-str"></a>

Value of the column

##### date: `date`<a id="date-date"></a>

Date to search as of

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to retrieve from

##### columns: `str`<a id="columns-str"></a>

Columns to retrieve, comma-separated (defaults to all columns)

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended, json-readable, or csv

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}/data/{keyColumn}/{keyValue}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.get_table_by_id_or_name`<a id="charthoptableget_table_by_id_or_name"></a>

Return a particular table by id or name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_table_by_id_or_name_response = charthop.table.get_table_by_id_or_name(
    org_id="orgId_example",
    table_id="tableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or name

#### 🔄 Return<a id="🔄-return"></a>

[`Table`](./chart_hop_python_sdk/pydantic/table.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.import_data_from_csv_file`<a id="charthoptableimport_data_from_csv_file"></a>

Import data from CSV file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_data_from_csv_file_response = charthop.table.import_data_from_csv_file(
    org_id="orgId_example",
    table_id="tableId_example",
    file=open('/path/to/file', 'rb'),
    date="1970-01-01",
    import_from_process_id="string_example",
    parent_process_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or unique name to update

##### file: `IO`<a id="file-io"></a>

##### date: `date`<a id="date-date"></a>

Date to update as of

##### import_from_process_id: `str`<a id="import_from_process_id-str"></a>

Import a file from another process, instead of directly uploading it

##### parent_process_id: `str`<a id="parent_process_id-str"></a>

Parent process id to attach to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUploadNewFileRequest`](./chart_hop_python_sdk/type/file_upload_new_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}/import` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.list_in_org_paginated`<a id="charthoptablelist_in_org_paginated"></a>

Return all tables in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_in_org_paginated_response = charthop.table.list_in_org_paginated(
    org_id="orgId_example",
    _from="string_example",
    limit=1,
    include_built_ins=True,
    names="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

Table id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### include_built_ins: `bool`<a id="include_built_ins-bool"></a>

Whether to include built-in tables

##### names: `str`<a id="names-str"></a>

Table names to filter to

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsTable`](./chart_hop_python_sdk/pydantic/results_table.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.remove_by_id`<a id="charthoptableremove_by_id"></a>

Delete a table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.table.remove_by_id(
    org_id="orgId_example",
    table_id="tableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.update_existing_row_data`<a id="charthoptableupdate_existing_row_data"></a>

Update an existing row

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_row_data_response = charthop.table.update_existing_row_data(
    org_id="orgId_example",
    table_id="tableId_example",
    key_column="keyColumn_example",
    key_value="keyValue_example",
    date="1970-01-01",
    scenario_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or unique name to update

##### key_column: `str`<a id="key_column-str"></a>

Column name to look up the row by (for example: id)

##### key_value: `str`<a id="key_value-str"></a>

Value of the key column

##### date: `date`<a id="date-date"></a>

Date to update as of

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}/data/{keyColumn}/{keyValue}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.update_existing_table`<a id="charthoptableupdate_existing_table"></a>

Update an existing table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.table.update_existing_table(
    org_id="orgId_example",
    table_id="tableId_example",
    name="budget-data",
    label="Budget Data",
    label_column_id="string_example",
    effective_dated=True,
    sensitive="GLOBAL",
    share_access=[
        {
            "access": "NONE",
            "user_id": "5887a7718f138b6a2a0041a7",
            "group_id": "5887a7718f138b6a2a0041a7",
            "fields": "name,image,title",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or name

##### name: `str`<a id="name-str"></a>

name of table

##### label: `str`<a id="label-str"></a>

human readable label for the table

##### label_column_id: `str`<a id="label_column_id-str"></a>

if set, use this column id as the label when referencing rows

##### effective_dated: `bool`<a id="effective_dated-bool"></a>

whether or not the table is time tracked with effective dates (allows time travel or not). If false, then the values set in the table will be the same across all dates.

##### sensitive: `str`<a id="sensitive-str"></a>

base sensitivity of this table and entities in it -- should be either ORG or HIGH

##### share_access: List[`ShareAccess`]<a id="share_access-listshareaccess"></a>

users who are specifically granted permission to this table

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTable`](./chart_hop_python_sdk/type/update_table.py)
Table data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.table.upsert_row_data`<a id="charthoptableupsert_row_data"></a>

Upsert row data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upsert_row_data_response = charthop.table.upsert_row_data(
    org_id="orgId_example",
    table_id="tableId_example",
    date="1970-01-01",
    scenario_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### table_id: `str`<a id="table_id-str"></a>

Table id or unique name to update

##### date: `date`<a id="date-date"></a>

Date to update as of

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppRunInstalledAppRequest`](./chart_hop_python_sdk/type/app_run_installed_app_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/table/{tableId}/data` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.delete_bulk_tasks`<a id="charthoptaskdelete_bulk_tasks"></a>

Bulk delete tasks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_bulk_tasks_response = charthop.task.delete_bulk_tasks(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`TaskDeleteBulkTasksRequest`](./chart_hop_python_sdk/type/task_delete_bulk_tasks_request.py)<a id="requestbody-taskdeletebulktasksrequestchart_hop_python_sdktypetask_delete_bulk_tasks_requestpy"></a>

List of task ids to delete

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/bulk-delete` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.get_all_tasks`<a id="charthoptaskget_all_tasks"></a>

Return all existing tasks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_tasks_response = charthop.task.get_all_tasks(
    org_id="orgId_example",
    user_id="string_example",
    assessment_id="string_example",
    status="string_example",
    type="string_example",
    entity_id="string_example",
    target_id="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### user_id: `str`<a id="user_id-str"></a>

Task User id

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

##### status: `str`<a id="status-str"></a>

Task.Status. (PENDING/DONE)

##### type: `str`<a id="type-str"></a>

Task.Type of task (form)

##### entity_id: `str`<a id="entity_id-str"></a>

Entity Id

##### target_id: `str`<a id="target_id-str"></a>

Target Id

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsTask`](./chart_hop_python_sdk/pydantic/results_task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.get_assessment_tasks_summary`<a id="charthoptaskget_assessment_tasks_summary"></a>

Return the tasks for a given assessment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.task.get_assessment_tasks_summary(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/summary/{assessmentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.get_current_user_tasks`<a id="charthoptaskget_current_user_tasks"></a>

Return the tasks for the current user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_user_tasks_response = charthop.task.get_current_user_tasks(
    org_id="orgId_example",
    assessment_id="string_example",
    status="string_example",
    type="string_example",
    entity_id="string_example",
    target_id="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

##### status: `str`<a id="status-str"></a>

Task.Status. (PENDING/ACTIVE)

##### type: `str`<a id="type-str"></a>

Task.Type of task (form)

##### entity_id: `str`<a id="entity_id-str"></a>

Entity Id

##### target_id: `str`<a id="target_id-str"></a>

Target Id

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsTask`](./chart_hop_python_sdk/pydantic/results_task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.mark_as_skipped`<a id="charthoptaskmark_as_skipped"></a>

Skip task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.task.mark_as_skipped(
    org_id="orgId_example",
    task_id="taskId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### task_id: `str`<a id="task_id-str"></a>

Task id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/{taskId}/skip` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.query_assessment_tasks`<a id="charthoptaskquery_assessment_tasks"></a>

Query tasks for assessments in the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_assessment_tasks_response = charthop.task.query_assessment_tasks(
    org_id="orgId_example",
    user_id="string_example",
    assessment_id="string_example",
    status="string_example",
    type="string_example",
    entity_id="string_example",
    target_id="string_example",
    limit=1,
    fields="string_example",
    format="string_example",
    _from="string_example",
    return_access="string_example",
    return_form_completion_links=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### user_id: `str`<a id="user_id-str"></a>

Task User id

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

##### status: `str`<a id="status-str"></a>

Task.Status. (PENDING/DONE)

##### type: `str`<a id="type-str"></a>

Task.Type. (FORM_SUBMIT/CHANGE_APPROVE)

##### entity_id: `str`<a id="entity_id-str"></a>

Entity Id

##### target_id: `str`<a id="target_id-str"></a>

Target Id

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### fields: `str`<a id="fields-str"></a>

Fields to retrieve, comma-separated

##### format: `str`<a id="format-str"></a>

Data format to use; default is json, can also use json-extended or json-readable

##### _from: `str`<a id="_from-str"></a>

Job id to start paginating from

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

##### return_form_completion_links: `bool`<a id="return_form_completion_links-bool"></a>

Return links that employees would use to complete a task if true else return links that direct to the form settings

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/task` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.remove_by_id`<a id="charthoptaskremove_by_id"></a>

Delete task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.task.remove_by_id(
    org_id="orgId_example",
    task_id="taskId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### task_id: `str`<a id="task_id-str"></a>

Task id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/{taskId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.remove_form_from_assessment`<a id="charthoptaskremove_form_from_assessment"></a>

Delete task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.task.remove_form_from_assessment(
    org_id="orgId_example",
    assessment_id="assessmentId_example",
    form_id="formId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### assessment_id: `str`<a id="assessment_id-str"></a>

Assessment id

##### form_id: `str`<a id="form_id-str"></a>

Form id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/{assessmentId}/{formId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.send_reminder_notification`<a id="charthoptasksend_reminder_notification"></a>

Send a reminder notification for a particular task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.task.send_reminder_notification(
    task_ids=[
        "string_example"
    ],
    org_id="orgId_example",
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_ids: [`TaskRemindRequestTaskIds`](./chart_hop_python_sdk/type/task_remind_request_task_ids.py)<a id="task_ids-taskremindrequesttaskidschart_hop_python_sdktypetask_remind_request_task_idspy"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### message: `str`<a id="message-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskRemindRequest`](./chart_hop_python_sdk/type/task_remind_request.py)
Request body

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/remind` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task.update_status`<a id="charthoptaskupdate_status"></a>

Mark task done

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.task.update_status(
    org_id="orgId_example",
    task_id="taskId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### task_id: `str`<a id="task_id-str"></a>

Task id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task/{taskId}/mark-done` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task_config.create_new_config`<a id="charthoptask_configcreate_new_config"></a>

Create a new task config

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_config_response = charthop.task_config.create_new_config(
    entity_id="588f7ee98f138b19220041a7",
    type="FORM_SUBMIT",
    past_due_action="NONE",
    org_id="orgId_example",
    description="string_example",
    assessment_id="588f7ee98f138b19220041a7",
    parent_entity_id="588f7ee98f138b19220041a7",
    due_date={
        "type": "EXACT",
        "due_day": "due_day_example",
        "due_time": "due_time_example",
    },
    is_skippable=True,
    label="string_example",
    delete_id="588f7ee98f138b19220041a7",
    delete_at="2017-01-24T13:57:52Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### entity_id: `str`<a id="entity_id-str"></a>

the primary entity being referenced by the task config

##### type: `str`<a id="type-str"></a>

type of task generated by the task config

##### past_due_action: `str`<a id="past_due_action-str"></a>

sets pastDueAction on the task when it's generated

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug

##### description: `str`<a id="description-str"></a>

description for all tasks associated with the config that should be used in notifications

##### assessment_id: `str`<a id="assessment_id-str"></a>

parent assessment id that this task config belongs to

##### parent_entity_id: `str`<a id="parent_entity_id-str"></a>

parent entity id that this task config belongs to, should be used with entityId

##### due_date: [`DueDate`](./chart_hop_python_sdk/type/due_date.py)<a id="due_date-duedatechart_hop_python_sdktypedue_datepy"></a>


##### is_skippable: `bool`<a id="is_skippable-bool"></a>

sets isSkippable on the task

##### label: `str`<a id="label-str"></a>

human-readable label that should be used for all tasks associated with the config as the task name

##### delete_id: `str`<a id="delete_id-str"></a>

deleted by user id

##### delete_at: `str`<a id="delete_at-str"></a>

deleted timestamp

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTaskConfig`](./chart_hop_python_sdk/type/create_task_config.py)
Task config to create

#### 🔄 Return<a id="🔄-return"></a>

[`TaskConfig`](./chart_hop_python_sdk/pydantic/task_config.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task-config` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task_config.get_all_configs`<a id="charthoptask_configget_all_configs"></a>

Get all task configs for an org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_configs_response = charthop.task_config.get_all_configs(
    org_id="orgId_example",
    _from="string_example",
    parent_entity_id="string_example",
    assessment_id="string_example",
    entity_id="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### _from: `str`<a id="_from-str"></a>

TaskConfig id to start paginating from

##### parent_entity_id: `str`<a id="parent_entity_id-str"></a>

ParentEntityId to query for

##### assessment_id: `str`<a id="assessment_id-str"></a>

AssessmentId to query for

##### entity_id: `str`<a id="entity_id-str"></a>

EntityId to query for

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsData`](./chart_hop_python_sdk/pydantic/results_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task-config` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.task_config.get_specific_config`<a id="charthoptask_configget_specific_config"></a>

Get a specific task config

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_config_response = charthop.task_config.get_specific_config(
    org_id="orgId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### id: `str`<a id="id-str"></a>

ID of the desired task config

#### 🔄 Return<a id="🔄-return"></a>

[`TaskConfig`](./chart_hop_python_sdk/pydantic/task_config.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/task-config/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.bulk_delete`<a id="charthoptemplatebulk_delete"></a>

Delete a set of templates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_delete_response = charthop.template.bulk_delete(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`TemplateBulkDeleteRequest`](./chart_hop_python_sdk/type/template_bulk_delete_request.py)<a id="requestbody-templatebulkdeleterequestchart_hop_python_sdktypetemplate_bulk_delete_requestpy"></a>

List of template ids to delete

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/bulk/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.create_bulk_duplicate`<a id="charthoptemplatecreate_bulk_duplicate"></a>

Duplicate a set of templates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bulk_duplicate_response = charthop.template.create_bulk_duplicate(
    body=[
        "string_example"
    ],
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### requestBody: [`TemplateCreateBulkDuplicateRequest`](./chart_hop_python_sdk/type/template_create_bulk_duplicate_request.py)<a id="requestbody-templatecreatebulkduplicaterequestchart_hop_python_sdktypetemplate_create_bulk_duplicate_requestpy"></a>

List of template ids to duplicate

#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/bulk/duplicate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.create_email`<a id="charthoptemplatecreate_email"></a>

Create a template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_response = charthop.template.create_email(
    name="string_example",
    content="string_example",
    tags=[
        "string_example"
    ],
    description="string_example",
    stylesheet="string_example",
    type="DOCUMENT",
    filename="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

template name, must be unique to organization

##### content: `str`<a id="content-str"></a>

template content

##### tags: [`CreateTemplateTags`](./chart_hop_python_sdk/type/create_template_tags.py)<a id="tags-createtemplatetagschart_hop_python_sdktypecreate_template_tagspy"></a>

##### description: `str`<a id="description-str"></a>

description of template

##### stylesheet: `str`<a id="stylesheet-str"></a>

template inline stylesheet

##### type: `str`<a id="type-str"></a>

type of template

##### filename: `str`<a id="filename-str"></a>

document filename CQL

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTemplate`](./chart_hop_python_sdk/type/create_template.py)
Template data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./chart_hop_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.create_new_template`<a id="charthoptemplatecreate_new_template"></a>

Create a template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_template_response = charthop.template.create_new_template(
    name="string_example",
    content="string_example",
    org_id="orgId_example",
    tags=[
        "string_example"
    ],
    description="string_example",
    stylesheet="string_example",
    type="DOCUMENT",
    filename="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

template name, must be unique to organization

##### content: `str`<a id="content-str"></a>

template content

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### tags: [`CreateTemplateTags`](./chart_hop_python_sdk/type/create_template_tags.py)<a id="tags-createtemplatetagschart_hop_python_sdktypecreate_template_tagspy"></a>

##### description: `str`<a id="description-str"></a>

description of template

##### stylesheet: `str`<a id="stylesheet-str"></a>

template inline stylesheet

##### type: `str`<a id="type-str"></a>

type of template

##### filename: `str`<a id="filename-str"></a>

document filename CQL

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTemplate`](./chart_hop_python_sdk/type/create_template.py)
Template data to create

#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./chart_hop_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.evaluate_against_job`<a id="charthoptemplateevaluate_against_job"></a>

Render a template by evaluating it against an existing job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
evaluate_against_job_response = charthop.template.evaluate_against_job(
    org_id="orgId_example",
    template_id="templateId_example",
    job_id="string_example",
    scenario_id="string_example",
    date="1970-01-01",
    format="TEXT",
    change_grouping_type="PRIMARY",
    change_grouping_id="string_example",
    use_scenario_changes=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### template_id: `str`<a id="template_id-str"></a>

Template id

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date

##### format: `str`<a id="format-str"></a>

Format

##### change_grouping_type: `str`<a id="change_grouping_type-str"></a>

Type of change grouping

##### change_grouping_id: `str`<a id="change_grouping_id-str"></a>

Change grouping id to query (null for primary)

##### use_scenario_changes: `bool`<a id="use_scenario_changes-bool"></a>

Generate documents for only the changes that are in the scenario. This option also allows you to reference the change within the template, which is otherwise not allowed

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateRenderResponse`](./chart_hop_python_sdk/pydantic/template_render_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/{templateId}/render` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.generate_pdfs_and_emails`<a id="charthoptemplategenerate_pdfs_and_emails"></a>

Automatically generate PDFs of the templates, and distribute emails to managers and people to download

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_pdfs_and_emails_response = charthop.template.generate_pdfs_and_emails(
    save_to_files=True,
    send_to_managers=True,
    send_to_persons=True,
    use_scenario_changes=True,
    org_id="orgId_example",
    template_id="templateId_example",
    filter="string_example",
    email_subject="string_example",
    email_message="string_example",
    file_sensitive="GLOBAL",
    file_field="string_example",
    scenario_id="string_example",
    date="1970-01-01",
    change_grouping_type="PRIMARY",
    change_grouping_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### save_to_files: `bool`<a id="save_to_files-bool"></a>

##### send_to_managers: `bool`<a id="send_to_managers-bool"></a>

##### send_to_persons: `bool`<a id="send_to_persons-bool"></a>

##### use_scenario_changes: `bool`<a id="use_scenario_changes-bool"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### template_id: `str`<a id="template_id-str"></a>

Template id

##### filter: `str`<a id="filter-str"></a>

##### email_subject: `str`<a id="email_subject-str"></a>

##### email_message: `str`<a id="email_message-str"></a>

##### file_sensitive: `str`<a id="file_sensitive-str"></a>

##### file_field: `str`<a id="file_field-str"></a>

##### scenario_id: `str`<a id="scenario_id-str"></a>

##### date: `date`<a id="date-date"></a>

##### change_grouping_type: `str`<a id="change_grouping_type-str"></a>

##### change_grouping_id: `str`<a id="change_grouping_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GenerateTemplateRequest`](./chart_hop_python_sdk/type/generate_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Process`](./chart_hop_python_sdk/pydantic/process.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/{templateId}/generate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.generate_template_preview`<a id="charthoptemplategenerate_template_preview"></a>

Preview template content without saving it

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_template_preview_response = charthop.template.generate_template_preview(
    content="string_example",
    org_id="orgId_example",
    stylesheet="string_example",
    job_id="string_example",
    scenario_id="string_example",
    date="1970-01-01",
    format="TEXT",
    change_grouping_type="PRIMARY",
    change_grouping_id="string_example",
    use_scenario_changes=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### content: `str`<a id="content-str"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### stylesheet: `str`<a id="stylesheet-str"></a>

##### job_id: `str`<a id="job_id-str"></a>

Job id

##### scenario_id: `str`<a id="scenario_id-str"></a>

Scenario id to query

##### date: `date`<a id="date-date"></a>

Date

##### format: `str`<a id="format-str"></a>

Format

##### change_grouping_type: `str`<a id="change_grouping_type-str"></a>

Type of change grouping

##### change_grouping_id: `str`<a id="change_grouping_id-str"></a>

Change grouping id to query (null for primary)

##### use_scenario_changes: `bool`<a id="use_scenario_changes-bool"></a>

Generate documents for only the changes that are in the scenario. This option also allows you to reference the change within the template, which is otherwise not allowed

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TemplatePreviewRequest`](./chart_hop_python_sdk/type/template_preview_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TemplateRenderResponse`](./chart_hop_python_sdk/pydantic/template_render_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/{templateId}/preview` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.get_all_in_orgs`<a id="charthoptemplateget_all_in_orgs"></a>

Return all templates in the organization paginated

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_in_orgs_response = charthop.template.get_all_in_orgs(
    org_id="orgId_example",
    type="DOCUMENT",
    _from="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Type of template to filter by

##### _from: `str`<a id="_from-str"></a>

Template id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsTemplate`](./chart_hop_python_sdk/pydantic/results_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.get_by_id`<a id="charthoptemplateget_by_id"></a>

Return a particular template by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = charthop.template.get_by_id(
    org_id="orgId_example",
    template_id="templateId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### template_id: `str`<a id="template_id-str"></a>

Template id

#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./chart_hop_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/{templateId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.get_by_name`<a id="charthoptemplateget_by_name"></a>

Return a particular email template by name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_name_response = charthop.template.get_by_name(
    template_name="templateName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_name: `str`<a id="template_name-str"></a>

Template name

#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./chart_hop_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/email/{templateName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.remove_by_id`<a id="charthoptemplateremove_by_id"></a>

Delete a template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.template.remove_by_id(
    org_id="orgId_example",
    template_id="templateId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### template_id: `str`<a id="template_id-str"></a>

Template id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/{templateId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.remove_email`<a id="charthoptemplateremove_email"></a>

Delete a template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.template.remove_email(
    template_name="templateName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_name: `str`<a id="template_name-str"></a>

Template name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/email/{templateName}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.update_email_template`<a id="charthoptemplateupdate_email_template"></a>

Update an existing template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.template.update_email_template(
    template_name="templateName_example",
    tags=[
        "string_example"
    ],
    description="string_example",
    name="string_example",
    content="string_example",
    stylesheet="string_example",
    type="DOCUMENT",
    filename="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_name: `str`<a id="template_name-str"></a>

Template name

##### tags: [`UpdateTemplateTags`](./chart_hop_python_sdk/type/update_template_tags.py)<a id="tags-updatetemplatetagschart_hop_python_sdktypeupdate_template_tagspy"></a>

##### description: `str`<a id="description-str"></a>

description of template

##### name: `str`<a id="name-str"></a>

template name, must be unique to organization

##### content: `str`<a id="content-str"></a>

template content

##### stylesheet: `str`<a id="stylesheet-str"></a>

template inline stylesheet

##### type: `str`<a id="type-str"></a>

type of template

##### filename: `str`<a id="filename-str"></a>

document filename CQL

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTemplate`](./chart_hop_python_sdk/type/update_template.py)
Template data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/email/{templateName}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.template.update_existing`<a id="charthoptemplateupdate_existing"></a>

Update an existing template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.template.update_existing(
    org_id="orgId_example",
    template_id="templateId_example",
    tags=[
        "string_example"
    ],
    description="string_example",
    name="string_example",
    content="string_example",
    stylesheet="string_example",
    type="DOCUMENT",
    filename="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### template_id: `str`<a id="template_id-str"></a>

Template id

##### tags: [`UpdateTemplateTags`](./chart_hop_python_sdk/type/update_template_tags.py)<a id="tags-updatetemplatetagschart_hop_python_sdktypeupdate_template_tagspy"></a>

##### description: `str`<a id="description-str"></a>

description of template

##### name: `str`<a id="name-str"></a>

template name, must be unique to organization

##### content: `str`<a id="content-str"></a>

template content

##### stylesheet: `str`<a id="stylesheet-str"></a>

template inline stylesheet

##### type: `str`<a id="type-str"></a>

type of template

##### filename: `str`<a id="filename-str"></a>

document filename CQL

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTemplate`](./chart_hop_python_sdk/type/update_template.py)
Template data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/template/{templateId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.approve_pending_request`<a id="charthoptimeoffapprove_pending_request"></a>

Approve a pending time off request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.timeoff.approve_pending_request(
    org_id="orgId_example",
    time_off_id="timeOffId_example",
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### time_off_id: `str`<a id="time_off_id-str"></a>

TimeOff id

##### message: `str`<a id="message-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffApproval`](./chart_hop_python_sdk/type/time_off_approval.py)
Approval information

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff/{timeOffId}/approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.create_entry`<a id="charthoptimeoffcreate_entry"></a>

Create a timeOff

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_entry_response = charthop.timeoff.create_entry(
    person_id="588f7ee98f138b19220041a7",
    start_date="1970-01-01",
    end_date="1970-01-01",
    org_id="orgId_example",
    external_id="588f7ee98f138b19220041a7",
    days=3.14,
    hours=3.14,
    type_description="string_example",
    note="string_example",
    approval="APPROVED",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

person taking the time off

##### start_date: `date`<a id="start_date-date"></a>

start date of time off, inclusive

##### end_date: `date`<a id="end_date-date"></a>

end date of time off, inclusive

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### external_id: `str`<a id="external_id-str"></a>

external identifier, if time off synced from external system

##### days: `Union[int, float]`<a id="days-unionint-float"></a>

number of days used

##### hours: `Union[int, float]`<a id="hours-unionint-float"></a>

number of hours used

##### type_description: `str`<a id="type_description-str"></a>

type of time off

##### note: `str`<a id="note-str"></a>

notes on the time off

##### approval: `str`<a id="approval-str"></a>

approval status of the time off

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTimeOffEntity`](./chart_hop_python_sdk/type/create_time_off_entity.py)
TimeOff data to create

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOff`](./chart_hop_python_sdk/pydantic/time_off.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.find_time_off_by_id`<a id="charthoptimeofffind_time_off_by_id"></a>

Return a particular timeOff by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_time_off_by_id_response = charthop.timeoff.find_time_off_by_id(
    org_id="orgId_example",
    time_off_id="timeOffId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### time_off_id: `str`<a id="time_off_id-str"></a>

TimeOff id

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffEntity`](./chart_hop_python_sdk/pydantic/time_off_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff/{timeOffId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.get_time_off`<a id="charthoptimeoffget_time_off"></a>

Retrieve time off

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_off_response = charthop.timeoff.get_time_off(
    org_id="orgId_example",
    person_id="string_example",
    from_date="1970-01-01",
    until_date="1970-01-01",
    _from="string_example",
    limit=1,
    return_access="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### person_id: `str`<a id="person_id-str"></a>

Person id to filter by

##### from_date: `date`<a id="from_date-date"></a>

From date, inclusive

##### until_date: `date`<a id="until_date-date"></a>

Until date, exclusive

##### _from: `str`<a id="_from-str"></a>

Time off id to start paginating from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### return_access: `str`<a id="return_access-str"></a>

Return access information -- pass a list of actions to check, for example: create,update,delete

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsTimeOffEntity`](./chart_hop_python_sdk/pydantic/results_time_off_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.reject_time_off_request`<a id="charthoptimeoffreject_time_off_request"></a>

Reject a pending time off request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.timeoff.reject_time_off_request(
    org_id="orgId_example",
    time_off_id="timeOffId_example",
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### time_off_id: `str`<a id="time_off_id-str"></a>

TimeOff id

##### message: `str`<a id="message-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffApproval`](./chart_hop_python_sdk/type/time_off_approval.py)
Rejection information

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff/{timeOffId}/reject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.remove_entry`<a id="charthoptimeoffremove_entry"></a>

Delete a timeOff

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.timeoff.remove_entry(
    org_id="orgId_example",
    time_off_id="timeOffId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### time_off_id: `str`<a id="time_off_id-str"></a>

TimeOff id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff/{timeOffId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.submit_time_off_request`<a id="charthoptimeoffsubmit_time_off_request"></a>

Request time off

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_time_off_request_response = charthop.timeoff.submit_time_off_request(
    start_date="1970-01-01",
    end_date="1970-01-01",
    org_id="orgId_example",
    person_id="string_example",
    type_description="string_example",
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `date`<a id="start_date-date"></a>

##### end_date: `date`<a id="end_date-date"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### person_id: `str`<a id="person_id-str"></a>

##### type_description: `str`<a id="type_description-str"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffRequest`](./chart_hop_python_sdk/type/time_off_request.py)
Time off request

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOff`](./chart_hop_python_sdk/pydantic/time_off.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff/request` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.update_time_off_entry`<a id="charthoptimeoffupdate_time_off_entry"></a>

Update an existing timeOff

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.timeoff.update_time_off_entry(
    org_id="orgId_example",
    time_off_id="timeOffId_example",
    external_id="588f7ee98f138b19220041a7",
    start_date="1970-01-01",
    end_date="1970-01-01",
    days=3.14,
    hours=3.14,
    type_description="string_example",
    note="string_example",
    approval="APPROVED",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### time_off_id: `str`<a id="time_off_id-str"></a>

TimeOff id

##### external_id: `str`<a id="external_id-str"></a>

external identifier, if time off synced from external system

##### start_date: `date`<a id="start_date-date"></a>

start date of time off, inclusive

##### end_date: `date`<a id="end_date-date"></a>

end date of time off, inclusive

##### days: `Union[int, float]`<a id="days-unionint-float"></a>

number of days used

##### hours: `Union[int, float]`<a id="hours-unionint-float"></a>

number of hours used

##### type_description: `str`<a id="type_description-str"></a>

type of time off

##### note: `str`<a id="note-str"></a>

notes on the time off

##### approval: `str`<a id="approval-str"></a>

approval status of the time off

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTimeOffEntity`](./chart_hop_python_sdk/type/update_time_off_entity.py)
TimeOff data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff/{timeOffId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.timeoff.validate_timeoff_request`<a id="charthoptimeoffvalidate_timeoff_request"></a>

Validate a time off request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_timeoff_request_response = charthop.timeoff.validate_timeoff_request(
    start_date="1970-01-01",
    end_date="1970-01-01",
    org_id="orgId_example",
    person_id="string_example",
    type_description="string_example",
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `date`<a id="start_date-date"></a>

##### end_date: `date`<a id="end_date-date"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### person_id: `str`<a id="person_id-str"></a>

##### type_description: `str`<a id="type_description-str"></a>

##### note: `str`<a id="note-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffRequest`](./chart_hop_python_sdk/type/time_off_request.py)
Time off request

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOff`](./chart_hop_python_sdk/pydantic/time_off.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/timeoff/request/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.usage.record_product_feature_usage`<a id="charthopusagerecord_product_feature_usage"></a>

Record usage of a product feature

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.usage.record_product_feature_usage(
    org_id="orgId_example",
    type="type_example",
    entity_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org identifier (either id or slug)

##### type: `str`<a id="type-str"></a>

Type of usage

##### entity_id: `str`<a id="entity_id-str"></a>

Entity id, if applicable

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/org/{orgId}/usage/{type}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.assign_role_to_multiple`<a id="charthopuserassign_role_to_multiple"></a>

Assign or remove multiple users a role within an org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.user.assign_role_to_multiple(
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserAssignRoleToMultipleRequest`](./chart_hop_python_sdk/type/user_assign_role_to_multiple_request.py)
User data

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/assign` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.change_password`<a id="charthopuserchange_password"></a>

Change a user's password, or switch a user to SSO

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.user.change_password(
    new_password="string_example",
    user_id="userId_example",
    old_password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_password: `str`<a id="new_password-str"></a>

password to change to

##### user_id: `str`<a id="user_id-str"></a>

User id

##### old_password: `str`<a id="old_password-str"></a>

password to change from

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangePasswordRequest`](./chart_hop_python_sdk/type/change_password_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/{userId}/password` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.create_new_user`<a id="charthopusercreate_new_user"></a>

Create a new user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = charthop.user.create_new_user(
    orgs=[
        {
            "org_id": "5887a7718f138b6a2a0041a7",
            "person_id": "5887a7718f138b6a2a0041a7",
            "access": "NONE",
            "role_id": "5887a7718f138b6a2a0041a7",
        }
    ],
    app_id="string_example",
    name={
        "first": "Jane",
        "middle": "Quidditch",
        "last": "Public",
        "pref": "JQ",
        "pref_last": "Smith",
    },
    email="bob@example.com",
    image_path="/",
    status="SUPERUSER",
    options={},
    internal_options={},
    secrets={},
    email_settings=[
        {
            "category": "ADMINISTRATIVE",
            "subscribed": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### orgs: List[`OrgAccess`]<a id="orgs-listorgaccess"></a>

list of member orgs with permission levels

##### app_id: `str`<a id="app_id-str"></a>

if the user is an app user, the id of the app

##### name: [`Name`](./chart_hop_python_sdk/type/name.py)<a id="name-namechart_hop_python_sdktypenamepy"></a>


##### email: `str`<a id="email-str"></a>

email address of user

##### image_path: `str`<a id="image_path-str"></a>

path to full-sized profile image in storage

##### status: `str`<a id="status-str"></a>

current status of user

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

for apps, options (specific options are specific to the particular app); for users, user-set preferences

##### internal_options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="internal_options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

internal (ChartHop controlled) options

##### secrets: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="secrets-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

write-only secrets; the content of these secrets are not retrievable via the external-facing API

##### email_settings: List[`UserEmailSetting`]<a id="email_settings-listuseremailsetting"></a>

Email settings for the user

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateUser`](./chart_hop_python_sdk/type/create_user.py)
User data to create

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./chart_hop_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.get_all_users_within_orgs`<a id="charthopuserget_all_users_within_orgs"></a>

Return all users within an org or across orgs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_users_within_orgs_response = charthop.user.get_all_users_within_orgs(
    org_id="string_example",
    _from="string_example",
    limit=1,
    sort="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

Org id to search within

##### _from: `str`<a id="_from-str"></a>

User id to start from

##### limit: `int`<a id="limit-int"></a>

Number of results to return

##### sort: `str`<a id="sort-str"></a>

Sort by

#### 🔄 Return<a id="🔄-return"></a>

[`ResultsUser`](./chart_hop_python_sdk/pydantic/results_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.get_current_user`<a id="charthopuserget_current_user"></a>

Return the currently logged in user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_user_response = charthop.user.get_current_user()
```

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./chart_hop_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.get_user_by_email`<a id="charthopuserget_user_by_email"></a>

Return a particular user by email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_email_response = charthop.user.get_user_by_email(
    email="email_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Email

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./chart_hop_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/email/{email}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.get_user_by_id`<a id="charthopuserget_user_by_id"></a>

Return a particular user by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_id_response = charthop.user.get_user_by_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User id

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./chart_hop_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.invite_multiple_new_users`<a id="charthopuserinvite_multiple_new_users"></a>

Create/invite multiple new users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invite_multiple_new_users_response = charthop.user.invite_multiple_new_users(
    body=[
        {
            "email": "bob@example.com",
            "orgs": [
                {
                    "org_id": "5887a7718f138b6a2a0041a7",
                    "person_id": "5887a7718f138b6a2a0041a7",
                    "access": "NONE",
                    "role_id": "5887a7718f138b6a2a0041a7",
                }
            ],
            "status": "SUPERUSER",
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserInviteMultipleNewUsersRequest`](./chart_hop_python_sdk/type/user_invite_multiple_new_users_request.py)
User data to create

#### 🔄 Return<a id="🔄-return"></a>

[`UserInviteMultipleNewUsersResponse`](./chart_hop_python_sdk/pydantic/user_invite_multiple_new_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/invite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.return_user_by_person_id`<a id="charthopuserreturn_user_by_person_id"></a>

Return a particular user by its corresponding person id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
return_user_by_person_id_response = charthop.user.return_user_by_person_id(
    person_id="personId_example",
    org_id="orgId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Person id to fetch user for

##### org_id: `str`<a id="org_id-str"></a>

Org id to search within

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./chart_hop_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/person/{personId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.revoke_access_token`<a id="charthopuserrevoke_access_token"></a>

Revoke a user's access token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.user.revoke_access_token(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/{userId}/token` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.revoke_access_tokens`<a id="charthopuserrevoke_access_tokens"></a>

Revoke multiple user's access tokens

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.user.revoke_access_tokens(
    body=[
        "string_example"
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserRevokeAccessTokensRequest`](./chart_hop_python_sdk/type/user_revoke_access_tokens_request.py)
User ids

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/token` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.send_password_reset_email`<a id="charthopusersend_password_reset_email"></a>

Send a password reset email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.user.send_password_reset_email(
    email="example@example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

email address

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailRequest`](./chart_hop_python_sdk/type/email_request.py)
User email address

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/sendreset` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.update_existing_user`<a id="charthopuserupdate_existing_user"></a>

Update an existing user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.user.update_existing_user(
    user_id="userId_example",
    app_id="string_example",
    name={
        "first": "Jane",
        "middle": "Quidditch",
        "last": "Public",
        "pref": "JQ",
        "pref_last": "Smith",
    },
    email="bob@example.com",
    orgs=[
        {
            "org_id": "5887a7718f138b6a2a0041a7",
            "person_id": "5887a7718f138b6a2a0041a7",
            "access": "NONE",
            "role_id": "5887a7718f138b6a2a0041a7",
        }
    ],
    image_path="/",
    status="SUPERUSER",
    options={},
    internal_options={},
    secrets={},
    email_settings=[
        {
            "category": "ADMINISTRATIVE",
            "subscribed": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User id

##### app_id: `str`<a id="app_id-str"></a>

if the user is an app user, the id of the app

##### name: [`Name`](./chart_hop_python_sdk/type/name.py)<a id="name-namechart_hop_python_sdktypenamepy"></a>


##### email: `str`<a id="email-str"></a>

email address of user

##### orgs: List[`OrgAccess`]<a id="orgs-listorgaccess"></a>

list of member orgs with permission levels

##### image_path: `str`<a id="image_path-str"></a>

path to full-sized profile image in storage

##### status: `str`<a id="status-str"></a>

current status of user

##### options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

for apps, options (specific options are specific to the particular app); for users, user-set preferences

##### internal_options: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="internal_options-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

internal (ChartHop controlled) options

##### secrets: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="secrets-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

write-only secrets; the content of these secrets are not retrievable via the external-facing API

##### email_settings: List[`UserEmailSetting`]<a id="email_settings-listuseremailsetting"></a>

Email settings for the user

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateUser`](./chart_hop_python_sdk/type/update_user.py)
User data to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/{userId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.user.viewed_user_details`<a id="charthopuserviewed_user_details"></a>

Return the user the user is currently viewing as

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
viewed_user_details_response = charthop.user.viewed_user_details()
```

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./chart_hop_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/user/me/view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.webauthn.check_existing_key`<a id="charthopwebauthncheck_existing_key"></a>

Check for an existing physical key for this user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.webauthn.check_existing_key()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webauthn/verify` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.webauthn.remove_registered_credentials_by_email`<a id="charthopwebauthnremove_registered_credentials_by_email"></a>

Delete registered credentials by the given email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.webauthn.remove_registered_credentials_by_email(
    email_base64="emailBase64_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email_base64: `str`<a id="email_base64-str"></a>

Email

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webauthn/register/{emailBase64}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.webauthn.verify_physical_key_for_user`<a id="charthopwebauthnverify_physical_key_for_user"></a>

Check for an existing physical key for this user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.webauthn.verify_physical_key_for_user()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webauthn/register` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.webauthn.verify_physical_key_for_user_0`<a id="charthopwebauthnverify_physical_key_for_user_0"></a>

Check for an existing WebAuthn key for this user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.webauthn.verify_physical_key_for_user_0(
    request_id="string_example",
    credential_response="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

##### credential_response: `str`<a id="credential_response-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebAuthnRequest`](./chart_hop_python_sdk/type/web_authn_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webauthn/register` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `charthop.webauthn.verify_physical_key_for_user_1`<a id="charthopwebauthnverify_physical_key_for_user_1"></a>

Check for an existing physical key for this user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
charthop.webauthn.verify_physical_key_for_user_1(
    request_id="string_example",
    credential_response="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

##### credential_response: `str`<a id="credential_response-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebAuthnRequest`](./chart_hop_python_sdk/type/web_authn_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webauthn/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
