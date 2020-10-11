from django.shortcuts import render

from . import util

import markdown


#markdown.markdownFromFile( #converts a markdown input file into html
#    input='input.md',
#    output='output.html',
#    encoding='utf8',
#)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    md_file = util.get_entry(f"entries/{name}.md")
    markdown.markdownFromFile(input=md_file,
        output='encyclopedia/templates/encyclopedia/converted.html',
        encoding='utf8')
    return render(request, "encyclopedia/converted.html" )
