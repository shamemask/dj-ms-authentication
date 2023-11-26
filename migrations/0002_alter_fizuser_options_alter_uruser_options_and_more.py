# Generated by Django 4.1.7 on 2023-11-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fizuser',
            options={'verbose_name': 'Физ.Лицо', 'verbose_name_plural': 'Физ.Лица'},
        ),
        migrations.AlterModelOptions(
            name='uruser',
            options={'verbose_name': 'Юр.Лицо', 'verbose_name_plural': 'Юр.Лица'},
        ),
        migrations.RemoveField(
            model_name='fizuser',
            name='shop_name',
        ),
        migrations.RemoveField(
            model_name='uruser',
            name='shop_name',
        ),
        migrations.AlterField(
            model_name='fizuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='fizuser',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='fizuser',
            name='is_active',
            field=models.BooleanField(default=False, null=True, verbose_name='Активный статус'),
        ),
        migrations.AlterField(
            model_name='fizuser',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='fizuser',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='fizuser',
            name='promo_code',
            field=models.CharField(blank=True, max_length=255, verbose_name='Промо-код'),
        ),
        migrations.AlterField(
            model_name='fizuser',
            name='terms_of_service',
            field=models.BooleanField(verbose_name='Условия обслуживания'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='account_number',
            field=models.CharField(max_length=20, verbose_name='Номер счета'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='bank',
            field=models.CharField(max_length=255, verbose_name='Банк'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='bik',
            field=models.CharField(max_length=9, verbose_name='БИК'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='correspondent_account',
            field=models.CharField(max_length=20, verbose_name='Корреспондентский счет'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='form',
            field=models.CharField(max_length=255, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='is_active',
            field=models.BooleanField(default=False, null=True, verbose_name='Активный статус'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='kpp',
            field=models.CharField(max_length=9, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='legal_address',
            field=models.CharField(max_length=255, verbose_name='Юридический адрес'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='organization_name',
            field=models.CharField(max_length=255, verbose_name='Название организации'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='uruser',
            name='terms_of_service',
            field=models.BooleanField(verbose_name='Условия обслуживания'),
        ),
    ]
