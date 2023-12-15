def is_prime(n):
    """
    Purpose
    ----------
    I create this python package for users to easily use FatSecret function. 
    Firstly, users can search for food brands when they feel it hard to decide which restruants to go to. The brand type includes "manufacturer", "restaurant" and "supermarket", and users can choose either one they want. 
    Secondly, the food categories category will make users to easier find a category for a food. They can use this function to know whether they may allergy to this food (by trace its categoy), and to know what kind of fodd they ate (this will be very efficient for users who want to balance the categories of foods they eat daily). 
    Thirdly, food sub categories will work in a similar way as the second one, but it classfied food more detaily. 
    Forthly, users can add favorite recipe, delete receipe and get all favorites in recipe by using this package. 
    The last one will give all supported recipe type names for users, which make it easier for them to make personal menu.
    
    Inputs 
    ------
    Boolean, Decimal, Int, Long, String
    
    Outputs
    -------
    Boolean, Decimal, Int, Long, String
    """
### 1） Food brands
#### Get brand by letter
def get_brands_by_letter(self, letter, brand_type='manufacturer', region=None, language=None, format='json'):
        endpoint = f'{self.base_url}?method=food_brands.get.v2&starts_with={letter}&brand_type={brand_type}'
        
        if region:
            endpoint += f'&region={region}'
        if language:
            endpoint += f'&language={language}'
        if format:
            endpoint += f'&format={format}'

        response = self.oauth.get(endpoint)
        response.raise_for_status()
        result = response.json()
        return result
### 2) Food categories
#### 2.1 Search food
import requests
from requests_oauthlib import OAuth1
class FatSecretApiClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://platform.fatsecret.com/rest/server.api'
        self.oauth = OAuth1(self.api_key, self.api_secret)

    def search_food(self, food_name):
        endpoint = f'{self.base_url}?method=foods.search&format=json&search_expression={food_name}'
        response = requests.get(endpoint, auth=self.oauth)
        response.raise_for_status()
        result = response.json()
        return result
#### 2.2 Get food¶
def get_food(self, food_id):
        endpoint = f'{self.base_url}?method=food.get&food_id={food_id}'
        response = requests.get(endpoint, auth=self.oauth)
        response.raise_for_status()
        result = response.json()
        return result
#### 2.3 Get meal¶
def get_meal(self, meal_type):
        endpoint = f'{self.base_url}?method=meal.get_meals&format=json&meal_type={meal_type}'
        response = requests.get(endpoint, auth=self.oauth)
        response.raise_for_status()
        result = response.json()
        return result
#### 2.4 Get food by category¶
def get_food_by_category(self, category_id, format='json'):
        endpoint = f'{self.base_url}?method=food.get&food_category_id={category_id}&format={format}'
        response = self.oauth.get(endpoint)

        response.raise_for_status()
        result = response.json()
        return result.get('food_entries', {}).get('food_entry', [])
#### 2.5 Create meals¶
def create_meal(self, saved_meal_name, saved_meal_description=None, meals=None, format='json'):
        endpoint = f'{self.base_url}?method=saved_meal.create&format={format}'
        data = {'saved_meal_name': saved_meal_name}
        if saved_meal_description:
            data['saved_meal_description'] = saved_meal_description
        if meals:
            data['meals'] = meals

        response = self.oauth.post(endpoint, data=data)
        response.raise_for_status()
        result = response.json()
        return result
### 3) Food subcategories¶
def get_food_sub_categories(self, food_category_id, format='json'):
        endpoint = f'{self.base_url}?method=food_sub_categories.get.v2&food_category_id={food_category_id}&format={format}'
        response = self.oauth.get(endpoint)
        response.raise_for_status()
        result = response.json()
        return result.get('food_sub_categories', {}).get('food_sub_category', [])
### 4) Recipes
#### 4.1 Add favorite recipes
def add_favorite_recipe(self, recipe_id, format='json'):
    endpoint = f'{self.base_url}?method=recipe.add_favorite&recipe_id={recipe_id}&format={format}'
    response = self.oauth.get(endpoint)
        
    response.raise_for_status()

    result = response.json()
    return result
#### 4.2 Delete receipe
def delete_favorite_recipe(self, recipe_id, format='json'):
    endpoint = f'{self.base_url}?method=recipe.delete_favorite&recipe_id={recipe_id}&format={format}'
    response = self.oauth.get(endpoint)
        
    response.raise_for_status()

    result = response.json()
    return result
#### 4.3 Get all favorites¶
def get_all_favorites(self, format='json'):
        endpoint = f'{self.base_url}?method=recipes.get_favorites&format={format}'
        response = self.oauth.get(endpoint)
        
        response.raise_for_status()

        result = response.json()
        return result
### 5） Recipe types¶
def get_recipe_types(self, format='json', region=None, language=None):
        endpoint = f'{self.base_url}?method=recipe_types.get.v2&format={format}'
        if region:
            endpoint += f'&region={region}'
        if language:
            endpoint += f'&language={language}'

        response = self.oauth.get(endpoint)
        response.raise_for_status()
        result = response.json()
        return result.get('recipe_types', {}).get('recipe_types', []) 