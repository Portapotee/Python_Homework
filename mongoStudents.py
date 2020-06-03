from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client['test-database']
studentdb = db.students
student =  {
            "name": "Bryan",
            "age": "12",
            "class": "python",
}

# Create
# result =studentdb.insert_one(student)
# if result.acknowledged:
#     print("Student Added. The Student Id is", result.inserted_id)
# else:
#     print("Error")

# allcourses = courses.find_one({'_id':ObjectId('5ea1bef16945e642b59040f5')})
# pprint(allcourses)

# for s in allcourses:
#     pprint(s)#pprint prints in json format

#Update
# new_update = {"price":150,"course":"Game"}
# result = courses.update_one(
#     {'_id':ObjectId('5ea1bef16945e642b59040f5')},
#     {'$set':new_update}
# )

#Delete
# x = db.students.delete_one({'id_':ObjectId('5eac3fdcde10d607510540a2')})
# print(x.deleted_count)

results = bookdb.insert_many(booklist)
for id in results.inserted_ids:
    print("Student is Added The Id is", str(id))