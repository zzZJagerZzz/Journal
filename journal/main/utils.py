class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = {'Главная'}
        context['logo'] = 'Journal'
        return context