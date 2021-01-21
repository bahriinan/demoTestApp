import requests
from flask import Flask, jsonify, Response, abort, request, url_for
import json

from werkzeug.utils import redirect

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


book = {}


def get_dict(incoming_id):
    temp={}
    count=0
    keep=0
    size = len(book.keys())
    for key in book:
        keep+=1
        if book[key] == incoming_id:
            for keep in range(size):
                temp.update({key:book[key]})
    return temp


def id_checker(incoming_id):
    check_id = incoming_id in book.values()
    if check_id:
        return True
    # End of If Statement
    return False
# End Of Definition


def check_field(incoming_json):
    check_author = 'Author' in incoming_json
    check_title = 'Title' in incoming_json
    if check_author and check_title:
        return "pass"
    elif not check_title and not check_author:
        return "Author and Title"
    elif not check_author:
        return "Author"
    else:
        return "Title"
    # End Of If Statement
# End Of Definition


def check_value(incoming_json):
    if not incoming_json['Author'] and not incoming_json['Title']:
        return "Author and Title"
    elif not incoming_json['Title']:
        return "Title"
    elif not incoming_json['Author']:
        return "Author"
    else:
        return "pass"
    # End Of If Statement
# End Of Definition


def book_checker(book_author, book_title):
    check_author = book_author in book.values()
    check_title = book_title in book.values()
    if check_title and check_author:
        return "Same Author and Same Title Exist"
    return "pass"
# End Of Definition


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
# End Of Definition


@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400
# End Of Definition


@app.route("/api/books/", methods=['GET', 'PUT'])
def get_all_or_add():
    counter = 1
    if request.method == 'GET':
        return Response(json.dumps(book), mimetype='application/json')
    elif request.method == 'PUT':
        content = request.get_json()
        key_handler = check_field(content)
        if key_handler != "pass":
            print("2.test", key_handler)
            abort(400, description=str(key_handler) + " is required")
        # End Of If Statement
        value_handler = check_value(content)
        if value_handler != "pass":
            print("3.test", value_handler)
            abort(400, description=str(value_handler) + " cannot be empty")
        # End Of If Statement
        name_getter = str(content['Author'])
        title_getter = str(content['Title'])
        if not book:
            book.update(Id=counter)
            book.update(content)
            counter += 1
            return Response(mimetype='application/json')
        # End Of If Statement
        book_check = book_checker(name_getter, title_getter)
        if book_check != 'pass':
            print("5.test", book_check)
            abort(400, description=book_check)
        # End Of Definition
        else:
            book.update(Id=counter)
            book.update(content)
            counter += 1
            # req = requests.get(get_book(book.get('Id')))
            # return Response(json.dumps(req.json()), mimetype='application/json')
        # End Of If Statement
    else:
        abort(400, description="Method is not allowed")
    # End Of If Statement
# End Of Definition


@app.route("/api/books/<int:saved_Id>", methods=['GET'])
def get_book(saved_Id):
    flag = id_checker(saved_Id)
    if flag:
        return Response(json.dumps(get_dict(saved_Id)), mimetype='application/json')
    else:
        abort(404, description="Id " + str(saved_Id) + " cannot be found")
    # End Of If Statement
# End Of Definition


if __name__ == '__main__':
    app.run()
