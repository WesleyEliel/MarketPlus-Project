from django.db import models
from django import forms
from .models import *
from Coupons.models import Coupon
import datetime
from django.utils import timezone
import re


def cc_expire_years():
    current_year = datetime.datetime.now().year
    years = range(current_year, current_year + 12)
    return [(str(x), str(x)) for x in years]


def cc_expire_months():
    months = []
    for month in range(1, 13):
        if len(str(month)) == 1:
            numeric = '0' + str(month)
        else:
            numeric = str(month)
        months.append((numeric, datetime.date(2009, month, 1).strftime('%B')))
    return months


CARD_TYPES = (('Mastercard', 'Mastercard'), ('VISA', 'VISA'),
              ('AMEX', 'AMEX'), ('Discover', 'Discover'),)


def strip_non_numbers(data):
    """ gets rid of all non-number characters """
    non_numbers = re.compile('\D')
    return non_numbers.sub('', data)


# Gateway test credit cards won't pass this validation
def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """
    digits_sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(0, num_digits):
        digit = int(card_number[count])
        if not ((count & 1) ^ oddeven):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        digits_sum = digits_sum + digit
    return ((digits_sum % 10) == 0)


class CheckoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        # override default attributes
        for field in self.fields:
            # Values for attrs size
            self.fields[field].widget.attrs['size'] = '30'
            self.fields['billing_state'].widget.attrs['size'] = '3'
            self.fields['billing_zip'].widget.attrs['size'] = '6'
            self.fields['credit_card_type'].widget.attrs['size'] = '1'
            self.fields['credit_card_expire_year'].widget.attrs['size'] = '1'
            self.fields['credit_card_expire_month'].widget.attrs['size'] = '1'
            self.fields['credit_card_cvv'].widget.attrs['size'] = '5'

            # Values for attrs class
            self.fields[field].widget.attrs['class'] = 'form-control'

            # Values for attrs aria-describedby

            self.fields['billing_country'].widget.attrs['aria-describedby'] = 'country'
            # Firsts Names
            self.fields['billing_first_name'].widget.attrs['aria-describedby'] = 'name2'
            # Lasts Names
            self.fields['billing_last_name'].widget.attrs['aria-describedby'] = 'last2'
            # Shipping Addresses
            self.fields['billing_address_1'].widget.attrs['aria-describedby'] = 'address'
            # Billing Addresses
            self.fields['billing_address_2'].widget.attrs['aria-describedby'] = 'address'
            # Email
            self.fields['email'].widget.attrs['aria-describedby'] = 'email'
            # Phone
            self.fields['phone'].widget.attrs['aria-describedby'] = 'phone'
            # City
            self.fields['billing_city'].widget.attrs['aria-describedby'] = 'city'
            # Others Notes
            self.fields['billing_other_note'].widget.attrs['aria-describedby'] = 'city'

            self.fields['shipping_different_address'].widget.attrs['aria-describedby'] = 'shipping_different_address'
            self.fields['billing_state'].widget.attrs['aria-describedby'] = 'state'
            self.fields['billing_state'].widget.attrs['aria-describedby'] = 'state'
            self.fields['billing_zip'].widget.attrs['aria-describedby'] = 'zip'

            self.fields['credit_card_type'].widget.attrs['aria-describedby'] = 'card_type'
            self.fields['credit_card_expire_year'].widget.attrs['aria-describedby'] = 'card_expire_year'
            self.fields['credit_card_expire_month'].widget.attrs['aria-describedby'] = 'card_expire_month'
            self.fields['credit_card_cvv'].widget.attrs['aria-describedby'] = 'card_cvv'

    class Meta:
        model = Order
        exclude = ('status', 'ip_address', 'user', 'transaction_id', 'coupon')
    
    credit_card_number = forms.CharField()
    credit_card_type = forms.CharField(widget=forms.Select(choices=CARD_TYPES))
    credit_card_expire_month = forms.CharField(widget=forms.Select(choices=cc_expire_months()))
    credit_card_expire_year = forms.CharField(widget=forms.Select(choices=cc_expire_years()))
    credit_card_cvv = forms.CharField()

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone) < 10:
            raise forms.ValidationError('Enter a valid phone number with area code.(e.g.555 - 555 - 5555)')
        return self.cleaned_data['phone']
    
    def clean_coupon_code(self):
        coupon_code = self.cleaned_data['coupon_code']
        now = datetime.datetime.now()
        try:
            coupon = Coupon.objects.get(code__iexact=coupon_code,
                                            valid_from__lte=now, 
                                            valid_to__gte=now, 
                                            active=True)
        except:
            raise forms.ValidationError('The coupon code you have enter is not working actually')
        return self.cleaned_data['coupon_code']
    
    def clean_credit_card_number(self):
        cc_number = self.cleaned_data['credit_card_number']
        stripped_cc_number = strip_non_numbers(cc_number)
        if not cardLuhnChecksumIsValid(stripped_cc_number):
            raise forms.ValidationError('The credit card you entered is invalid.')


class ShippingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        # override default attributes
        for field in self.fields:
            # Values for attrs size
            self.fields[field].widget.attrs['size'] = '30'
            self.fields['shipping_state'].widget.attrs['size'] = '3'
            self.fields['shipping_state'].widget.attrs['size'] = '3'
            self.fields['shipping_zip'].widget.attrs['size'] = '6'
            self.fields['shipping_state'].widget.attrs['size'] = '3'
            self.fields['shipping_state'].widget.attrs['size'] = '3'
            self.fields['shipping_zip'].widget.attrs['size'] = '6'

    class Meta:
        model = ShippingAddress
        exclude = ('order',)
