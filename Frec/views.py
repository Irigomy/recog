from django.shortcuts import render
from Frec.frec_logic import *

def dash(request):
	pass

def recog(request):
	return render(request, "index.html")

def attend(request):
	return render(request, "attendance.html")

def student(request):
	return render(request, "student.html")

def sysmon(request):
	pass

def source(request):
	pass

def login(request):
	return render(request, "login.html")
