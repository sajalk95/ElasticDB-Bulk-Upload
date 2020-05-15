import tqdm
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from data_dev import DATA
from mappings import MAPPINGS

DATASET_PATH = "./data_dev.py"


def generate_actions(operationType, index):
    for doc in DATA:
        Id = doc.pop('_id', None)
        newDoc = {
            '_op_type': operationType,
            '_index': index,
            '_id': Id,
            'doc': doc
        }
        yield newDoc


def create_index(client, index):
    client.indices.create(
        index=index,
        body=MAPPINGS
    )


def main():
    number_of_docs = len(DATA)
    index = "job-docs-bulktest"
    operationType = 'update'

    client = Elasticsearch(
        [{'host': 'localhost', 'port': 9200}]
    )

    if (client.indices.exists(index="job-docs-bulktest") != True):
        create_index(client, index)

    progress = tqdm.tqdm(unit="docs", total=number_of_docs)
    successes = 0
    for ok, action in streaming_bulk(
        client=client, index="job-docs-bulktest", actions=generate_actions(operationType=operationType, index=index),
    ):
        print(action)
        progress.update(1)
        successes += ok
    print("Indexed %d/%d documents" % (successes, number_of_docs))


if __name__ == "__main__":
    main()
