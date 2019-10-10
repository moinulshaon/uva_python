import sys
from collections import Counter
if __name__ == "__main__":
    for line in sys.stdin:
        counter = Counter([x for x in line if x.isalpha()])

        # print(counter)

        maxFreq = max(counter.values())
        # print(counter.keys())
        ans = [x for x in counter.keys() if counter.get(x) is maxFreq]
        ans.sort()

        print("".join(ans), maxFreq)