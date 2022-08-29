from post.models import *

def extras(request):
    context={}
    context['category_list'] = Category.objects.all()
    context['settings_list']=Settings.objects.all().order_by('-id')[:1]
    return context