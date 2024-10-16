import speech_recognition as sr 
import pyttsx3  

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr_Microphone() as source2:
                r.adjust_for_ambiant_noise(source2, duration=0.2)
                
                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)


        except sr.RequestError as e:
            print("Could not requests result; {0}".format(e))

        except sr.UnknowValueError:
            print("Unknow error")   

    return  

def outpout_text():
    f = open("outpout.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    outpout_text(text)

    print("Wrote text")


