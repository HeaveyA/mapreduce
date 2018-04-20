#!/usr/bin/env python
import sys

def mapper1():
    for line in sys.stdin:
        user_id, friends = line.split("\t")
        friend_ids = friends.split(",")
    
        for friend in friend_ids:
            yield (user_id + "," + friend, 0)
        for friend_i in friend_ids:
            for friend_j in friend_ids:
                if friend_i == friend_j:
                    continue
                yield (friend_i + "," + friend_j, 1)

def main():
    mapper1()
    sys.stdin = sys.__stdin__
if __name__ == "__main__":
    main()