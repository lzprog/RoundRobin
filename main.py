from tarefas import Tasks
from escalonador import Scheduler
from multiprocessing import Process

def main():

    task = Tasks()
    p1 = Process(target=task.sum)
    p2 = Process(target=task.check)
    p3 = Process(target=task.walk)
    p4 = Process(target=task.stay)
    process_list = [p1, p2, p3, p4]
    Scheduler(process_list)



if __name__=="__main__":
    main()