# Generated by Django 2.2 on 2019-04-08 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_exam', '0009_auto_20190408_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_img',
            field=models.ImageField(blank=True, upload_to='answer_img'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_img',
            field=models.ImageField(blank=True, upload_to='question_img'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_listen',
            field=models.FileField(blank=True, upload_to='question_listen'),
        ),
    ]
