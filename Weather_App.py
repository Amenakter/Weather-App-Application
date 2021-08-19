import tkinter as tk
from PIL import Image,ImageTk
from Weather_Api import weather_information

def open_weather_icon(icon):
    size = int(information_frame.winfo_height()*0.20)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png'))
    weather_icon.delete('all')
    weather_icon.create_image(0,0, anchor ='nw', image = img)
    weather_icon.image = img


def get_weather_info(city_name):
    weather_report = weather_information(city_name)
    result["text"]= weather_report[0]
    weather_icon_name = weather_report[1]
    open_weather_icon(weather_icon_name)





app = tk.Tk()
canvas = tk.Canvas(app, height=590, width=690)
canvas.pack()
app.resizable(False, False)
app.title("Weather App")


#background

background_image = tk.PhotoImage(file="background-image.png")
background_lebel = tk.Label(app, image=background_image)
background_lebel.place(relheight=1, relwidth=1)

#headding of the app

heading = tk.Label(app, text="Weather Information",
                    font=("Helvatica", 25 , "bold" ),
                    bg =  "#ffff99" ,
                    bd = 5)
heading.place(relwidth=1)

#input frame
frame = tk.Frame(app, bg="#42c2f4", bd= 5)
frame.place(x=110, y=100, relwidth=0.75, relheight=0.1)

#input text box

textbox= tk.Entry(frame, font=("courier", 16))
textbox.place(relwidth=0.65, relheight=1)

# submit button
submit_button = tk.Button(frame,
                    text='Search Weather',
                    font=35,
                    command=lambda:get_weather_info(textbox.get()))
submit_button.place(x=360 , relwidth=0.3, relheight=1)

#information frame

information_frame = tk.Frame(app, bg="#42c2f4", bd= 6)
information_frame.place(x=150, y=200, relheight=0.65, relwidth=0.55)


# result 

result = tk.Label(information_frame,
                   font=('courier', 14),
                   anchor="nw",
                   justify="left",
                   bg="white",
                   bd= 4)

result.place(relheight=1, relwidth=1)    

# canvas for weather icon
weather_icon = tk.Canvas(result, bg='white', bd=0,highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

app.mainloop()