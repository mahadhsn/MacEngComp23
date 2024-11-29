import speech_recognition as sr

def speech2text():
    x=0
    while x<1:
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            
            print("Please say something:")
            
            audio = r.listen(source)
            
            try:
                print("You have said: \n "+r.recognize_google(audio))
                
            except Exception as e:
                print("error: "+str(e))
        x+=1
        return
speech2text()
