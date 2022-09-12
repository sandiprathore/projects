

def get_mongo_url():

    from airflow.models import Variable
    print("RUNTIME: get_mongo_url")
    mongo_url = Variable.get("mongodb_ver", deserialize_json=False)
    return mongo_url


def get_collection(
        db_name: str,
        collection_name: str):
    print("RUNTIME: get_collection")
    """ Get a mongodb collection to write.
    Args:
    :param db_name:(str,optional): [description]07. Defaults to None.
    :param collection_name: (str,optional): [description]. Defaults to None.
    :param mongo_url: (str,optional): [description]. Defaults to None.
    
    Returns:
        pymongo.collection.Collection: [description]
    
    """
    import pymongo
    
    mongo_url = get_mongo_url()
    client = pymongo.MongoClient(mongo_url)
    db = client[db_name]
    collection = db[collection_name]
    return collection