import threading
import time


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 通过args元祖传参
    sing_t = threading.Thread(target=sing, args=("唱歌",))
    # 通过字典传参
    dance_t = threading.Thread(target=dance, kwargs={"msg": "跳舞"})
    sing_t.start()
    dance_t.start()
