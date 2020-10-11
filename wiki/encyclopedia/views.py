from django.shortcuts import render

from . import util

import markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):
    file = open("encyclopedia/templates/encyclopedia/converted.html","w")
    md = markdown.Markdown()
    file.write(md.convert(util.get_entry(name)))
    file.close()

    return render(request, "encyclopedia/converted.html")
