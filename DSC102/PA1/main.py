products = dd.read_csv(
    "products.csv",
    dtype={
        'asin': 'object',
        'salesRank': 'object',
        'imUrl': 'object',
        'categories': 'object',
        'title': 'object',
        'description': 'object',
        'price': 'float64',
        'related': 'object',
        'brand': 'object'
    }
)
reviews = dd.read_csv(
    "user_reviews.csv",
    dtype={
        'reviewerID': 'object',
        'asin': 'object',
        'reviewerName': 'object',
        'helpful': 'object',
        'reviewText': 'object',
        'overall': 'float32',
        'summary': 'object',
        'unixReviewTime': 'object',
        'reviewTime': 'object'
    }
)

ans1 = reviews.isna().mean().compute().to_dict()

for key,val in ans1.items():
    ans1[key] = round(val * 100, 2)

ans2 = products.isna().mean().compute().to_dict()

for key,val in ans2.items():
    ans2[key] = round(val * 100, 2)

grouped3 = products[['asin','price']].merge(reviews[['asin','overall']], on='asin', how='inner')
ans3 = round(float(grouped3.corr(numeric_only=True).compute()['price']['overall']), 2)

ans4 = products['price'].describe().compute()\
    .rename(index={'std':'standard deviation', '50%':'median'})\
    .loc[['mean','standard deviation','median','min','max']]\
    .to_dict()

for key,val in ans4.items():
    ans4[key] = round(val, 2)

ans5 = products['categories'].str.split("'").str[1].value_counts().compute().sort_values(ascending=False).to_dict()

from dask.distributed import as_completed, wait

def check_partition(df, valid):
    bad = ~df["asin"].isin(valid)
    return bool(bad.any())

product_asins = products['asin'].unique()

delayed_checks = reviews['asin'].map_partitions(
    check_partition,
    product_asins, 
    meta=('dangling', 'bool')
).to_delayed()

futures = client.compute(delayed_checks)

ans6 = 0
remaining_futures = set(futures)

try:
    for fut in as_completed(futures):
        try:
            remaining_futures.discard(fut)
            result = fut.result(timeout=30)
            if any(result):
                ans6 = 1
                break
        except Exception as e:
            print(f"Error processing future: {e}")
            continue
finally:
    if remaining_futures:
        client.cancel(list(remaining_futures))

review_asins = reviews['asin'].unique()

delayed_checks = products['asin'].map_partitions(
    check_partition,
    review_asins, 
    meta=('dangling', 'bool')
).to_delayed()

futures = client.compute(delayed_checks)

ans7 = 0
remaining_futures = set(futures)

try:
    for fut in as_completed(futures):
        try:
            remaining_futures.discard(fut)
            result = fut.result(timeout=30)
            if any(result):
                ans7 = 1
                break
        except Exception as e:
            print(f"Error processing future: {e}")
            continue
finally:
    if remaining_futures:
        client.cancel(list(remaining_futures))