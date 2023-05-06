from django.shortcuts import render

# Create your views here.

def view(reqest):
    return render(reqest,'grid.html')

