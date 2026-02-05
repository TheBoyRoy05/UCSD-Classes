import random
import string
from collections import defaultdict


def getGlobalAverage(trainRatings):
    return sum(trainRatings) / len(trainRatings)


def trivialValidMSE(ratingsValid, globalAverage):
    return sum((r[2] - globalAverage) ** 2 for r in ratingsValid) / len(ratingsValid)


def alphaUpdate(ratingsTrain, alpha, betaU, betaI, lamb):
    return sum(r[2] - betaU[r[0]] - betaI[r[1]] for r in ratingsTrain) / len(ratingsTrain)


def betaUUpdate(ratingsPerUser, alpha, betaU, betaI, lamb):
    return {
        u: sum(r - alpha - betaI[i] for i, r in ratingsPerUser[u]) / (lamb + len(ratingsPerUser[u]))
        for u in ratingsPerUser
    }


def betaIUpdate(ratingsPerItem, alpha, betaU, betaI, lamb):
    return {
        i: sum(r - alpha - betaU[u] for u, r in ratingsPerItem[i]) / (lamb + len(ratingsPerItem[i]))
        for i in ratingsPerItem
    }


def msePlusReg(ratingsTrain, alpha, betaU, betaI, lamb):
    n = len(ratingsTrain)
    mse = sum((r - alpha - betaU[u] - betaI[i]) ** 2 for u, i, r in ratingsTrain) / n
    regularizer = sum(b**2 for b in betaU.values()) + sum(b**2 for b in betaI.values())
    return mse, mse + lamb * regularizer


def validMSE(ratingsValid, alpha, betaU, betaI):
    n = len(ratingsValid)
    return sum((r - alpha - betaU.get(u, 0) - betaI.get(i, 0)) ** 2 for u, i, r in ratingsValid) / n


def goodModel(ratingsTrain, ratingsPerUser, ratingsPerItem, alpha, betaU, betaI):
    for i in range(10):
        alpha = alphaUpdate(ratingsTrain, alpha, betaU, betaI, 1)
        betaU = betaUUpdate(ratingsPerUser, alpha, betaU, betaI, 1)
        betaI = betaIUpdate(ratingsPerItem, alpha, betaU, betaI, 1)
    return alpha, betaU, betaI


def writePredictionsRating(alpha, betaU, betaI):
    # Write your predictions to a file that you can submit
    predictions = open("predictions_Rating.csv", "w")
    for l in open("pairs_Rating.csv"):
        if l.startswith("userID"):
            predictions.write(l)
            continue
        u, b = l.strip().split(",")
        bu = 0
        bi = 0
        if u in betaU:
            bu = betaU[u]
        if b in betaI:
            bi = betaI[b]
        _ = predictions.write(u + "," + b + "," + str(alpha + bu + bi) + "\n")

    predictions.close()


def generateValidation(allRatings, ratingsValid):
    userBooks = defaultdict(set)
    for u, b, _ in allRatings:
        userBooks[u].add(b)

    allBooks = list({b for _, b, _ in allRatings})
    readValid = [(u, b) for u, b, _ in ratingsValid]
    notRead = []
    for u, _ in readValid:
        while True:
            b_neg = random.choice(allBooks)
            if b_neg not in userBooks[u]:
                notRead.append((u, b_neg))
                break

    return readValid, notRead


def baseLineStrategy(mostPopular, totalRead):
    return1 = set()
    count = 0
    for ic, i in mostPopular:
        count += ic
        return1.add(i)
        if count > totalRead / 2:
            break

    return return1


def improvedStrategy(mostPopular, totalRead):
    return1 = set()
    count = 0
    for ic, i in mostPopular:
        count += ic
        return1.add(i)
        if count > totalRead * 0.7:
            break
    return return1


def evaluateStrategy(return1, readValid, notRead):
    correct = sum(1 for u, b in readValid if b in return1)
    correct += sum(1 for u, b in notRead if b not in return1)
    return correct / (len(readValid) + len(notRead))


def Jaccard(s1, s2):
    if not s1 or not s2:
        return 0
    return len(set(s1) & set(s2)) / len(set(s1) | set(s2))


def jaccardThresh(u, b, ratingsPerItem, ratingsPerUser):
    userBooks = {u: [b for b, _ in ratingsPerUser[u]] for u in ratingsPerUser.keys()}
    bookUsers = {b: [u for u, _ in ratingsPerItem[b]] for b in ratingsPerItem.keys()}
    maxSim = max(Jaccard(bookUsers[b], bookUsers[bp]) for bp in userBooks[u])
    return int(maxSim > 0.013 or len(ratingsPerItem[b]) > 40)


def writePredictionsRead(ratingsPerItem, ratingsPerUser):
    predictions = open("predictions_Read.csv", "w")
    for l in open("pairs_Read.csv"):
        if l.startswith("userID"):
            predictions.write(l)
            continue
        u, b = l.strip().split(",")
        pred = jaccardThresh(u, b, ratingsPerItem, ratingsPerUser)
        _ = predictions.write(u + "," + b + "," + str(pred) + "\n")

    predictions.close()


def featureCat(datum, words, wordId, wordSet):
    feat = [0] * len(words)
    punctuation = set(string.punctuation)
    r = "".join([c for c in datum["review_text"].lower() if not c in punctuation])
    for word in r.split():
        if word in wordSet:
            feat[wordId[word]] += 1
    feat.append(1)
    return feat


def betterFeatures(data):
    wordCount = defaultdict(int)
    punctuation = set(string.punctuation)
    for d in data:
        r = "".join([c for c in d["review_text"].lower() if not c in punctuation])
        for w in r.split():
            wordCount[w] += 1

    counts = [(wordCount[w], w) for w in wordCount]
    counts.sort()
    counts.reverse()

    words = [x[1] for x in counts[:1000]]
    wordId = dict(zip(words, range(len(words))))
    wordSet = set(words)

    return [featureCat(d, words, wordId, wordSet) for d in data]


# def runOnTest(data_test, mod):
#     Xtest = [featureCat(d) for d in data_test]
#     pred_test = mod.predict(Xtest)


# def writePredictionsCategory(pred_test):
#     predictions = open("predictions_Category.csv", "w")
#     pos = 0

#     for l in open("pairs_Category.csv"):
#         if l.startswith("userID"):
#             predictions.write(l)
#             continue
#         u, b = l.strip().split(",")
#         _ = predictions.write(u + "," + b + "," + str(pred_test[pos]) + "\n")
#         pos += 1

#     predictions.close()
