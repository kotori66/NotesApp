from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeNotes.as_view(), name='index'),
    path('add/', AddNotes.as_view(), name='add'),
    path('about/', About.as_view(), name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<note_slug>/', ViewNote.as_view(), name='view'),
    path('<note_slug>/delete/', DeleteNote.as_view(), name='delete'),
    path('<note_slug>/update/', UpdateNote.as_view(), name='update')
]
