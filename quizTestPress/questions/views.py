from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Questions, UserQuestions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout


def loginpage(request):
    form = UserCreationForm
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Either password or username is incorrect")
    context = {'form': form}
    return render(request, 'login.html', context)


def userlogout(request):
    logout(request)
    return redirect("/")


def home(request, number, userId, setId,home):
    return redirect("/")


def createquiz(request, userId, setId):
    questions = Questions.objects.filter(Set=setId)
    if UserQuestions.objects.filter(Set_Id=setId, User_ID=userId):
        UserQuestions.objects.filter(Set_Id=setId, User_ID=userId).delete()

    UserQuestions.objects.create(User_ID=userId, Set_Id=setId, Attempt=0, Question_1=questions[0].Number,
                                 Question_2=questions[1].Number, Question_3=questions[2].Number,
                                 Question_4=questions[3].Number,
                                 Question_5=questions[4].Number, Question_6=questions[5].Number,
                                 Question_7=questions[6].Number, Question_8=questions[7].Number,
                                 Question_9=questions[8].Number, Question_10=questions[9].Number, Question_1_Status=0,
                                 Question_2_Status=0, Question_3_Status=0, Question_4_Status=0, Question_5_Status=0,
                                 Question_6_Status=0, Question_7_Status=0, Question_8_Status=0, Question_9_Status=0,
                                 Question_10_Status=0, )


def index(request):
    question_set = []
    questions = Questions.objects.all()
    user_logged = False
    if request.user.username:
        username = request.user.username
        user_logged = True
    print(request.user.username)
    for q in questions:
        question_set.append(q.Set)
    question_set = list(set(question_set))
    print(user_logged)
    if user_logged:
     content = {'questions': question_set, 'user_logged': user_logged, 'user' : username }
    else:
     content = {'questions': question_set, 'user_logged': user_logged}
    return render(request, 'all_quiz.html', content)


def answer(request, number, option):
    questions = Questions.objects.all()
    return HttpResponseRedirect('/questions/')


def total_marks(request, userId, setId):
    all_answer = UserQuestions.objects
    total_marks = 0
    theist = {
        1: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_1_Status],
        2: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_2_Status],
        3: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_3_Status],
        4: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_4_Status],
        5: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_5_Status],
        6: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_6_Status],
        7: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_7_Status],
        8: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_8_Status],
        9: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_9_Status],
        10: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_10_Status]
    }
    for i in range(1, 11):
        if theist[i][0] == 1:
            total_marks += 1

    return total_marks


def test_completed(request, userId, setId):
    all_answer = UserQuestions.objects
    answered = 0
    theist = {
        1: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_1_Status],
        2: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_2_Status],
        3: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_3_Status],
        4: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_4_Status],
        5: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_5_Status],
        6: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_6_Status],
        7: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_7_Status],
        8: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_8_Status],
        9: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_9_Status],
        10: [all_answer.filter(User_ID=userId, Set_Id=setId)[0].Question_10_Status]
    }
    for i in range(1, 11):
        if theist[i][0] > 0:
            answered += 1
    if answered == 10:
        return True
    else:
        return False


def get_answer(request):
    ans = []
    if request.GET.get('option_1'):
        ans.append(int(request.GET.get('option_1')))
    else:
        ans.append(0)
    if request.GET.get('option_2'):
        ans.append(int(request.GET.get('option_2')))
    else:
        ans.append(0)
    if request.GET.get('option_3'):
        ans.append(int(request.GET.get('option_3')))
    else:
        ans.append(0)
    if request.GET.get('option_4'):
        ans.append(int(request.GET.get('option_4')))
    else:
        ans.append(0)

    return ans


def question(request, number, userId, setId):
    if request.user.username:
        username = request.user.username
        print(username)
    show_previous = False
    show_next = False
    question_answered = False
    question_status = ''
    ans = []

    if number == 0 or number > 10:
        number = 1
    if not UserQuestions.objects.filter(User_ID=userId, Set_Id=setId):
        createquiz(request, userId, setId)

    numbers = UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)
    theist = {
        1: [numbers[0].Question_1, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_1_Status',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_1_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_1_Status=2)'],
        2: [numbers[0].Question_2, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_2_Status',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_2_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_2_Status=2)'],
        3: [numbers[0].Question_3, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_3_Status',
            ' UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_3_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_3_Status=2)'],
        4: [numbers[0].Question_4, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_4_Status',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_4_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_4_Status=2)'],
        5: [numbers[0].Question_5, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_5_Status',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_5_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_5_Status=2)'],
        6: [numbers[0].Question_6, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_6_Status',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_6_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_6_Status=2)'],
        7: [numbers[0].Question_7, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_7_Status',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_7_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_7_Status=2)'],
        8: [numbers[0].Question_8, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_8_Status',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_8_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_8_Status=2)'],
        9: [numbers[0].Question_9, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_9_Status',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_9_Status=1)',
            'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_9_Status=2)'],
        10: [numbers[0].Question_10, 'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId)[0].Question_10_Status',
             'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_10_Status=1)',
             'UserQuestions.objects.filter(User_ID=userId, Set_Id=setId).update(Question_10_Status=2)']
    }
    print(theist[number][1], userId, setId)
    questions = Questions.objects.filter(Number=theist[number][0])
    print(eval(theist[number][1]))
    if eval(theist[number][1]) == 0:

        if request.GET.get('option_1') or request.GET.get('option_2') or request.GET.get('option_3') or request.GET.get(
                'option_4'):
            ans = get_answer(request)
            if (ans[0] == int(questions[0].Option_1_Correct)) and (ans[1] == int(questions[0].Option_2_Correct)) and (
                    ans[
                        2] == int(questions[
                                      0].Option_3_Correct)) and (ans[3] == int(questions[0].Option_4_Correct)):
                eval(theist[number][2])
            else:
                print(ans[0] == int(questions[0].Option_1_Correct))
                print(ans[1] == int(questions[0].Option_2_Correct))
                print(ans[2] == int(questions[0].Option_3_Correct))
                print(ans[3] == int(questions[0].Option_4_Correct))
                eval(theist[number][3])
    if number in range(2, 11):
        show_previous = True
    if number in range(1, 10):
        show_next = True
    if eval(theist[number][1]) > 0:
        question_answered = True
        if eval(theist[number][1]) == 1:
            question_status = 'Correct Answer'
        else:
            question_status = 'Incorrect Answer '
    total = total_marks(request, userId, setId)
    test_finished = test_completed(request, userId, setId)
    content = {'q': questions[0], 'test_finished': test_finished, 'number': number, 'show_previous': show_previous,
               'show_next': show_next,
               'question_answered': question_answered, 'question_status': question_status, 'progress': number * 10,
               'total': total}
    return render(request, 'quiz_exam.html', content)


def all_quiz_sets(request):
    return HttpResponse('Get ready')
