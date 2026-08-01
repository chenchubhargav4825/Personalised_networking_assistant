from fastapi import APIRouter

from models.schemas import (
    EventInput,
    FactCheckRequest
)

from services import (
    event_analyzer,
    fact_checker,
    history_logger
)

router = APIRouter()


@router.post("/analyze")
def analyze_event(data: EventInput):

    topics = event_analyzer.extract_event_themes(
        data.description
    )

    history_logger.save_history({
        "event": data.description,
        "interests": data.interests,
        "generated": topics
    })

    return {
        "topics": topics
    }


@router.post("/fact-check")
def fact_check(data: FactCheckRequest):

    return fact_checker.verify_fact(data.topic)