from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.cryptocurrency_arbitrage_bot.schemas import AgenticCryptocurrencyArbitrageBotSessionCreate, AgenticCryptocurrencyArbitrageBotSessionResponse
from app.domain.cryptocurrency_arbitrage_bot.service import AgenticCryptocurrencyArbitrageBotService

router = APIRouter(prefix="/api/v1/cryptocurrency_arbitrage_bot", tags=["Agentic Cryptocurrency Arbitrage Bot Domain"])

@router.post("/sessions", response_model=AgenticCryptocurrencyArbitrageBotSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticCryptocurrencyArbitrageBotSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Cryptocurrency Arbitrage Bot.
    """
    return AgenticCryptocurrencyArbitrageBotService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticCryptocurrencyArbitrageBotSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticCryptocurrencyArbitrageBotService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
