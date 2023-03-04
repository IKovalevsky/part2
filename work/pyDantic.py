from pydantic import BaseModel

import string

class User(BaseModel):
    articul: int
    nameArticul: string
    brand: string
