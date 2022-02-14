from .models import *

menu = [{'title': 'About us', 'url_name': 'about'},
        {'title': 'Main page', 'url_name': 'home'},
        {'title': 'Articles', 'url_name': 'articles'},
        {'title': 'Tasks', 'url_name': 'tasks'},
        {'title': 'Add feedback', 'url_name': 'add_feedback'}]

class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                cats = Category.objects.all()
                context['menu'] = menu
                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context