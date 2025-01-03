t=input()
t=float(t)
t=int(t)

if t<0:
    print("Freezing weather")
elif 0<=t<10:
    print("Very Cold weather")
elif 10<=t<20:
    print("Cold weather")
elif 20<=t<30:
    print("Normal")
elif 30<=t<40:
    print("Hot")
else:
    print("Very Hot")