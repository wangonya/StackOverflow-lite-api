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
            'body': body,
            'by': 'test_user'
        }
        qs.append(question)
        return jsonify({'question': question}), 201


@questions.route('/api/v1/questions/<int:q_id>', methods=['DELETE'])
def delete_question(q_id):
    question = [q for q in qs if q['id'] == q_id]
    if len(question) == 0:
        return jsonify({'msg': 'question with id {} does not exist'.format(q_id)})
    qs.remove(question[0])
    return jsonify({'msg': 'question with id {} deleted successfully'.format(q_id)})
