from typing import Literal
from pydantic import BaseModel

class Route(BaseModel):
  route: Literal['bbc', 'web']

class Grade(BaseModel):
  relevant:bool