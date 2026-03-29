import os
import time
import signal
import logging
import psutil
from datetime import datetime, timedelta

CONFIG_PATH = "/etc/monitord/config.conf"
LOG_FILE = "/var/log/monitord/monitord.log"

state = {"running": True, "config": {}, "last_alerts": {}}

def load_config():
    new_config = {}
    try:
        with open(CONFIG_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"): continue
                key, value = line.split("=")
                new_config[key.strip()] = value.strip()
        
        new_config['intervalo_segundos'] = int(new_config.get('intervalo_segundos', 60))
        new_config['umbral_cpu'] = int(new_config.get('umbral_cpu', 90))
        new_config['umbral_mem'] = int(new_config.get('umbral_mem', 90))
        new_config['umbral_disco'] = int(new_config.get('umbral_disco', 90))
        new_config['cooldown_minutos'] = int(new_config.get('cooldown_minutos', 30))
        new_config['particion_disco'] = new_config.get('particion_disco', '/')
        
        state["config"] = new_config
        logging.info("Configuración cargada/recargada.")
    except Exception as e:
        logging.error(f"Error en configuración: {e}")

def handle_signals(signum, frame):
    if signum == signal.SIGHUP:
        load_config()
    else:
        state["running"] = False

def send_alert(message, alert_type):
    now = datetime.now()
    last_sent = state["last_alerts"].get(alert_type)
    cooldown = timedelta(minutes=state["config"]["cooldown_minutos"])

    if last_sent and (now - last_sent) < cooldown:
        return 

    logging.warning(f"ALERTA: {message}")
    os.system(f'echo "Monitord ALERT: {message}" | wall')
    state["last_alerts"][alert_type] = now

def main():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

    signal.signal(signal.SIGHUP, handle_signals)
    signal.signal(signal.SIGTERM, handle_signals)
    signal.signal(signal.SIGINT, handle_signals)

    load_config()
    logging.info("Servicio Monitord Iniciado.")

    while state["running"]:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disco = psutil.disk_usage(state["config"]["particion_disco"]).percent

        logging.info(f"STATUS - CPU: {cpu}%, Mem: {mem}%, Disco: {disco}%")

        conf = state["config"]
        if cpu > conf["umbral_cpu"]: send_alert(f"CPU al {cpu}%", "cpu")
        if mem > conf["umbral_mem"]: send_alert(f"Memoria al {mem}%", "mem")
        if disco > conf["umbral_disco"]: send_alert(f"Disco al {disco}%", "disco")

        time.sleep(conf["intervalo_segundos"])

if __name__ == "__main__":
    main()
