from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Online(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name


class ChatGroup(models.Model):
    name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

    @property
    def link(self):
        channel_name = self.channel_name(self.id)
        return f'/ws/chat/{channel_name}/'

    @staticmethod
    def channel_name(group_id):
        return f'group_{group_id}'


class GroupParticipant(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='group_user', on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(ChatGroup, related_name='group_participant', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class ChatMessage(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='user_message', on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(ChatGroup, related_name='group_message', on_delete=models.CASCADE, null=True)
    message = models.TextField(default='')

    def __str__(self):
        return self.message
