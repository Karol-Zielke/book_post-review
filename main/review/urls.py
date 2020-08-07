from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('',views.review_list, name='review_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:review>/', views.single_review, name='single_review'),
]