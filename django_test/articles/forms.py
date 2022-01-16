from django import forms
from .models import Tag
from .models import Article

'''
class ArticleForm(forms.Form):
    name=forms.CharField(label = 'Название статьи', max_length = 100)
    text=forms.CharField(label = 'Текст статьи')
    tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())
'''

class  ArticleForm(forms.ModelForm):
    article_name = forms.CharField(label = 'Название статьи')

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('article_name', 'article_text')
        # exclude = ('tags')