from django.urls import path
from algorithms import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bubblesort/', views.bubblesort, name="bubblesort"),
    path('insertionsort/', views.insertionsort, name="insertionsort"),
    path('mergesort/', views.mergesort, name="mergesort"),
    path('quicksort/', views.quicksort, name="quicksort"),
    path('selectionsort/', views.selectionsort, name="selectionsort"),
]