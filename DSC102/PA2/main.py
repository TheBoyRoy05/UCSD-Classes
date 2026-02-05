PID = 'a17787465' # your pid, for instance: 'a43223333'
INPUT_FORMAT = 'dataframe' # choose a format of your input data, valid options: 'dataframe', 'rdd', 'koalas'

import os
import getpass
from pyspark.sql import SparkSession
from utilities import SEED
from utilities import PA2Test
from utilities import PA2Data
from utilities import data_cat
from pa2_main import PA2Executor
import time
if INPUT_FORMAT == 'dataframe':
    import pyspark.ml as M
    import pyspark.sql.functions as F
    import pyspark.sql.types as T
if INPUT_FORMAT == 'koalas':
    import databricks.koalas as ks
elif INPUT_FORMAT == 'rdd':
    import pyspark.mllib as M
    from pyspark.mllib.feature import Word2Vec
    from pyspark.mllib.linalg import Vectors
    from pyspark.mllib.linalg.distributed import RowMatrix

os.environ['PYSPARK_SUBMIT_ARGS'] = '--py-files utilities.py,assignment2.py \
--deploy-mode client \
pyspark-shell'

class args:
    review_filename = data_cat.review_filename
    product_filename = data_cat.product_filename
    product_processed_filename = data_cat.product_processed_filename
    ml_features_train_filename = data_cat.ml_features_train_filename
    ml_features_test_filename = data_cat.ml_features_test_filename
    output_root = '/home/{}/{}-pa2/test_results'.format(getpass.getuser(), PID)
    test_results_root = data_cat.test_results_root
    pid = PID

pa2 = PA2Executor(args, input_format=INPUT_FORMAT)
data_io = pa2.data_io
data_dict = pa2.data_dict
begin = time.time()

# Bring the part_1 datasets to memory and de-cache part_2 datasets. 
# Execute this once before you start working on this Part
data_dict, _ = data_io.cache_switch(data_dict, 'part_1')

def task_0(data_io, product_data):
    # -----------------------------Column names--------------------------------
    # Inputs:
    asin_column = 'asin'
    overall_column = 'overall'
    # Outputs:
    mean_rating_column = 'meanRating'
    count_rating_column = 'countRating'
    # -------------------------------------------------------------------------

    # ---------------------- Your implementation begins------------------------

    product_data.show(5)
    product_data[['asin']].show(5)
    product_data.where(F.col('asin') == 'B00I8KEOTM').show()
    count_rows = product_data.count()
    mean_price = product_data.select(F.avg(F.col('price'))).head()[0]
    # -------------------------------------------------------------------------

    # ---------------------- Put results in res dict --------------------------
    # Calculate the values programmatically. Do not change the keys and do not
    # hard-code values in the dict. Your submission will be evaluated with
    # different inputs.
    # Modify the values of the following dictionary accordingly.
    res = {'count_total': None, 'mean_price': None}
    
    # Modify res:

    res['count_total'] = count_rows
    res['mean_price'] = mean_price

    # -------------------------------------------------------------------------

    # ----------------------------- Do not change -----------------------------
    return res
    # -------------------------------------------------------------------------
    
if INPUT_FORMAT == 'dataframe':
    res = task_0(data_io, data_dict['product'])
    pa2.tests.test(res, 'task_0')
    
