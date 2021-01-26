from django.db import models
from core import models as core_models
from users import models as user_models
from rooms import models as room_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    content = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanLiness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()

    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room = models.ForeignKey(room_models.Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "리뷰 관리"

    def __str__(self):
        return f"{self.content} - {self.room}"
