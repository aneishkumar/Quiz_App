from django.contrib import admin
from .models import Questions, UserQuestions


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('Content','Set', 'Number', 'Option_1', 'Option_2', 'Option_3', 'Option_4', 'Option_1_Correct', 'Option_2_Correct',
                    'Option_3_Correct', 'Option_4_Correct')


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(UserQuestions)

# Register your models here.
