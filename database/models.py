from pydantic import BaseModel
from typing import List


# User Profile
class UserProfile(BaseModel):
    user_id: str
    bio_text: str
    interests: List[str]


# Event Context
class EventContext(BaseModel):
    event_id: str
    event_description: str
    analyzed_themes: List[str]


# Networking Session
class NetworkingSession(BaseModel):
    session_id: str
    user_id: str
    event_id: str


# Generated Conversation Starter
class GeneratedStarter(BaseModel):
    starter_id: str
    session_id: str
    starter_text: str
    context_prompt_used: str


# Wikipedia Fact Check
class WikipediaFactCheck(BaseModel):
    factcheck_id: str
    session_id: str
    verified_query_text: str
    verification_status: str
    wikipedia_source_url: str


# Log Entry
class LogEntry(BaseModel):
    log_id: str
    session_id: str
    action_type: str
    payload_json: str
    timestamp: str