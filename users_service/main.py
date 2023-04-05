from fastapi import FastAPI, HTTPException
from data.users import User

users: list[User] = [
    User(0, "Александр Макаров", "89858581640", "г.Москва ул.Керченская д.20"),
    User(1, "Дмитрий Зеленин", "89630093636", "г.Москва ул.Яблочкова д.52"),
    User(2, "Илья Мерзликин", "88005553535", "г.Москва ул.Севастопольская д.17"),
]

users_app = FastAPI()


@users_app.get("/users")
async def get_all_users():
    return users


@users_app.get("/user/{_id}")
async def get_user_by_id(_id: int):
    result = [item for item in users if item.id == _id]
    if len(result) > 0:
        return result[0]

    return HTTPException(status_code=404, detail="User wasn't found.")