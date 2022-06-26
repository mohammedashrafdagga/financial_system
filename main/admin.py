from django.contrib import admin
from .models import Transactions
# Register your models here.


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created_at', 'category')
    ordering = ('created_at',)
    list_filter = ('category', )
