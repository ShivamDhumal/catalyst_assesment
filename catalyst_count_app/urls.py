from django.urls import path
from . import views


urlpatterns = [
  path('uploaddata', views.csv_upload , name = "uploaddata"),
  path('Querybuilder/' , views.querybuilder , name = 'querybuilder'),
  path('userdata/' ,views.userdata , name = 'userdata'),
#   path('useradd/', views.useradd , name = 'useradd' ),
#   path('delete/', views.deletedata , name = 'delete' ),

]
    
