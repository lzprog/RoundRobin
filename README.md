# Round Robin Scheduler

Simulação de um escalonador de processos baseado no algoritmo **Round Robin**, utilizando **Python** e **multiprocessamento**.

## Estrutura do Projeto

###  Classe `Tasks`
Representa as tarefas que serão escalonadas.  
- Possui um contador que incrementa a cada novo processo iniciado (mais por fins ilustrativos).
- Contém métodos como:
  - `walk()`
  - `stay()`
  - `check()`
  - `sum()`

Esses métodos simulam diferentes comportamentos de uso de CPU, como cálculos, operações com vetores ou loops de espera para consumir tempo de CPU.

###  Classe `Scheduler`
Responsável pela lógica do **escalonador Round Robin**.
- Inicializada com a lista de processos gerados no `main`.
- O tempo de quantum é definido por uma variável global (`quantum_time`), facilmente ajustável pelo usuário.
- O método `exec()` realiza o controle Round Robin da seguinte forma:
  1. Inicializa todos os processos com `.start()`, atribuindo o tempo de quantum.
  2. Após iniciar todos, entra em um loop onde:
     - Retoma o processo atual com `SIGCONT`.
     - Aguarda com `join(timeout=quantum)` — que só espera até o quantum ou até o processo terminar (otimizando o tempo de execução).
     - Pausa o processo com `SIGSTOP`.
     - Verifica se ainda está vivo com `.is_alive()`.
     - Processos finalizados são adicionados a uma lista de concluídos, que é exibida ao final.

### Execução
Basta executar o arquivo principal:

```bash
python3 main.py
