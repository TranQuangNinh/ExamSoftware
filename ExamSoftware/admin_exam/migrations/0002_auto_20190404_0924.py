# Generated by Django 2.1.7 on 2019-04-04 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(default=1)),
                ('exam_name', models.CharField(max_length=100)),
                ('total_time_to_do_exam', models.IntegerField(default=0)),
                ('exam_slug', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(default=1)),
                ('exam', models.ForeignKey(on_delete=False, to='admin_exam.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(default=1)),
                ('level_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MODELNAME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(default=1)),
                ('answer_name', models.CharField(max_length=255)),
                ('answer_img', models.CharField(blank=True, max_length=255, null=True)),
                ('correct_answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(default=1)),
                ('notifi_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(default=1)),
                ('question_name', models.CharField(max_length=255)),
                ('question_img', models.CharField(blank=True, max_length=255, null=True)),
                ('question_listen', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=0)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Level')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.IntegerField(default=1)),
                ('total_correct_question', models.IntegerField(default=0)),
                ('point', models.FloatField(default=0)),
                ('result_slug', models.TextField()),
                ('exam_question', models.ForeignKey(on_delete=False, to='admin_exam.Exam_Question')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='created_date',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list_user',
            name='stt',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='role',
            name='stt',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='subject',
            name='stt',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='stt',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='list_user',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=False, to='admin_exam.UserInfo'),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Subject'),
        ),
        migrations.AddField(
            model_name='notification',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Batch'),
        ),
        migrations.AddField(
            model_name='modelname',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Question'),
        ),
        migrations.AddField(
            model_name='exam_question',
            name='question',
            field=models.ForeignKey(on_delete=False, to='admin_exam.Question'),
        ),
        migrations.AddField(
            model_name='exam',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Batch'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_exam.Subject'),
        ),
    ]
