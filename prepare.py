# prepare.py

import pandas as pd
from env import get_connection

def load_data():
    query = '''
            SELECT sale_date, sale_amount,
            item_brand, item_name, item_price,
            store_address, store_zipcode, 
            store_city, store_state
            FROM sales
            LEFT JOIN items USING(item_id)
            LEFT JOIN stores USING(store_id);
            '''

    url = get_connection('tsa_item_demand')

    df = pd.read_sql(query, url)
    return df

def prepare_data(df):
    df = convert_sale_date_to_datetime(df)
    df = sort_by_sale_date(df)
    df = set_sale_date_as_index(df)
    df = add_month_and_day_of_week(df)
    df = compute_sales_total(df)
    return df

def convert_sale_date_to_datetime(df):
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    return df

def sort_by_sale_date(df):
    return df.sort_values('sale_date')

def set_sale_date_as_index(df):
    if 'sale_date' in df.columns:
        df.set_index('sale_date', inplace=True)
    return df

def add_month_and_day_of_week(df):
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    return df

def compute_sales_total(df):
    df['sales_total'] = df.sale_amount * df.item_price
    return df

# Visualization functions (optional and separate)
def visualize_sale_amount_distribution(df):
    import matplotlib.pyplot as plt
    plt.hist(df.sale_amount, bins=50)
    plt.title('Distribution of sale amount')
    plt.xlabel('sales_amount in $')
    plt.ylabel('count')
    plt.show()

def visualize_item_price_distribution(df):
    import matplotlib.pyplot as plt
    plt.hist(df.item_price, bins=50)
    plt.title('Distribution of item price')
    plt.xlabel('Item Price')
    plt.ylabel('Count')
    plt.show()



def opsd_germ_prep(df):
    '''
    locate file here if you don't have it saved already
    url = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
    df = pd.read_csv(url)
    Input: df
    Output: df with updates to date, added month/year, filled nulls
    '''
    # convert column names to lower
    df.columns = df.columns.str.lower()
    # convert date column to datetime format
    df.date = pd.to_datetime(df.date, format='%Y-%m-%d')
    # set index to datetime
    df = df.set_index('date')
    df = df.sort_index()
    # add month and year column to df
    df['month'] = df.index.month
    df['year'] = df.index.year
    # fill nulls with 0
    df = df.fillna(0)
    return df