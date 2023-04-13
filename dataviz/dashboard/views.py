from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import *
from dashboard.serializers import DataSerializer
#from rest_framework import generics
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.
def dashboard(request):
      data = Data.objects.all()
      
      context = {
            'data': data
      }
      return render(request, 'Home.html', context)

def chart_data(request):
       data = Data.objects.all()
       labels = []
       intensity_data = {}
       

       for item in data:
              if item.intensity not in labels:
                     labels.append(item.intensity)
                     intensity_data[item.intensity] = 1
              else:
                     intensity_data[item.intensity] += 1

       chart_data = {
              'labels': labels,
              'intensity': intensity_data,
       }
       
       return JsonResponse(chart_data)

def intensity_data(request):
       data = Data.objects.all()
       label_x = []
       label_y = {}

       for item in data: 
              if item.country is not '':
                     if(item.country not in label_x):
                            label_x.append(item.country)
                            label_y[item.country] = 1
                            
                     else:
                            label_y[item.country] += 1

       chart_data = {
              'labelsx' : label_x.sort(),
              'labelsy' : label_y
       }
       
       return JsonResponse(chart_data)
                     
                     
def pub_data(request):
       data = Data.objects.all().order_by('published')
       label_x = []
       label_y = {}

       for item in data: 
              if item.published is not None:
                     if(item.published.strftime('%Y-%m') not in label_x):
                            label_x.append(item.published.strftime('%Y-%m') )
                            label_y[item.published.strftime('%Y-%m')] = 1
                     else:
                            
                            label_y[item.published.strftime('%Y-%m')] += 1


       chart_data = {
              'labelsx' : label_x,
              'labelsy' : label_y
       }
       
       return JsonResponse(chart_data)

def year_topics(request):
       data = Data.objects.all()
       dx = []
       dy = {}
       

       for item in data: 
              if item.topic != '':
                     if item.topic not in dx:
                            dx.append(item.topic)
                            dy[item.topic] = 1
                     else: 
                            dy[item.topic] += 1


       chart_data = {
              'dx' : dx,
              'dy' : dy,    
       }
       
       return JsonResponse(chart_data)


def published_yr_data(request):
       data = Data.objects.all()
       dx = []
       dy = {}
       dyd = []
       COLORS = []

       for i in data: 
              if i.published is not None:
                     item =  int(i.published.strftime('%Y'))
                     if item not in dx:
                            dx.append(item)
                            dy[item] = 1;
                     else:
                            dy[item] += 1
       dx.sort()
       l = len(dx)
       x = int(255/l)
       r = 0
       for i in dx:
              dyd.append(dy[i])
              r = r + x
              g = (255 - 255%(x))/2
              b = 255 - r
              color = f'rgb({r}, {g}, {b})'
              COLORS.append(color)
       
              



       chart_data = {
              'dx': dx,
              'dy': dyd,
              'COLORS': COLORS
       }
       
       return JsonResponse(chart_data)
      
def published_month_data(request):
       data = Data.objects.all()
       dx = []
       dy = {}
       dyd = []
       COLORS = []

       for i in data: 
              if i.published is not None:
                     item =  int(i.published.strftime('%m'))
                     if item not in dx:
                            dx.append(item)
                            dy[item] = 1;
                     else:
                            dy[item] += 1
       dx.sort()
       l = len(dx)
       x = int(255/l)
       r = 0
       for i in dx:
              dyd.append(dy[i])
              r = r + x
              g = (255 - 255%(x))/2
              b = 255 - r
              color = f'rgb({r}, {g}, {b})'
              COLORS.append(color)
       
              



       chart_data = {
              'dy': dyd,
              'COLORS': COLORS
       }
       
       return JsonResponse(chart_data)

def country_month_data(request):
       data = Data.objects.all()
       COLORS = []
       cd = []
       dp = {}
       d_ = []
       for i in data:
              d = {}
              if i.intensity != '' and i.published is not None:
                     d['x'] = i.published.strftime('%m')
                     d['y'] = i.intensity
                     d['r'] = 1
                     
                     s = d['x'] + d['y']
                     if s not in d_:
                            d_.append(s)
                            dp[s] = 1
                            cd.append(d)
                     else:
                            dp[s] += 1

       newdatalist = []
       for di in cd:
              s = di['x'] + di['y'] 
              di['r'] = dp[s]
              if di not in newdatalist:
                     newdatalist.append(di)

       months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
       chartdata= [[] for i in range(12)]
       for d in newdatalist:
              chartdata[int(d['x'])-1].append(d)
       
       for ls in chartdata:
             for li in ls:
                    li['x'] = li['y']
                    li['y'] = li['r']
                    li['r'] = 5

       
       intensity = [i for i in range(101)]
       r = 110
       for i in range(12):
              j = i + 1
              r = r + j*j
              g = (255 - 255%(j*j))/2
              b = 255 - j*j
              color = f'rgb({r}, {g}, {b})'
              COLORS.append(color)
       data = []
       for i in range(12):
              dobj = {}
              dobj['label'] = months[i]
              dobj['data'] = chartdata[i]
              dobj['bgcolor'] = COLORS[i]
              data.append(dobj)
       
       print(data)
       
       chart_data = {
              'lebels' : intensity,
              'data' : data,
              'COLORS': COLORS

       }
       
       return JsonResponse(chart_data)
       
      

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    search_fields = ['end_year', 'title', 'topic', 'sector','insight', 'region', 'published', 'pestle', 'source', 'country', 'city', 'start_year', 'added']
    filterset_fields = ['end_year', 'title', 'topic', 'sector','insight', 'region', 'published', 'pestle', 'source', 'country', 'city', 'start_year', 'added']

