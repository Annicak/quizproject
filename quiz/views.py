from django.shortcuts import render
def startpage(request):
	return render(request,"quiz/startsida.html")
def quiz(request):
	return render(request,"quiz/quizsida.html")
def question(request):
	return render(request,"quiz/question.html")
def completed(request):
	return render(request,"quiz/resultat.html")



# Create your views here.
