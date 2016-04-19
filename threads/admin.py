from django.contrib import admin
from .models import Subject, Thread, Post
from polls.models import Poll

admin.site.register(Subject)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Poll)