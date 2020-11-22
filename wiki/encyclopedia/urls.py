from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search_func"),
    path("newpage", views.new, name= "new_page"),
    path("randomiser", views.randomiser, name="randomiser"),
    path("<str:def_input>", views.entry, name="def_input"),
    path("<str:def_input>/edit", views.edit, name= "edit"),

    #the search path uses the "  " on the left above as the
    #input parameter for search, not the text input in the searchbox
    #that i want it to
]
