from munch import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from admin_exam.models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import decorators
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from datetime import datetime
from slugify import slugify
import random
import string
from collections import OrderedDict
from django.core.files.storage import FileSystemStorage
import json
import time
from django.core.paginator import Paginator

# Create your views here.
menu = Menu.objects.all()


# Hàm check thông báo


def check_show_notification():
    batch_true = Batch.objects.filter(status=True)

    batch_false = Batch.objects.filter(status=False)

    real_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    for i in batch_true:
        time_from = datetime.strftime(i.time_from, "%Y-%m-%d %H:%M")
        time_to = datetime.strftime(i.time_to, "%Y-%m-%d %H:%M")

        if time_from > real_time:
            i.status = False
            i.show_notifi = True
            i.save()

        if real_time >= time_to:
            i.status = False
            i.show_notifi = False
            i.save()

        if real_time > time_from:
            i.show_notifi = True
            i.save()

    for i in batch_false:
        time_from = datetime.strftime(i.time_from, "%Y-%m-%d %H:%M")
        time_to = datetime.strftime(i.time_to, "%Y-%m-%d %H:%M")

        if time_from <= real_time <= time_to:
            i.status = True
            i.show_notifi = True
            i.save()

        if real_time < time_from:
            i.status = False
            i.show_notifi = True
            i.save()

        if real_time >= time_to:
            i.show_notifi = False
            i.save()


# Errors


def error_404(request, exception):

    get_user = User.objects.all()
    get_user_info = UserInfo.objects.all()

    check_show_notification()

    ######################################
    notifi = []

    batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

    for _notifi in batch_notifi:
        notifi.append(_notifi)

    len_notifi = len(notifi)
    ######################################
    context = {
        'get_user': get_user,
        'get_user_info': get_user_info,
        'menu': menu,
        'notifi': notifi,
        'len_notifi': len_notifi,
        'batch_notifi': batch_notifi,
     }
    return render(request, 'errors/404.html', context)


def error_500(request):
    return render(request, 'errors/500.html')



def Feedback(request):
    get_user = User.objects.all()
    get_user_info = UserInfo.objects.all()

    check_show_notification()

    ######################################
    notifi = []

    batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

    for _notifi in batch_notifi:
        notifi.append(_notifi)

    len_notifi = len(notifi)
    ######################################
    context = {
        'get_user': get_user,
        'get_user_info': get_user_info,
        'menu': menu,
        'notifi': notifi,
        'len_notifi': len_notifi,
        'batch_notifi': batch_notifi,
    }
    return render(request, 'student/feedback.html', context)

# Trang chủ


class HomeView(View):

    def get(self, request):
        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()

        check_show_notification()

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################

        get_batchs = Batch.objects.filter(status=True).order_by('-id')
        get_exams = Exam.objects.all()
        get_subjects = Subject.objects.all()

        array = []
        for item_batch in get_batchs:
            for item_exam in get_exams:
                if item_batch.id == item_exam.batch_id:
                    for item_subject in get_subjects:
                        if item_exam.subject_id == item_subject.id:
                            array.append(item_subject)

        remove_duplicate = list(OrderedDict.fromkeys(array))

        for i in range(len(get_batchs)):
            get_batchs[i].stt = i + 1
            get_batchs[i].save()

        for i in range(len(get_subjects)):
            get_subjects[i].stt = i + 1
            get_subjects[i].save()

        context = {
            'get_user': get_user,
            'get_user_info': get_user_info,
            'menu': menu,
            'active_class': '',
            'notifi': notifi,
            'len_notifi': len_notifi,
            'batch_notifi': batch_notifi,
            'remove_duplicate': remove_duplicate,
            'get_batchs': get_batchs,
        }

        return render(request, 'student/index.html', context)


# Tham gia thi