# %load -s task_1 assignment2.py
def task_1(data_io, review_data, product_data):
    # -----------------------------Column names--------------------------------
    # Inputs:
    asin_column = 'asin'
    overall_column = 'overall'
    # Outputs:
    mean_rating_column = 'meanRating'
    count_rating_column = 'countRating'
    # -------------------------------------------------------------------------

    # ---------------------- Your implementation begins------------------------
    # Calculate mean and count of ratings for each product
    ratings_agg = review_data.groupBy(asin_column) \
        .agg(
            F.avg(overall_column).alias(mean_rating_column),
            F.count(overall_column).alias(count_rating_column)
        )
    
    # Join with product data to include products with no reviews
    result = product_data.join(ratings_agg, asin_column, 'left')
    
    # Calculate statistics
    count_total = result.count()
    mean_meanRating = result.select(F.avg(mean_rating_column)).head()[0]
    variance_meanRating = result.select(F.variance(mean_rating_column)).head()[0]
    numNulls_meanRating = result.filter(F.col(mean_rating_column).isNull()).count()
    mean_countRating = result.select(F.avg(count_rating_column)).head()[0]
    variance_countRating = result.select(F.variance(count_rating_column)).head()[0]
    numNulls_countRating = result.filter(F.col(count_rating_column).isNull()).count()

    # -------------------------------------------------------------------------

    # ---------------------- Put results in res dict --------------------------
    res = {
        'count_total': count_total,
        'mean_meanRating': mean_meanRating,
        'variance_meanRating': variance_meanRating,
        'numNulls_meanRating': numNulls_meanRating,
        'mean_countRating': mean_countRating,
        'variance_countRating': variance_countRating,
        'numNulls_countRating': numNulls_countRating
    }
    # -------------------------------------------------------------------------

    # ----------------------------- Do not change -----------------------------
    data_io.save(res, 'task_1')
    return res
    # -------------------------------------------------------------------------

res = task_1(data_io, data_dict['review'], data_dict['product'])
pa2.tests.test(res, 'task_1')

# %load -s task_2 assignment2.py
def task_2(data_io, product_data):
    # -----------------------------Column names--------------------------------
    # Inputs:
    salesRank_column = 'salesRank'
    categories_column = 'categories'
    asin_column = 'asin'
    # Outputs:
    category_column = 'category'
    bestSalesCategory_column = 'bestSalesCategory'
    bestSalesRank_column = 'bestSalesRank'
    # -------------------------------------------------------------------------

    # ---------------------- Your implementation begins------------------------
    # Extract first category from nested array
    result = product_data.withColumn(
        category_column,
        F.when(
            (F.col(categories_column).isNull()) | (F.size(F.col(categories_column)) == 0),
            F.lit(None)
        ).otherwise(F.element_at(F.element_at(F.col(categories_column), 1), 1))
    )
    
    # Flatten salesRank into two columns
    result = result.withColumn(
        bestSalesCategory_column,
        F.when(
            F.col(salesRank_column).isNull(),
            F.lit(None)
        ).otherwise(F.map_keys(F.col(salesRank_column))[0])
    ).withColumn(
        bestSalesRank_column,
        F.when(
            F.col(salesRank_column).isNull(),
            F.lit(None)
        ).otherwise(F.map_values(F.col(salesRank_column))[0])
    )
    
    # Calculate statistics
    count_total = result.count()
    mean_bestSalesRank = result.select(F.avg(bestSalesRank_column)).head()[0]
    variance_bestSalesRank = result.select(F.variance(bestSalesRank_column)).head()[0]
    numNulls_category = result.filter(F.col(category_column).isNull()).count()
    countDistinct_category = result.select(F.countDistinct(category_column)).head()[0]
    numNulls_bestSalesCategory = result.filter(F.col(bestSalesCategory_column).isNull()).count()
    countDistinct_bestSalesCategory = result.select(F.countDistinct(bestSalesCategory_column)).head()[0]

    # -------------------------------------------------------------------------

    # ---------------------- Put results in res dict --------------------------
    res = {
        'count_total': count_total,
        'mean_bestSalesRank': mean_bestSalesRank,
        'variance_bestSalesRank': variance_bestSalesRank,
        'numNulls_category': numNulls_category,
        'countDistinct_category': countDistinct_category,
        'numNulls_bestSalesCategory': numNulls_bestSalesCategory,
        'countDistinct_bestSalesCategory': countDistinct_bestSalesCategory
    }
    # -------------------------------------------------------------------------

    # ----------------------------- Do not change -----------------------------
    data_io.save(res, 'task_2')
    return res
    # -------------------------------------------------------------------------

res = task_2(data_io, data_dict['product'])
pa2.tests.test(res, 'task_2')