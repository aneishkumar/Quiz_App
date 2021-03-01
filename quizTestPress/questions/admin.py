from django.contrib import admin
from .models import Questions, UserQuestions


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('Content','Set', 'Number', 'Option_1', 'Option_2', 'Option_3', 'Option_4', 'Option_1_Correct', 'Option_2_Correct',
                    'Option_3_Correct', 'Option_4_Correct')


class UserQuestionsAdmin(admin.ModelAdmin):
    list_display = ('User_ID','Set_Id', 'Question_1_Status', 'Question_2_Status', 'Question_3_Status', 'Question_4_Status', 'Question_5_Status', 'Question_6_Status', 'Question_7_Status',
                    'Question_8_Status', 'Question_9_Status','Question_10_Status')


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(UserQuestions, UserQuestionsAdmin)

# Register your models here.
