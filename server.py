from flask import Flask, request, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def api_gh_pr():
    if request.headers['Content-Type'] == 'application/json':
        pull_req = json.dumps(request.json['pull_request'])
        return pull_req

if __name__ == '__main__':
    app.run(debug=True)

