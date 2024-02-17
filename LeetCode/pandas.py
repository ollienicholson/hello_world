import pandas as pd

# Write a solution to modify the salary column by multiplying each salary by 2.

def modifySalaryColumn(df: pd.DataFrame) -> pd.DataFrame:
    # df['salary'] = df['salary'] * 2
    df['salary'] *=2
    return df


# Write a solution to rename the columns as follows:

# id to student_id
# first to first_name
# last to last_name
# age to age_in_years

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    columns = {
        'id':'student_id',
        'first':'first_name',
        'last':'last_name',
        'age':'age_in_years'}
    students = students.rename(columns=columns)
    # students.columns = ['student_id','first_name','last_name','age_in_years']
    return students


# The grade column is stored as floats, convert it to integers.
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students.grade = students.grade.astype(int)
    # students['grade'] = students['grade'].astype(int)
    return students


# Write a solution to fill in the missing value as 0 in the quantity column.
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.quantity.fillna(0, inplace=True)
    return products


# Write a solution to concatenate these two DataFrames vertically into one DataFrame.
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df3 = pd.concat([df1, df2])
    return df3


# Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    new_table = weather.pivot(index='month', columns='city', values='temperature')
    # return new_table.rename_axis(columns=None)
    return new_table


# Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['Product'], var_name='Quarter', value_name='Sales')


# Write a solution to list the names of animals that weigh strictly more than 100 kilograms.
# Return the animals sorted by weight in descending order.

def findHeavyAnimals(df: pd.DataFrame) -> pd.DataFrame:
    sorted_df = df.sort_values(by='weight', ascending=False)
    filtered_df = sorted_df[sorted_df['weight'] >100][['name']]
    # return animals[animals['weight'] > 100].sort_values(['weight'],ascending=False)[['name']]
    return filtered_df



# A country is big if:

# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).
# Write a solution to find the name, population, and area of the big countries.

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]
    return df[['name','population','area']]


# Write a solution to find the ids of products that are both low fat and recyclable.
def find_products(df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = df[(df['low_fats'] == 'Y') & (df['recyclable'] == 'Y')]
    # return df[(df['low_fats'] == 'Y') & (df['recyclable'] == 'Y')][['product_id']]
    return filtered_df[['product_id']]



# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(self, nums: List[int], target: int) -> List[int]:
    value_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in value_indices:
            return [value_indices[complement], i]
        value_indices[num] = i
        
# Alternative --
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i