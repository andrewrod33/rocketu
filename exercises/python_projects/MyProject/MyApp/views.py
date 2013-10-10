from django.http import HttpResponse
from django.shortcuts import render_to_response

def cards(request):
    deck = []
    for suit in ['H', 'C','O','S']:
        for i in range(1,14):
            deck.append((suit,i))
    print deck
    response = render_to_response('card.html',{'deck':deck})
    return response

# def hello(request,name=''):
#     data = {'player':{
#                 'name': 'Andrew'
#
#         }
#     }
#
#     response = render_to_response('hello.html',data)
#     return response

# def home(request):
#     return HttpResponse("This is my homepage")
#
# def say_hello(request, name="Anonymous"):
#     # return HttpResponse("Hello{}".format(name))
#     data = {"name":name}
#     response = render_to_response('home.html',data)
#     return response
#
# game_score = 0
# def game(request):
#     global game_score
#     data = {'game':game_score}
#     print request.session['fav_color']
#     if request.session.get('game') is not None:
#         return request.session['game']
#     else:
#         request.session["fav_color"] = "blue"
#
#     return HttpResponse("This is my homepage")
#
# count = 0
# def counter(request):
#     global count
#     count +=1
#     data = {'count':count}
#     return render_to_response('counter.html',data)