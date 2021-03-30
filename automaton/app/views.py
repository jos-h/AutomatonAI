from django.http import JsonResponse
from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Tasks
import plotly.express as px
import pandas as pd
import datetime


def demo(request):
    return render(request, 'home.html', {})


def home(request):
    return render(request, 'home.html', {})


def associate(request):
    return render(request, 'associate.html', {})


def manager(request):
    priority = request.GET.get('value')
    if priority:
        queryset = Tasks.objects.filter(priority=priority)
    else:
        queryset = Tasks.objects.filter()
    data_list = list()
    for each in queryset.values():
        data = {}
        data.update(Start=datetime.datetime.now().strftime("%Y-%m-%d"))
        data.update(Resource=each['user'])
        data.update(Finish=(datetime.datetime.now() + datetime.timedelta(each['no_of_days'])).strftime("%Y-%m-%d"))
        if each['priority'] == 'High':
            data.update(each)
        if each['priority'] == 'Medium':
            data.update(each)
        if each['priority'] == 'Low':
            data.update(each)
        data_list.append(data)
    df = pd.DataFrame(data_list)
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="goal", color="Resource")
    fig.update_yaxes(autorange="reversed")
    graph = fig.to_html(full_html=False, default_height=700, default_width=1000)
    return render(request, 'manager.html', {'data': graph})


def submit_data(request):
    data = {key: value for key, value in request.GET.items()}
    print(data)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data = serializer.data
        data.update(success="true")
        return JsonResponse(data)
