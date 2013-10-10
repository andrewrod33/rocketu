from django.contrib.auth import authenticate

from django.shortcuts import render, HttpResponseRedirect

from models import Poll,PollAnswer

from forms import PollAnswerForm,PollForm, UserForm, SignupForm, User, Authenticate #PollFormNew

from django.views.decorators.cache import cache_page

def poll(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)

    data = {
        "poll": poll
    }

    return render(request, "home.html", data)

def poll_results(request, poll_id):
    poll= Poll.objects.get(pk=poll_id)

    data = {
        "poll": poll,
        "results": True
    }

    return render(request,"home.html", data)

# @cache_page(900)
def add_poll_answer(request):
    data = {}
    if request.method == "POST":
        form = PollAnswerForm(request.POST)
        if form.is_valid():
            poll = form.cleaned_data["poll"]
            new_answer = form.cleaned_data["answer"]

            answer = PollAnswer(poll=poll, answer=new_answer)
            answer.save()

            data["message"] = "Answer saved."
    else:
        form = PollAnswerForm()

    data["poll_form"] = form

    return render(request,"forms.html", data)

def add_poll(request):
    data = {}
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            # question = form.cleaned_data["question"]
            # description = form.cleaned_data["description"]
            # active = form.cleaned_data["active"]
            #
            # answer = Poll(question=question, description=description, active=active)
            # answer.save()
            form.save()
            data["message"] = "Answer saved."
    else:
        form = PollForm()

    data["poll_form"] = form

    return render(request,"form.html", data)

def latest_poll(request):
    data = {"latest" : Poll.objects.latest("pk")}
    return render(
        request,
        "admin/latest_poll.html",
        data
    )

# def radio_poll(request, poll_id):
#     poll = Poll.objects.get(pk=poll_id)
#     data = {}
#     if request.method == "POST":
#         form = PollFormNew(request.POST)
#         if form.is_valid():
#             poll_answer_id=form.cleaned_data["answer"]
#             poll_answer = PollAnswer.objects.get(pk=poll_answer_id)
#             poll_answer.vote_count+=1
#             poll_answer.save()
#         else:
#             form = PollFormNew()
#     data["form"]=form
#
#     return render(request,"radio.html", data)

def sample_form(request):
    data = {}
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"]
            )
            data["message"] = "Answer saved."
    else:
        form = SignupForm()

    data["form"] = form

    return render(request,"sampleform.html", data)

def login_form(request):
    print "authenticate"
    data = {}
    if request.method == "POST":
        form = Authenticate(request.POST)
        if form.is_valid():
            print "form is valid"
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print username, password
            user = authenticate(username=username, password=password)
            print user
            if user is not None:
                return HttpResponseRedirect('/add-poll')
            else:
                return HttpResponseRedirect('/add-poll-answer')
    else:
        form = Authenticate()

    data["form"] = form

    return render(request,"loginform.html", data)

# def my_form_view(request):
#     data = {}
#     render(request, "my_form.html", data)