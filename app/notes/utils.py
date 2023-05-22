menu = [{'title': 'Заметки', 'url_name': 'index'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить заметку', 'url_name': 'add'}
        ]


class DataMixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
            user_menu.pop()

        context['menu'] = user_menu
        return context
