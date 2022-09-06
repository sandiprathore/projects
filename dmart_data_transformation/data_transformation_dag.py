import collections
from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
from airflow.operators.dummy import DummyOperator

from dmart_data_transformation.utilities.slack_utils import start_alert
from dmart_data_transformation.utilities.slack_utils import end_alert
from dmart_data_transformation.utilities.slack_utils import failure_callback
from dmart_data_transformation.utilities.tasks import process_runtime_parameters
from dmart_data_transformation.utilities.tasks import transformation_and_load_data

DAG_ID = 'dmart_data_transformation'

with DAG(
    dag_id=DAG_ID,
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    tags=["mongo_dag"],
    on_failure_callback=failure_callback,
    catchup=False,
) as dag:

        start_alert =  PythonOperator(
            task_id='start_alert',
            python_callable=start_alert,
            trigger_rule='none_failed'
            )

        # process runtime parameters
        process_runtime_parameters = BranchPythonOperator(
            task_id='process_runtime_parameters',
            python_callable=process_runtime_parameters,
            provide_context=True,
            do_xcom_push=False
            )
        
        # Execute jupyter notebooks from papermill and stores output in mongo collections
        transformation_and_load_data = PythonOperator(
            task_id='transformation_and_load_data',
            python_callable=transformation_and_load_data
        )

        # if something wrong in runtime parameters
        wrong_parameters =  DummyOperator(
            task_id='wrong_parameters'
            )
        
        # ending task
        end_alert =  PythonOperator(
            task_id='end_alert',
            python_callable=end_alert,
            trigger_rule='none_failed'
            )

start_alert >> process_runtime_parameters >> [ transformation_and_load_data, wrong_parameters ] 
wrong_parameters >> end_alert 
transformation_and_load_data >> end_alert

 
