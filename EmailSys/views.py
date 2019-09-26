from django.shortcuts import render
import sys
from subprocess import call
from subprocess import PIPE

def button(request):
    return render(request,'UI.html')

def output(request):
    call("python C:\\Users\\sachin.thorat\\PycharmProjects\\PartnerPerformanceEmailSystem\\PartnerPerformanceEmailSystem.py",shell=False, stdout=PIPE)
    data1="Successful!"
    print(data1)
    return render(request,'UI.html',{'data1',data1})