import pandas as pd
import numpy as np
import os

link = r'../customaddons/merchandising/utils/data/ecommerce-data'
# link = r'data/ecommerce-data'
file_path = os.path.join(os.getcwd(),link)
users = pd.read_csv(file_path+'/users.csv')
ratings = pd.read_csv(file_path+'/ratings.csv')
products = pd.read_csv(file_path+'/products.csv')


n_users = users.shape[0]
print('Number of users:', n_users)

ratings_base = pd.read_csv(file_path+'/train_data.csv')
ratings_test = pd.read_csv(file_path+'/test_data.csv')

rates = ratings.values
rate_train = ratings_base.values
rate_test = ratings_test.values

print ('Number of traing rates:', rate_train.shape[0])
print ('Number of test rates:', rate_test.shape[0])

items = pd.read_csv(file_path+'/products.csv',)
n_items = items.shape[0]
print('Number of items:', n_items)

# print('Number of users:', n_users)
# print('Shape of users table:', users.shape)
# print('Shape of ratings table:', ratings.shape)
# print('Shape of items table:', items.shape)

ratings = ratings[ratings['user_id'] == 19]

# print(rate_train)

# Kiểm tra thông tin
print(ratings)