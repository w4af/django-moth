from django.views.generic import TemplateView
from django.shortcuts import render


class FamilyIndexTemplateView(TemplateView):
    '''
    When no URL pattern matches and it's a family URL (like /audit/ for example)
    we generate a page with links to all the tests in that directory.
    '''
    # The template to use to render this view
    template_name = "moth/index-of-family.html"
    
    def __init__(self, family, subviews, *args, **kwds):
        '''
        :param family: The URL that lead to the generation of this index.
        :param subviews: The vulnerable views (which are inside this directory.
        '''
        self._family = family
        self._subviews = subviews
        super(FamilyIndexTemplateView, self).__init__(*args, **kwds)
    
    def _generate_link_structure(self):
        '''
        :return: A dict containing:
                    {'plugin1': [(title1, link1), (title2, link2)],
                     'plugin2': [(title4, link4),],
                     ...
                     'pluginN': [(titleN, linkN),],}
                 
                 The keys of the dictionary are retrieved from the subviews
                 URL attribute, by getting the first directory of the path. 
        '''
        result = {}
        
        for view in self._subviews:
            if not view.linked:
                continue
            
            _, plugin_name = view.get_family_plugin()
            path = '%s/%s' % (plugin_name, view.get_trailing_url_part())
            tags = view.tags
            
            if plugin_name not in result:
                result[plugin_name] = [(view.title, path, tags),]
            else:
                result[plugin_name].append((view.title, path, tags))
        
        for plugin_name in result:
            result[plugin_name] = sorted(result[plugin_name], key=lambda x: x[0])
        
        return result
    
    def get(self, request):
        '''
        :return: An HttpResponse with links to all subviews.
        '''
        links = self._generate_link_structure()
        links = sorted(links.items(), key=lambda x: x[0])
        
        context = {}
        context['family'] = self._family.title() 
        context['links'] = links
        
        return render(request, self.template_name, context)
