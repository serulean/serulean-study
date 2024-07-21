from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status, Depends
from database.connection import Database

from models.events import Event, EventUpdate
from typing import List

from auth.authenticate import authenticate


event_database = Database(Event)

event_router = APIRouter(tags=["Events"])


# 모든 이벤트나 특정 ID 이벤트만 추출(조회)
@event_router.get('/', response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event


# 이벤트 생성
@event_router.post('/new')
async def create_event(body: Event, user: str=Depends(authenticate)) -> dict:
    body.creator = user
    await event_database.save(body)
    return {
        "message": "Event created successfully."
    }


# 이벤트 변경
@event_router.put('/{id}', response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate, user: str=Depends(authenticate)) -> Event:
    event = await event_database.get(id)
    if event.creator!=user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation not allowed"
        )

    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event


# 이벤트 삭제
@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId, user: str=Depends(authenticate)) -> dict:
    event = await event_database.get(id)
    if event.creator!=user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operation not allowed"
        )
    
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {
        "message": "Event deleted successfully"
    }




# curl -X 'POST' 'http://127.0.0.1:8000/event/new' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"title": "fastapi", "image":"book.png", "description":"new book", "tags":["python", "fastapi"], "location": "1234"}'

# 인증 토큰 사용시
# curl -X 'POST' 'http://127.0.0.1:8000/event/new' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZmFzdGFwaTIyQHBhY2t0LmNvbSIsImV4cGlyZXMiOjE2OTczNzA1NjEuMDMzMDc4NH0.7jIwkNW57OYo_W6kz2dReb9omYZvLLJAK4MY6bqu0Gg' -H 'Content-Type: application/json' -d '{"title": "fastapi", "image":"book.png", "description":"new book", "tags":["python", "fastapi"], "location": "where"}'
