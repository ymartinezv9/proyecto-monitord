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

Instalacion y Despliegue
Requisitos

El sistema requiere Python 3 y la libreria psutil. El script de instalacion gestionara las dependencias automaticamente en sistemas basados en Debian/Ubuntu.
Proceso de Instalacion

    Clonar el repositorio o descargar los archivos.

    Otorgar permisos de ejecucion al script de instalacion:
    Bash

    chmod +x scripts/install.sh

    Ejecutar el instalador con privilegios de superusuario:
    Bash

    sudo ./scripts/install.sh

Administracion del Servicio

El servicio se gestiona mediante systemctl. Los comandos principales son:

    Ver estado: systemctl status monitord

    Ver registros (logs): tail -f /var/log/monitord/monitord.log

    Recargar configuracion: sudo systemctl reload monitord

    Detener servicio: sudo systemctl stop monitord

Configuracion

El archivo de configuracion se ubica en /etc/monitord/config.conf. Los parametros disponibles son:
Parametro	Descripcion
intervalo_segundos	Tiempo de espera entre cada medicion.
umbral_cpu	Porcentaje limite de uso de CPU.
umbral_mem	Porcentaje limite de uso de RAM.
cooldown_minutos	Tiempo minimo entre alertas del mismo tipo.
particion_disco	Ruta de la particion a monitorear (ej. /).
Seguridad y Hardening

    Usuario del Sistema: El demonio corre bajo el usuario 'monitord', el cual carece de shell y privilegios de administracion.

    Restriccion de Escritura: Gracias a la directiva ProtectSystem=strict, el servicio solo tiene permiso de escritura en su directorio de logs.

    Control de Procesos: Se utiliza NoNewPrivileges=true para evitar que el proceso obtenga privilegios adicionales durante su ejecucion.

Desinstalacion

Para eliminar el servicio y limpiar los archivos del sistema:
Bash

sudo ./scripts/uninstall.sh

