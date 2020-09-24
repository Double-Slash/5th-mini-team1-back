from django.http import HttpResponse
from django.template import loader


import datetime

def ping(request):
    msg = datetime.datetime.now()
    # template = loader.get_template('where/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    return HttpResponse(msg, content_type='text/plain')
