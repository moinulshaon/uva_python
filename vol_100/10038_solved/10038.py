import sys

if __name__ == "__main__":
    for line in sys.stdin:
        arr = [int(x) for x in line.split()][1:]
        # print(arr)
        n = len(arr)

        vis = set()
        for i in range(1,n):
            vis.add(abs(arr[i]-arr[i-1]))
        
        # print(n, vis)
        if len(list(filter(lambda x: x in vis, range(1,n)))) == n-1:
            print("Jolly")
        else:
            print("Not jolly")