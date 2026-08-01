from pydantic import BaseModel
from typing import List


# Event Analyzer Input
class EventInput(BaseModel):
    description: str
    interests: List[str]


# Conversation Request
class ConversationRequest(BaseModel):
    event_description: str
    interests: List[str]


# Conversation Response
class ConversationResponse(BaseModel):
    conversation_starters: List[str]


# Fact Check Request
class FactCheckRequest(BaseModel):
    topic: str


# Fact Check Response
class FactCheckResponse(BaseModel):
    status: str
    summary: str