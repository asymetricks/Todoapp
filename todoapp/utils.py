import uuid
from todoapp.models import Task

def generate_token():
    return str(uuid.uuid4())


def get_token(request_meta):
    print request_meta
    if request_meta.get('HTTP_TOKEN'):
        return request_meta.get('HTTP_TOKEN')
    return generate_token()


def get_tasks_by_token(token):
    return [{
                 'task_id': str(task.id),
                 'activity': task.activity,
                 'status': task.status
             }
             for task in Task.objects.filter(token=token, is_archived=False)
             ]