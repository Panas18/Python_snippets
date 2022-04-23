from flask import Flask, request, make_response
import redis
import string
import random

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)


def get_id():
    user_id =  request.cookies.get("id",0)
    if user_id == 0:
        id_chars= string.ascii_letters + string.punctuation + string.digits
        user_id= ''.join(random.choice(id_chars) for i in range(8))
    return user_id


def get_visit(user_id):
    if r.exists(user_id):
        r.incr(user_id)
    else:
        r.set(user_id, 1)

    return r.get(user_id)
   


@app.route('/')
def index(): 
    user_id = get_id()
    visit = get_visit(user_id).decode()
    message = f"<h1 align = center >you visited {visit} times</h1>"
    response = make_response(message)
    response.set_cookie("id", user_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)