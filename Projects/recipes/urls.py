from django.urls import path
from recipes.views import index, rice


urlpatterns = [
    path('', index), 
    path('prepare-rice/', rice )
]
