from pymongo import MongoClient
from bson.objectid import ObjectId
import json

def getBookDB():
    client = MongoClient('mongodb://localhost:27017')
    db = client['test-database']
    books = db.books
    return books

def getBooks():
    bookdb = getBookDB()
    result = bookdb.find()
    bookList = []
    for book in result:
        book.pop('_id',None)
        bookList.append(book)
    return bookList

if __name__=='__main__':
    books = getBooks()
    for book in books:
        print(book)