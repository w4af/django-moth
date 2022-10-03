from django.shortcuts import render
from moth.views.base.vulnerable_template_view import VulnerableTemplateView


COOKIE_NAME = 'TestCookie'
COOKIE_VALUE = 'something from somewhere'


class SetCookieView(VulnerableTemplateView):
    description = title = 'Sets a "TestCookie" for testing'
    url_path = 'set-cookie.py'
    
    def get(self, request, *args, **kwds):
        context = self.get_context_data()
        context['html'] = 'See HTTP response headers.'
        
        response = render(request, self.template_name, context)
        response['Set-Cookie'] = '%s=%s;' % (COOKIE_NAME, COOKIE_VALUE)
        
        return response

class GetCookieView(VulnerableTemplateView):
    description = title = 'Checks for "TestCookie"'
    url_path = 'get-cookie.py'
    
    def get(self, request, *args, **kwds):
        context = self.get_context_data()
        
        if COOKIE_NAME in request.COOKIES:
            if request.COOKIES[COOKIE_NAME]:
                msg = 'Cookie was sent.'
        else:
            msg = 'Cookie was NOT sent.'
        
        context['html'] = msg
        
        return render(request, self.template_name, context)

class EchoCookiesView(VulnerableTemplateView):
    description = title = 'Echoes all cookies'
    url_path = 'echo-cookies.py'
    
    def get(self, request, *args, **kwds):
        context = self.get_context_data()
        
        html = ''
        msg_fmt = 'Cookie "%s" with value "%s" <br/>\n'
        
        for cookie_name in request.COOKIES:
            html += msg_fmt % (cookie_name, request.COOKIES[cookie_name])
            
        context['html'] = html
        
        return render(request, self.template_name, context)

