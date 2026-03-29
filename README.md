# Monitord: Demonio de Monitorización de Recursos y Alertas

**Monitord** es un servicio robusto para sistemas Linux diseñado para supervisar el estado del hardware (CPU, Memoria y Disco) en tiempo real. 
Funciona como un demonio de `systemd`, permitiendo una ejecución en segundo plano con altos estándares de seguridad y eficiencia.

## Características principales
* **Monitorización en tiempo real:** Captura el uso de CPU, RAM y Disco en intervalos configurables.
* **Alertas Inteligentes:** Notifica a los usuarios mediante `wall` cuando se superan los umbrales.
* **Sistema de Cooldown:** Evita el spam de alertas mediante un tiempo de espera configurable.
* **Recarga en Caliente:** Capacidad de recargar la configuración (señal `SIGHUP`) sin detener el servicio.
* **Hardening de Seguridad:** Ejecución con usuario sin privilegios y aislamiento de sistema mediante directivas de `systemd`.

## Estructura del Proyecto
```text
proyecto-monitord/
├── src/
│   └── monitord.py         # Código fuente del demonio (Python)
├── conf/
│   └── config.conf         # Archivo de configuración clave=valor
├── systemd/
│   └── monitord.service    # Archivo de unidad para systemd
├── scripts/
│   ├── install.sh          # Script de instalación automatizada
│   └── uninstall.sh        # Script de desinstalación limpia
└── README.md               # Documentación del proyecto
```

## Instalacion y Despliegue

### Requisitos

El sistema requiere Python 3 y la libreria psutil. El script de instalacion gestionara las dependencias automaticamente en sistemas basados en Debian/Ubuntu.

### Proceso de Instalacion
1. Clonar el repositorio o descargar los archivos.
2. Otorgar permisos de ejecucion al script de instalacion: `chmod +x scripts/install.sh`
3. Ejecutar el instalador con privilegios de superusuario: `sudo ./scripts/install.sh`
<img width="970" height="414" alt="Screenshot from 2026-03-28 22-07-56" src="https://github.com/user-attachments/assets/e0e97814-db84-4aa4-86d7-722a1bd8af48" />



### Administracion del Servicio
El servicio se gestiona mediante systemctl. Los comandos principales son:
1. Ver estado: `systemctl status monitord`
2. Ver registros (logs): `tail -f /var/log/monitord/monitord.log`
3. Recargar configuracion: `sudo systemctl reload monitord`
4. Detener servicio: `sudo systemctl stop monitord`

<img width="823" height="725" alt="Screenshot from 2026-03-28 22-09-05" src="https://github.com/user-attachments/assets/3763d697-3df2-4304-a4ca-e65b3eef7efc" />


<img width="824" height="738" alt="Screenshot from 2026-03-28 22-09-51" src="https://github.com/user-attachments/assets/2c011a0b-6c07-4f01-9270-cae9f36219e6" />


## Configuracion

El archivo de configuracion se ubica en `/etc/monitord/config.conf`. Los parametros disponibles son:
1. Parametro Descripcion
2. intervalo_segundos Tiempo de espera entre cada medicion.
3. umbral_cpu Porcentaje limite de uso de CPU.    
4. umbral_mem	Porcentaje limite de uso de RAM.
5. cooldown_minutos	Tiempo minimo entre alertas del mismo tipo.
6. particion_disco Ruta de la particion a monitorear (ej. /).
7. Seguridad y Hardening

Usuario del Sistema: El demonio corre bajo el usuario `monitord`, el cual carece de shell y privilegios de administracion.
Restriccion de Escritura: Gracias a la directiva ProtectSystem=strict, el servicio solo tiene permiso de escritura en su directorio de logs.
Control de Procesos: Se utiliza `NoNewPrivileges=true` para evitar que el proceso obtenga privilegios adicionales durante su ejecucion.

## Desinstalacion

Para eliminar el servicio y limpiar los archivos del sistema: `sudo ./scripts/uninstall.sh`

