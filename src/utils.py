def ip_list_generator():
    ip_list = []

# Generar direcciones IP de la subred 10.39.144.0 a 10.39.174.255
# cambiar el valor cuando sea necesario, si tiene en su posibilidad un sistema de mulitprocesadores procure mappear toda la subred apartir
# del octavo bit para mejores resultados, el mapeo tomara tiempo por lo que vaya y tome una taza de cafe mientras tanto
    for i in range(150, 175):
        for j in range(0, 256):
            ip = "10.39.{}.{}".format(i, j)
            ip_list.append(ip)

    # Agregar la subred 10.39.175.0
    for j in range(0, 256):
        ip = "10.39.175.{}".format(j)
        ip_list.append(ip)
        
    return ip_list
