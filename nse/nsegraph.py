import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
def livegraph(bank,stock_change):
    plt.switch_backend("AGG")
    plt.figure(figsize=(7,3))
    plt.title("NSE LIVE STOCK")
    #plt.subplot(1,2,1)
    plt.bar(bank,stock_change,color="blue")
    #for index, value in enumerate(stock_change):
        #plt.text(value, index, str(value))

    #plt.subplot(1,2,2)
    #plt.pie(stock_change)
    plt.xticks(rotation=45)
    plt.xlabel("NSE TOP STOCKS")
    plt.ylabel("VALUE")
    plt.tight_layout()
    buffer=BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode("utf-8")
    buffer.close()
    return graph
    
def piegraph(bank,stock_change):
    plt.switch_backend("AGG")
    plt.figure(figsize=(4,3))
    plt.title("NSE LIVE STOCK")
    plt.plot(bank,stock_change)
    plt.xticks(rotation=45)
    plt.xlabel("NSE TOP STOCKS")
    plt.ylabel("VALUE")
    plt.tight_layout()
    buffer=BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode("utf-8")
    buffer.close()
    return graph
def vizgraph(csvname,xplot,yplot):
    xplot=str(xplot)
    p="f://Dev projects//nselive//Scripts//stockanalysis//media//visualizations//{}".format(csvname)
    df=pd.read_csv(p)
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title("graph report")
    df.plot(x=xplot,y=yplot,kind='line')
    plt.xticks(rotation=45)
    plt.xlabel(xplot)
    plt.ylabel("y axis")
    plt.tight_layout()
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph
