from django import forms
from Products.models import *


class ProductReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductReviewForm, self).__init__(*args, **kwargs)
        # override default attributes
        # Values for attrs class
        self.fields['title'].widget.attrs['class'] = 'size-111 bor8 stext-102 cl2 p-lr-20'
        self.fields['content'].widget.attrs['class'] = 'size-110 bor8 stext-102 cl2 p-lr-20'

        #Values of attrs placeholer

        self.fields['content'].widget.attrs['placeholder'] = 'Write Your Review ...'
    class Meta:
        model = ProductReview
        exclude = ('user','product', 'is_approved')

class ProductAnonymousReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductAnonymousReviewForm, self).__init__(*args, **kwargs)
        # override default attributes
        # Values for attrs class
        self.fields['title'].widget.attrs['class'] = 'size-111 bor8 stext-102 cl2 p-lr-20'
        
        self.fields['complete_name'].widget.attrs['class'] = 'size-111 bor8 stext-102 cl2 p-lr-20'
        self.fields['email'].widget.attrs['class'] = 'size-111 bor8 stext-102 cl2 p-lr-20'
        self.fields['content'].widget.attrs['class'] = 'size-110 bor8 stext-102 cl2 p-lr-20'
        
        #Values of attrs placeholder 
        self.fields['complete_name'].widget.attrs['placeholder'] = 'Complete Name'
        self.fields['email'].widget.attrs['placeolder'] = 'Your Email'
        """self.fields[field].widget.attrs['class'] = 'size-110 bor8 stext-102 cl2 p-lr-20'
        self.fields[field].widget.attrs['class'] = 'size-110 bor8 stext-102 cl2 p-lr-20'
        self.fields[field].widget.attrs['class'] = 'size-110 bor8 stext-102 cl2 p-lr-20'"""
    class Meta:
        model = ProductAnonymousReview
        exclude = ('user','product', 'is_approved')