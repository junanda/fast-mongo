from typing import List
from bson.objectid import ObjectId
from ..utils.database import student_collection, student_helper


async def retrieve_students():
    students: List[dict] = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


async def retrieve_student(id_std: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id_std)})
    if student:
        return student_helper(student)


async def update_student(id_std: str, data: dict):
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id_std)})
    if student:
        update = await student_collection.update_one(
            {"_id": ObjectId(id_std)},
            {"$set": data}
        )

        if update:
            return True
        return False


async def delete_student(id_std: str):
    student = await student_collection.find_one({"_id": ObjectId(id_std)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id_std)})
        return True
