from rest_framework import serializers
from videocontent.models import VideoModel
from accounts.serializers import MentorRegisterSerializer
from accounts.models import Mentor


class VideoModelSerializer(serializers.ModelSerializer):
    mentor = serializers.SlugRelatedField(
        many=True, slug_field='username', queryset=Mentor.objects.all())
    #     mentoruser = MentorRegisterSerializer(many=True, read_only=True)

    #     # def get_creators(self, members):
    #     #     members_name = []
    #     #     for mem in members:
    #     #         # member_instance, created = Mentor.objects.get_or_create(
    #     #         #     pk=mem.get('pk'), defaults=mem)
    #     #         member_instance = Mentor.objects.get(email=mem)
    #     #         members_name.append(member_instance)
    #     #     return members_name

    # def add_creator(self, validated_data):
    # creator = validated_data.pop('mentoruser', [])
    # video = VideoModel.objects.create(**validated_data)
    # # video.creators.set(self.get_creators(creator))
    # for key in creator:
    #     Mentor.objects.create(videomodel_id=video.id, **key)
    # return video

    class Meta:
        model = VideoModel
        fields = ['title', 'description' ,'mentor']
