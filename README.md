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
