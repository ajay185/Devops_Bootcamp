from flask import Flask, render_template, request, jsonify

import uuid

# create flask app
app = Flask(__name__)

# configure pusher object

# index route, shows index.html view
@app.route('/')
def index():
    return render_template('index.html')

# feed route, shows feed.html view
@app.route('/feed')
def feed():
    return render_template('feed.html')

# store post
@app.route('/post', methods=['POST'])
def addPost():
    data = {
        'id': "post-{}".format(uuid.uuid4().hex),
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'status': 'active',
        'event_name': 'created'
    }
    return jsonify(data)


@app.route('/post/<id>', methods=['PUT', 'DELETE'])
def updatePost(id):
    data = {'id': id}
    if request.method == 'DELETE':
        data['event_name'] = 'deleted'
    else:
        data['event_name'] = 'deactivated'
    return jsonify(data)

app.run(debug=True)
