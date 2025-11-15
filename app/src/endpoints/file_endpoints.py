from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/post-pdfs")
def post_pdfs():
     return {"message": "Hello Files"}