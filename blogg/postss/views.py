from django.shortcuts import render
from .models import Report

# Create your views here.
def team_fc(request) :
    rep1s = Report.objects.all()
    return render(request, 'team_fc.html', {'rep1s': rep1s})

def single(request, pk) :
    rep2s = Report.objects.get(id=pk)
    #Query to Retrieve the Post object from the database with the given primary key (pk)
    return render(request, 'single.html', {'rep2s':rep2s})