class JoinTestView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        get_user_info = UserInfo.objects.all()
        get_user = User.objects.all()

        check_show_notification()

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################

        exam_list = Exam.objects.all()

        batch_true = Batch.objects.filter(status=True)
        get_exam = Exam.objects.all()

        for item_batch_true in batch_true:
            get_exam = Exam.objects.filter(
                batch=item_batch_true.id).order_by('-id').reverse()

            for a in range(len(get_exam)):
                get_exam[a].stt = a + 1
                get_exam[a].save()
        
        len_get_exam = len(get_exam)

        paginator = Paginator(get_exam, 10)
        page = request.GET.get('page') 
        gets_exams = paginator.get_page(page)

        context = {
            'get_user': get_user,
            'get_user_info': get_user_info,
            'menu': menu,
            'active_class': 'join',
            'notifi': notifi, 
            'len_notifi': len_notifi,
            'batch_notifi': batch_notifi, 
            'batch_status': batch_true,
            'len_get_exam':len_get_exam,
            'gets_exams': gets_exams,
        }
        return render(request, 'student/choose-exam.html', context)


# Làm bài thi


class StartTestView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):

        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()

        check_show_notification()

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################

        get_exam = Exam.objects.get(id=id)

        list_answer = Answer.objects.all()
        list_subject = Subject.objects.all()

        total_question_each_exam = 15

        array_choose_question = [] 
  
        # Random câu hỏi 
        for item_subject in list_subject:
            if get_exam.subject_id == item_subject.id:
                list_question = Question.objects.filter(
                    status=True, subject_id=item_subject.id)
                if len(list_question) > 0:
                    for i in range(total_question_each_exam):
                        while True:
                            if len(array_choose_question) < total_question_each_exam:
                                random_choose = random.choice(list_question)
                                if random_choose not in array_choose_question:
                                    array_choose_question.append(random_choose)
                                    break
                                else:
                                    total_question_each_exam += 1
 
        length_array_question = len(array_choose_question)
 
        for item in range(len(array_choose_question)):
            array_choose_question[item].stt = item + 1
            array_choose_question[item].save()

        context = { 
            'get_user': get_user,
            'get_user_info': get_user_info,
            'menu': menu, 
            'active_class': 'join',
            'notifi': notifi,
            'len_notifi': len_notifi,
            'get_exam': get_exam,
            'batch_notifi': batch_notifi,
            'list_question': list_question,
            'list_answer': list_answer,
            'array_choose_question': array_choose_question,
            'length_array_question': length_array_question,
        }
        return render(request, 'student/exam.html', context)

# Tính điểm


@decorators.login_required(login_url='/login/')
def CalculatorPoint(request):

    if request.method == 'POST':
        body_unicode = munchify(request.body.decode('utf-8'))
        body_data = json.loads(body_unicode)
        exam = body_data.get('id_exam')
        total_question = body_data.get('total_question')
        complete = body_data.get('complete')
        list_answer_question = body_data.get('list_answer_question')

        len_total_question = int(total_question)

        total_question_true = 0

        get_correct_answer = Answer.objects.filter(correct_answer=True)

        key_time = time.mktime(time.localtime())

        if len(list_answer_question) > 0: 
            for i in list_answer_question:
                result = Result(
                    choose_answer = int(i['value']),
                    exam_id = int(exam),
                    question_id = int(i['name']),
                    user_id = request.user.id,
                    complete = complete,
                    key = key_time,
                )
                result.save()
                for item_correct_answer in get_correct_answer: 
                    if int(i['value']) == item_correct_answer.id:
                        total_question_true += 1
                  
            point = round(((10 / len_total_question) * total_question_true), 2)
        else: 
            point = 0 

        rate = str(total_question_true) + '/' + total_question   

        rank = '' 
        if point < 4:
            rank = 'Kém'
        elif 4 <= point < 5:
            rank = 'Yếu'
        elif 5 <= point < 5.5:
            rank = 'Trung bình yếu'
        elif 5.5 <= point < 6.5:
            rank = 'Trung bình' 
        elif 6.5 <= point < 7: 
            rank = 'Trung bình khá'
        elif 7 <= point < 8:
            rank = 'Khá'
        elif 8 <= point < 8.5:
            rank = 'Khá giỏi'
        else:
            rank = 'Giỏi'

        exam_result = Exam_Result(
            total_correct_question = rate,
            point = point,
            user_id = request.user.id,
            exam_id = int(exam),
            rank = rank,
            date = datetime.now().strftime("%Y-%m-%d %H:%M"),
            key=key_time,
        )
        exam_result.save()

        response = {
            'id': exam_result.id,
            'key': key_time,
        }
        return JsonResponse(response)
        # return HttpResponse(json.dumps(response), content_type='application/json')

