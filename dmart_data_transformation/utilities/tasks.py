def process_runtime_parameters(**kwargs: dict):
    """
    if runtime parameters passed overwrite the default parameters  
    parameters
    ----------
    runtime_conf: dict
        runtime configuration
    
    return 
    ----------
        if the correct parameters hase passed then return 'run_example_notebook'
        else return 'wrong_parameters' 
    """
    ti = kwargs['ti']
    DAG_PARAMETERS = {
        "DB_NAME": "",
        "DMART_ALL_DATA_COL_NAME": "", 
        "GENERIC_PRODUCTS_COL_NAME": "",
        "BRANDED_PRODUCTS_COL_NAME": ""
     }

    runtime_configuration = kwargs['dag_run'].conf
    if runtime_configuration:
        if ("DB_NAME" and 
            "DMART_ALL_DATA_COL_NAME" and 
            "GENERIC_PRODUCTS_COL_NAME" and
            "BRANDED_PRODUCTS_COL_NAME" in  runtime_configuration.keys()
            ):
            if (runtime_configuration["DB_NAME"] and 
                runtime_configuration["DMART_ALL_DATA_COL_NAME"] and
                runtime_configuration["GENERIC_PRODUCTS_COL_NAME"] and
                runtime_configuration["BRANDED_PRODUCTS_COL_NAME"]
                ):
                for key in runtime_configuration.keys():
                    if key in DAG_PARAMETERS.keys():
                        DAG_PARAMETERS[key] = runtime_configuration[key]
                ti.xcom_push(key = "DAG_PARAMETERS", value = DAG_PARAMETERS) 
                # for key in DAG_PARAMETERS.keys():
                #     ti.xcom_push(key=key, value=DAG_PARAMETERS.get(key))
                #     print(key)
                # pushing params to xcom 
                return 'transformation_and_load_data'

    print('INFO: Function: "process_runtime_parameters": Something wrong in runtime parameters please verify the parameters')
    return 'wrong_parameters'


def transformation_and_load_data(**kwargs: dict):
    """
    parameters
    ----------
    kwargs: airflow DagRun Context.
    """
    from dmart_data_transformation.utilities.transformation import dmart_data_transformation
    ti = kwargs['ti']
    # runtime_parameters = ti.xcom_pull(key='DAG_PARAMETERS', task_ids='process_run_time_parameters')
    runtime_parameters=ti.xcom_pull(task_ids='process_runtime_parameters', key='DAG_PARAMETERS')
    print(runtime_parameters)
    db_name = runtime_parameters["DB_NAME"]
    dmart_all_data_col_name = runtime_parameters["DMART_ALL_DATA_COL_NAME"]
    generic_products_col_name = runtime_parameters["GENERIC_PRODUCTS_COL_NAME"]
    branded_products_col_name = runtime_parameters["BRANDED_PRODUCTS_COL_NAME"]
    print( 
        db_name,
        dmart_all_data_col_name ,
        generic_products_col_name,
        branded_products_col_name)
    dmart_data_transformation( 
        db_name,
        dmart_all_data_col_name ,
        generic_products_col_name,
        branded_products_col_name)