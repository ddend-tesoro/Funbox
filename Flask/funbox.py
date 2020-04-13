from flask import Flask, jsonify, request, abort
import re, redis, json,  time

app = Flask(__name__)




def insert_into_redis(s1, s2):
    r = redis.Redis(host='redis', port=6379)
    r.set(s1, json.dumps(s2))
    r.bgsave()


def retrive_from_redis(k):
    r = redis.Redis(host='redis', port=6379)
    return json.loads(r.get(k))


# функция которая вырезает домен из строки запроса
def parse_links(s):
    pattern = re.compile(r'(?:www\.)*((?:[\w]+\.)+\w+)/*')
    return pattern.findall(s)


n = 0


@app.route('/visited_links', methods=['POST'])
def visited_links():
    if not request.json:
        abort(400)
    last_links = {
        'links': request.json['links'],
        'time': str(int(time.time()))
    }
    global n
    k = 'links ' + str(n)
    n += 1
    insert_into_redis(k, last_links)
    return {
        'status': 'ok'
    }


@app.route('/visited_domains', methods=['GET'])
def visited_domain():
    r = redis.Redis('redis', 6379)
    start = int(request.args.get('from'))
    end = int(request.args.get('to'))
    result = {}
    j = 0
    for i in r.scan_iter():
        tm = json.loads(r.get(i)).get('time')
        if end >= int(tm) >= start:
            result[r.keys()[j].decode('utf-8')] = [parse_links(k)[0] for k in json.loads(r.get(i))['links']]
            j += 1
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
