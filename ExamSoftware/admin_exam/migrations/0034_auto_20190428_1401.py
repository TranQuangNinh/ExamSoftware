# Generated by Django 2.2 on 2019-04-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_exam', '0033_auto_20190428_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='batch',
            name='time_from',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='batch',
            name='time_to',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exam_result',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
