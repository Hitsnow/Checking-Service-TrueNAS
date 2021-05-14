import tkinter
from tkinter import messagebox
import reboot_domotique
import fonction
import threading
import video_service
from video_service import check_video_service

def check_serveur():
    ip="192.168.x.xx"
    status = fonction.ping(ip)
    label_serveur.set(status)
    return

def Check_Domotique () : 
     th1 = threading.Thread(target=Check_Domotique_device)
     th2 = threading.Thread(target=Check_Domotique_service)

     th1.start()
     th2.start()
     return

def Check_Domotique_service():
    status_service_domotique = reboot_domotique.service()
    label_domotique_service.set(status_service_domotique)
    return

def Check_Domotique_device():
    status_devices_domotique = "Devices :"+ reboot_domotique.devices()
    label_domotique_device.set(status_devices_domotique)
    return

def check_video() : 
    status_video = check_video_service()
    return label_video_service.set(status_video)

def ALL_CHECKING() : 
     th1 = threading.Thread(target=Check_Domotique_device)
     th2 = threading.Thread(target=Check_Domotique_service)
     th3 = threading.Thread(target=check_serveur)
     th4 = threading.Thread(target=check_video)
     
     
     th1.start()
     th2.start()
     th3.start()
     th4.start()


app = tkinter.Tk()
color_bg='gray'
color_text_button = 'blue'
#Position et taille de la fenetre
app.geometry("300x400")
app.configure(bg=color_bg)
windowWidth = app.winfo_reqwidth()
windowHeight = app.winfo_reqheight()
positionRight = int(app.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(app.winfo_screenheight()/2 - windowHeight/2)
app.geometry("+{}+{}".format(positionRight, positionDown))


app.title("Rapport Serveur")
Button_serveur = tkinter.Button(app, text="ALL CHECKING" , command = ALL_CHECKING,fg = color_text_button).pack()
espace = tkinter.Label(app,textvariable="",bg=color_bg).pack()

#check server_principal
Button_serveur = tkinter.Button(app, text="Check Server" , command = check_serveur,fg = color_text_button).pack()
label_serveur = tkinter.StringVar()
label_serveur.set("Non vérifié")
Domotique_service = tkinter.Label(app,textvariable=label_serveur,bg=color_bg).pack()

# check domotique
Button_domotique = tkinter.Button(app, text="Domotiques" , command = Check_Domotique,fg = color_text_button).pack()

label_domotique_service = tkinter.StringVar()
label_domotique_service.set("Non vérifié")
Domotique_service = tkinter.Label(app,textvariable=label_domotique_service,bg=color_bg).pack()

#Button_domotique = tkinter.Button(app, text="Domotique - Devices" , command = Check_Domotique_device,fg = color_text_button).pack()

label_domotique_device = tkinter.StringVar()
label_domotique_device.set("")
Domotique_device = tkinter.Label(app,textvariable=label_domotique_device,bg=color_bg).pack()

#check service video
Button_video = tkinter.Button(app, text="Check Video Services" , command = check_video,fg = color_text_button).pack()

label_video_service = tkinter.StringVar()
label_video_service.set("Services : Non vérifié")
video_service = tkinter.Label(app,textvariable=label_video_service,bg=color_bg).pack()

app.mainloop()