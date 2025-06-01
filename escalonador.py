import time
import os
import signal
import logging

QUANTUM_TIME = 0.05  # 50 ms

# Logging simplificado: apenas INFO e mensagens curtas
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(message)s'  # Sem timestamp, sem nível
)


class Scheduler:
    def __init__(self, process_list):
        self.quantum = QUANTUM_TIME
        self.process_list = process_list
        self.exec(process_list)

    def exec(self, process_list):
        complete = []
        j = 0
        i = 0

        while i < len(process_list):
            if not process_list[i].is_alive():
                process_list[i].start()
                logging.info(f"Processo {process_list[i].pid} iniciado")

            time.sleep(self.quantum)
            if process_list[i].is_alive():
                os.kill(process_list[i].pid, signal.SIGSTOP)
                i = i + 1
            else:
                logging.info(f"Processo {process_list[i].pid} finalizado")
                complete.append(process_list[i])
                process_list.pop(i)

        while len(process_list) > 0:
            os.kill(process_list[j].pid, signal.SIGCONT)
            process_list[j].join(timeout=self.quantum)

            if process_list[j].is_alive():
                os.kill(process_list[j].pid, signal.SIGSTOP)
                j = (j + 1) % len(process_list)
            else:
                logging.info(f"Processo {process_list[j].pid} finalizado")
                complete.append(process_list[j])
                process_list.pop(j)
                if len(process_list) > 0:
                    j = j % len(process_list)

        logging.info("Todos os processos foram concluídos.")
        

