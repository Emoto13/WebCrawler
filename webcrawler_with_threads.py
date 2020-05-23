from threading import Thread
from main import main


def main_threads():
    t1 = Thread(target=main)
    t2 = Thread(target=main)
    t3 = Thread(target=main)
    t4 = Thread(target=main)
    t5 = Thread(target=main)
    t6 = Thread(target=main)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()


if __name__ == '__main__':
    main_threads()
