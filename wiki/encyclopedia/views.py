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
    md_file = util.get_entry(name) #this is setting md_file to the
                                    #of the markdown file itself
                                    #Need to save this string as a file instead
    markdown.markdownFromFile(input=md_file,
        output='encyclopedia/converted.html',
        encoding='utf8')
    return render(request, "encyclopedia/converted.html" )
