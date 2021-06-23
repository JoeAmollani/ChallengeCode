# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:28:02 2021

@author: Joen
"""

V1Dictionary = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'
            ,11:'eleven',12:'twelve',13:'therteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

V2Dictionary = {2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

V3Dictionary = {3:'hundred',4:'thousand',7:'million',9:'billion'}

''' Read text '''
with open('Text.txt') as f:
    text = f.readlines()
text = ', '.join(text)


def Digits(TextNumber):
    
    if len(TextNumber) == 1:
        Var = V1Dictionary[int(TextNumber[0])]
    elif len(TextNumber) == 2:
        
        if TextNumber[0] == '0':    
            Var = V1Dictionary[int(TextNumber[-1])]   
        elif TextNumber[0] == '1':
            
            Var = V1Dictionary[int(TextNumber)]     
        else:
            Var = V2Dictionary[int(TextNumber[0])]+' '+V1Dictionary[int(TextNumber[-1])]
            
    elif len(TextNumber) == 3:
        
        if TextNumber == '000':
            Var = ''      
        elif TextNumber[-2:] == '00':
            Var = V1Dictionary[int(TextNumber[0])] +' '+ V3Dictionary[3]      
        elif TextNumber[0:2] == '00':
            Var = V1Dictionary[int(TextNumber[-2:])]
        elif TextNumber[1] == '1' and TextNumber[0] == '0':
            Var = V1Dictionary[int(TextNumber[-2:])]
        elif TextNumber[1] == '0':
            Var = V1Dictionary[int(TextNumber[0])] +' '+ V3Dictionary[3] +' '+V1Dictionary[int(TextNumber[-1])]      
        else:
            if TextNumber[0] == '0' and TextNumber[1] > '1':
                Var = V2Dictionary[int(TextNumber[-2])]+' '+V1Dictionary[int(TextNumber[-1])]
            else:
                Var = V1Dictionary[int(TextNumber[0])] +' '+ V3Dictionary[3]+' '+ V2Dictionary[int(TextNumber[-2])]+' '+V1Dictionary[int(TextNumber[-1])]        
    else:
       Var = 'number invalid'
    return Var

def PrintNumber(text):
     
    try:
         String = str([int(x) for x in text.split() if x.isdigit()]).strip("[]")
    except:
         String = 'number invalid'
    
    if len(String) < 4:
        
        print(Digits(String))

    elif len(String) >= 4 and len(String) <= 6:
        
        if Digits(String[-3:]) == '':
             print(Digits(String[0:len(String)-3])+' '+ V3Dictionary[4]+''+
                   Digits(String[-3:])+' ')

        else: 
             print(Digits(String[0:len(String)-3])+' '+ V3Dictionary[4]+' and '+
                   Digits(String[-3:]))

    elif len(String) > 6 and len(String) <= 9:
        
        if Digits(String[-3:]) == '' and Digits(String[-6:-3]) == '':
            
            print(Digits(String[0:len(String)-6]) + ' ' + V3Dictionary[7])

        elif Digits(String[-3:]) != '000' and Digits(String[-6:-3]) == '000':
            
            print(Digits(String[0:len(String)-6]) + ' ' + V3Dictionary[7] + ' and ' + 
                  Digits(String[-3:]))

        elif Digits(String[-3:]) == '000' and Digits(String[-6:-3]) != '000':
            
            print(Digits(String[0:len(String)-6]) + ' ' + V3Dictionary[7] + ' ' +
                  Digits(String[-6:-3])+' '+ V3Dictionary[4]+ ' and '+
                  Digits(String[-3:]))
        else:
            
            print(Digits(String[0:len(String)-6]) + ' ' + V3Dictionary[7] + ', ' +
                  Digits(String[-6:-3])+' '+ V3Dictionary[4]+ ' and '+
                  Digits(String[-3:]))            

    elif len(String) > 9 and len(String) <= 12:
        
        if Digits(String[-9:-6]) != '' and Digits(String[-6:-3]) != '':
            
           print(Digits(String[0:len(String)-9]) + ' ' + V3Dictionary[9] + ', ' +
                 Digits(String[-9:-6])+' '+ V3Dictionary[7]+ ', '+
                 Digits(String[-6:-3])+' '+ V3Dictionary[4]+' and '+
                 Digits(String[-3:]))

        if Digits(String[-9:-6]) == '' and Digits(String[-6:-3]) == '':
            
            print(Digits(String[0:len(String)-9]) + ' ' + V3Dictionary[9]+ ' and ' + 
                  Digits(String[-3:]))              

        if Digits(String[-9:-6]) == '' and Digits(String[-6:-3]) != '':

           print(Digits(String[0:len(String)-9]) + ' ' + V3Dictionary[9] + ', ' +
                 Digits(String[-6:-3])+' '+ V3Dictionary[4]+ ' and '+
                 Digits(String[-3:]))

        if Digits(String[-9:-6]) != '' and Digits(String[-6:-3]) == '':
            
           print(Digits(String[0:len(String)-9]) + ' ' + V3Dictionary[9] + ', ' +
                 Digits(String[-9:-6])+' '+ V3Dictionary[7]+ ' and '+
                 Digits(String[-3:]))
    else:
        print('Script does not handle trillions')

#text = 'The database has 66723107008 records'

PrintNumber(text)








