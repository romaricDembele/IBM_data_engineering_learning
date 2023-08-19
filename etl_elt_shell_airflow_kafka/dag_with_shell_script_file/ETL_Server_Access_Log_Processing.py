from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

arguments = {
    'owner': 'Romaric DEMBELE',
    'start_date': days_ago(0),
    "email": ["romadembele@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ETL_Server_Access_Log_Processing',
    default_args = arguments,
    description = "Retrieve daily user info",
    schedule_interval = timedelta(days=1)
)

extract_transform_and_load = BashOperator(
    task_id = "extract_transform_and_load",
    bash_command = '/home/project/airflow/dags/ETL_Server_Access_Log_Processing.sh',
    dag = dag
)


extract_transform_and_load
