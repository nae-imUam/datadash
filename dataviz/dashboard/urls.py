from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from dashboard.views import DataViewSet
from rest_framework.routers import DefaultRouter
'''
data_list = DataViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

data_detail = DataViewSet.as_view({
    'get': 'retrive',
    'put': 'update', 
    'patch': 'partial_update', 
    'delete': 'destroy'
})


urlpatterns = [
    
    path('', views.dashboard, name='dashboard'), 
    path('chart-data/', views.chart_data, name='chart-data'),
    path('intensity-data/', views.intensity_data, name='intensity-data'),
    path('pub-data/', views.pub_data, name='pub-data'),
    #path('api/datas/', views.DataList.as_view()),
    path('api/data/', data_list, name='data-list'),
    #path('api/datas/<int:pk>/', views.DataDetail.as_view()),
    path('data/<int:pk>/', data_detail, name='data-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
'''

router = DefaultRouter()
router.register(r'data', views.DataViewSet, basename='data')

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('chart-data/', views.chart_data, name='chart-data'),
    path('year_topics/', views.year_topics, name='year_topics'),
    path('published_yr_data/', views.published_yr_data, name='published_yr_data'),
    path('published_month_data/', views.published_month_data, name='published_month_data'),
    path('country_month_data/', views.country_month_data, name='country_month_data'),
    path('intensity-data/', views.intensity_data, name='intensity-data'),
    path('pub-data/', views.pub_data, name='pub-data'),
    path('api/', include(router.urls), name='api'),
]