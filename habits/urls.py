from django.urls import path

from habits import views

urlpatterns = [
    path('create/', views.HabitCreateAPI.as_view(), name='create-habit'),
    path('<int:pk>/', views.HabitView.as_view(), name='habit'),
    path('my-all-habits/', views.HabitListAPIView.as_view(), name='all-habit'),
    path('all-published-habits/', views.NotMyHabitListAPIView.as_view(), name='all-published-habit'),
    path('<int:pk>/update/', views.HabitUpdateAPI.as_view(), name='update-habit'),
    path('<int:pk>/delete/', views.HabitDeleteAPI.as_view(), name='delete-habit'),
]


