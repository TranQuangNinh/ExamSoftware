from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from slugify import slugify
from datetime import datetime
# Create your models here.


class Role(models.Model):
    stt = models.IntegerField(default=1)
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    birth_day = models.DateField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    stt = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Menu(models.Model):
    menu_icon = models.CharField(max_length=100)
    menu_name = models.CharField(max_length=100)
    menu_link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.menu_name


class Subject(models.Model):
    stt = models.IntegerField(default=1)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Batch(models.Model):
    batch_name = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField()
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    status = models.BooleanField(default=False)
    stt = models.IntegerField(default=1)
    show_notifi = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.batch_name

    def get_absolute_url(self):
        return reverse("student:notif_detail", kwargs={"slug": self.slug})


class Exam(models.Model):
    stt = models.IntegerField(default=1)
    exam_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_time_to_do_exam = models.IntegerField(default=0)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.exam_name


class Question(models.Model):
    stt = models.IntegerField(default=1)
    question_main = models.TextField()
    question_sub = models.TextField(blank=True, null=True)
    question_img = models.ImageField(
        upload_to='question_img', blank=True, null=True)
    question_listen = models.FileField(
        upload_to='question_listen', blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)

    def __str__(self):
        return f'{self.question_main} {self.question_sub}'


class Answer(models.Model):
    stt = models.IntegerField(default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_name = models.TextField()
    answer_img = models.ImageField(
        upload_to='answer_img', blank=True, null=True)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_name


class Result(models.Model):
    stt = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choose_answer = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    key = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Exam_Result(models.Model):
    stt = models.IntegerField(default=1)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    total_correct_question = models.CharField(max_length=50)
    point = models.FloatField(default=0)
    rank = models.CharField(max_length=50)
    key = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


def create_slug(instance, new_slug=None):
    slug = slugify(instance.batch_name)
    if new_slug is not None:
        slug = new_slug
    qs = Batch.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_batch_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_batch_receiver, sender=Batch)
