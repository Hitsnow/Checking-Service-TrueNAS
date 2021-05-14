
from fonction import ping , ssh

def service():
    print ("REDEMARRAGE DE LA DOMOTIQUE")
    cmd_status_homebridge = "systemctl status homebridge"
    cmd_status_mosquitto = "systemctl status mosquitto"
    cmd_restart_homebridge = "systemctl restart homebridge"
    cmd_restart_mosquitto = "systemctl restart mosquitto"
    tentative =1
    ip = "192.168.x.xxx"
    user = "192.168.x.xxx"

    status_homebdrige = ssh(cmd_status_homebridge,ip,user)
    status_mosquitto = ssh(cmd_status_mosquitto,ip,user)
    status_h = "Hors ligne"
    status_m = "Hors ligne"
    status = "NC"    
    if "active (running)" in status_homebdrige :
        print("Homebridge OK")
        status_h = "En ligne"
    else :
        print("HomeBridge ERREUR")
        tentative = 1
        while tentative <4 :
            print("Start HomeBridge - Essai n°'%d'" % tentative)
            ssh(cmd_restart_homebridge,ip,user)
            status_homebdrige = ssh(cmd_status_homebridge,ip,user)
            if "active (running)" in status_homebdrige :
                print("Homebridge OK")
                status_h = "Reboot : OK"
                break
            i = i+1

    if "active (running)" in status_mosquitto :
        print("Mosquitto OK")
        status_m = "En ligne"
    else :
        print("Mosquitto ERREUR")
        tentative = 1
        while tentative <4 :
            print("Start Mosquitto - Essai n°'%d'" % tentative)
            ssh(cmd_restart_mosquitto,ip,user)
            status_mosquitto = ssh(cmd_status_mosquitto,ip,user)
            if "active (running)" in status_mosquitto :
                print("Mosquitto OK")
                status_m = "reboot : OK"

                break
            i = i+1
    if tentative ==4 :
        domotique_serveur_ip = "196.168.x.xxx"
        status_ping = ping(domotique_serveur_ip)
        if status_ping == "ERREUR" :
            status = "Domotique Hors Ligne"
    else : 
        status = "Mosquitto : "+status_m+"\n Homebridge : "+status_h
    return status








def devices() :
    Salon_lumière = "192.168.1.xxx"
    Salon_led = "192.168.1.xxx"
    Lumière_Chambre = "192.168.1.xxx"
    Lumière_Bureau = "192.168.1.xxx"
    status_Salon_lumière = ping(Salon_lumière)
    status_Salon_led = ping(Salon_led)
    status_Lumière_Chambre = ping(Lumière_Chambre)
    status_Lumière_Bureau = ping(Lumière_Bureau)

    status_erreur = []

    if (status_Lumière_Bureau == "ERREUR"):
        status_erreur.append("Lumière Bureau")

    if (status_Salon_led == "ERREUR"):
        status_erreur.append("Led Salon")

    if (status_Lumière_Chambre == "ERREUR"):
        status_erreur.append("Lumière Chambre")

    if (status_Salon_lumière == "ERREUR"):
        status_erreur.append("Lumière Salon")

    if (len(status_erreur) == 0):
        print("Ping all OK")
        retour = "OK"
    else:
        print(status_erreur)
        retour = "Erreur devices : " + status_erreur
    return retour