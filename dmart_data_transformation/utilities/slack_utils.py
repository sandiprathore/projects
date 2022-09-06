

def send_notification(message_body):
    """
    send notifications on slack with basehook and requests
    parameters
    ----------
    message_body: str
        body of the message that want to send 
    """
    import requests
    from airflow.hooks.base_hook import BaseHook
    import json
    slack_webhook_token = BaseHook.get_connection("slack_conn").host
    requests.post(slack_webhook_token, data=json.dumps({"text": message_body}))


def start_alert(**kwargs):
    """
    jod is started notifiy on slack 
    parameters
    ----------
    kwargs: airflow DagRun Context.
    """
    ti = kwargs['task_instance']
    job_execution_id = kwargs["dag_run"].run_id

    message = f"""
        :large_blue_circle: Job Started.
        *DAG:* {ti.dag_id}
        *Job execution id*: {job_execution_id}
        *Execution date:* {ti.execution_date}

    """
    send_notification(message)


def failure_callback(kwargs):
    """
    slack alert is any task has failed
    parameters
    ----------
    kwargs: airflow DagRun Context.
    """
    ti = kwargs['task_instance']
    dag_run = kwargs["dag_run"]
    
    job_execution_id = dag_run.run_id

    message = f"""
        :red_circle: Job failed.
        *DAG:* {ti.dag_id}
        *Job Execution id*: {job_execution_id}
        *Task ID:* {ti.task_id}
        *Execution date:* {ti.execution_date}
        *Log url*: {ti.log_url}
    """
    print(message)
    send_notification(message)


def end_alert(**kwargs):
    """
    jod has ended notifiy on slack 
    parameters
    ----------
    kwargs: airflow DagRun Context.
    """
    ti = kwargs['task_instance']
    job_execution_id = kwargs["dag_run"].run_id
    message = f"""
        :large_green_circle: Job succeed.
        *DAG:* {ti.dag_id}
        *Job execution id*: {job_execution_id}
        *Execution date:* {ti.execution_date}
    """
    send_notification(message)