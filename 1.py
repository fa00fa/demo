import multiprocessing
from multiprocessing import Process
from threading import Thread

def one(li,s):
    s.put(li[:3])
    # return li[:3]


def two(li,s):
    s.put(li[3:6])
    # return li[3:6]


def three(li,s):
    s.put(li[6:9])
    # return li[6:9]


def main():
    # 创建初始对象
    q = multiprocessing.Queue()
    a = [1, 2, 4, 2, 21, 2, 6, 4, 7, 9, 3, 2, 3, 5, 6, 3, 5, 4, 3]
    b=[]
    p1 = Process(target=one, args=(a,q))
    p2 = Process(target=two, args=(a,q))
    p3 = Process(target=three, args=(a,q))

    tasks = [p1,p2,p3]
    for t in tasks:
        b.append(t)
        t.daemon = True
        t.start()

    for t in tasks:
        t.join()
    results = [q.get() for j in b]
    print(results)


if __name__ == '__main__':
    main()

# import multiprocessing






# q = multiprocessing.Queue()
# jobs = []
# for i in range(10):
#     p = multiprocessing.Process(target=worker, args=(str(i), q))
#     jobs.append(p)
#     p.start()
#
# for p in jobs:
#     p.join()
#
# results = [q.get() for j in jobs]
# print(results)