# Kết quả thi


class ResultView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()

        check_show_notification() 

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################
        
        exams = Exam.objects.all()

        exam_result = Exam_Result.objects.filter(user_id = request.user.id).order_by('-id')

        len_exam_result = len(exam_result)

        for a in range(len(exam_result)):
            exam_result[a].stt = a + 1
            exam_result[a].save()

        paginator = Paginator(exam_result, 10)
        page = request.GET.get('page')
        exams_results = paginator.get_page(page)

        context = { 
            'get_user': get_user, 
            'get_user_info': get_user_info,
            'menu': menu, 
            'active_class': 'result',
            'notifi': notifi,
            'len_notifi': len_notifi, 
            'batch_notifi': batch_notifi,
            'exams':exams,
            'len_exam_result':len_exam_result,
            'exams_results':exams_results,
        }
        return render(request, 'student/result.html', context)
 

# Chi tiết kết quả thi

@decorators.login_required(login_url='/login/')
def DetailResultView(request, id, key):
    get_user = User.objects.all()
    get_user_info = UserInfo.objects.all()

    check_show_notification()

    ######################################
    notifi = []

    batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

    for _notifi in batch_notifi:
        notifi.append(_notifi)

    len_notifi = len(notifi)
    ######################################

    exams = Exam.objects.all()

    exam_result = Exam_Result.objects.all()

    get_exam_result = Exam_Result.objects.get(id=id)
    get_key_exam_result = key

    results = Result.objects.filter(key=key)
    
    correct_answer = Answer.objects.filter(correct_answer = True)

    for a in range(len(results)):
        results[a].stt = a + 1
        results[a].save()

    list_answer_true = []
    list_answer_false = []
    for result in results:
        for item_correct_answer in correct_answer:
            if result.choose_answer == item_correct_answer.id:
                list_answer_true.append(result.choose_answer)
                list_answer_true = list(OrderedDict.fromkeys(list_answer_true))
            if result.choose_answer in list_answer_true:
                if result.choose_answer in list_answer_false:
                    list_answer_false.remove(result.choose_answer)
            else:
                list_answer_false.append(result.choose_answer)
                list_answer_false = list(
                    OrderedDict.fromkeys(list_answer_false))

    get_question = Question.objects.all()
    
    context = { 
        'get_user': get_user,
        'get_user_info': get_user_info,
        'menu': menu, 
        'active_class': 'result',
        'notifi': notifi,
        'len_notifi': len_notifi,
        'batch_notifi': batch_notifi,
        'results':results,
        'exams': exams, 
        'exam_result': exam_result,
        'get_key_exam_result':get_key_exam_result,
        'list_answer_true':list_answer_true,
        'list_answer_false':list_answer_false,
        'get_question':get_question,
    }
    return render(request, 'student/result-detail.html', context)


# Thông báo


class NotificationView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()
 
        check_show_notification() 

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################

        for a in range(len(batch_notifi)):
            batch_notifi[a].stt = a + 1
            batch_notifi[a].save()

        paginator = Paginator(batch_notifi, 10)
        page = request.GET.get('page') 
        batchs_notifications = paginator.get_page(page)

        context = {
            'get_user': get_user, 
            'get_user_info': get_user_info,
            'menu': menu,
            'active_class': 'notification',
            'notifi': notifi,
            'len_notifi': len_notifi,
            'batch_notifi': batch_notifi, 
            'batchs_notifications':batchs_notifications,
        }

        return render(request, 'student/notification.html', context)


