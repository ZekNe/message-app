from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import MsgSerializer
from .models import Msg

def msg_list(request):
    msgs = Msg.objects.all().order_by("-created_at")
    return render(request, "core/msg_list.html", {"msgs": msgs})

class MsgList(APIView):
    def get(self, request):
        msgs = Msg.objects.all().order_by("created_at")
        serializer = MsgSerializer(msgs, many=True)
        return Response(serializer.data)



