from airflow import DAG
import pendulum
from datetime import datetime, timedelta
from includes.reporting.load_aggregate_adverse_events_task import build_load_aggregate_adverse_events_task
from includes.reporting.load_aggregate_appointment_task import build_load_aggregate_appointment_task
from includes.reporting.load_aggregate_art_history_task import build_load_aggregate_art_history_task
from includes.reporting.load_aggregate_tx_new_task import build_load_aggregate_tx_new_task
from includes.reporting.load_aggregate_covid_task import build_load_aggregate_covid_task
from includes.reporting.load_aggregate_dsd_appts_by_stability_task import build_load_aggregate_dsd_appts_by_stability_task
from includes.reporting.load_aggregate_dsd_stable_task import build_load_aggregate_dsd_stable_task
from includes.reporting.load_aggregate_dsd_task import build_load_aggregate_dsd_task
from includes.reporting.load_aggregate_dsd_unstable_task import build_load_aggregate_dsd_unstable_task
from includes.reporting.load_aggregate_expecteduploads_task import build_load_aggregate_expecteduploads_task
from includes.reporting.load_aggregate_hts_client_self_tested_task import build_load_aggregate_hts_client_self_tested_task
from includes.reporting.load_aggregate_hts_client_tested_as_task import build_load_aggregate_hts_client_tested_as_task
from includes.reporting.load_aggregate_ct_dhis2_task import build_load_aggregate_ct_dhis2_task
from includes.reporting.load_aggregate_defaulter_tracing_outcome_task import build_load_aggregate_defaulter_tracing_outcome_task
from includes.reporting.load_aggregate_hts_dhis2_task import build_load_aggregate_hts_dhis2_task
from includes.reporting.load_aggregate_hts_entrypoint_task import build_load_aggregate_hts_entrypoint_task
from includes.reporting.load_aggregate_hts_months_last_test_task import build_load_aggregate_hts_months_last_test_task
from includes.reporting.load_aggregate_hts_pns_knowledge_HIV_status_task import build_load_aggregate_hts_pns_knowledge_HIV_status_task
from includes.reporting.load_aggregate_hts_pns_sexualpartner_task import build_load_aggregate_hts_pns_sexualpartner_task
from includes.reporting.load_aggregate_hts_pnschildren_task import build_load_aggregate_hts_pnschildren_task
from includes.reporting.load_aggregate_hts_tbscreening_task import build_load_aggregate_hts_tbscreening_task
from includes.reporting.load_aggregate_hts_teststrategy_task import build_load_aggregate_hts_teststrategy_task
from includes.reporting.load_aggregate_hts_uptake_task import build_load_aggregate_hts_uptake_task
from includes.reporting.load_aggregate_iit_tracing_status_task import build_load_aggregate_iit_tracing_status_task
from includes.reporting.load_aggregate_nupi_task import build_load_aggregate_nupi_task
from includes.reporting.load_aggregate_optimize_current_regimens_task import build_load_aggregate_optimize_current_regimens_task
from includes.reporting.load_aggregate_optimize_start_regimens_task import build_load_aggregate_optimize_start_regimens_task
from includes.reporting.load_aggregate_otz_eligibility_and_enrollments_task import build_load_aggregate_otz_eligibility_and_enrollments_task
from includes.reporting.load_aggregate_otz_outcome_task import build_load_aggregate_otz_outcome_task
from includes.reporting.load_aggregate_otz_task import build_load_aggregate_otz_task
from includes.reporting.load_aggregate_ovc_count_task import build_load_aggregate_ovc_count_task
from includes.reporting.load_aggregate_prep_cascade_task import build_load_aggregate_prep_cascade_task
from includes.reporting.load_aggregate_prep_discontinuations_task import build_load_aggregate_prep_discontinuations_task
from includes.reporting.load_aggregate_prep_STIOutcomes_task import build_load_aggregate_prep_STIOutcomes_task
from includes.reporting.load_aggregate_prep_testing_at_1month_refill_task import build_load_aggregate_prep_testing_at_1month_refill_task
from includes.reporting.load_aggregate_prep_testing_at_3month_refill_task import build_load_aggregate_prep_testing_at_3month_refill_task
from includes.reporting.load_aggregate_recencyuploads_task import build_load_aggregate_recencyuploads_task
from includes.reporting.load_aggregate_time_to_art_grp_task import build_load_aggregate_time_to_art_grp_task
from includes.reporting.load_aggregate_time_to_art_last_12m_task import build_load_aggregate_time_to_art_last_12m_task
from includes.reporting.load_aggregate_time_to_art_task import build_load_aggregate_time_to_art_task
from includes.reporting.load_aggregate_time_to_first_vl_grp_task import build_load_aggregate_time_to_first_vl_grp_task
from includes.reporting.load_aggregate_time_to_vl_12m_task import build_load_aggregate_time_to_vl_12m_task
from includes.reporting.load_aggregate_time_to_vl_task import build_load_aggregate_time_to_vl_task
from includes.reporting.load_aggregate_TPT_task import build_load_aggregate_TPT_task
from includes.reporting.load_aggregate_treatmentoutcomes_task import build_load_aggregate_treatmentoutcomes_task
from includes.reporting.load_aggregate_txcurr_task import build_load_aggregate_txcurr_task
from includes.reporting.load_aggregate_tx_new_hts_cascade_task import build_load_aggregate_tx_new_hts_cascade_task
from includes.reporting.load_aggregate_vl_outcome_and_uptake_task import build_load_aggregate_vl_outcome_and_uptake_task
from includes.reporting.load_aggregate_heis_task import build_load_aggregate_heis_task
from includes.reporting.load_aggregate_PBFW_task import build_load_aggregate_PBFW_task
from includes.reporting.load_aggregate_concordance_HTSPOS_task import build_load_aggregate_concordance_HTSPOS_task
from includes.reporting.load_aggregate_concordance_TxCurr_task import build_load_aggregate_concordance_TxCurr_task
from includes.reporting.load_aggregate_durable_ldl_task import build_load_aggregate_durable_ldl_task


