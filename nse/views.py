from django.shortcuts import render
import pandas as pd
from . nsegraph import livegraph,piegraph,vizgraph
from . models import graphdata
import pandas as pd
def home(request):
    stockdata=pd.read_csv("https://docs.google.com/spreadsheets/d/10Lo29Amnhpb9v0iiT-qmRWPk-vrWhGpNGXcypu2fnoY/export?format=csv")
    bank=stockdata.TICKER
    stock_open=stockdata.OPEN
    stock_high=stockdata.HIGH
    stock_low=stockdata.LOW
    stock_close=stockdata.PREVCLOSE
    stock_change=stockdata.CHANGE
    graph=livegraph(bank,stock_change)
    pie=piegraph(bank,stock_change)
    return render(request,"nse/home.html",{"stock":bank,"stockopen":stock_open,"stockhigh":stock_high,"stocklow":stock_low,"stockclose":stock_close,"stockchange":stock_change,"graph":graph,"piegraph":pie})
def profile(request):
    return render(request,"nse/profile.html")
def livestock(request):
    if(request.method=="POST"):
        stockname=request.POST.get("stockname")
        if(stockname=="InternationalStock"):
            sheetid="2134911051"
        elif(stockname=="IndiaIT"):
            sheetid="1713860492"
        elif(stockname=="IndiaMedia"):
            sheetid="376057235"
        elif(stockname=="german"):
            sheetid="644470221"
        else:
            sheetid="302276032"
        nsesheet="https://docs.google.com/spreadsheets/d/10Lo29Amnhpb9v0iiT-qmRWPk-vrWhGpNGXcypu2fnoY/export?gid={}&format=csv".format(sheetid)
        globalstock=pd.read_csv(nsesheet)
        bank=globalstock.TICKER
        stock_open=globalstock.OPEN
        stock_high=globalstock.HIGH
        stock_low=globalstock.LOW
        stock_close=globalstock.PREVCLOSE
        stock_change=globalstock.CHANGE
        graph=livegraph(bank,stock_change)
        return render(request,"nse/livestocks.html",{"stock":bank,"stockopen":stock_open,"stockhigh":stock_high,"stocklow":stock_low,"stockclose":stock_close,"stockchange":stock_change,"graph":graph})
        
    return render(request,"nse/livestocks.html")
def graph(request):
    rdata=[]
    global csvname
    if(request.method=="POST") and "loadfile" in request.POST:
        dataset=request.FILES.get("csvdata")
        csvname=dataset.name
        graphdata.objects.create(csvfile=dataset)
        setlocation="f://Dev projects//nselive//Scripts//stockanalysis//media//visualizations//{}".format(csvname)
        csvfile=pd.read_csv(setlocation)
        for i in csvfile:
            rdata.append(i)
        return render(request,"nse/graph.html",{"filedata":rdata})
    if(request.method=="POST") and "getgraph" in request.POST:
        xplot=request.POST.get("xplot")
        yplot=request.POST.getlist("yplot")
        print(xplot,yplot)
        graph=vizgraph(csvname,xplot,yplot)
        return render(request,"nse/graph.html",{"filedata":rdata,"graph":graph})
    return render(request,"nse/graph.html")
