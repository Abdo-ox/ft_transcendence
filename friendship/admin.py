from django.contrib import admin
from friend.models import FriendList, FriendRequest

class FreindListAdmin(amin.ModleAdmin):
    list_filster = ['user']
    list_display = ['user']
    search_fields = ['user']
    readonly_fields = ['user']

    class Meta:
        model = friendlist


