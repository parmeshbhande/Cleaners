from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mob_num = request.POST.get('mob_num')
        context = {
            'name': name,
            'email': email,
            'mob_num': mob_num
        }

        #getting our showdata template
        template = loader.get_template('showdata.html')

        #returing the template
        return HttpResponse(template.render(context, request))
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('index.html')
        return HttpResponse(template.render())


