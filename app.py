# comment_service.py

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

comments = {
   '1' : { 'user_id' : '1', 'post_id' : '2', 'comments' : 'Amazing Post' },
   '2' : { 'user_id' : '2', 'post_id' : '2', 'comments' : 'I did not know that' },
}

USER_SERVICE_URL = 'https://abhishekuserservice.agreeablewater-91d2a3ce.canadacentral.azurecontainerapps.io'
POST_SERVICE_URL = 'https://abhishekpostservice.agreeablewater-91d2a3ce.canadacentral.azurecontainerapps.io'

@app.route('/')
def hello():
    return 'Comment serive is live!'

#retrive comment_service

@app.route('/comments/', methods=["GET"])
def get_comment():
 return jsonify(comments)


@app.route('/comments/<id>', methods=["GET"])
def get_comment(id):
 comment_info = comments.get(id,{})
 return jsonify(comment_info)

# delete comment_service

@app.route('/comments/<id>', methods=["DELETE"])
def delete_comment(id):
    try: 
       
        delete_comment = comments.pop(id)
        return jsonify({"result": "Comment deleted", "delete_comment": delete_comment})
    except KeyError:
        return jsonify({"error":"Comment not found"}), 404

# update comment_service

@app.route('/comments/<id>', methods=["PUT"])
def update_comment(id):
   
   if id in comments:
    updated_comment = request.get_json()
    comments[id].update(updated_comment)
    return jsonify({"message": "Comment updated", "updated_comment": comments[id]})
   else: 
     return jsonify({"error": "Comment not found"}), 404

# create comment_service

@app.route('/comments/<id>', methods=["POST"])
def create_comment():
    
    new_comment = request.get_json()
    id = str(len(comments) + 1)
    comments[id] = new_comment
    new_comment["id"] = id
    return jsonify({"message": "Comment created", "new_comment": new_comment}), 201

if __name__ == '_main_':
 app.run(port=5002)