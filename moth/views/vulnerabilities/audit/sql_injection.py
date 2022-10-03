from django.contrib.auth.models import User
from django.shortcuts import render

from moth.forms.generic import GenericForm
from moth.views.base.form_template_view import FormTemplateView
from moth.views.base.vulnerable_template_view import VulnerableTemplateView


class SQLIntegerFormView(FormTemplateView):
    template_name = "moth/vulnerability-users-table.html"
    title = 'Trivial SQL injection'
    tags = ['WHERE', 'integer', 'form']
    description = 'Trivial SQL injection in a SQL query WHERE section, integer'\
                  ' field which is reachable using an HTML form with one'\
                  ' parameter.'
    url_path = 'where_integer_form.py'
    
    def post(self, request, *args, **kwds):
        # pylint: disable=E1101
        form = GenericForm(data=request.POST)
        if not form.is_valid():
            context = self.get_context_data(success=False,
                                            form=GenericForm())
        else:
            user_input = form.cleaned_data[GenericForm.INPUT]
            query = "SELECT * FROM auth_user WHERE id = %s" % user_input
            
            db_error, users = get_users(query)
            
            context = self.get_context_data(db_error=db_error,
                                            users=users,
                                            success=True,
                                            form=GenericForm())
            
        return render(request, self.template_name, context)


class SQLIntegerQSView(VulnerableTemplateView):
    title = 'Trivial SQL injection'
    tags = ['WHERE', 'integer', 'query-string']
    description = 'Trivial SQL injection in a SQL query WHERE section, integer'\
                  ' field which is reachable using a query string.'
    url_path = 'where_integer_qs.py?id=1'
    template_name = "moth/vulnerability-users-table.html"
    
    def get(self, request, *args, **kwds):
        user_input = request.GET.get('id', '1')
        query = "SELECT * FROM auth_user WHERE id = %s" % user_input
        
        db_error, users = get_users(query)
        
        context = self.get_context_data(db_error=db_error,
                                        users=users,
                                        success=True)
        
        return render(request, self.template_name, context)


class SQLSingleQuoteStringQSView(VulnerableTemplateView):
    title = 'Trivial SQL injection'
    tags = ['WHERE', 'string', 'single-quote', 'query-string']
    description = 'Trivial SQL injection in a SQL query WHERE section, single'\
                  ' quote string field which is reachable using a query string.'
    url_path = 'where_string_single_qs.py?uname=pablo'
    template_name = "moth/vulnerability-users-table.html"
    
    def get(self, request, *args, **kwds):
        user_input = request.GET.get('uname', 'pablo')
        query = "SELECT * FROM auth_user WHERE username = '%s'" % user_input
        
        db_error, users = get_users(query)
        
        context = self.get_context_data(db_error=db_error,
                                        users=users,
                                        success=True)
        
        return render(request, self.template_name, context)


def get_users(query):
    db_error = None
    users = []
    
    try:
        users_qs = User.objects.raw(query)
        users = [u for u in users_qs]
    except Exception as dbe:
        db_error = str(dbe)
    
    return db_error, users
