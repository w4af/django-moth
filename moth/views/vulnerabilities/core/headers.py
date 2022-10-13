import logging

from django.shortcuts import render
from moth.views.base.vulnerable_template_view import VulnerableTemplateView


class EchoHeadersView(VulnerableTemplateView):
    description = title = 'Echoes all request headers'
    url_path = 'echo-headers.py'
    logger = logging.getLogger(__name__)

    KNOWN_HEADERS = ('CONTENT_LENGTH',)

    def is_http_header(self, hname):
        return hname.startswith('HTTP_') or hname in self.KNOWN_HEADERS

    def translate_header(self, hname):
        hname = hname.replace('HTTP_', '')
        hname = hname.replace('_', '-')
        hname = hname.lower()
        hname = hname.title()
        return hname

    def translate_header_value(self, hvalue):
        try:
            return hvalue.encode('iso-8859-1').decode('utf-8')
        except UnicodeDecodeError as e:
            self.logger.warn("Unable to decode header as unicode - maybe it wasn't a unicode header")
            return hvalue
        
    def get(self, request, *args, **kwds):
        context = self.get_context_data()
        
        html = ''
        msg_fmt = 'Header "%s" with value "%s" <br/>\n'
        
        for hname in request.META:
            if self.is_http_header(hname):
                html += msg_fmt % (self.translate_header(hname),
                                   self.translate_header_value(request.META[hname]))
            
        context['html'] = html
        
        return render(request, self.template_name, context)

