from django.shortcuts import render

def Start(request):
    return render(request,'index.html')
def Question(request):
    return render(request,'questionnaire.html')