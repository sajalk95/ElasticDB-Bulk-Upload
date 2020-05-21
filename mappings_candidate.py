"""Contains the mapping structure."""
true = True
false = False

MAPPINGS = {
    "settings": {
        "number_of_shards": 1,
        "index": {
            "analysis": {
                "analyzer": {
                    "trim": {
                        "tokenizer": "keyword",
                        "filter": ["trim"]
                    },
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
                    "shingles": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "shingle",
                            "lowercase",
                            "apostrophe"
                        ]
                    },
                    "start_word_analyzer": {
                        "tokenizer": "keyword",
                        "filter": [
                            "lowercase",
                            "edge_ngram",
                            "apostrophe"
                        ]
                    },
                    "start_phrase_analyzer": {
                        "tokenizer": "start_phrase_tokenizer",
                        "filter": [
                            "lowercase",
                            "apostrophe",
                            "token_limit"
                        ]
                    }
                },
                "filter": {
                    "shingle": {
                        "type": "shingle",
                        "min_shingle_size": 2,
                        "max_shingle_size": 4
                    },
                    "stop_words": {
                        "type": "stop",
                        "stopwords": "_english_",
                        "remove_trailin": false
                    },
                    "token_limit": {
                        "type": "limit",
                        "max_token_count": 5
                    }
                },
                "tokenizer": {
                    "edge_ngram_tokenizer": {
                        "type": "edge_ngram",
                        "min_gram": 2,
                        "max_gram": 4,
                        "token_chars": [
                            "letter",
                            "digit"
                        ]
                    },
                    "start_phrase_tokenizer": {
                        "type": "path_hierarchy",
                        "delimiter": " "
                    }
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "id": {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    },
                    "trim": {
                        "type": "text",
                        "analyzer": "trim"
                    },
                    "standard": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "isActive": {
                "type": "boolean"
            },
            "firstName": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    },
                    "trim": {
                        "type": "text",
                        "analyzer": "trim"
                    },
                    "standard": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "lastName": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    },
                    "trim": {
                        "type": "text",
                        "analyzer": "trim"
                    },
                    "standard": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "applied" : {
                "type" : "text"
            },
            "selected" : {
                "type" : "text"
            },
            "mobile": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    },
                    "trim": {
                        "type": "text",
                        "analyzer": "trim"
                    },
                    "standard": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "email": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    },
                    "trim": {
                        "type": "text",
                        "analyzer": "trim"
                    },
                    "standard": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "locationArea": {
                "type": "nested",
                "properties": {
                    "id": {
                        "type": "text"
                    },
                    "name": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
                        "fields": {
                            "raw": {
                                "type": "keyword"
                            },
                            "trim": {
                                "type": "text",
                                "analyzer": "trim"
                            },
                            "standard": {
                                "type": "text",
                                "analyzer": "standard"
                            }
                        }
                    },
                    "pincode": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
                        "fields": {
                            "raw": {
                                "type": "keyword"
                            },
                            "trim": {
                                "type": "text",
                                "analyzer": "trim"
                            },
                            "standard": {
                                "type": "text",
                                "analyzer": "standard"
                            }
                        }
                    },
                    "locationDistrict": {
                        "type": "nested",
                        "properties": {
                            "id": {
                                "type": "text"
                            },
                            "name": {
                                "type": "text",
                                "analyzer": "edge_ngram_analyzer",
                                "fields": {
                                    "raw": {
                                        "type": "keyword"
                                    },
                                    "trim": {
                                        "type": "text",
                                        "analyzer": "trim"
                                    },
                                    "standard": {
                                        "type": "text",
                                        "analyzer": "standard"
                                    }
                                }
                            }
                        }
                    },
                    "locationState": {
                        "type": "nested",
                        "properties": {
                            "id": {
                                "type": "text"
                            },
                            "name": {
                                "type": "text",
                                "analyzer": "edge_ngram_analyzer",
                                "fields": {
                                    "raw": {
                                        "type": "keyword"
                                    },
                                    "trim": {
                                        "type": "text",
                                        "analyzer": "trim"
                                    },
                                    "standard": {
                                        "type": "text",
                                        "analyzer": "standard"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "preferredLocations": {
                "type": "nested",
                "dynamic": true,
                "properties": {
                    "id": {
                        "type": "text"
                    },
                    "name": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
                        "fields": {
                            "raw": {
                                "type": "keyword"
                            },
                            "trim": {
                                "type": "text",
                                "analyzer": "trim"
                            },
                            "standard": {
                                "type": "text",
                                "analyzer": "standard"
                            }
                        }
                    },
                    "pincode": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
                        "fields": {
                            "raw": {
                                "type": "keyword"
                            },
                            "trim": {
                                "type": "text",
                                "analyzer": "trim"
                            },
                            "standard": {
                                "type": "text",
                                "analyzer": "standard"
                            }
                        }
                    },
                    "locationDistrict": {
                        "type": "nested",
                        "properties": {
                            "id": {
                                "type": "text"
                            },
                            "name": {
                                "type": "text",
                                "analyzer": "edge_ngram_analyzer",
                                "fields": {
                                    "raw": {
                                        "type": "keyword"
                                    },
                                    "trim": {
                                        "type": "text",
                                        "analyzer": "trim"
                                    },
                                    "standard": {
                                        "type": "text",
                                        "analyzer": "standard"
                                    }
                                }
                            },
                            "locationState": {
                                "type": "nested",
                                "properties": {
                                    "id": {
                                        "type": "text"
                                    },
                                    "name": {
                                        "type": "text",
                                        "analyzer": "edge_ngram_analyzer",
                                        "fields": {
                                            "raw": {
                                                "type": "keyword"
                                            },
                                            "trim": {
                                                "type": "text",
                                                "analyzer": "trim"
                                            },
                                            "standard": {
                                                "type": "text",
                                                "analyzer": "standard"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "preferredJobCategories": {
                "type": "nested",
                "dynamic": true,
                "properties": {
                    "jobCategory": {
                        "type": "nested",
                        "properties": {
                            "name": {
                                "type": "text",
                                "analyzer": "edge_ngram_analyzer",
                                "fields": {
                                    "raw": {
                                        "type": "keyword"
                                    },
                                    "trim": {
                                        "type": "text",
                                        "analyzer": "trim"
                                    },
                                    "standard": {
                                        "type": "text",
                                        "analyzer": "standard"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "educationalDetails": {
                "type": "nested",
                "dynamic": true,
                "properties": {
                    "institutionName": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
                        "fields": {
                            "raw": {
                                "type": "keyword"
                            },
                            "trim": {
                                "type": "text",
                                "analyzer": "trim"
                            },
                            "standard": {
                                "type": "text",
                                "analyzer": "standard"
                            }
                        }
                    },
                    "educationLevel": {
                        "type": "nested",
                        "properties": {
                            "educationalBoards": {
                                "type": "nested",
                                "properties": {
                                    "name": {
                                        "type": "text",
                                        "analyzer": "edge_ngram_analyzer",
                                        "fields": {
                                            "raw": {
                                                "type": "keyword"
                                            },
                                            "trim": {
                                                "type": "text",
                                                "analyzer": "trim"
                                            },
                                            "standard": {
                                                "type": "text",
                                                "analyzer": "standard"
                                            }
                                        }
                                    }
                                }
                            },
                            "educationalDegrees": {
                                "type": "nested",
                                "properties": {
                                    "name": {
                                        "type": "text",
                                        "analyzer": "edge_ngram_analyzer",
                                        "fields": {
                                            "raw": {
                                                "type": "keyword"
                                            },
                                            "trim": {
                                                "type": "text",
                                                "analyzer": "trim"
                                            },
                                            "standard": {
                                                "type": "text",
                                                "analyzer": "standard"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "exploymentDetail": {
                "type": "nested",
                "dynamic": true,
                "properties": {
                    "noOfExpInMonths": {
                        "type": "integer",
                        "fields": {
                            "standard": {
                                "type": "text",
                                "analyzer": "standard"
                            },
                            "trim": {
                                "type": "text",
                                "analyzer": "trim"
                            },
                            "raw": {
                                "type": "keyword"
                            }
                        }
                    }
                }
            },
            "candidateScore": {
                "type": "integer",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    },
                    "trim": {
                        "type": "text",
                        "analyzer": "trim"
                    },
                    "standard": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            }
        }}}
