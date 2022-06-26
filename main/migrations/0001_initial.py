# Generated by Django 4.0.5 on 2022-06-26 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desc', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('Income', 'income'), ('Expenses', 'expenses')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profile')),
            ],
        ),
    ]
