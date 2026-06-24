from pydantic import BaseModel
from typing import List


class SubTopic(BaseModel):
    name: str


class Topic(BaseModel):
    name: str
    subtopics: List[SubTopic]


class TopicBuilderOutput(BaseModel):
    user_goal: str
    topics: List[Topic]