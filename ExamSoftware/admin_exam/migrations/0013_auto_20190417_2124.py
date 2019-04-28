# Generated by Django 2.2 on 2019-04-17 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_exam', '0012_auto_20190416_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(default=1)),
                ('total_correct_question', models.IntegerField(default=0)),
                ('point', models.FloatField(default=0)),
                ('rank', models.CharField(max_length=50)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Exam')),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='exam_question',
        ),
        migrations.RemoveField(
            model_name='result',
            name='point',
        ),
        migrations.RemoveField(
            model_name='result',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='result',
            name='total_correct_question',
        ),
        migrations.AddField(
            model_name='result',
            name='choose_answer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Answer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='result',
            name='exam',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Exam'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin_exam.List_User'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Exam_Question',
        ),
    ]
