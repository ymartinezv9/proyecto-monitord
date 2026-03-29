#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "Ejecuta como sudo" 
   exit 1
fi

# Crear usuario si no existe
id -u monitord &>/dev/null || useradd -r -s /sbin/nologin monitord

# Crear directorios y copiar archivos
mkdir -p /etc/monitord /var/log/monitord
cp src/monitord.py /usr/local/bin/monitord.py
cp conf/config.conf /etc/monitord/config.conf
cp systemd/monitord.service /etc/systemd/system/

# Permisos
chown -R monitord:monitord /var/log/monitord /etc/monitord
chmod +x /usr/local/bin/monitord.py

# Iniciar servicio
systemctl daemon-reload
systemctl enable monitord
systemctl start monitord

echo "--- INSTALACIÓN COMPLETADA ---"
systemctl status monitord
