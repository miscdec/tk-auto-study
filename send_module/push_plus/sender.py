import requests
import json
import datetime

send_sess = requests.session()
send_key = ""


def set_key(key):
    global send_key
    send_key = key


def send(title, content) -> dict:
    content.replace("\n", "\n\n")
    
    data = {
	    "token":f"{send_key}",
	    "title":f"{title} {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f UTC')}",
	    "content":f"# {title}\n\n{content}",
            "template":"markdown"
            }
    body=json.dumps(data).encode(encoding='utf-8')
    push_headers = {'Content-Type':'application/json'}
    resp = send_sess.post(url=f"http://www.pushplus.plus/send",data=body,headers=push_headers )
    send_res = resp.json()
    success = send_res['code'] == 200
    print(success)
    return {
        'success': success,
        'message': send_res['msg'] if not success else '发送成功'
    }

