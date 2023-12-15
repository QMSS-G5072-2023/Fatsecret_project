from final_project_for_mds import final_project_for_mds
import pandas as pd
api_key = 'api_key'
api_secret = 'api_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'
client = YourApiClient(api_key, api_secret, access_token, access_token_secret)
selected_category_id = '1'  
food_sub_categories_result = client.get_food_sub_categories(selected_category_id)
print(f'Food Sub Categories for Category {selected_category_id}:')
print(food_sub_categories_result)