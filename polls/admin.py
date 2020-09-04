from django.contrib import admin
from polls.models import Question, Choice


# UI 순서 바꾸기
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# 필드 분리해서 보여주기
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Question Statement', {'fields': ['question_text']}),
#         # ('Date Information', {'fields': ['pub_date']}), ]
#         ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), # 접어서 보여주기
#     ]


# Question & Choice를 한 화면에서 변경하기
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):  # 테이블 형식으로 보여주기
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')  # 레코드 리스트 칼럼 항목 지정하기
    list_filter = ['pub_date']  # 필터 사이드 바 추가
    search_fields = ['question_text']  # 검색 박스 추가


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
