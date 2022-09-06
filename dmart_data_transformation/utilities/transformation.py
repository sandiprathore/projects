def dmart_data_transformation(
    db_name: str,
    dmart_all_data_col_name : str,
    generic_products_col_name: str,
    branded_products_col_name: str):

    print( 
    db_name,
    dmart_all_data_col_name ,
    generic_products_col_name,
    branded_products_col_name)
    # import pandas as pd    
    # from dmart_data_transformation.utilities.mongo_utils import get_collection
    # # get dmart_all_data collection 
    # dmart_all_data_col = get_collection(
    #     db_name = db_name,
    #     collection_name = dmart_all_data_col_name
    # )
    
    # dmart_all_data_df = pd.DataFrame(list(dmart_all_data_col.find()))
    
    # # deleting products which have 0 price
    # dmart_all_data_df = dmart_all_data_df[dmart_all_data_df.Price != 0]
    # dmart_all_data_df = dmart_all_data_df[dmart_all_data_df.Price.notnull()]
    
    # # categorize other branded and generic products 
    # generic_products_df = dmart_all_data_df[pd.isnull(dmart_all_data_df['Brand'])]
    # branded_products_df = dmart_all_data_df[pd.notnull(dmart_all_data_df['Brand'])]
    
    # # short data based on prince 
    # shorted_generic_products_df = generic_products_df.sort_values(by='Price')
    # shorted_branded_products_df = branded_products_df.sort_values(by='Price')
    
    # # get dmart_all_data collection 
    # branded_products_col = get_collection(
    #     db_name = db_name,
    #     collection_name = branded_products_col_name
    # )
    
    # # get generic_product collection 
    # generic_products_col = get_collection(
    #     db_name = db_name,
    #     collection_name = generic_products_col_name
    # )
    
    # branded_products_col.insert_many(shorted_branded_products_df.to_dict('records'))
    # generic_products_col.insert_many(shorted_generic_products_df.to_dict('records'))