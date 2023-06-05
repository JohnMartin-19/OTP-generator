import pyotp
from timeit import default_timer as timer

with open("secret_key.txt","r")as rf:
    base_32_secret_key = rf.read()
    
#print(base_32_secret_key)

#OTP GENERATION
Timebasedotp = pyotp.TOTP(base_32_secret_key)
current_otp = Timebasedotp.now()

#print(current_otp)

def verification(time_gap, entered_otp,otp,Timebasedotp):
    if(time_gap)<30 and (entered_otp == otp):
        print("Hello user, you are successfully verified.$$")
        return 
    elif(time_gap)<30 and (entered_otp != otp):
        print("Sorry.Invalid OTP")
        resend_otp()
    elif(time_gap)>=30:
        print("Time Up. Your OTP expired.Generate a new one!")
        resend_otp(Timebasedotp)

def resend_otp(Timebasedotp):
    current_otp = Timebasedotp.now()
    while True:
        new_current_otp = Timebasedotp.now()
        if new_current_otp != current_otp:
            print(f"current_otp: (new_current_otp)")
            start=timer()
            enter_otp=input("ENter current_otp: ")
            end=timer()
            resend_time_interval = end-start
            print(f"Time taken : {resend_time_interval} ")
            verification(resend_time_interval, enter_otp, new_current_otp, Timebasedotp)
            break
        return
    

while True:
    new_current_otp = Timebasedotp.now()
    if new_current_otp != current_otp:
        print(f'current_otp: {new_current_otp}')
        start= timer()
        enter_otp = input("Enter current_otp: ")
        end = timer()
            
        time_interval = end-start
        print(f"Time taken: {time_interval}")
        verification(time_interval,enter_otp,new_current_otp,Timebasedotp)
        break
    