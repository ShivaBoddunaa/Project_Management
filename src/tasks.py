from fastapi import APIRouter
from utils import database_url ,api_key


router = APIRouter(tags=['Tasks'])
@router.get('/taks')
def root_taks():
    return {"Message":"Hello from Tasks Root"}