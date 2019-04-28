# Generated by Django 2.2 on 2019-04-20 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_exam', '0020_auto_20190420_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_suggest',
            new_name='question_main',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_name',
        ),
        migrations.AddField(
            model_name='question',
            name='question_sub',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
