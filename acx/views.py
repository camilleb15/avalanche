from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Sum, F, Count, Max, Min, Avg
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from django.core import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import SectionSerializer, QuestionSerializer, SurveyQuestionSerializer, AnswerSerializer, SurveySerializer, ClientSerializer
from django.contrib.auth.decorators import login_required
from requests import Request, Session
from .models import Client,Survey, Section, Question, SurveyQuestion, Answer
from pandas.io.html import read_html
from repo.models import WebPages, SectionsData, ModelStillMedia, CoinsPortfolio,CoinsQuotes
from .models import Question, Survey, Section, SurveyQuestion, Answer 









class ClientViewSet(viewsets.ModelViewSet):
    """                                                                                              
    API endpoint that allows main tatement to be viewed or edited.

    """

    def retrieve( self, request, *args, **kwargs):
        params= kwargs
        st = Client.objects.filter(statement = params['pk'])
        serializer = ClientSerializer(st, many = True)
        return Response(serializer.data)
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer




class SurveyViewSet(viewsets.ModelViewSet):
    """                                                                                              
    API endpoint that allows section of financial statement to be viewed or edited.
    """

    def retrieve( self, request, *args, **kwargs):
        params= kwargs
        survey = Survey.objects.filter(client = params['pk'])
        serializer = SurveySerializer(preOpsAssets, many = True)
        return Response(serializer.data)
    
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SectionViewSet(viewsets.ModelViewSet):
    """                                                                                              
    API endpoint that allows section of financial statement to be viewed or edited.

    """

    def retrieve( self, request, *args, **kwargs):
        params= kwargs
        sections = Section.objects.filter(sectionID = params['pk'])
        serializer = SectionSerializer(sections, many = True)
        return Response(serializer.data)
    
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """                                                                                              
    API endpoint that allows section of financial statement to be viewed or edited.

    """

    def retrieve( self, request, *args, **kwargs):
        params= kwargs
        questions = Question.objects.filter(survey = params['pk'])
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)
    
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyQuestionViewSet(viewsets.ModelViewSet):
    """                                                                                              
    API endpoint that allows section of financial statement to be viewed or edited.

    """

    def retrieve( self, request, *args, **kwargs):
        params= kwargs
        SurveyQ = SurveyQuestion.objects.filter(survey = params['pk']).order_by('-ID')
        serializer = SurveyQuestionSerializer(surveyQ, many = True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        params= kwargs

        instance = get_object_or_404(SurveyQuestion, surveyQuestionID = params['pk'])
        instance.delete()
        
        return Response(data="deleted")

    
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer


    
class AnswerViewSet(viewsets.ModelViewSet):
    """                                                                                             
    API endpoint that allows section of financial statement to be viewed or edited.

    """


    
    def retrieve( self, request, *args, **kwargs):
        params= kwargs
        answer = Answer.objects.filter(author = params['pk'])
        serializer = AnswerSerializer(answers, many = True)
        return Response(serializer.data)

    #querySet= Answer.objects.values('answerMain').order_by().annotate(Count('answerMain'))
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer





    
class AnswerStructViewSet(viewsets.ModelViewSet):
    """                                                                                             
    API endpoint that allows section of financial statement to be viewed or edited.

    """

    def get_queryset(self):
        hoursE=10
        daysE=0
        surveyS= self.request.GET.get('survey')
        authorsS = self.request.GET.get('authors')
      
        startDate = datetime.today()
        startDate_minus5 = startDate - timedelta(days = daysE, hours = hoursE)

        #return Answer.objects.filter(questionSurvey__survey__surveyName = surveyS).annotate(totalAuthors = Count('author'))#.annotate(low = Min('coinPrice')).order_by('coinQuotesSnapDate__date')
        # return CoinsQuotes.objects.filter(coinID__coinSymbol = coinS, coinQuotesSnapDate__gte = startDate_minus5).order_by('coinQuoteLastUpdated')
        
        return Answer.objects.filter(questionSurvey__survey__surveyID = surveyS).order_by('author')


    
    def retrieve( self, request, *args, **kwargs):
        params= kwargs
        answer = Answer.objects.filter(author = params['pk'])
        serializer = AnswerSerializer(answers, many = True)
        return Response(serializer.data)

    #querySet= Answer.objects.values('answerMain').order_by().annotate(Count('answerMain'))
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer



    



def index(request):
    #Part1 : Set Schedule
    return HttpResponse("<h1>ACX portal with multimedia info </h1>")




def graphAcx(request):
    server = "192.168.128.48"
    ref =  request.META.get("refresh")
    ref2 =  request.META.get("statement")
    if 'sort' in request.GET:
        sortVal = "-" + request.GET.get('sort', 'coinBookDate')
    else:
        sortVal = 'coinName'

    if 'refresh' in request.GET:
        url = "https://"+ server+"/acx/answerStruct"
        parameters = {
            
        }
        headers = {
            'Accepts': 'application/json',
            
        }
        session = Session()
        session.headers.update(headers)
        try:
            refResponse = session.get(url, params=parameters)
            refData1 = json.loads(refResponse.text)
            refData2 =  pd.json_normalize(refData1, errors='ignore')

            
            
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print("total loss")
            print(e)

    else:
        print("No refresh")
        refData = "FALSE"

    staticRoot = settings.STATIC_ROOT
    currentDB= settings.DATABASES
    statement = Client.objects.filter(clientID = 2)
    webpage = WebPages.objects.get(question_text = 'Graph')
    myWebPage = WebPages.objects.all()
    sectionsdata = SectionsData.objects.filter(PageReference= webpage)
    modelstill = ModelStillMedia.objects.filter(pageref = webpage)

    #coin = request.GET.get('coinid')
    #articlelink = Articles.objects.filter(ratVal__gte = 3)

    
    # portfolio = CoinsPortfolio.objects.all().order_by(sortVal).annotate(myMv = F('coinMarketPrice')*F('coinAmount')).annotate(myPnl = (F('coinMarketPrice')-F('coinBookPrice'))*F('coinAmount')).annotate(totalMv = Count('myPnl'))
    # totalMv = (CoinsPortfolio.objects.all().aggregate(totalMv = Sum(F('coinMarketPrice') * F('coinAmount')))['totalMv'])
    # totalPnl = (CoinsPortfolio.objects.all().aggregate(totalPnl = Sum( F('coinAmount')* (F('coinMarketPrice') - F('coinBookPrice'))))['totalPnl'])
    # max_date = CoinsPortfolio.objects.all().aggregate(max_date = Max('coinQuoteLastUpdated'))['max_date']
    totalPoints = (Answer.objects.all().aggregate(totalPoints = Sum(F('answerMain')))['totalPoints'])
    totalYes = (Answer.objects.filter(answerMain ="YES").aggregate(totalYes = Count(F('answerMain')))['totalYes'])
    totalNo = (Answer.objects.filter(answerMain="NO").aggregate(totalNo = Count(F('answerMain')))['totalNo'])

    statsPerAuthor = Answer.objects.values('author',"answerType").order_by('author').annotate(AvgPoints=Avg(F('answerMain'))).annotate(totalPoints=Sum(F('answerMain'))).annotate(totalYes=Count(F('answerMain'))).annotate(totalNo = Count(F('answerMain')))
    

     # totalPnlperCoin = CoinsPortfolio.objects.values('coinID','coinName').order_by('coinName').annotate(bookPrice=Avg(F('coinBookPrice'))).annotate(marketPrice=F('coinMarketPrice')).annotate(totalAmount=Sum(F('coinAmount'))).annotate(totalNotional=Sum(F('coinUSDNotional'))).annotate(totalPnl = Sum( F('coinAmount')* (F('coinMarketPrice') - F('coinBookPrice')))).annotate(totalMv = Sum(F('coinMarketPrice') * F('coinAmount')))

    # latest_date = CoinsQuotes.objects.aggregate(latest1 = Max('coinQuotesSnapDate'))['latest1']
    # pct_chg = CoinsQuotes.objects.filter(coinQuotesSnapDate__gte = (latest_date - timedelta(seconds=5)))    
    # portfolio2= CoinsPortfolio.objects.select_related('coinID')
    # quotes = CoinsQuotes.objects.filter (coinID = coin)
            
    #defining tensorFlow code 

    #context = {'object' : statement, 'links': myWebPage, 'modelstills': modelstill, 'portfolio' : portfolio, 'portfolio2': portfolio2 , 'quotes' :  quotes , 'totalMv': totalMv, 'totalPnl': totalPnl, 'max_date': max_date , 'totalBv': totalBv ,  'pct_chg': pct_chg , 'latest_date': latest_date , 'totalPnlperCoin': totalPnlperCoin, 'refData': refData, 'articlelinks' : articlelink }
    context = {'object' :  sectionsdata ,'links': myWebPage, 'modelstills': modelstill, 'ref2':ref2, 'Project':statement,'statsPerAuthor': statsPerAuthor ,'totalPoints': totalPoints, 'totalYes': totalYes,'totalNo': totalNo ,'staticRoot':staticRoot , 'currentDB':currentDB }
    return render(request, 'graphAcx.html', context)







@api_view(('GET',))
def renderAnswer(request):

    if request.method == 'GET':
        statement = request.GET.get('client',None)
    else:
        statement = request.GET.get('client',None)
    
    

    project = 4


    urlSection = "http://192.168.128.48/Pservlet/acx/surveyQestion/"+ str(project)
    urlPreOpsAssets = "http://192.168.128.48/Pservlet/acx/section/"+ str(project)


    
    parameters = {
        'symbol': 'BTC,ETH',
        #  'start':'1',
        #  'limit':'5000',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'c402bfd2-9b0f-4d97-940b-4a84e6a73144',
    }

    symbols = 'BTC,ETH,DOGE',
    session = Session()
    
    #session.headers.update(headers)
    #response = session.get(url, params=parameters)
    responseSections = session.get(urlSection)
    responseAssets = session.get(urlPreOpsAssets)

    
 

#    dataIRR = json.loads(cFlowV2.getIRRFlows().to_json())
#    dataLS = json.loads(stmV2WithLoan1.getLoanSchedule().to_json())
#    dataWC = json.loads(wCapitalV2.getWorkingCapitalSchedule().to_json())
#    dataDep= json.loads(preOpsV2.getDepreciationSchedule().to_json())
#    dataFlow = json.loads(cFlowV2.getCashFlowStatement().to_json())
#    data = json.loads(stmV2.getStatement().loc[:,~stmV2.getStatement().columns.str.contains('PctChg')].to_json())

    statsPerAuthor = Answer.objects.values('author',"answerType").order_by('author').annotate(AvgPoints=Avg(F('answerMain'))).annotate(totalPoints=Sum(F('answerMain'))).annotate(totalYes=Count(F('answerMain'))).annotate(totalNo = Count(F('answerMain'))).values()

    qsJson =  serializers.serialize('json', statsPerAuthor, fields=('structure',))


    
    if statement == "IS":
        dataOut = qsJson
        return Response(dataOut)
    elif statement == "CF" :
        dataOut = dataFlow
        return Response(dataOut)
    elif statement == "WC" :
        dataOut = dataWC
        return Response(dataOut)
    elif statement == "DEP" :
        dataOut = dataDep
        return Response(dataOut)
    elif statement == "LS" :
        dataOut = dataLS
        return Response(dataOut)
    elif statement == "IRR" :
        dataOut = dataIRR
        return Response(dataOut)






def portal(request):
    ref =  request.META.get("refresh")
    if 'sort' in request.GET:
        sortVal = "-" + request.GET.get('sort', 'coinBookDate')
    else:
        sortVal = 'coinName'
    if 'refresh' in request.GET:
        url = 'https://www.avalancheconsultancy.com/repo/coinData/'
        parameters = {
            
        }
        headers = {
            'Accepts': 'application/json',
            
        }
        session = Session()
        session.headers.update(headers)
        try:
            refResponse = session.get(url, params=parameters)
            refData1 = json.loads(refResponse.text)
            refData2 =  pd.json_normalize(refData1, errors='ignore')

            refData = refData2[['snapTime']]
            
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print("total loss")
            print(e)

    else:
        print("No refresh")
        refData = "FALSE"

    
    webpage = WebPages.objects.get(question_text = 'Graph')
    myWebPage = WebPages.objects.all()
    sectionsdata = SectionsData.objects.filter(PageReference= webpage)
    modelstill = ModelStillMedia.objects.filter(pageref = webpage)
    coin = request.GET.get('coinid')
    portfolio = CoinsPortfolio.objects.all().order_by(sortVal).annotate(myMv = F('coinMarketPrice')*F('coinAmount')).annotate(myPnl = (F('coinMarketPrice')-F('coinBookPrice'))*F('coinAmount')).annotate(totalMv = Count('myPnl'))
    totalMv = (CoinsPortfolio.objects.all().aggregate(totalMv = Sum(F('coinMarketPrice') * F('coinAmount')))['totalMv'])
    totalPnl = (CoinsPortfolio.objects.all().aggregate(totalPnl = Sum( F('coinAmount')* (F('coinMarketPrice') - F('coinBookPrice'))))['totalPnl'])
    max_date = CoinsPortfolio.objects.all().aggregate(max_date = Max('coinQuoteLastUpdated'))['max_date']
    totalBv = (CoinsPortfolio.objects.all().aggregate(totalBv = Sum(F('coinUSDNotional')))['totalBv'])

    survey = Survey.objects.all()
    surveyQuestion = SurveyQuestion.objects.all()
    question = Question.objects.all()
    answer = Answer.objects.all()
    
    totalPnlperCoin = CoinsPortfolio.objects.values('coinID','coinName').order_by('coinName').annotate(bookPrice=Avg(F('coinBookPrice'))).annotate(marketPrice=F('coinMarketPrice')).annotate(totalAmount=Sum(F('coinAmount'))).annotate(totalNotional=Sum(F('coinUSDNotional'))).annotate(totalPnl = Sum( F('coinAmount')* (F('coinMarketPrice') - F('coinBookPrice')))).annotate(totalMv = Sum(F('coinMarketPrice') * F('coinAmount')))

    latest_date = CoinsQuotes.objects.aggregate(latest1 = Max('coinQuotesSnapDate'))['latest1']
    pct_chg = CoinsQuotes.objects.filter(coinQuotesSnapDate__gte = (latest_date - timedelta(seconds=5)))
    #pct_chg = CoinsQuotes.objects.filter(coinQuotesSnapDate__gte = latest_date)
    
    portfolio2= CoinsPortfolio.objects.select_related('coinID')
    quotes = CoinsQuotes.objects.filter (coinID = coin)
            
    #defining tensorFlow code 

    context = {'object' : sectionsdata, 'links': myWebPage, 'modelstills': modelstill, 'portfolio' : portfolio, 'portfolio2': portfolio2 , 'quotes' :  quotes , 'totalMv': totalMv, 'totalPnl': totalPnl, 'max_date': max_date , 'totalBv': totalBv ,  'pct_chg': pct_chg , 'latest_date': latest_date , 'totalPnlperCoin': totalPnlperCoin, 'refData': refData , 'survey':survey, 'surveyQuestion': surveyQuestion, 'question': question, 'answer':answer}
    return render(request, 'acxPortal.html', context)

