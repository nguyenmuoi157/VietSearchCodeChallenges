from flask import Flask
from flask import request
from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': 'localhost'}])
indexing = 'science_search'
doc_type = 'data'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'hello, world'


@app.route('/insert', methods=['POST'])
def insert():
    req = json.loads(request.data)
    if req["title"] is not None:
        post = {
            "title": req["title"],
            "content": req["content"],
            "published_date": req["published_date"]
        }
        result = es.index(index=indexing, doc_type='data', body=post)
        return result
    else:
        return {
            "err": True,
            "message": "Data is null"
        }


@app.route('/update', methods=['PUT'])
def update():
    req = json.loads(request.data)
    if req["ids"] is not None:
        post = {
            "title": req["title"],
            "content": req["content"],
            "published_date": req["published_date"]
        }
        result = es.update(indexing, doc_type="data", id=req["ids"], body=post)
        return result
    else:
        return {
            "err": True,
            "message": "Data is null"
        }


@app.route('/delete_one/<ids>', methods=['DELETE'])
def delete_one(ids):
    if ids is not None:
        query = {
            "query": {
                "match": {
                    "_id": ids
                }
            }
        }
        result = es.delete(indexing, doc_type=doc_type, body=query)
        return result
    else:
        return {
            "err": True,
            "message": "ids is null"
        }


@app.route('/delete_many', methods=['DELETE'])
def delete_many():
    req = json.loads(request.data)
    if len(req) <= 0:
        for ids in req:
            query = {
                "query": {
                    "match": {
                        "_id": ids
                    }
                }
            }
            es.delete_by_query(indexing, query)
        return {
            "err": False,
            "message": "Success"
        }


@app.route('/get_by_id_one/<ids>', methods=['GET'])
def get_by_id_one(ids):
    if ids is None:
        return {
            "err": True,
            "message": "ids is null"
        }
    query = {
        "query": {
            "match": {
                "_id": ids
            }
        }
    }
    result = es.search(indexing, query)
    return result


@app.route('/get_by_id_many', methods=['POST'])
def get_by_id_many():
    req = json.loads(request.data)
    result = []
    if len(req) <= 0:
        return {
            "err": True,
            "message": "ids is null"
        }
    for ids in req:
        query = {
            "query": {
                "match": {
                    "_id": ids
                }
            }
        }
        res = es.search(indexing, query)
        if len(result["hits"]["hits"] > 0):
            result.append(res)
    return result


@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('q')
    if keyword is None:
        query = {
            "query": {
                "match_all": {}
            }
        }
    else:
        query = {
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ["_id", "content", "title", "published_date"]
                }
            }
        }

    result = es.search(indexing, query)
    return result


if __name__ == "__main__":
    app.run()
