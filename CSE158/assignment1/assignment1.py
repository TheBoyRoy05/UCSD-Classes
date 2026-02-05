import os
import gzip
from tqdm import tqdm
from scipy.sparse import load_npz
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from scipy.sparse import hstack
import re

def readGz(path):
    for l in gzip.open(path, "rt"):
        yield eval(l)


def readCSV(path):
    f = gzip.open(path, "rt")
    f.readline()
    for l in f:
        yield l.strip().split(",")


############################################
################# Rating ###################
############################################
allRatings = [(u, b, int(r)) for u, b, r in readCSV("train_Interactions.csv.gz")]

ratingsTrain = allRatings[:190000]
ratingsValid = allRatings[190000:]
ratingsPerUser = defaultdict(list)
ratingsPerItem = defaultdict(list)

for u, b, r in ratingsTrain:
    ratingsPerUser[u].append((b, r))
    ratingsPerItem[b].append((u, r))

trainRatings = [r[2] for r in ratingsTrain]
globalAverage = sum(trainRatings) / len(trainRatings)

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

def predictRating(u, b, alpha, betaU, betaI):
    return alpha + betaU.get(u, 0) + betaI.get(b, 0)

def modpredictRating(u, b, **kwargs):
    baseline = predictRating(u, b, **kwargs)
    if b in kwargs["ratingsPerItem"] and len(kwargs["ratingsPerItem"][b]) > 0:
        item_avg = sum(r for _, r in kwargs["ratingsPerItem"][b]) / len(kwargs["ratingsPerItem"][b])
        if item_avg > baseline:
            return baseline - 0.115*(item_avg - baseline)
    return baseline

lamb = 4.5
steps = 50
betaU = {u: 0 for u in ratingsPerUser}
betaI = {b: 0 for b in ratingsPerItem}
alpha = globalAverage

for _ in tqdm(range(steps), desc="Training rating model"):
    alpha = alphaUpdate(ratingsTrain, alpha, betaU, betaI, lamb)
    betaU = betaUUpdate(ratingsPerUser, alpha, betaU, betaI, lamb)
    betaI = betaIUpdate(ratingsPerItem, alpha, betaU, betaI, lamb)

kwargs = {
    "alpha": alpha,
    "betaU": betaU,
    "betaI": betaI,
    "ratingsPerItem": ratingsPerItem
}

predictions = open("predictions_Rating.csv", "w")
for l in tqdm(open("pairs_Rating.csv"), desc="Writing rating predictions"):
    if l.startswith("userID"):
        predictions.write(l)
        continue
    u, b = l.strip().split(",")
    pred = max(0.0, min(5.0, modpredictRating(u, b, **kwargs)))
    predictions.write(f"{u},{b},{pred}\n")
predictions.close()

##########################################
################# Read ###################
##########################################
bookCount = defaultdict(int)
userCount = defaultdict(int)
totalRead = 0

for user,book,_ in readCSV("train_Interactions.csv.gz"):
    bookCount[book] += 1
    userCount[user] += 1
    totalRead += 1

def build_popular_books(bookCount, totalRead, threshold=0.72):
    mostPopular = [(bookCount[x], x) for x in bookCount]
    mostPopular.sort()
    mostPopular.reverse()
    
    count = 0
    popular = set()
    for ic, i in mostPopular:
        count += ic
        popular.add(i)
        if count > totalRead * threshold:
            break
    return popular

def build_active_users(userCount, totalRead, threshold=0.01):
    mostActive = [(userCount[x], x) for x in userCount]
    mostActive.sort()
    mostActive.reverse()
    
    count = 0
    active = set()
    for ic, i in mostActive:
        count += ic
        active.add(i)
        if count > totalRead * threshold:
            break
    return active

def Jaccard(s1, s2):
    return len(set(s1) & set(s2)) / len(set(s1) | set(s2))

userBooks = {u: set(b for b, _ in ratingsPerUser[u]) for u in ratingsPerUser.keys()}
bookUsers = {b: set(u for u, _ in ratingsPerItem[b]) for b in ratingsPerItem.keys()}
popularBooks = build_popular_books(bookCount, totalRead)
activeUsers = build_active_users(userCount, totalRead)

def predictRead(u, b):
    if u not in userBooks or not userBooks[u]:
        return int(b in popularBooks)

    if b not in bookUsers or not bookUsers[b]:
        return int(u in activeUsers)
    
    maxSim = 0
    for bp in userBooks[u]:
        if bp in bookUsers:
            sim = Jaccard(bookUsers[b], bookUsers[bp])
            maxSim = max(maxSim, sim)
            if maxSim > 0.025:
                return 1
    
    return int(b in popularBooks)

predictions = open("predictions_Read.csv", "w")
for l in tqdm(open("pairs_Read.csv"), desc="Writing read predictions"):
    if l.startswith("userID"):
        predictions.write(l)
        continue
    u, b = l.strip().split(",")
    predictions.write(f"{u},{b},{predictRead(u, b)}\n")
predictions.close()

############################################
################# Category #################
############################################
def clean(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9\s']", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()

data = [d for d in readGz("train_Category.json.gz")]
texts = [clean(d["review_text"]) for d in data]
y = [d["genreID"] for d in data]

word_vec = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1,3),
    min_df=2,
    stop_words="english"
)
char_vec = TfidfVectorizer(
    analyzer="char",
    ngram_range=(3,5),
    min_df=2,
    max_features=30000
)

def load_text_features(Xw_file="Xw_features.npz", Xc_file="Xc_features.npz"):
    if os.path.exists(Xw_file) and os.path.exists(Xc_file):
        print("Loading saved vectorized features...")
        Xw = load_npz(Xw_file)
        Xc = load_npz(Xc_file)
        print(f"Loaded Xw shape: {Xw.shape}, Xc shape: {Xc.shape}")
    else:
        print("Computing TF-IDF features (this may take a while)...")
        Xw = word_vec.fit_transform(texts)
        Xc = char_vec.fit_transform(texts)
    return Xw, Xc

Xw, Xc = load_text_features()

X = hstack([Xw, Xc])
n = X.shape[0]
cut = 9 * n // 10

Xtrain = X[:cut]
ytrain = y[:cut]
Xvalid = X[cut:]
yvalid = y[cut:]

mod = LinearSVC(C=0.1)
mod.fit(Xtrain, ytrain)
mod.score(Xvalid, yvalid)

predictions = open("predictions_Category.csv", "w")
predictions.write("userID,reviewID,prediction\n")

for l in tqdm(readGz("test_Category.json.gz"), desc="Writing category predictions"):
    text = clean(l["review_text"])

    Xw = word_vec.transform([text])
    Xc = char_vec.transform([text])
    Xtest = hstack([Xw, Xc])

    pred = mod.predict(Xtest)[0]
    predictions.write(f"{l['user_id']},{l['review_id']},{pred}\n")

predictions.close()