from dataclasses import fields
from unicodedata import category
from django import forms
from .models import Transactions


class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('amount', 'desc', 'category',)
