from django.db import models
from django.conf import settings
#from .validators import validate_file_extension

# Create your models here.



class Client(models.Model):

    PROJECT_TYPE = [
        (0, 'BDDING STAGE'),
        (2, 'FOLLOW-UP'),
        (3, 'WAITING FOR ANSWER'),
        (4, 'CLOSED'),
        (5, 'COMPLETED'),
        (6, 'WON'),
        
    ]
    
    clientID = models.AutoField(primary_key=True)
    clientName = models.CharField(max_length= 200)
    joinDate = models.DateTimeField('Join Date')
    streamSize = models.IntegerField(default=1)
    projectStatus = models.IntegerField(choices=PROJECT_TYPE, default=0)
    description = models.TextField()
    officialEmail=  models.EmailField()
    lastModified = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.clientName



class Survey(models.Model):
    surveyID = models.AutoField(primary_key=True)
    surveyName = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    surveyDescription = models.TextField()
    surveySetDate = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return "<" + str(self.client)+ ">"+ self.surveyName

    
class Section(models.Model):
    sectionID = models.AutoField(primary_key=True)
    sectionName = models.CharField(max_length=200)
    sectionDescription = models.TextField()
    #survey = models.CharField(max_length=255)
    survey =  models.CharField(max_length=200)
    sectionSetDate = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.sectionName

# class SubSection(models.Model):
#     subSectionID = models.AutoField(primary_key=True)
#     subSectionName = models.CharField(max_length=200)
#     #section =models.CharField(max_length=255)
#     #section = models.ForeignKey(Section, on_delete=models.CASCADE) 
#     subSectionDescription = models.TextField()
#     subSectionSetDate = models.DateTimeField(auto_now_add =True)

#     def __str__(self):
#         return self.subSectionName

    
class Question( models.Model):
    questionID = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)
    description = models.TextField()
   # subSection = models.CharField(max_length=255)
    #subSection = models.ForeignKey(SubSection, on_delete=models.CASCADE, default ="Valet Parking") 
    section = models.ForeignKey(Section, on_delete=models.CASCADE) 
    survey =  models.ManyToManyField(Survey, through='SurveyQuestion')
    questionSetDate = models.DateTimeField(auto_now_add =True)
    
    class Meta:
        unique_together = ["question", "section"]

    def __str__(self):
        return "[" + str(self.section) + "] " + self.question


class SurveyQuestion( models.Model):
    surveyQuestionID = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    surveyQuestionAttribute = models.CharField(max_length=255)
    rank = models.DecimalField(decimal_places=2, max_digits=20, default="100.00")

#    class Meta:
#       unique_together = ["survey", "question"]
    
    
    def __str__(self):
        return  "<" + str(self.survey) + "> " + str(self.question) + " " + " (" + str(self.question.description) + ")"

    def getSurveyQuestion(self):
        return self.survey + self.question


class Answer( models.Model):
    answerID = models.AutoField(primary_key=True)
    answerMain = models.CharField(max_length=255, default= "YES")
    answerAdditional = models.CharField(max_length=255)
    questionSurvey = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    answerType = models.CharField(max_length=255)
    answerSetDate = models.DateTimeField(auto_now_add =True)

    class Meta:
        unique_together = ["questionSurvey", "author"]
    
    def __str__(self):
        return self.answerMain

