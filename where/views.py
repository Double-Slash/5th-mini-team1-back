from django.http import HttpResponse
from django.template import loader


import datetime

def ping(request):
    time = datetime.datetime.now()
    msg = str(time)
    # template = loader.get_template('where/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    return HttpResponse(time, content_type='text/plain')
