from django.shortcuts import render

from moth.utils.plugin_families import get_plugin_families


def home(request):
    plugin_families = get_plugin_families()
    context = {'families': plugin_families}
    
    response = render(request, 'moth/home.html', context)
    response['X-Powered-By'] = 'PHP/5.1.2-1+b1 ubuntu'

    return response


def about(request):
    return render(request, 'moth/about.html')
