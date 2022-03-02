import requests
import datetime

response = requests.get('https://www.cbr-xml-daily.ru/daily.xml')
resp_text = response.text

charcode = input().upper()
value = ''

start = resp_text.find('Date=')
end = resp_text.find(' name')

date_str =''

for i in range(start, end):
    if resp_text[i].isdigit() or resp_text[i]=='.':
        date_str+=resp_text[i]
        
str_date_list = date_str.split('.')
int_date_list = list(map(int, str_date_list))

date = datetime.date(int_date_list[2], int_date_list[1], int_date_list[0])
print(date)
if charcode in resp_text:
    charcode_index = resp_text.index(charcode)
    
    start = resp_text.find('Value', charcode_index)
    end = resp_text.find('/Value', charcode_index)
    for i in range(start, end):
        if resp_text[i].isdigit():
            value+=resp_text[i]
        elif resp_text[i]==',':
            value+='.'
value = float(value)
print(value)
            
    