local_tz = pendulum.timezone("Africa/Nairobi")
default_args = {
    'owner': 'kenyahmis',
    'depends_on_past': False,
    'start_date': datetime(2022, 10, 13, tzinfo=local_tz),
    'email': ['paul.nthusi@thepalladiumgroup.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(dag_id='reporting_aggregate_tables_etl_dag',
          schedule_interval=None,
          default_args=default_args,
          )


load_aggregate_adverse_events = build_load_aggregate_adverse_events_task(dag = dag)
load_aggregate_appointment = build_load_aggregate_appointment_task(dag = dag)
load_aggregate_art_history = build_load_aggregate_art_history_task(dag = dag)
load_aggregate_tx_new = build_load_aggregate_tx_new_task(dag = dag)
load_aggregate_covid = build_load_aggregate_covid_task(dag = dag)
load_aggregate_dsd_appts_by_stability = build_load_aggregate_dsd_appts_by_stability_task(dag = dag)
load_aggregate_dsd_stable = build_load_aggregate_dsd_stable_task(dag = dag)
load_aggregate_dsd = build_load_aggregate_dsd_task(dag = dag)
load_aggregate_dsd_unstable = build_load_aggregate_dsd_unstable_task(dag = dag)
load_aggregate_expecteduploads = build_load_aggregate_expecteduploads_task(dag = dag)
load_aggregate_hts_client_self_tested = build_load_aggregate_hts_client_self_tested_task(dag = dag)
load_aggregate_hts_client_tested_as = build_load_aggregate_hts_client_tested_as_task(dag = dag)
load_aggregate_ct_dhis2 = build_load_aggregate_ct_dhis2_task(dag = dag)
load_aggregate_defaulter_tracing_outcome = build_load_aggregate_defaulter_tracing_outcome_task(dag = dag)
load_aggregate_hts_dhis2 = build_load_aggregate_hts_dhis2_task(dag = dag)
load_aggregate_hts_entrypoint = build_load_aggregate_hts_entrypoint_task(dag = dag)
load_aggregate_hts_months_last_test = build_load_aggregate_hts_months_last_test_task(dag = dag)
load_aggregate_hts_pns_knowledge_HIV_status = build_load_aggregate_hts_pns_knowledge_HIV_status_task(dag = dag)
load_aggregate_hts_pns_sexualpartner = build_load_aggregate_hts_pns_sexualpartner_task(dag = dag)
load_aggregate_hts_pnschildren = build_load_aggregate_hts_pnschildren_task(dag = dag)
load_aggregate_hts_tbscreening = build_load_aggregate_hts_tbscreening_task(dag = dag)
load_aggregate_hts_teststrategy = build_load_aggregate_hts_teststrategy_task(dag = dag)
load_aggregate_hts_uptake = build_load_aggregate_hts_uptake_task(dag = dag)
load_aggregate_iit_tracing_status = build_load_aggregate_iit_tracing_status_task(dag = dag)
load_aggregate_nupi = build_load_aggregate_nupi_task(dag = dag)
load_aggregate_optimize_current_regimens = build_load_aggregate_optimize_current_regimens_task(dag = dag)
load_aggregate_optimize_start_regimens = build_load_aggregate_optimize_start_regimens_task(dag = dag)
load_aggregate_otz_eligibility_and_enrollments = build_load_aggregate_otz_eligibility_and_enrollments_task(dag = dag)
load_aggregate_otz_outcome = build_load_aggregate_otz_outcome_task(dag = dag)
load_aggregate_ovc_count = build_load_aggregate_ovc_count_task(dag = dag)
load_aggregate_prep_cascade = build_load_aggregate_prep_cascade_task(dag = dag)
load_aggregate_prep_discontinuations = build_load_aggregate_prep_discontinuations_task(dag = dag)
load_aggregate_prep_STIOutcomes = build_load_aggregate_prep_STIOutcomes_task(dag = dag)
load_aggregate_prep_testing_at_1month_refill = build_load_aggregate_prep_testing_at_1month_refill_task(dag = dag)
load_aggregate_prep_testing_at_3month_refill = build_load_aggregate_prep_testing_at_3month_refill_task(dag = dag)
load_aggregate_recencyuploads = build_load_aggregate_recencyuploads_task(dag = dag)
load_aggregate_time_to_art_grp = build_load_aggregate_time_to_art_grp_task(dag = dag)
load_aggregate_time_to_art_last_12m = build_load_aggregate_time_to_art_last_12m_task(dag = dag)
load_aggregate_time_to_art = build_load_aggregate_time_to_art_task(dag = dag)
load_aggregate_time_to_first_vl_grp = build_load_aggregate_time_to_first_vl_grp_task(dag = dag)
load_aggregate_time_to_vl_12m = build_load_aggregate_time_to_vl_12m_task(dag = dag)
load_aggregate_time_to_vl = build_load_aggregate_time_to_vl_task(dag = dag)
load_aggregate_otz = build_load_aggregate_otz_task(dag = dag)
load_aggregate_TPT = build_load_aggregate_TPT_task(dag = dag)
load_aggregate_treatmentoutcomes = build_load_aggregate_treatmentoutcomes_task(dag = dag)
load_aggregate_txcurr = build_load_aggregate_txcurr_task(dag = dag)
load_aggregate_tx_new_hts_cascade = build_load_aggregate_tx_new_hts_cascade_task(dag = dag)
load_aggregate_vl_outcome_and_uptake = build_load_aggregate_vl_outcome_and_uptake_task(dag = dag)
load_aggregate_heis = build_load_aggregate_heis_task(dag = dag)
load_aggregate_PBFW = build_load_aggregate_PBFW_task(dag = dag)
load_aggregate_concordance_HTSPOS = build_load_aggregate_concordance_HTSPOS_task(dag = dag)
load_aggregate_concordance_TxCurr = build_load_aggregate_concordance_TxCurr_task(dag = dag)
load_aggregate_durable_ldl = build_load_aggregate_durable_ldl_task(dag = dag)


load_aggregate_adverse_events >> load_aggregate_appointment >> load_aggregate_art_history >> load_aggregate_tx_new >> load_aggregate_covid >> load_aggregate_dsd_appts_by_stability >> load_aggregate_dsd_stable >> load_aggregate_dsd >> load_aggregate_dsd_unstable >> load_aggregate_heis >> load_aggregate_PBFW >> load_aggregate_expecteduploads >> load_aggregate_durable_ldl
load_aggregate_expecteduploads >> load_aggregate_hts_client_self_tested >> load_aggregate_hts_client_tested_as >> load_aggregate_ct_dhis2 >> load_aggregate_defaulter_tracing_outcome >> load_aggregate_hts_dhis2 >> load_aggregate_hts_entrypoint >> load_aggregate_hts_months_last_test >>load_aggregate_hts_pns_knowledge_HIV_status >> load_aggregate_hts_pns_sexualpartner
load_aggregate_hts_pns_sexualpartner >> load_aggregate_hts_pnschildren >> load_aggregate_hts_tbscreening >> load_aggregate_hts_teststrategy  >> load_aggregate_hts_uptake >> load_aggregate_iit_tracing_status >> load_aggregate_nupi >> load_aggregate_optimize_current_regimens  >> load_aggregate_optimize_start_regimens  >> load_aggregate_prep_cascade >> load_aggregate_time_to_vl
load_aggregate_prep_cascade >> load_aggregate_recencyuploads >> load_aggregate_time_to_art_grp  >> load_aggregate_time_to_art_last_12m >> load_aggregate_time_to_art  >> load_aggregate_time_to_first_vl_grp >> load_aggregate_time_to_vl_12m >> load_aggregate_otz  >> load_aggregate_TPT  >> load_aggregate_treatmentoutcomes >> load_aggregate_txcurr
load_aggregate_txcurr >> load_aggregate_tx_new_hts_cascade  >> load_aggregate_vl_outcome_and_uptake >> load_aggregate_otz_eligibility_and_enrollments >> load_aggregate_otz_outcome >> load_aggregate_ovc_count >> load_aggregate_prep_STIOutcomes >> load_aggregate_prep_discontinuations >> load_aggregate_prep_testing_at_1month_refill >> load_aggregate_prep_testing_at_3month_refill
load_aggregate_concordance_HTSPOS >> load_aggregate_concordance_HTSPOS