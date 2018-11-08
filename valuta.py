import requests
from bs4 import BeautifulSoup

ValutaArray=['USD','EUR','RUB','AUD','CAD','CHF','CZK','DKK','GBP','HUF','ILS','JPY','NOK','PLN','SEK','UAH']


def CourseUaHtoOtherValuta(valuta):
    if valuta in ValutaArray:
        ValutaServer = "https://kurs.censor.net.ua/currencies"
        DataValute = requests.get(ValutaServer)
        soup = BeautifulSoup(DataValute.text, 'html.parser').find("table").find_all('tr')[2:]
        CurrentValuta=str(soup[ValutaArray.index(valuta)])
        MainData=CurrentValuta.split('<td>')[-2:]
        for i in range(2):
            MainData[i] = MainData[i].split(">")[1].split("<")[0]
        return ("Покупка -"+MainData[0]+ '\n'+"Продажа -"+MainData[1])
    else:
        return("Такої валюти не існує")
def CourseFromOneValutaToAnotherValuta(valuta1,valuta2):
    if valuta1 in ValutaArray and valuta2 in ValutaArray:
        BuyForValuta1= float(CourseUaHtoOtherValuta(valuta1).split('-')[2])
        SellForValuta2= float( CourseUaHtoOtherValuta(valuta2).split('-')[1].split('\n')[0])
        return BuyForValuta1/SellForValuta2
    else:
        return "Такої валюти не існує"
def Calculator(money1,valuta1, valuta2):
    money1=float(money1)
    if valuta1 in ValutaArray and valuta2 in ValutaArray:
        if valuta1 == "UAH":
            result= 1/float(CourseUaHtoOtherValuta(valuta2).split('-')[2])*money1
        elif valuta2 == "UAH":
            result=float((CourseUaHtoOtherValuta(valuta1).split('-')[1].split('\n')[0])) * money1
        else:
            result=float(CourseFromOneValutaToAnotherValuta(valuta1,valuta2))*money1
        return result
    else:
        return "Такої валюти не існує"
def All_valutas():
    result=""
    for val in ValutaArray:
        result+= val+'\n'
    return result