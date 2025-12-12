from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from . import models, schemas, database
import os

API_SECRET = os.getenv("API_SECRET", "bbcd5eec0f2c189fcdc28cb2dd9aab8ce7560153a226ac9bd724e9db88acf615")
router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")
    token = authorization.split()[1]
    if token != API_SECRET:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/api/register", response_model=schemas.WarrantyOut)
def register_warranty(warranty: schemas.WarrantyCreate, db: Session = Depends(get_db), authorization: str = Header(None)):
    verify_token(authorization)
    existing = db.query(models.Warranty).filter(models.Warranty.asset_id == warranty.asset_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Asset already registered")
    new_warranty = models.Warranty(**warranty.dict())
    db.add(new_warranty)
    db.commit()
    db.refresh(new_warranty)
    return new_warranty
