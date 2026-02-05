import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


def feat(d, catID, maxLength, includeCat=True, includeReview=True, includeLength=True):
    feat = []
    if includeCat:
        onehot = [0] * len(catID)
        if d["beer/style"] in catID:
            onehot[catID[d["beer/style"]]] = 1
        feat.extend(onehot)
    if includeReview:
        ratings = ["aroma", "appearance", "palate", "taste", "overall"]
        feat.extend([d["review/" + r] for r in ratings])
    if includeLength:
        feat.append(len(d["review/text"]) / maxLength)
    return feat + [1]


def pipeline(
    C,
    catID,
    dataTrain,
    dataValid,
    dataTest,
    includeCat=True,
    includeReview=True,
    includeLength=True,
):
    mod = linear_model.LogisticRegression(C=C, class_weight="balanced")

    maxLength = max([len(d["review/text"]) for d in dataTrain])

    Xtrain = [
        feat(d, catID, maxLength, includeCat, includeReview, includeLength)
        for d in dataTrain
    ]
    Xvalid = [
        feat(d, catID, maxLength, includeCat, includeReview, includeLength)
        for d in dataValid
    ]
    Xtest = [
        feat(d, catID, maxLength, includeCat, includeReview, includeLength)
        for d in dataTest
    ]

    yTrain = [d["beer/ABV"] > 7 for d in dataTrain]
    yValid = [d["beer/ABV"] > 7 for d in dataValid]
    yTest = [d["beer/ABV"] > 7 for d in dataTest]

    # (1) Fit the model on the training set
    mod.fit(Xtrain, yTrain)
    # (2) Compute validation BER
    y_pred_valid = mod.predict(Xvalid)
    TP_valid = sum(y_pred_valid[i] == 1 and yValid[i] == 1 for i in range(len(yValid)))
    TN_valid = sum(y_pred_valid[i] == 0 and yValid[i] == 0 for i in range(len(yValid)))
    FP_valid = sum(y_pred_valid[i] == 1 and yValid[i] == 0 for i in range(len(yValid)))
    FN_valid = sum(y_pred_valid[i] == 0 and yValid[i] == 1 for i in range(len(yValid)))
    validBER = 0.5 * (
        FP_valid / (FP_valid + TN_valid) + FN_valid / (FN_valid + TP_valid)
    )
    # (3) Compute test BER
    y_pred_test = mod.predict(Xtest)
    TP_test = sum(y_pred_test[i] == 1 and yTest[i] == 1 for i in range(len(yTest)))
    TN_test = sum(y_pred_test[i] == 0 and yTest[i] == 0 for i in range(len(yTest)))
    FP_test = sum(y_pred_test[i] == 1 and yTest[i] == 0 for i in range(len(yTest)))
    FN_test = sum(y_pred_test[i] == 0 and yTest[i] == 1 for i in range(len(yTest)))
    testBER = 0.5 * (FP_test / (FP_test + TN_test) + FN_test / (FN_test + TP_test))
    return mod, validBER, testBER


def Q1(catID, dataTrain, dataValid, dataTest):
    return pipeline(10, catID, dataTrain, dataValid, dataTest, True, False, False)


def Q2(catID, dataTrain, dataValid, dataTest):
    return pipeline(10, catID, dataTrain, dataValid, dataTest)


def Q3(catID, dataTrain, dataValid, dataTest):
    best_validBER = float("inf")
    best_testBER = float("inf")
    best_mod = None
    best_c = None
    for c in [0.001, 0.01, 0.1, 1, 10]:
        mod, validBER, testBER = pipeline(c, catID, dataTrain, dataValid, dataTest)
        if validBER < best_validBER:
            best_validBER = validBER
            best_testBER = testBER
            best_mod = mod
            best_c = c
    return best_mod, best_validBER, best_testBER


def Q4(C, catID, dataTrain, dataValid, dataTest):
    mod, validBER, testBER_noCat = pipeline(
        C, catID, dataTrain, dataValid, dataTest, False, True, True
    )
    mod, validBER, testBER_noReview = pipeline(
        C, catID, dataTrain, dataValid, dataTest, True, False, True
    )
    mod, validBER, testBER_noLength = pipeline(
        C, catID, dataTrain, dataValid, dataTest, True, True, False
    )
    return testBER_noCat, testBER_noReview, testBER_noLength


def Jaccard(s1, s2):
    if not s1 or not s2:
        return 0
    return len(set(s1) & set(s2)) / len(set(s1) | set(s2))


def mostSimilar(i, N, usersPerItem):
    similarities = []
    for item in usersPerItem:
        if item != i:
            similarity = Jaccard(usersPerItem[i], usersPerItem[item])
            similarities.append((similarity, item))
    similarities.sort(key=lambda x: x[0], reverse=True)
    return similarities[:N]


def MSE(y, ypred):
    return mean_squared_error(y, ypred)


def getMeanRating(dataTrain):
    return np.mean([d["star_rating"] for d in dataTrain])


def getUserAverages(itemsPerUser, ratingDict):
    return {
        user: np.mean([ratingDict[(user, item)] for item in items])
        for user, items in itemsPerUser.items()
    }


def getItemAverages(usersPerItem, ratingDict):
    return {
        item: np.mean([ratingDict[(user, item)] for user in users])
        for item, users in usersPerItem.items()
    }


def predictRating(
    user,
    item,
    ratingMean,
    reviewsPerUser,
    usersPerItem,
    itemsPerUser,
    userAverages,
    itemAverages,
):
    if item not in usersPerItem:
        return ratingMean

    numer, denom = 0, 0
    for review in reviewsPerUser.get(user, []):
        j = review["product_id"]
        if j == item or j not in usersPerItem:
            continue

        sim = Jaccard(usersPerItem[item], usersPerItem[j])
        numer += (review["star_rating"] - itemAverages[j]) * sim
        denom += abs(sim)

    if denom == 0:
        return itemAverages.get(item, ratingMean)
    return itemAverages[item] + numer / denom


def predictRatingQ7(
    user,
    item,
    ratingMean,
    reviewsPerUser,
    usersPerItem,
    itemsPerUser,
    userAverages,
    itemAverages,
):
    if item not in usersPerItem:
        return ratingMean

    numer, denom = 0, 0
    for review in reviewsPerUser.get(user, []):
        j = review["product_id"]
        if j == item or j not in usersPerItem:
            continue

        sim = Jaccard(usersPerItem[item], usersPerItem[j])
        numer += (review["star_rating"] - itemAverages[j]) * sim
        denom += abs(sim)

    return ratingMean + 0.15 * (numer / denom if denom != 0 else 0)
