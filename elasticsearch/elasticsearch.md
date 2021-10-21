# elasticsearch 笔记

## filter

```json
{
    "size": 0,
    "query": {
        "bool": {
            "filter": [
                {
                    "term": {
                        "host.keyword": "dispatch.api.huitouche.io"
                    }
                },
                {
                    "bool": {
                        "should": [
                            {
                                "prefix": {
                                    "path.keyword": {
                                        "value": "/nearby?"
                                    }
                                }
                            },
                            {
                                "prefix": {
                                    "path.keyword": {
                                        "value": "/backhaul?"
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    },
    "aggregations": {
        "request_count": {
            "terms": {
                "field": "deviceId.keyword",
                "size": 1000
            }
        }
    }
}
```
