#to reference a url we need to add a path function
from django.urls import path
from . import views


#in this list we map various urls to its view funcs
#/products
#products/new
#products/new/trending
urlpatterns = [
    path('', views.index),#represents the root of this app.Note that it's not calling it, it's referencing it
    #bc djanga will take care of calling it at run time when the client sends http request to the server
    path('new', views.new)
]