#!/bin/bash

# Verificar que se corre como root
if [[ $EUID -ne 0 ]]; then
   echo "Por favor, ejecuta este script como sudo." 
   exit 1
fi

echo "--- INICIANDO DESINSTALACIÓN DE MONITORD ---"

# 1. Detener y deshabilitar el servicio en systemd
echo "Deteniendo el servicio..."
systemctl stop monitord
systemctl disable monitord

# 2. Eliminar el archivo de unidad de systemd
echo "Eliminando archivos del sistema..."
rm -f /etc/systemd/system/monitord.service
systemctl daemon-reload
systemctl reset-failed

# 3. Eliminar el ejecutable
rm -f /usr/local/bin/monitord.py

# 4. Eliminar configuraciones y logs
# Nota: A veces se prefiere dejar los logs, pero para una limpieza total los borramos.
rm -rf /etc/monitord
rm -rf /var/log/monitord

# 5. Eliminar el usuario y grupo (opcional pero recomendado para limpieza)
echo "Eliminando usuario monitord..."
userdel monitord

echo "--- DESINSTALACIÓN COMPLETADA CON ÉXITO ---"
