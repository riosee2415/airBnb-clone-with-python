from django.db import models
from core import models as core_models
from users import models as user_models


class Conversation(core_models.TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField(user_models.User, blank=True)

    class Meta:
        verbose_name_plural = "대화창 관리"

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):
    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "매세지 관리"

    def __str__(self):
        return f"{self.user} says : {self.message}"
