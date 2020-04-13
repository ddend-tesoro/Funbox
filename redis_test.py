import redis, json, time

r = redis.Redis(host='redis', port=6379)
pattern = {
"links": [
"https://ya.ru",
"https://ya.ru?q=123",
"funbox.ru", "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
],
'time': str(int(time.time()))}

for i in range(10):
    ln = 'links' + str(i)
    r.set(ln, json.dumps(pattern))
    time.sleep(10)

r.bgsave()