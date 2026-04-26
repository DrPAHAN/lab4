from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import init_db, get_db, engine
from models import ParsedPage
from parser import parse_url


app = FastAPI(title="Parser API", version="1.0")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs"}

@app.get("/parse")
def parse_endpoint(url: str = Query(...), db: Session = Depends(get_db)):
    try:
        data = parse_url(url)
        
        # Сохраняем в БД через SQLAlchemy
        existing = db.query(ParsedPage).filter(ParsedPage.url == data["url"]).first()
        if existing:
            existing.title = data["title"]
            existing.description = data["description"]
            existing.content_length = data["content_length"]
        else:
            new_page = ParsedPage(**data)
            db.add(new_page)
        db.commit()
        
        return {"status": "success", "data": data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/data")
def get_data(db: Session = Depends(get_db)):
    try:
        records = db.query(ParsedPage).order_by(ParsedPage.parsed_at.desc()).all()
        return {"count": len(records), "results": [r.to_dict() for r in records]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))