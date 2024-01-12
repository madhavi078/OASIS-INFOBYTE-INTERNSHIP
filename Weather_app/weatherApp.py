#Advance level Weather App using tkinter and API in Python

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

#GUI
root = Tk()
root.title("weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getWeather():
    try:
            
        city=textfield.get()
        
        user_api = 'a33d867f071747f724fa3fb0882ec60d'
        
        geolocator= Nominatim(user_agent="geoExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home=pytz.timezone(result)
        local_time = datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+user_api
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        t.config(text = (temp, "° C"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=(wind,"kmph"))
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=(pressure,"hpa"))
    
    except Exception as e:
        messagebox.showerror("Weather App","Inv") 
    
    
    
    
#Search box
Search_image = PhotoImage(file="C:\\Users\MADHAVI\\Oasis_Infobyte_Internship\\Weather_app\\search.png")
myimage = Label(image = Search_image)
myimage.place(x=20,y=20)

textfield= tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon = PhotoImage(file="C:\\Users\\MADHAVI\\Oasis_Infobyte_Internship\\Weather_app\\search_icon.png")
myimage_icon = Button(image = Search_icon,borderwidth=0, cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
logo_image= PhotoImage(file="C:\\Users\\MADHAVI\\Oasis_Infobyte_Internship\\Weather_app\\weatherlogo1.png")
myimage_logo = Label(image = logo_image,cursor="hand2")
myimage_logo.place(x= 150,y = 100)

#bottom box
frame_image = PhotoImage(file="C:\\Users\\MADHAVI\\Oasis_Infobyte_Internship\\Weather_app\\box.png")
myimage_frame = Label(image = frame_image)
myimage_frame.pack(padx=5,pady=5,side=BOTTOM)

#time
name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1 = Label(root, text="WIND",font=("Helvtica",15,'bold'),fg="white",bg="#00B2EE")
label1.place(x=120,y=400)

label1 = Label(root, text="HUMIDITY",font=("Helvtica",15,'bold'),fg="white",bg="#00B2EE")
label1.place(x=250,y=400)

label1 = Label(root, text="DESCRIPTION",font=("Helvtica",15,'bold'),fg="white",bg="#00B2EE")
label1.place(x=430,y=400)

label1 = Label(root, text="PRESSURE",font=("Helvtica",15,'bold'),fg="white",bg="#00B2EE")
label1.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arail",20,"bold"),bg="#00B2EE")
w.place(x=120,y=430)
h=Label(text="...",font=("arail",20,"bold"),bg="#00B2EE")
h.place(x=280,y=430)
d=Label(text="...",font=("arail",20,"bold"),bg="#00B2EE")
d.place(x=430,y=430)
p=Label(text="...",font=("arail",20,"bold"),bg="#00B2EE")
p.place(x=670,y=430)




root.mainloop()