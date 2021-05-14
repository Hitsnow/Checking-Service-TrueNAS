# AUTO CKECKING SERVICE 

Programme en python d'autocheck permentant : 
        - Verifier le fonctionnement de service de Domotique sur Debian, et de les rebooter au besoin
        - Verifier le fonctionnemnet de service video sous debian et plugging Truenas et les rebooter au besoin
        - Une fonction ping pour vérifier la connection en cas de non réponse en SSH 

Systeme : TrueNAS 12 avec 2 VM DEBIAN (HOMBEBRIDGE, Mosquitto, Plex, Radarr, Sonarr, jackett, Tauttuli, Ombi)
Import : paramiko, rich, tkinter, os, threading