import datetime
import random
import re
from threading import Thread
import tkinter as tk
from tkinter import messagebox
from autocorrect import spell
import pyttsx3
import speech_recognition as sr
import ANN
import pandas as pd
k=1
##### End of part 1 ######
engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate',150)
engineio.setProperty('voice',voices[1].id)

conv_start = ['unwell','bad','unhealthy','sad']
conv_start_reply = ['No issues, lets start the diagnosis','Ok, you seem to be suffering from some disease, lets try to find out what it is, shall we?']
conv_stop = ['Get well soon', 'Have a nice day!']
quit_words = ['bye','exit','quit','close','terminate','goodbye','stop']
affirmative = ['okay','ok','fine','allright','yes','please']

def speak(text):
    engineio.say(text)
    engineio.runAndWait()
    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.update()
        root.destroy()

def speech_to_text():
    recorded_voice = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recorded_voice.listen(source)    
    try:
        text_from_speech = recorded_voice.recognize_google(audio)
        return text_from_speech
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
        
def print_user_msg(user_msg):
    user_msg = "You: " + str(user_msg)
    label = tk.Label(frame, text=user_msg, bg="#bcb1ef",fg="black", borderwidth=5, relief="raised",padx=15,pady=10,font=("Helvetica", 11))
    label.pack(anchor = "e")

def print_bot_reply(response):
    response = "Dr Strange: " + str(response)
    label = tk.Label(frame,text = response,bg="#b6efb1", borderwidth=5, relief="raised",padx=15,pady=15,font=("Helvetica", 11))
    label.pack(anchor = "w")
    root.update()
    response = re.sub('Dr Strange:','',response)
    thread = Thread(target = speak, args = (response, ))
    thread.start()

def get_questions():
    questions = ["Do you experience chest pain?   0.No 1.Yes","Do you experience Weight Loss?   0.No 1.Yes","Do you experience Fatigue?   0.No 1.Yes","Do you have Fever?   0.No 1.Yes 2.Severe","Do you experience Chills?   0.No 1.Yes","Do you experience Loss of Appetite?   0.No 1.Yes","Do you experience Vomiting?   0.No 1.Yes","Do you experience Muscle Pain?   0.No 1.Yes","Do you experience Sore Throat?  0.No 1.Yes", "Diagnosing..."]
    print_bot_reply("Do you experience coughing? 0.No 1.Yes")
    return questions
    
user_to_quit = False
user_is_greeting = False
diagnosis_begin = False
flag = 0
index = 0
maxind = 0
diagnosis_inputs = False
user_ans = []
def on_configure(event):
    canvas.configure(scrollregion=(0,0,30000,30000))
root = tk.Tk()
root.title("Medical Expert System: Your virtual doctor")
root.iconbitmap(r'heart_beat.ico')
titleLabel = tk.Label(root, text = "Medical Expert System", bg = "#BFB3B3", fg = "black")
input_user = tk.StringVar()

input_field = tk.Entry(root, width = 125, text=input_user, bd=0, relief = "sunken", background = '#1f2223', fg='white')
input_field.config(font=("Helvetica", 14))
input_field.pack(side=tk.BOTTOM, anchor='w')

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT)
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill='y')
canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind('<Configure>', on_configure)
def enter_pressed(event):
  global user_to_quit
  global user_is_greeting
  global flag
  global diagnosis_begin
  global index
  global questions
  global maxind
  global diagnosis_inputs
  global user_ans
  flag = 0
  if(input_field.get() in quit_words):
      user_to_quit=True
      on_closing()
  
  
  if(diagnosis_begin == False):
      input_get_1 = input_field.get()
      if(input_get_1  == 'v'):
          user_msg = speech_to_text()
          input_user.set(user_msg)
      else:
          input_get=input_get_1.split(' ')
          input_user.set('')
          for i in input_get:
              s=input_get.index(i)
              i=re.sub('[^a-zA-Z0-9-]','',i)
              correct_word=spell(i)
              input_get[s]=correct_word
          input_get=' '.join(input_get)
          user_msg = input_get_1
          root.update()
          print_user_msg(user_msg)
          
      #Storing user's message in user_msg:
          for word in user_msg.split():
            if word in quit_words:
              user_to_quit = True
              Print = random.choice(conv_stop)
              print_bot_reply(Print)
              on_closing()
          if (user_to_quit==False):
            user_is_greeting = False
            for word in user_msg.split():
              if word.lower() in conv_start:
                bot_reply = random.choice(conv_start_reply)
                print_bot_reply(bot_reply)
                user_is_greeting = True
                flag = 1
              elif word.lower() in affirmative:
                  questions = get_questions()
                  diagnosis_begin = True
                  index = 0
                  maxind = len(questions)
                  #ask inputs
                  #print_bot_reply():
            '''if(flag==0):
                Print = "Sorry, I did not catch that!"
                print_bot_reply(Print)'''
        
  else:
    if(diagnosis_begin == True and diagnosis_inputs == False):
        #new get inputs from the user
        input_get = input_field.get()
        input_user.set('')
        if(input_get == 'v'):
          user_msg = speech_to_text()
          input_user.set(user_msg)
        else:
            print_user_msg(str(input_get))
            user_ans.append(str(input_get))
            print_bot_reply(questions[index])
            index +=1
            if(index==maxind):
                diagnosis_inputs = True
    if(diagnosis_inputs == True):
        #call rhythms function
        print(len(user_ans))
        cleanedAns = [x for x in user_ans if str(x) != 'nan']
        print(cleanedAns)
        disease = ANN.main(user_ans)[0]
        toPrint = "You seem to be suffering from: " + disease
        print_bot_reply(toPrint)
        disease_details = pd.read_csv('diseases_details.csv')
        x = list(disease_details.iloc[:,0])
        index = x.index(disease)
        about = disease_details.iloc[:,1][index]
        spread = disease_details.iloc[:,2][index]
        treatment = disease_details.iloc[:,3][index]
        doctors = disease_details.iloc[:,4][index]
        msg = 'About ' + disease + ': ' + about
        print_bot_reply(msg)
        msg = 'How ' + disease + 'spreads: ' + spread
        print_bot_reply(msg)
        msg ='Possible treatment options for ' + disease + ' '+ treatment
        print_bot_reply(msg)
        msg = 'Visit specialist doctor of: ' + doctors
        print_bot_reply(msg)
        diagnosis_begin = False
        
frame = tk.Frame(canvas, width=1366, height=30000, bg="#3b4042")
frame.pack_propagate(False) # prevent frame to resize to the labels size
question = input_field.get()
input_field.bind("<Return>", enter_pressed)
currentTime = datetime.datetime.now()
if currentTime.hour < 12:
  greet_message = "Good morning!"
elif 12 <= currentTime.hour < 18:
  greet_message = 'Good afternoon!'
else:
  greet_message = 'Good evening! '   
greet_message += "How are you feeling today? "    
print_bot_reply(greet_message)

# k=test3.main().disease_prediction(k)
# resulting_disease=test3.main()

canvas.create_window((0,0), window=frame, anchor='nw')
canvas.config(width=1350,height=30000)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()