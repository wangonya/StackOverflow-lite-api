from flask import request, abort, jsonify, Blueprint

questions = Blueprint('questions', __name__)
qs = []


@questions.route('/api/v1/questions', methods=['POST'])
def post_question():
    # make sure there's data and its properly formatted
    if None or not request.json:
        abort(400)

    title = request.json['title']
    body = request.json['body']
    
    if 2 > len(title) or 15 < len(title):
        return jsonify({'msg': 'title length invalid'}), 400
    elif 20 > len(body):
        return jsonify({'msg': 'body length invalid'}), 400
    else:
        try:
            q_id = qs[-1]['id'] + 1
        except IndexError:
            q_id = 1
        question = {
            'id': q_id,
            'title': title,
            'body': body
        }
        qs.append(question)
        return jsonify({'question': question}), 201
