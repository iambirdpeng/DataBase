import redis

r = redis.StrictRedis(host='192.168.3.11', port='6379')
pipe = r.pipeline()
pipe.get('py11')
m = pipe.execute()
print(m)