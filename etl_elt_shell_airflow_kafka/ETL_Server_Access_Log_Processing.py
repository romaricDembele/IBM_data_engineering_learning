from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

arguments = {
    'owner': 'Romaric Dembélé',
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

download = BashOperator(
    task_id = "download",
    bash_command = 'wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt"',
    dag = dag
)

extract = BashOperator(
    task_id = "extract",
    bash_command = 'cut -d"#" -f1,4 < /home/project/airflow/dags/web-server-access-log.txt > /home/project/airflow/dags/extracted_data.txt',
    dag = dag
)

transform = BashOperator(
    task_id = "transform",
    bash_command = "tr '[a-z]' '[A-Z]' < extracted_data.txt > transformed_data.txt",
    dag = dag
)

load = BashOperator(
    task_id = "load",
    bash_command = "tar -czvf web-server-access-log.tar.gz transformed_data.txt",
    dag = dag
)

download >> extract >> transform >> load
