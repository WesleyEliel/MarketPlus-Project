from django import forms
from Search.models import SearchTerm, ImageSearchTools


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchTerm
        exclude = ['', ]

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        default_text = 'Search'
        self.fields['q'].widget.attrs['value'] = default_text
        self.fields['q'].widget.attrs['onfocus'] = "if (this.value=='" + default_text + "')this.value = ''"
    include = ('q',)


class ImageSearchForm(forms.ModelForm):
    class Meta:
        model = ImageSearchTools
        exclude = ['', ]

    def __init__(self, *args, **kwargs):
        super(ImageSearchForm, self).__init__(*args, **kwargs)
        self.fields['file_input'].widget.attrs['class'] = 'custom-file-input col-md-10 col-sm-10' 
        default_text = 'Search'
        self.fields['file_input'].widget.attrs['value'] = default_text
        self.fields['file_input'].widget.attrs['onfocus'] = "if (this.value=='" + default_text + "')this.value = ''"
    include = ('file_input',)

