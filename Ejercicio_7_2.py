import time

def endTime (hour = int(time.strftime('%H')), min = int(time.strftime('%M'))):
    if hour >= 19:
        return "Ya es hora de irse a casa"
    
    return f"Quedan {19-hour} horas y {59-min} minutos para irse a casa"

print(endTime())
