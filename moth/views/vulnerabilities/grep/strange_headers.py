from django.shortcuts import render
from moth.views.base.vulnerable_template_view import VulnerableTemplateView


class StrangeHeadersView(VulnerableTemplateView):
    title = 'Strange HTTP response headers'
    description = 'Strange HTTP response headers'
    url_path = 'strange_headers.py'
    
    def get(self, request, *args, **kwds):
        context = self.get_context_data()
        context['html'] = 'View HTTP response headers.'
        
        response = render(request, self.template_name, context)
        response['w3af-rocks'] = 'http://www.example.com/'
        
        return response