# Chi tiết thông báo


@decorators.login_required(login_url='/login/')
def NotificationDetailView(request, slug):
    get_user = User.objects.all()
    get_user_info = UserInfo.objects.all()

    check_show_notification()
 
    ######################################
    notifi = []

    batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

    for _notifi in batch_notifi:
        notifi.append(_notifi)

    len_notifi = len(notifi)
    ######################################

    get_batch = Batch.objects.get(slug=slug)

    context = {
        'get_user': get_user,
        'get_user_info': get_user_info,
        'menu': menu,
        'active_class': 'notification',
        'notifi': notifi,
        'len_notifi': len_notifi,
        'get_batch': get_batch,
        'batch_notifi': batch_notifi,
    }
    return render(request, 'student/notification-detail.html', context)


# Thông tin cá nhân


class ProfileView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()

        user = User.objects.get(id=request.user.id)
        user_info = UserInfo.objects.get(user=user)

        check_show_notification()

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################

        context = {
            'get_user': get_user,
            'get_user_info': get_user_info,
            'user':user,
            'user_info': user_info,
            'menu': menu,
            'active_class': 'profile',
            'notifi': notifi,
            'len_notifi': len_notifi,
            'batch_notifi': batch_notifi,
        }
        return render(request, 'student/profile.html', context)


# Cập nhật thông tin cá nhân


class ProfileUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()

        check_show_notification()

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################

        user = User.objects.get(id=request.user.id)
        user_info = UserInfo.objects.get(user=user)

        context = {
            'get_user': get_user, 
            'get_user_info': get_user_info,
            'user':user,
            'user_info': user_info,
            'menu': menu,
            'active_class': 'profile',
            'notifi': notifi,
            'len_notifi': len_notifi,
            'batch_notifi': batch_notifi,
        }
        return render(request, 'student/profile-update.html', context)

    def post(self, request):
        user_login = User.objects.get(id=request.user.id)

        user_info = UserInfo.objects.filter(user=user_login)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_day = request.POST.get('birth_day')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        date = datetime.strptime(birth_day,"%d-%m-%Y") 
        birth_day = datetime.strftime(date, "%Y-%m-%d")

        user_info.update(
            birth_day=birth_day,
            phone_number=phone_number,
            address=address,
        )

        user_login.first_name = first_name
        user_login.last_name = last_name
        user_login.email = email
        user_login.save()

        return HttpResponseRedirect('/profile/')


# Cập nhật ảnh đại diện

