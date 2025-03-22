from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow_user',
    'start_date': datetime(2025, 3, 22),
    'email': [‘narendra’v64@gmail.com],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='A DAG that processes web logs daily',
    schedule_interval='@daily'
)

start = DummyOperator(
    task_id='start',
    dag=dag
)

start


2from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow_user',
    'start_date': datetime(2025, 3, 22),
    'email': [‘narendrav64@gmail.com],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='A DAG that processes web logs daily',
    schedule_interval='@daily'
)

start = DummyOperator(
    task_id='start',
    dag=dag
)

start

3
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import re

def extract_ip():
    log_file = "/path/to/webserver.log"  # Update with actual log file path
    output_file = "/path/to/extracted_data.txt"  # Update with actual output path
    
    with open(log_file, "r") as f:
        logs = f.readlines()
    
    ip_addresses = [re.match(r'^(\S+)', line).group(1) for line in logs if re.match(r'^(\S+)', line)]
    
    with open(output_file, "w") as f:
        f.write("\n".join(ip_addresses))

default_args = {
    'owner': 'airflow_user',
    'start_date': datetime(2025, 3, 22),
    'email': [‘narendra’v64@gmail.com],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='A DAG that processes web logs daily',
    schedule_interval='@daily'
)

start = DummyOperator(
    task_id='start',
    dag=dag
)

extract_data = PythonOperator(
    task_id='extract_data',
    python_callable=extract_ip,
    dag=dag
)

start >> extract_data

4
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import re

def extract_ip():
    log_file = "/path/to/webserver.log"  # Update with actual log file path
    output_file = "/path/to/extracted_data.txt"  # Update with actual output path
    
    with open(log_file, "r") as f:
        logs = f.readlines()
    
    ip_addresses = [re.match(r'^(\S+)', line).group(1) for line in logs if re.match(r'^(\S+)', line)]
    
    with open(output_file, "w") as f:
        f.write("\n".join(ip_addresses))

def transform_ip():
    input_file = "/path/to/extracted_data.txt"  # Update with actual extracted file path
    output_file = "/path/to/transformed_data.txt"  # Update with actual output path
    
    with open(input_file, "r") as f:
        ip_addresses = f.readlines()
    
    filtered_ips = [ip.strip() for ip in ip_addresses if ip.strip() != "198.46.149.143"]
    
    with open(output_file, "w") as f:
        f.write("\n".join(filtered_ips))

default_args = {
    'owner': 'airflow_user',
    'start_date': datetime(2025, 3, 22),
    'email': [‘narendrav64@gmail.com’],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='A DAG that processes web logs daily',
    schedule_interval='@daily'
)

start = DummyOperator(
    task_id='start',
    dag=dag
)

extract_data = PythonOperator(
    task_id='extract_data',
    python_callable=extract_ip,
    dag=dag
)

transform_data = PythonOperator(
    task_id='transform_data',
    python_callable=transform_ip,
    dag=dag
)

start >> extract_data >> transform_data

# Defining the task pipeline
start >> extract_data >> transform_data >> load_data

airflow dags unpause process_web_log
