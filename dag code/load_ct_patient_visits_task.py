from airflow import DAG
from datetime import datetime, timedelta
from airflow.models import Variable
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

spark_app_home = Variable.get("SPARK_APP_HOME")
spark_driver_port = Variable.get("SPARK_DRIVER_PORT")
spark_driver_block_manager_port = Variable.get("SPARK_DRIVER_BLOCK_MANAGER_PORT")
spark_driver_host = Variable.get("SPARK_DRIVER_HOST")
spark_driver_bind_address = Variable.get("SPARK_DRIVER_BIND_ADDRESS")

spark_openlineage_host = Variable.get("SPARK_OPENLINEAGE_HOST")
spark_extra_listeners = Variable.get("SPARK_EXTRA_LISTENERS")
spark_openlineage_namespace = Variable.get("SPARK_OPENLINEAGE_NAMESPACE")

dc_spark_source_database_name = Variable.get("DC_SPARK_SOURCE_DATABASE_NAME")
dc_spark_source_database_host = Variable.get("DC_SPARK_SOURCE_DATABASE_HOST")
dc_spark_source_url = Variable.get("DC_SPARK_SOURCE_URL")
dc_spark_source_driver = Variable.get("DC_SPARK_SOURCE_DRIVER")
dc_spark_source_user = Variable.get("DC_SPARK_SOURCE_USER")
dc_spark_source_password = Variable.get("DC_SPARK_SOURCE_PASSWORD")
dc_spark_source_numpartitions = Variable.get("DC_SPARK_SOURCE_NUMPARTITIONS")
dc_spark_sink_url = Variable.get("DC_SPARK_SINK_URL")
dc_spark_sink_driver = Variable.get("DC_SPARK_SINK_DRIVER")
dc_spark_sink_user = Variable.get("DC_SPARK_SINK_USER")
dc_spark_sink_password = Variable.get("DC_SPARK_SINK_PASSWORD")

ctpv_spark_source_metadata_table = Variable.get("CTPV_SPARK_SOURCE_METADATA_TABLE")
ctpv_spark_sink_dbtable = Variable.get("CTPV_SPARK_SINK_DBTABLE")

def build_load_ct_patient_visits_task(dag:DAG):
    load_ct_patient_visits = SparkSubmitOperator(task_id='load_ct_patient_visits',
                                              conn_id='spark_standalone',
                                              application=f'{spark_app_home}/load-ct-patient-visits-1.0-SNAPSHOT-jar-with-dependencies.jar',
                                              total_executor_cores=1,
                                              executor_cores=2,
                                              executor_memory='1g',
                                              driver_memory='1g',
                                              name='load_ct_patient_visits',
                                              conf={
                                                "spark.openlineage.namespace": spark_openlineage_namespace,
                                                "spark.openlineage.host": spark_openlineage_host,
                                                "spark.extraListeners": spark_extra_listeners,                                                
                                                "spark.driver.port":spark_driver_port,
                                                "spark.driver.blockManager.port":spark_driver_block_manager_port,
                                                "spark.driver.host": spark_driver_host,
                                                "spark.driver.bindAddress": spark_driver_bind_address,
                                                "spark.source.database-name": dc_spark_source_database_name,
                                                "spark.source.metadata-table": ctpv_spark_source_metadata_table,
                                                "spark.source.database-host": dc_spark_source_database_host,
                                                "spark.source.url": dc_spark_source_url,
                                                "spark.source.driver": dc_spark_source_driver,
                                                "spark.source.user": dc_spark_source_user,
                                                "spark.source.password": dc_spark_source_password,
                                                "spark.source.numpartitions": dc_spark_source_numpartitions,
                                                "spark.sink.url": dc_spark_sink_url,
                                                "spark.sink.driver": dc_spark_sink_driver,
                                                "spark.sink.user":dc_spark_sink_user ,
                                                "spark.sink.password":dc_spark_sink_password,
                                                "spark.sink.dbtable":ctpv_spark_sink_dbtable
                                              },
                                              execution_timeout=timedelta(minutes=10),
                                              dag=dag
                                              )
    return load_ct_patient_visits