from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from todoapp.models import Task
from todoapp.utils import get_token, get_tasks_by_token
import json

# Create your views here.


@require_http_methods(['GET'])
def get_all_tasks(request):
    token = get_token(request.META)
    data = {'data': get_tasks_by_token(token), 'token': token}
    return JsonResponse(data, status=200, safe=True)


@require_http_methods(['POST'])
@csrf_exempt
def upsert_task(request):
    token = get_token(request.META)
    print 'zzzbzzzbzzz'
    print request.POST
    print request.body
    post_data = json.loads(request.body)
    task_id = post_data.get('task_id')
    print token
    print task_id

    try:
        if task_id:
            task = Task.objects.get(id=task_id, token=token)
        else:
            raise Task.DoesNotExist
    except Task.DoesNotExist:
        task = Task()

    task.token = token
    task.activity = post_data.get('activity')
    task.is_archived = post_data.get('is_archived')
    task.status = post_data.get('status')
    print task.to_json()
    task.save()
    response = {'message': 'success', 'token': token, 'data':get_tasks_by_token(token)}
    return JsonResponse(response, safe=True, status=200)
