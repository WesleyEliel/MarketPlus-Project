from django import forms
from Blog.models import *


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(EmailPostForm, self).__init__(*args, **kwargs)
        # override default attributes
        for field in self.fields:
            # Class attribute
            self.fields['name'].widget.attrs['class'] = 'stext-111 cl2 plh3 size-116 p-lr-18'
            self.fields['email'].widget.attrs['class'] = 'stext-111 cl2 plh3 size-116 p-lr-18'
            self.fields['to'].widget.attrs['class'] = 'stext-111 cl2 plh3 size-116 p-lr-18'
            self.fields['comments'].widget.attrs['class'] = 'stext-111 cl2 plh3 size-120 p-lr-18 p-tb-15'
            
            # Placeholder attribute
            self.fields['name'].widget.attrs['placeholder'] = 'Name *'
            self.fields['email'].widget.attrs['placeholder'] = 'Email *'
            self.fields['to'].widget.attrs['placeholder'] = 'To *'
            self.fields['comments'].widget.attrs['placeholder'] = 'Comment... *'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body')
        widget = {'body': forms.Textarea}
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # override default attributes
        for field in self.fields:
            # Class attribute
            self.fields['name'].widget.attrs['class'] = 'stext-111 cl2 plh3 size-116 p-lr-18'
            self.fields['email'].widget.attrs['class'] = 'stext-111 cl2 plh3 size-116 p-lr-18'
            self.fields['website'].widget.attrs['class'] = 'stext-111 cl2 plh3 size-116 p-lr-18'
            self.fields['body'].widget.attrs['class'] = 'stext-111 cl2 plh3 size-120 p-lr-18 p-tb-15'
            
            # Placeholder attribute
            self.fields['name'].widget.attrs['placeholder'] = 'Name *'
            self.fields['email'].widget.attrs['placeholder'] = 'Email *'
            self.fields['website'].widget.attrs['placeholder'] = 'Website'
            self.fields['body'].widget.attrs['placeholder'] = 'Comment... *'


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for fieldv in self.fields:
            self.fields['query'].widget.attrs['class'] = 'stext-103 cl2 plh4 size-116 p-l-28 p-r-55'
            self.fields['query'].widget.attrs['placeholder'] = 'Search'
