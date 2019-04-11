import redis
import time
import json
a={
  "uid": 76546,
   "userName":  "\u58a8\u5c0f\u96e8",
   "sex":  "\u4fdd\u5bc6",
   "level":  5,
   "sign":  "\u56e0\u4e3a\u6635\u79f0\u5df2\u88ab\u5360\u7528\u6240\u4ee5 \u6211\u5c31\u662f\u54af\u5623\u5566~",
   "vip":  2,
   "follow":  43,
   "fans":  0
}
b=json.dumps(a)
c=b.encode()
print(json.loads(c))

