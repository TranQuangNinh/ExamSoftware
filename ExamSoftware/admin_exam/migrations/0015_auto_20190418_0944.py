# Generated by Django 2.2 on 2019-04-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_exam', '0014_exam_result_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_result',
            name='total_correct_question',
            field=models.CharField(max_length=50),
        ),
    ]
