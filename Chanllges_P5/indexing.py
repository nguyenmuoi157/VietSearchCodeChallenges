import json
from elasticsearch import Elasticsearch, helpers


def indexing_data():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    with open('data/science.json', 'r', encoding='utf8') as fr:
        json_data = fr.read()
        data = json.loads(json_data)
        helpers.bulk(es, data, index='science_search', doc_type='data')


if __name__ == '__main__':
    indexing_data();
