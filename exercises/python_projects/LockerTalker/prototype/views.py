from django.http import HttpResponse
from django.shortcuts import render_to_response

def get_espn(request):
    url = '13'
    p = requests.get('http://api.espn.com/v1/sports/football/nfl/teams/'+ url +'/news/?apikey=6pz3x9tcb269689jvg23swm8')
    data = {
        p:p
    }
    return render_to_response(request, 'home.html')

