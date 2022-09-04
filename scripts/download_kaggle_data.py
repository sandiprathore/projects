# Add packages
import os

# All required credentials
KAGGLE_USERNAME = "<your_kaggle_user_name>"   
KAGGLE_KEY = "<your_kaggle_api_key>"          #key for authenticating with the Kaggle API.
KAGGLE_DATASET_NAME = "<name_of_datset>"
KAGGLE_DATASET_URL = "<kaggle_dataset_url>"


os.environ[KAGGLE_USERNAME]
os.environ[KAGGLE_KEY]
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_url, dataset_name):
    """Download dataset from kaggle.
    Parameters
    ----------
    dataset_url: str:
        The URL of the Kaggle dataset 
    dataset_name: str:
        The name of the dataset you want to download.
    """
    # the dataset name is derived from the dataset URL 
    derived_dataset_name = "/".join(dataset_url.split("/")[-2:])
    
    # authentication
    api = KaggleApi()
    api.authenticate()
    datasets=api.dataset_list(search=dataset_name,license_name='cc', file_type='csv')
    if datasets:
        for dataset in datasets:
            if derived_dataset_name == str(dataset):
                api.dataset_download_files(str(dataset), path='./', unzip=True)

# Download dmart dataset from kaggle           
download_dataset(KAGGLE_DATASET_URL, KAGGLE_DATASET_NAME)
