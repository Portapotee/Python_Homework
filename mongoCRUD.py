from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client['test-database']
courses = db.courses

course = {
    'Instructor':'Balaji',
    'course':'MongoDB Tutorial',
    'price': 100,
    'rating': 5,
}

#Create
# result = courses.insert_one(course)
# if result.acknowledged:
#     print("Course Added. The course Id is", result.inserted_id)
# allcourses = courses.find_one({'_id':ObjectId('5ea1bef16945e642b59040f5')})
# pprint(allcourses)

# for s in allcourses:
#     pprint(s)#pprint prints in json format

#Update
new_update = {"price":150,"course":"Game"}
result = courses.update_one(
    {'_id':ObjectId('5ea1bef16945e642b59040f5')},
    {'$set':new_update}
)

x = courses.delete_one({'id_':ObjectId('5ea1c6df6d5e3d0d3f14d669')})
print(x.deleted_count)