# lab.py


import os
import pandas as pd
import numpy as np
import requests
import bs4
import lxml


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def question1():
    """
    NOTE: You do NOT need to do anything with this function.
    The function for this question makes sure you
    have a correctly named HTML file in the right
    place. Note: This does NOT check if the supplementary files
    needed for your page are there!
    """
    # Don't change this function body!
    # No Python required; create the HTML file.
    return


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------



def extract_book_links(text):
    soup = bs4.BeautifulSoup(text, features='lxml')
    book_links = []
    
    for book in soup.select(".product_pod"):
        rating_class = book.select_one(".star-rating")['class']
        if "Four" in rating_class or "Five" in rating_class:
            price = book.select_one(".price_color").text[2:]
            if float(price) < 50:
                link = book.select_one("h3 a")['href']
                book_links.append(link)
                
    return book_links

def get_product_info(text, categories):
    soup = bs4.BeautifulSoup(text, features='lxml')
    
    category = soup.select_one("ul.breadcrumb li:nth-last-child(2) a").text
    if category not in categories:
        return None
    
    return {
        "Title": soup.select_one("h1").text,
        "Description": soup.select_one("article.product_page > p").text,
        "Rating": soup.select_one("p.star-rating")['class'][1],
        "UPC": soup.select_one("table tr:nth-child(1) td").text,
        "Product Type": soup.select_one("table tr:nth-child(2) td").text,
        "Price (excl. tax)": soup.select_one("table tr:nth-child(3) td").text,
        "Price (incl. tax)": soup.select_one("table tr:nth-child(4) td").text,
        "Tax": soup.select_one("table tr:nth-child(5) td").text,
        "Availability": soup.select_one("table tr:nth-child(6) td").text,
        "Number of reviews": soup.select_one("table tr:nth-child(7) td").text,
        "Category": category,
    }

def scrape_books(k, categories):
    res = []
    
    for i in range(k):
        text = requests.get(f'https://books.toscrape.com/catalogue/page-{i + 1}.html').text
        book_links = extract_book_links(text)
        
        for link in book_links:
            text = requests.get(f'https://books.toscrape.com/catalogue/{link}').text
            product_info = get_product_info(text, categories)
            
            if product_info:
                res.append(product_info)
                
    return pd.DataFrame(res)


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def stock_history(ticker, year, month):
    url = (f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?'
           f'from={year}-{month:02d}-01&'
           f'to={year + (month == 12)}-{(month + 1) % 12:02d}-01&'
           f'apikey=UgeDKEjd5uwx2DbT9vA0lAXpx6t9tAB3')
        
    data = requests.get(url).json()
    return pd.DataFrame(data['historical'][1:])

def stock_stats(history):
    if history.empty: return ("+0.00%", "0.00B")
    
    change = history.iloc[0]['close'] / history.iloc[-1]['open'] - 1
    volume = history.apply(lambda row: (row['high'] + row['low']) / 2 * row['volume'], axis=1).sum()
    return f'{change:+.2%}', f'{volume / 1e9:.2f}B'


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def get_comments(storyid):
    data = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{storyid}.json').json()
    
    comments = []
    for kid in data['kids']:
        comments.extend(get_comments_dfs(kid))
        
    return pd.DataFrame(comments) if comments else pd.DataFrame()

def get_comments_dfs(storyid):
    data = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{storyid}.json').json()
    if 'dead' in data and data['dead']: return []
    
    comments = [{
        'id': data['id'],
        'by': data.get('by', 'Unknown'),
        'text': data.get('text', ''),
        'parent': data.get('parent'),
        'time': pd.Timestamp(data['time'], unit='s')
    }]
    
    for kid in data.get('kids', []):
        comments.extend(get_comments_dfs(kid))
    
    return comments