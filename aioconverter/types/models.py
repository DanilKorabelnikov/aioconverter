from pydantic import BaseModel

from typing import Optional


class Model(BaseModel):
    status: int = None
    data: Optional[dict] = None