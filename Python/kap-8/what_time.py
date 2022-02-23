from datetime import datetime
stunde = datetime.today().hour
minute = datetime.today().minute
if stunde >= 12:
    stunde = stunde - 12
if minute < 30:
    print(minute,"nach",stunde)
elif minute > 30:
    print(60 - minute, "vor", stunde + 1)
elif minute == 0:
    print(stunde)
else:
    print("halb", stunde + 1)
