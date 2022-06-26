
from django.urls import path
from . import views as vs
app_name = 'main'

urlpatterns = [
    path('', vs.index, name='index'),
    path('add-transactions/', vs.add_trans, name='add_trans'),
    path('edit-transactions/<tran_id>/',
         vs.edit_trans, name='edit_trans'),
    path('dashbord/', vs.dashbord, name='dashbord'),
    path('transcations/', vs.trans, name='side_trans'),
    path('income-transcations/', vs.income_trans, name='income_trans'),
    path('expenses-transcations/', vs.expenses_trans, name='expenses_trans'),
    path('user-profile/', vs.user_page, name='user_page'),
    path('success-delete', vs.success_delete, name='success_delete'),
    path('delete-trans/<delete_item>/', vs.delete_tran, name='delete-tran'),
]
