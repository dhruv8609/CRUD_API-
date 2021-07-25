from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from accounts.models import *
from videocontent.models import VideoModel
from videocontent.serializers import VideoModelSerializer


@api_view(['GET', ])
def get_all_video(request):
    try:
        lists = VideoModel.objects.all()
        lecture_title = []
        for key in lists:
            lecture_title.append(key.title)
        return Response({"lectures": lecture_title})
    except:
        return Response({"response": "query not fulfilled!"})


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_video(request, slug):
    account = request.user
    try:
        video = VideoModel.objects.get(slug=slug)
        if(video.attendees.find(str(account.username)) == -1):
            video.attendees += ("{} ".format(account.username))
            video.save()

    except VideoModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(video.attendees)
    if request.method == "GET":
        serializer = VideoModelSerializer(video)
        return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_video(request, slug):

    user = request.user
    try:
        video = VideoModel.objects.get(slug=slug)
        test_serializer = video.mentor.all()
        mentors = []
        for key in test_serializer:
            mentors.append(key.username)
        if user.username not in mentors:
            return Response({"response": "You are not authorized to make any changes!"})
    except VideoModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # edit_access = VideoModelSerializer(video)
    # if user.username not in edit_access['mentor']:
    #     return Response({"response": "Sorry! you can't edit"})
    if request.method == "PUT":
        serializer = VideoModelSerializer(video, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "data updated"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def delete_video(request, slug):
    user = request.user
    try:
        video = VideoModel.objects.get(slug=slug)
        mentors = []
        for key in video.mentor.all():
            mentors.append(key.username)
        if user.username not in mentors:
            return Response({"response": "You are not authorized to delete!"})
    except VideoModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        curr = video.delete()
        data = {}
        if curr:
            data['success'] = "data deleted"
        else:
            data['error'] = "delete failed"
        return Response(data=data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def create_video(request):

    if request.method == "POST":
        if len(request.data['mentor']) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = VideoModelSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            print("valid data --- creating object ")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_video_views(request, slug):
    try:
        video = VideoModel.objects.get(slug=slug)

    except VideoModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        lists = video.attendees.split(" ")
        lists = lists[1:]
        return Response({"viewed_by": lists})
