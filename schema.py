from pydantic import BaseModel

class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    publicacion: int