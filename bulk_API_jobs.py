import tqdm
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from data_dev_jobs import DATA
from mappings_job import MAPPINGS

DATASET_PATH = "./data_dev.py"


def generate_actions(operationType, index):
    for doc in DATA:
        Id = doc['id']
        doc['applied'] = []
        doc['shortlisted'] = []
        doc['interviewScheduled'] = []
        doc['interviewCompleted'] = []
        doc['selected'] = []
        doc['rejected'] = []
        doc['offerReleased'] = []
        doc['candidateJoined'] = []
        newDoc = {
            '_op_type': operationType,
            '_index': index,
            '_id': Id,
            '_source': doc
        }
        yield newDoc


def create_index(client, index):
    client.indices.create(
        index=index,
        body=MAPPINGS
    )


def main():
    number_of_docs = len(DATA)
    INDEX = "job_docs_dev"
    OPERATION_TYPE = 'index'

    client = Elasticsearch(
        'localhost',
        http_auth=('elastic', 'password'),
        port=9200,
    )

    if (client.indices.exists(index=INDEX) == False):
        create_index(client, INDEX)

    progress = tqdm.tqdm(unit="docs", total=number_of_docs)
    successes = 0
    for ok, action in streaming_bulk(
        client=client, index=INDEX, actions=generate_actions(operationType=OPERATION_TYPE, index=INDEX),
    ):
        progress.update(1)
        successes += ok
    print("Indexed %d/%d documents" % (successes, number_of_docs))


if __name__ == "__main__":
    main()
