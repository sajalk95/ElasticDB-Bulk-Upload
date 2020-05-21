false = False

MAPPINGS = {
    "settings": {
        "number_of_shards": 1,
        "index": {
            "analysis": {
                "analyzer": {
                    "edge_ngram_analyzer": {
                        "tokenizer": "edge_ngram_tokenizer",
                        "filter": [
                            "lowercase",
                            "apostrophe"
                        ],
                        "char_filter": [
                            "html_strip"
                        ]
                    },
                    "raw_analyzer" : {
                        "tokenizer" : "keyword",
                        "filter": [
                            "lowercase",
                            "apostrophe"
                        ],
                        "char_filter": [
                            "html_strip"
                        ]
                    }
                  },
                "tokenizer": {
                    "edge_ngram_tokenizer": {
                        "type": "edge_ngram",
                        "min_gram": 2,
                        "max_gram": 20,
                        "token_chars": [
                            "letter",
                            "digit"
                        ]
                    }
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "area": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
                "fields": {
                    "standard": {
                        "type": "text",
                        "analyzer" : "standard"
                    },
                    "raw" : {
                        "type" : "text",
                        "analyzer" : "raw_analyzer"
                    }
                }
            },
            "district": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
                "fields": {
                    "standard": {
                        "type": "text",
                        "analyzer" : "standard"
                    },
                    "raw" : {
                        "type" : "text",
                        "analyzer" : "raw_analyzer"
                    }
                }
            },
            "district_id": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "id": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "pincode": {
                "type": "text"
            },
            "state": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
                "fields": {
                    "standard": {
                        "type": "text",
                        "analyzer" : "standard"
                    },
                    "raw" : {
                        "type" : "text",
                        "analyzer" : "raw_analyzer"
                    }
                }
            },
            "state_id": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            }
        }
    }
}