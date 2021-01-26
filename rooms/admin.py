from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("name", "descriptions", "contury", "address", "price"),
            },
        ),
        (
            "Times",
            {
                "fields": ("check_in", "check_out", "instant_book"),
            },
        ),
        (
            "More About The Space",
            {
                "classes": ("collapse",),  # Hide OR View
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        (
            "Spaces",
            {
                "fields": ("guests", "beds", "bedrooms", "baths"),
            },
        ),
        (
            "Last Detail",
            {
                "fields": ("host",),
            },
        ),
    )

    list_display = (
        "name",
        "contury",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "contury",
    )

    search_fields = (
        "city",
        "host__username",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):

        return obj.amenities.count()

    count_amenities.short_description = "Amenities Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ PhotoAdmin Admin Definition """

    pass
