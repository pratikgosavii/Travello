import django_filters
from .models import clientdetails

class SnippetFliter(django_filters.FilterSet):

    class Meta:
        models = clientdetails
        fields = {'title', 'body', 'creater'}
