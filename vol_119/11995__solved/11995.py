import sys
import queue

if __name__ == "__main__":
    for line in sys.stdin:
        op = int(line)
        stk = []
        q = queue.Queue()
        pq = queue.PriorityQueue()

        ans = [True, True, True]
        for _ in range(op):
            t, val = (int(x) for x in input().split())
            
            # print(t, val)
            if t == 1:
                stk.append(val)
                q.put(val)
                pq.put(-val)
            else:
                ans[0] = ans[0] and len(stk)>0 and stk.pop()==val
                ans[1] = ans[1] and not q.empty() and q.get()==val
                ans[2] = ans[2] and not pq.empty() and pq.get()==-val

        if int(ans[0]) + int(ans[1]) + int(ans[2]) == 0:
            print("impossible")
        elif int(ans[0]) + int(ans[1]) + int(ans[2]) > 1:
            print("not sure")
        elif ans[0]:
            print("stack")
        elif ans[1]:
            print("queue")
        else:
            print("priority queue")
