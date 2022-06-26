
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from userapp.models import Profile
from .models import Transactions
from django.contrib.auth.models import User
from django.db.models import Sum
from .forms import TransactionsForm
import datetime
from django.core.mail import send_mail

from django.conf import settings
# Create your views here.


class GetTranscaion:
    def __init__(self, category):
        self.tran = Transactions.objects.filter(category=category)

    def get_instance(self, user):

        return Profile.objects.get(id=user)

    def get_all(self, user):
        user = self.get_instance(user)
        amount = self.tran.filter(user=user).aggregate(
            Sum('amount'))['amount__sum']
        if amount is None:
            return 0

        return (amount) / 1000

    def get_today(self, user):
        user = self.get_instance(user)
        today_min = datetime.datetime.combine(
            datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(
            datetime.date.today(), datetime.time.max)
        amount = self.tran.filter(user=user, created_at__range=(today_min, today_max)).aggregate(
            Sum('amount'))['amount__sum']

        if amount is None:
            return 0

        return (amount) / 1000

    def get_last_week(self, user):
        user = self.get_instance(user)
        last_w = datetime.date.today() - datetime.timedelta(days=7)
        amount = self.tran.filter(user=user, created_at__gte=last_w).aggregate(
            Sum('amount'))['amount__sum']

        if amount is None:
            return 0

        return amount / 1000

    def get_last_month(self, user):
        user = self.get_instance(user)
        last_m = datetime.date.today() - datetime.timedelta(days=30)
        amount = self.tran.filter(user=user, created_at__gte=last_m).aggregate(
            Sum('amount'))['amount__sum']

        if amount is None:
            return 0

        return amount / 1000


income_tran = GetTranscaion('Income')  # To Access All Buninsess Logic
expends_tran = GetTranscaion('Expenses')  # To Access All Buninsess Logic


@login_required(login_url='/login/')
def index(request):
    all_total = 0.0
    trans = Transactions.objects.filter(user=request.user.id)
    income = income_tran.get_today(user=request.user.id)
    expenede = expends_tran.get_today(user=request.user.id)
    all_total = income - expenede
    context = {'trans': trans, 'all_total': all_total,
               'income_total': income,
               'expenses_total': expenede}
    return render(request, 'main/index.html', context=context)


@login_required(login_url='/login/')
def add_trans(request):

    if request.method == 'POST':
        form = TransactionsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            profiles = Profile.objects.get(id=request.user.id)
            form.user = profiles
            form.save()
            return redirect('main:index')

    return render(request, 'main/add_trans.html')


@login_required(login_url='/login/')
def edit_trans(request, tran_id):
    values = Transactions.objects.get(pk=tran_id)
    context = {'values': values}
    if request.method == 'POST':
        form = TransactionsForm(request.POST, instance=values)
        if form.is_valid():
            form = form.save(commit=False)
            profiles = Profile.objects.get(id=request.user.id)

            form.user = profiles
            form.save()
            return redirect('main:index')
    return render(request, 'main/edit_trans.html', context)


@login_required(login_url='/login/')
def dashbord(request):
    return render(request, 'main/dash_b.html')


@login_required(login_url='/login/')
def trans(request):
    trans = Transactions.objects.filter(user=request.user.id)
    context = {'trans': trans}
    return render(request, 'main/trans.html', context)


@login_required(login_url='/login/')
def income_trans(request):

    trans = Transactions.objects.filter(
        user=request.user.id, category='Income')
    context = {'trans': trans,
               'all_income': income_tran.get_all(user=request.user.id),

               'today': income_tran.get_today(user=request.user.id),
               'last_week': income_tran.get_last_week(user=request.user.id),
               'last_month': income_tran.get_last_month(user=request.user.id),
               }
    return render(request, 'main/income_trans.html', context)


@login_required(login_url='/login/')
def expenses_trans(request):

    trans = Transactions.objects.filter(
        user=request.user.id, category='Expenses')
    context = {'trans': trans,
               'all_expenses': expends_tran.get_all(user=request.user.id),
               'today': expends_tran.get_today(user=request.user.id),
               'last_week': expends_tran.get_last_week(user=request.user.id),
               'last_month': expends_tran.get_last_month(user=request.user.id),
               }
    return render(request, 'main/expenses_trans.html', context)


@login_required(login_url='/login/')
def user_page(request):
    return render(request, 'main/user_page.html', {'user': Profile.objects.get(pk=request.user.id)})


@login_required(login_url='/login/')
def delete_tran(request, delete_item):
    trans = Transactions.objects.get(id=delete_item)
    user = User.objects.get(id=trans.user.id)
    subject = "Delete Your  Transction Successfully "
    message = '''
        Delete This  Trancation \n
        Information Message  \n
        User Owner: {},
        Amount: {} in Category {},
        description is: {},
    
        '''.format(trans.user, trans.amount, trans.category, trans.desc)

    email_from = settings.EMAIL_HOST_USER

    recipient_list = [user.email, ]
    send_mail(subject, message, email_from,
              recipient_list,  fail_silently=False,)
    return redirect('main:success_delete')


def success_delete(request):
    return render(request, 'main/delete_sucess.html')


def error_404(request, exception):
    return render(request, 'main/404.html')
