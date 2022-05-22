from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'home.html')


def room(request, room):

    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'room': room,
        'room_details': room_details,
    })

def checkview(request):
    room = request.POST['room_name']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room)

def send(request):
    message = request.POST['message']

    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, room=room_id)
    new_message.save()

def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
