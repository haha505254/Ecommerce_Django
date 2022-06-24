from django.shortcuts import render
import datetime


def home(request):
    now = datetime.datetime.now()  # 現在時間
    context = {'now': now}
    return render(request, 'home.html', context)
