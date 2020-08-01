#djnago 'I have created this file - Santosh'
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext= request.POST.get('text','default')

    #Check checkbox values
    remove_punc = request.POST.get('remove_punc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    remove_spaces = request.POST.get('remove_spaces', 'off')
    remove_line = request.POST.get('remove_line', 'off')
    char_count= request.POST.get('char_count', 'off')
    armstrong= request.POST.get('armstrong', 'off')

    #remove punctuation
    if remove_punc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        #Analyzed Text
        return render(request, 'analyze.html', params)

    #Change to uppercase
    elif capitalize== "on":
        analyzed=""
        for char in djtext:
            analyzed= analyzed+ char.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        #Analyzed Text
        return render(request, 'analyze.html', params)

    # New line remover
    elif remove_line=="on":
        analyzed = ""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        # Analyzed Text
        return render(request, 'analyze.html', params)

    # Extra space remover
    elif remove_spaces == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        # Analyzed Text
        return render(request, 'analyze.html', params)

    #To count the character
    elif char_count == 'on':
        count = 0
        for char in djtext:
            if char.isalpha():
                count = count + 1
        params = {'purpose': 'Number of characters in the line ', 'analyzed_text':count}
        return render(request, 'analyze.html',params)
    #If none of the option selected
    else:
        return HttpResponse('<h1>Please select what you want to do.</h1>')
