from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Client,Survey, Section, Question, SurveyQuestion, Answer




class ClientSerializer(serializers.ModelSerializer):

    
    
    def get_serializer_context(self):
        return self.context['request'].data

    def create(self, validated_data):
        """                                                                                                                                                                     
        Create and return a new `statement` instance, given the validated data.                                                                                                      
        """
        return Client.objects.create(**validated_data)

    class Meta:
        model = Client
        fields = ("clientID", "clientName","joinDate", "streamSize", "projectStatus","description","officialEmail", "lastModified")




class SurveySerializer(serializers.ModelSerializer):
    clients = serializers.CharField(source='client.clientName', read_only=False)
    #statements = serializers.ReadOnlyField(source='statement.ID', read_only=True)
        
    def get_serializer_context(self):
        return self.context['request'].data


    def create(self, validated_data):
        """                                                                          
        Create and return a new `Survey` instance, given the validated data.        
        
        """        

        st = Client.objects.get(clientName = validated_data.pop("client")["clientName"])
        instance = Survey.objects.create (**validated_data, client = st)
        instance.save()
                
        return instance

    
    class Meta:
        model = Survey
        fields = ('surveyID', 'surveyName', 'clients','surveyDescription')

        
class SectionSerializer(serializers.ModelSerializer):
  #  sectioner = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title_initialValue')
   # statements = serializers.CharField(source='statement.ID', read_only=False)
    #statements = serializers.ReadOnlyField(source='statement.ID', read_only=True)
    
    def get_serializer_context(self):
        return self.context['request'].data

    def create(self, validated_data):
        """                                                                                                                                                                           
        Create and return a new `section` instance, given the validated data.                                                                                                      
        """
        return Section.objects.create(**validated_data)

    class Meta:
        model = Section
        fields = ('sectionID', 'sectionName', 'sectionDescription', 'survey')



        


        


        
class AnswerSerializer(serializers.ModelSerializer):
    #statements = serializers.ReadOnlyField(source='statement.ID', read_only=True)
    surveyQuestionsID = serializers.CharField(source='questionSurvey.surveyQuestionID', read_only=False)
    survey = serializers.CharField(source='questionSurvey.survey', read_only=False)
    question = serializers.CharField(source='questionSurvey.question', read_only=False)
    authors = serializers.CharField(source='author.username', read_only=False)    

    def get_serializer_context(self):
        return self.context['request'].data



    def create(self, validated_data):
        """                                                                                                 Create and return a new `PreOperatingCosts` instance, given the validated data.                     """        
        #st = authors.objects.get(ID= validated_data.pop("statement")["ID"])
        pd = SurveyQuestion.objects.get(ID= validated_data.pop("questionSurvey")["surveyQuestionID"])
        instance = Answer.objects.create (**validated_data, author = authors, questionSurvey = pd)
        instance.save()
                
        return instance

    class Meta:
        model = Answer
        fields = ('answerID', 'survey','question', 'authors','answerMain','answerAdditional','answerType', 'surveyQuestionsID')



        
class QuestionSerializer(serializers.ModelSerializer):
    sections = serializers.CharField(source='section.sectionID', read_only=False)
    #statements = serializers.ReadOnlyField(source='statement.ID', read_only=False)
    #productVariableItems = serializers.SlugRelatedField(read_only=True, many=True, slug_field='variableCostName')        
    #productVariableItems = VariableCostItemsSerializer(many=True, required=False)
    
    def get_serializer_context(self):
        return self.context['request'].data

    def create(self, validated_data):
        """                                                                                                 Create and return a new `ProductsCosts` instance, given the validated data.                     """        
        st = Section.objects.get(ID= validated_data.pop("section")["sectionID"])
        instance = Question.objects.create (**validated_data, statement = st)
        instance.save()
                
        return instance

    
    class Meta:
        model = Question
        fields = ['questionID', 'question', 'sections','description','questionSetDate']



        
class SurveyQuestionSerializer(serializers.ModelSerializer):
    #statements = serializers.PrimaryKeyRelatedField(queryset = Statement.objects.all(), source = 'statement.ID', many=False)
    surveys = serializers.CharField(source='survey.surveyName', read_only=False)
    questions = serializers.CharField(source='question.question', read_only=False)
    
    def get_serializer_context(self):
        return self.context['request'].data

    def create(self, validated_data):
        """                                                                                                 Create and return a new `FixedCosts` instance, given the validated data.             

        """        
        st = Survey.objects.get(ID= validated_data.pop("survey")["surveyID"])
        instance = SurveyQuestion.objects.create (**validated_data, survey = st)
        instance.save()
                
        return instance

    class Meta:
        model = SurveyQuestion
        fields = ('surveyQuestionID', 'surveys','questions','surveyQuestionAttribute','rank')


        
        
