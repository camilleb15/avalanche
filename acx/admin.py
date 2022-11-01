from django.contrib import admin
from .models import Client,Survey,Question,Section, SurveyQuestion,  Answer

# Register your models here.




class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientID','clientName','joinDate','streamSize', 'description','projectStatus','officialEmail', 'lastModified') 
    list_filter = ('clientName','joinDate','projectStatus') 
admin.site.register(Client,ClientAdmin)


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('surveyID','surveyName','client', 'surveyDescription', 'surveySetDate') 
    list_filter = ('surveyName','surveyDescription') 
admin.site.register(Survey,SurveyAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('questionID','question','section', 'description' , 'questionSetDate') 
    list_filter = ('question','survey') 
admin.site.register(Question,QuestionAdmin)

class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('surveyQuestionID','survey', 'question', 'surveyQuestionAttribute', 'rank') 
    list_filter = ('survey','question') 
admin.site.register(SurveyQuestion,SurveyQuestionAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('sectionID','sectionName', 'survey','sectionDescription','sectionSetDate') 
    list_filter = ('sectionName', 'sectionDescription' ) 
admin.site.register(Section,SectionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answerID', 'questionSurvey', 'answerMain','answerAdditional', 'author','answerType', 'answerSetDate') 
    list_filter = ('answerMain','questionSurvey','author', 'answerType') 
admin.site.register(Answer,AnswerAdmin)

