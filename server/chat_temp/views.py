# chat/views.py
from django.shortcuts import render


def index(request):
    return render(request, "chat_temp/index.html")


def room(request, room_name):
    return render(request, "chat_temp/room.html", {"room_name": room_name})
