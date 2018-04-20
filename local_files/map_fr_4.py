#!/usr/bin/env python
import sys

for line in sys.stdin:
    user_id, friends = line.split("\t")
    friend_ids = friends.split(",")
    
    for friend in friend_ids:
        print (user_id + "," + friend, 0)
    for friend_i in friend_ids:
        for friend_j in friend_ids:
            if friend_i == friend_j:
                continue
            print '%s,%s\t%s' % (friend_i,friend_j, "1")