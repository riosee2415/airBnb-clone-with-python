from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Room Model Difinitions """

    class Meta:
        verbose_name_plural = "객실유형 관리"
        ordering = ["name"]


class Amenity(AbstractItem):
    """ Amenity Model Difinitions """

    class Meta:
        verbose_name_plural = "편의시설 관리"


class Facility(AbstractItem):
    """ Facility Model Difinitions """

    class Meta:
        verbose_name_plural = "시설 관리"


class HouseRule(AbstractItem):
    """ HouseRule Model Difinitions """

    class Meta:
        verbose_name_plural = "규칙 관리"


# #################### Main Class ####################
class Room(core_models.TimeStampedModel):

    """ Rooms Model Definition """

    name = models.CharField(max_length=140)
    descriptions = models.TextField()
    contury = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140, default="")

    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()

    check_in = models.TimeField()
    check_out = models.TimeField()

    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)

    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    class Meta:
        verbose_name_plural = "객실 관리"

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "객실 이미지 관리"

    def __str__(self):
        return self.caption
