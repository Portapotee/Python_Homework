from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017')
db = client['test-database']
courses = db.courses

course = {
    'Instructor':'Balaji',
    'course':'MongoDB Tutorial',
    'price': 100,
    'rating': 5,
}

# result = courses.insert_one(course)
# if result.acknowledged:
#     print("Course Added. The course Id is", result.inserted_id)
allcourses = courses.find()
print(allcourses)

for s in allcourses:
    pprint(s)#pprint prints in json format
