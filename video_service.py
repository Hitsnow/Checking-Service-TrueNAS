
from fonction import ssh
 

def check_video_service() :
    cmd = "iocage list"
    ip = "192.168.1.xxx"
    user = "xxx"
    status =str(ssh(cmd, ip, user))
    if 'Plex-Server  | up' in status :
        plex = "ok"
    else : 
        cmd_temp ="iocage start Plex-Server "
        ssh(cmd_temp, ip, user)
        status = str(ssh(cmd, ip, user))
        if 'Plex-Server  | up' in status :
            plex = "Reload ok"
        else : 
            plex = "Reload Echec"

    if 'Transmission | up' in status :
        Transmission = "ok"
    else : 
        cmd_temp ="iocage start Transmission "
        ssh(cmd_temp, ip, user)
        status = str(ssh(cmd, ip, user))
        if 'Transmission | up' in status :
            Transmission = "Reload ok"
        else : 
            Transmission = "Reload echec"


    if 'tautulli     | up' in status :
        tautulli = "ok"
    else : 
        cmd_temp ="iocage start tautulli "
        ssh(cmd_temp, ip, user)
        status = str(ssh(cmd, ip, user))
        if 'tautulli     | up' in status :
            tautulli = "Reload ok"
        else : 
            tautulli = "Reload Echec"

    if 'radarr       | up' in status :
        radarr = "ok"
    else : 
        cmd_temp ="iocage start radarr "
        ssh(cmd_temp, ip, user)
        status = str(ssh(cmd, ip, user))
        if 'radarr       | up' in status :
            radarr = "Reload ok"
        else : 
            radarr = "Reload Echec"

    if 'sonarr       | up' in status :
        sonarr = "ok"
    else : 
        cmd_temp ="iocage start sonarr "
        ssh(cmd_temp, ip, user)
        status = str(ssh(cmd, ip, user))
        if 'sonarr       | up' in status :
            sonarr = "Reload ok"
        else : 
            sonarr = "Reload Echec"

    cmd = "docker ps"
    ip = "192.168.x.xxx"
    user = "xxxx"
    status =str(ssh(cmd, ip, user))
    if 'jackett' in status :
        if 'flaresolverr' in status :
            jackett = "ok"
    else : 
        jackett = "Erreur"
  
    if 'ombi' in status :
        ombi = "ok"
    else : 
        ombi = "Erreur"
    
    retour =("Plex : " + plex + "\nTransmission : " + Transmission + "\nTautulli : " + tautulli + "\nRadarr : " + radarr + "\nSonarr : " + sonarr + "\nJackett : " + jackett + "\nOmbi : " + ombi)
    return retour