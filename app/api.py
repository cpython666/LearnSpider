from fastapi import APIRouter
from app.main import app
router = APIRouter()


# @router.get("/dailycount")
# def init_():
#
#     return get_page_count()

app.include_router(router,prefix="/api")