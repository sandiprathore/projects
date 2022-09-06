<h2 style="text-align:center;">DMart Data Transformation Pipeline</h2>

![image](https://user-images.githubusercontent.com/93520937/188064662-02186b61-590e-4a9e-98c9-e43e05835d5d.png)


**Introduction:** DMart is a one-stop supermarket chain that aims to offer customers a wide range of basic home and personal products under one roof. Each DMart store stocks home utility products - including food, toiletries, beauty products, garments, kitchenware, bed and bath linen, home appliances, and more - available at competitive prices that our customers appreciate. Our core objective is to offer customers good products at a great value. 

"dmart_data_transformation" pipeline for analyzing DMart raw data and categorizing it into branded and generic products.

##### Prerequisite:
* airflow 2.2.3
* MongoDB access URL
* slack connection URL 


**Download DMart raw data and insert it in mongo collection**


Goto: create account on <a href = "https://www.kaggle.com/">kaggle.com</a>  and generate api_token

Dataset name: DMart Products
 
Dataset URL: https://www.kaggle.com/datasets/chinmayshanbhag/dmart-products 

you can use this script to <a href = "https://github.com/sandiprathore/projects/blob/dev/scripts/download_kaggle_data.py">download dataset</a> 




**File structure of the dag:**

    dmart_data_transformation
                         ├──utilities
                         |         ├── mongo_utils.py
                         |         ├── slack_utils.py  
                         |         ├── tasks.py  
                         |         ├── transformation.py
                         └──data_transformation_dag.py
**Dag structure**
![image](https://user-images.githubusercontent.com/93520937/187752047-b734547f-735b-4d6a-ae99-b22755236028.png)

**Set up the dag:**


**Step 1:** Download the <a href = "https://github.com/sandiprathore/projects/tree/dev">"dmart_data_transformation"</a> directory and add it to the airflow dags directory

**Step 2:** Add a new slack connection
* Goto Admin->connection
![Capture](https://user-images.githubusercontent.com/93520937/188052176-f275b810-66cc-436d-b7c3-b02721953b2c.PNG)
</br>

* click on the plus icon to add a new connection 
![Capture_2](https://user-images.githubusercontent.com/93520937/188052245-2279e896-06fb-45b5-8776-b8efcce534b4.PNG)
</br>

* add connection 
![image](https://user-images.githubusercontent.com/93520937/188053774-ba5f66de-75da-4dfd-a651-f6b253eb075a.png)

**Step 3:** Add MongoDB access URL in airflow variable 

* Goto Admin-> variables 
![image](https://user-images.githubusercontent.com/93520937/188054026-9526e207-7bb2-4648-8960-65c96825c64e.png)
</br>

* click on the plus icon to add a new variable 
![image](https://user-images.githubusercontent.com/93520937/188054124-25057327-54ff-4937-81ef-b3e7b8c9f73e.png)
</br>

* add variable 
![image](https://user-images.githubusercontent.com/93520937/188054264-06553302-9d20-4e0a-b1dd-3ed8db3531ef.png)


**To run the dag:** 
Run the dag with the configuration 
```JSON
{
    "DB_NAME": "<name_of_database>",
    "DMART_ALL_DATA_COL_NAME": "<raw_data_col_name>", 
    "GENERIC_PRODUCTS_COL_NAME": "<generic_pro_col_name>",
    "BRANDED_PRODUCTS_COL_NAME": "<branded_pro_col_name>"
}
```