@decorators.login_required(login_url='/login/')
def UpdateAvatar(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['avatar']
        fs = FileSystemStorage()
        name = fs.save('avatar/' + uploaded_file.name, uploaded_file)

        url = fs.url(name).replace("/", " ").split()[2:]

        id = User.objects.get(username=request.user.username).id
        user_info = UserInfo.objects.filter(user=id)

        avatar = "/".join(url)

        user_info.update(
            avatar=avatar,
        )

        return HttpResponseRedirect('/profile/')
    else:
        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()

        check_show_notification()

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################

        context = {
            'get_user': get_user,
            'get_user_info': get_user_info,
            'menu': menu,
            'active_class': 'profile',
            'notifi': notifi,
            'len_notifi': len_notifi,
            'batch_notifi': batch_notifi,
        }
        return render(request, 'student/update_avatar.html', context)


# Đổi mật khẩu


class ChangePassView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()

        check_show_notification()

        ######################################
        notifi = []

        batch_notifi = Batch.objects.filter(show_notifi=True).order_by('-id')

        for _notifi in batch_notifi:
            notifi.append(_notifi)

        len_notifi = len(notifi)
        ######################################

        context = {
            'get_user': get_user,
            'get_user_info': get_user_info,
            'menu': menu,
            'notifi': notifi,
            'len_notifi': len_notifi,
            'batch_notifi': batch_notifi,
        }
        return render(request, 'student/changepassword.html', context)

    def post(self, request):
        old_pass = request.POST.get('oldpass')
        new_pass = request.POST.get('newpass')
        confirm_new_pass = request.POST.get('confirmnewpass')
        user = User.objects.get(username=request.user.username)
        if user.check_password(old_pass):
            if new_pass == confirm_new_pass:
                user.set_password(new_pass)
                user.save()
                return HttpResponseRedirect('/logout/')
            else:
                errors = 'Xác nhận mật khẩu không chính xác !!!'
                return render(request, 'student/changepassword.html', {
                    'errors': errors,
                    'menu': menu
                })
        errors = 'Mật khẩu cũ không chính xác !!!'
        get_user = User.objects.all()
        get_user_info = UserInfo.objects.all()
        return render(request, 'student/changepassword.html', {
            'get_user': get_user,
            'get_user_info': get_user_info,
            'errors': errors,
            'menu': menu
        })


# Đăng nhập


class LoginView(View):
    def get(self, request):
        if request.user.username:
            return HttpResponseRedirect('/')
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'])

                login(request, user)

                id = User.objects.get(username=request.user.username).id
                user_info = UserInfo.objects.get(user=id).role

                if str(user_info) == 'Student':
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/admin/')

            else:
                errors = 'Tên tài khoản hoặc mật khẩu không chính xác !!!'
                return render(request, 'login/login.html', {
                    'form': form,
                    'errors': errors
                })


# Đăng ký


class RegisterView(View):
    def get(self, request):
        if request.user.username:
            return HttpResponseRedirect('/')
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'login/register.html', context)

    def post(self, request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                birth_day = form.cleaned_data['birth_day']
                phone_number = form.cleaned_data['phone_number']
                address = form.cleaned_data['address']

                date = datetime.strptime(birth_day,"%d-%m-%Y") 
                birth_day = datetime.strftime(date, "%Y-%m-%d")

                user = User.objects.filter(username=username)
                user[0].userinfo_set.create(
                    avatar='avatar/default_avatar.png',
                    birth_day=birth_day,
                    phone_number=phone_number,
                    address=address,
                    role_id=3,
                )
                return HttpResponseRedirect('/login/')
            else:
                errors = form.errors
                return render(request, 'login/register.html', {
                    'form': form,
                    'errors': errors
                })


# Đăng xuất


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# Lấy ngẫu nhiên chuỗi trong phạm vi 10 ký tự


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# Quên mật khẩu


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'login/forgot-password.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        users = User.objects.all()
        for user in users:
            if user.username == username:
                get_email = User.objects.get(username=username).email
                if get_email == email:
                    new_password = randomString(10)
 
                    subject = 'ExamSoftware xin chào bạn !'
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [get_email]
                    message = 'Cảm ơn bạn đã đăng ký và sử dụng phần mềm. \nBạn đã sử dụng chức năng lấy lại mật khẩu. \nTài khoản bạn muốn lấy lại mật khẩu là: %s \nVui lòng đăng nhập lại bằng mật khẩu sau: %s' % (
                        username, new_password)

                    send_mail(
                        subject,
                        message,
                        from_email, 
                        to_list,
                        fail_silently=False)

                    user_login = User.objects.get(username=username)
                    user_login.set_password(new_password)
                    user_login.save()

                    return HttpResponseRedirect('/login/')
                else:
                    errors = 'Tên đăng nhập hoặc Email không chính xác khi đăng ký !!!'
                    return render(request, 'login/forgot-password.html',
                                  {'errors': errors})
        errors = 'Tên đăng nhập hoặc Email không chính xác khi đăng ký !!!'
        return render(request, 'login/forgot-password.html',
                      {'errors': errors})
