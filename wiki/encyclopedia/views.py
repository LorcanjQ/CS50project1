from django.shortcuts import render

from . import util

from markdown2 import Markdown

from django import forms

import random




class SearchForm(forms.Form):
    task = forms.CharField(label="Search")

class NewTitleForm(forms.Form):
    title = forms.CharField()

class NewEntryForm(forms.Form):
    entry = forms.CharField(
    widget=forms.Textarea(attrs={"rows":2, "cols":100}))

class EditEntry(forms.Form):
    editable = forms.CharField(widget=
    forms.Textarea(attrs={'rows':2, 'cols':100}))




def search(request):
    search_lst = []
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task"]

            if util.get_entry(task) is not None:
                #if search item is name of page
                return entry(request, task)
            else:
                #if search item not name of page
                for encyc in util.list_entries():
                    if task in encyc:
                        #checks if search item is substring of page
                        search_lst.append(encyc) #appends page to search list

                if not search_lst: #if search list empty
                    return entry(request, task)

                else:# if not empty, list is posted as search results
                    return render(request, "encyclopedia/index.html", {
                        "title" : "Search Results",
                        "entries": search_lst,
                        "search_form": SearchForm()
                        })
        else:
            return index(request)
    else:
        return index(request)



def index(request):
    return render(request, "encyclopedia/index.html", {
        "title": "All Pages",
        "entries": util.list_entries(),
        "search_form": SearchForm()
    })


def entry(request, def_input):
    try:
        def_entry = util.get_entry(def_input)
        md = Markdown()
        return render(request, "encyclopedia/entries.html", {
        "md_content": md.convert(def_entry),
        "def_input":def_input.capitalize(),
        "search_form": SearchForm()
        })
    except TypeError:
        return render(request, "encyclopedia/error.html", {
        "name":def_input,
        "search_form": SearchForm()
        })



def new(request):

    if request.method == "POST":
        form_title = NewTitleForm(request.POST)
        form_entry = NewEntryForm(request.POST)

        if form_title.is_valid() and form_entry.is_valid():
            Title = form_title.cleaned_data["title"]
            Entry = form_entry.cleaned_data["entry"]
            if Title not in util.list_entries():
                util.save_entry(Title,Entry)
                return entry(request,Title)
            else:
                return render(request, "encyclopedia/error_page_exists.html", {
                "entry_name":Title,
                "search_form": SearchForm()
                })
    else:
        return render(request, "encyclopedia/new_page.html", {
        "title_form":NewTitleForm(),
        "entry_form": NewEntryForm(),
        "search_form": SearchForm()
        })

def edit(request,def_input):

    initial_data = {
    "editable" : util.get_entry(def_input)
    }
    if request.method == "POST":
        edited_entry = EditEntry(request.POST)
        if edited_entry.is_valid():
            editable = edited_entry.cleaned_data["editable"]
            util.save_entry(def_input,editable)
            return entry(request,def_input)
    else:

        return render(request, "encyclopedia/edit.html", {
        "Title":def_input,
        "editable":EditEntry(initial = initial_data),
        "search_form": SearchForm()
    })



def randomiser(request):
    list1 = util.list_entries()
    return entry(request,random.choice(list1))
