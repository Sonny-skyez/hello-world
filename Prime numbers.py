'''
Prime Numbers:
this progam will generate and show next prime numbers untill user decides to stop.
The prime number is number that can be devided only by 1 and the number itself.

Written: 26.11.2018
Author: Chris Brymer
'''


welcome = '''
   dBBBBBb dBBBBBb    dBP dBBBBBBb  dBBBP     dBBBBb  dBP dBP dBBBBBBb dBBBBb   dBBBP dBBBBBb .dBBBBP
       dB'     dBP             dBP               dBP               dBP    dBP             dBP BP     
   dBBBP'  dBBBBK   dBP dBPdBPdBP dBBP      dBP dBP dBP dBP dBPdBPdBP dBBBK'  dBBP    dBBBBK  `BBBBb 
  dBP     dBP  BB  dBP dBPdBPdBP dBP       dBP dBP dBP_dBP dBPdBPdBP dB' db  dBP     dBP  BB     dBP 
 dBP     dBP  dB' dBP dBPdBPdBP dBBBBP    dBP dBP dBBBBBP dBPdBPdBP dBBBBP' dBBBBP  dBP  dB'dBBBBP'  
 '''

bye = '''                                                                                                    
                                                                                                             __ 
 _____ _           _          ___                    _                                                      |  |
|_   _| |_ ___ ___| |_ ___   |  _|___ ___    _ _ ___|_|___ ___    _____ _ _    ___ ___ ___ ___ ___ ___ _____|  |
  | | |   | .'|   | '_|_ -|  |  _| . |  _|  | | |_ -| |   | . |  |     | | |  | . |  _| . | . |  _| .'|     |__|
  |_| |_|_|__,|_|_|_,_|___|  |_| |___|_|    |___|___|_|_|_|_  |  |_|_|_|_  |  |  _|_| |___|_  |_| |__,|_|_|_|__|
                                                          |___|        |___|  |_|         |___|                 '''

print(welcome)

press_key = 'Press any key to start printing following prime numbers!\n'.center(100)
input(press_key)

num = 2
x = ''


while x.lower() != 'exit':

    for a in range(2, num):

        if num % a == 0:
            num += 1
            break

    else:
        print(num,'is a prime.')
        x = input('Press any key to continue or type "exit" to exit program... ')
        num+=1

print(bye)