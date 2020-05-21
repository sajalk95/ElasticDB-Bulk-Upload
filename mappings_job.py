"""Contains the mapping structure."""

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
                "type": "text"
            },
            "applied": {
                "type": "text"
            },
            "shortlisted": {
                "type": "text"
            },
            "interviewScheduled": {
                "type": "text"
            },
            "interviewCompleted": {
                "type": "text"
            },
            "selected": {
                "type": "text"
            },
            "rejected": {
                "type": "text"
            },
            "offerReleased": {
                "type": "text"
            },
            "candidateJoined": {
                "type": "text"
            },
            "title": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
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
            },
            "type": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
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
            },
            "isActive": {
                "type": "boolean"
            },
            "jobExams": {
                "type": "nested",
                "properties": {
                    "weight": {
                        "type": "long"
                    },
                    "id": {
                        "type": "text"
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
                    },
                    "pincode": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
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
                    }
                }
            },
            "category": {
                "type": "nested",
                "properties": {
                    "id": {
                        "type": "text"
                    },
                    "name": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
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
            "educationLevel": {
                "type": "nested",
                "properties": {
                    "id": {
                        "type": "text"
                    },
                    "title": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
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
            "postedCompany": {
                "type": "nested",
                "properties": {
                    "id": {
                        "type": "text"
                    },
                    "name": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
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
            "jobDescrition": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
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
                    },
                    "shingles": {
                        "type": "text",
                        "analyzer": "shingles"
                    }
                }
            },
            "skillsRequired": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
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
            },
            "shiftType": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
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
            },
            "employmentLevel": {
                "type": "text",
                "analyzer": "edge_ngram_analyzer",
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
            },
            "minSalary": {
                "type": "long",
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
            },
            "maxSalary": {
                "type": "long",
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
            },
            "minExperienceInYear": {
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
            },
            "maxExperienceInYear": {
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
    }
}
