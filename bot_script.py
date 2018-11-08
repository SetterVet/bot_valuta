# short instruction
# command:
# /aval - show all available valutas
# /calc VALUTA - show course buy and sell for VALUTA to UAH
# /2val VALUTA1,VALUTA2 - only , between first and second valuta show course between 2 not UAH valuta
# /calc COUNT_OF_FIRST_VALUTA, VALUTA1, VALUTA2 -show count in second valuta
#
#
# adress_of_bot -@courseofvalutabot
# firstly, write your first command and then run this script
#

import requests
import json
from valuta import CourseUaHtoOtherValuta, CourseFromOneValutaToAnotherValuta, Calculator,All_valutas
from time import sleep
from token import bottoken
token = bottoken
link = "https://api.telegram.org/bot"+token+"/"

global last_update_id
last_update_id=0
def get_updates():
    url=link+"getupdates"
    response=requests.get(url)
    return response.json()

def get_message():
    json_data=get_updates()
    current_update_id=json_data['result'][-1]['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id=json_data['result'][-1]['message']['chat']['id']
        message_text=json_data['result'][-1]['message']['text']
        return { "chat_id": chat_id, "text": message_text} #  Функція повертає словник з 2 елементами id чату та повідомленням від користувача
    return None
def send_message(chat_id,text):
    url=link+"sendmessage?chat_id="+str(chat_id)+"&text="+text
    requests.get(url)

def main():
    while True:
        answer=get_message()
        if answer != None:
            if answer['text'][:5] =='/curs':
                v1=answer['text'].split(" ")[1]
                send_message(answer['chat_id'],CourseUaHtoOtherValuta(v1))
            elif answer['text'][:5]=='/2val':
                data=answer['text'].split(" ")[1].split(',')
                send_message(answer['chat_id'],str(CourseFromOneValutaToAnotherValuta(data[0],data[1])))
            elif answer['text'][:5]=='/calc':
                data=answer['text'].split(" ")[1].split(',')
                send_message(answer['chat_id'],str(Calculator(data[0],data[1],data[2])))
            elif answer['text'][:5] == '/aval':
                send_message(answer["chat_id"],str(All_valutas()))
            else:
                send_message(answer['chat_id'],"Такої Функції не існує")

if __name__=='__main__':
    main()
