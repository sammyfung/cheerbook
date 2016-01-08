from django.contrib import admin
from cheerbook.models import CheerBoard


class CheerBoardAdmin(admin.ModelAdmin):
    list_display = ('scraptime', 'posttime', 'poster', 'message')
    list_filter = ['poster']

admin.site.register(CheerBoard, CheerBoardAdmin)
