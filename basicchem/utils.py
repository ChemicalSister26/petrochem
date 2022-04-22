from .models import *

menu = [{'title': 'About us', 'url_name': 'about'},
        {'title': 'Main page', 'url_name': 'home'},
        {'title': 'Articles', 'url_name': 'articles'},
        {'title': 'Tasks', 'url_name': 'tasks'},
        {'title': 'Add feedback', 'url_name': 'add_feedback'},
        ]



class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
            context = kwargs
            cats = Category.objects.all()

            user_menu = menu.copy()
            if not self.request.user.is_authenticated:
                    user_menu.pop(4)
            context['menu'] = user_menu

            context['cats'] = cats
            return context