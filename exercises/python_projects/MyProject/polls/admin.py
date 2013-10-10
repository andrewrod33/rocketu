from django.contrib import admin
from polls.models import Poll, PollAnswer, Comment

class PollAnswerAdmin(admin.ModelAdmin):
    readonly_fields = ("vote_count",)

class CommentInLineAdmin(admin.StackedInline):
    model = Comment
    max_num = 1
    extra = 1


class PollAnswerInLineAdmin(admin.StackedInline):
    model = PollAnswer
    max_num = 3
    extra = 3

class PollAdmin(admin.ModelAdmin):
    inlines = [CommentInLineAdmin, PollAnswerInLineAdmin]

admin.site.register(Poll, PollAdmin)
admin.site.register(PollAnswer, PollAnswerAdmin)