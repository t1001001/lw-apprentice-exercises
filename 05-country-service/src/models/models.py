from pydantic import BaseModel, Field
from typing import List

class Info(BaseModel):
    name: str = Field(alias="name")
    capital: List[str] = Field(alias="capital")
    languages: List[str] = Field(alias="languages")
    borders: List[str] = Field(alias="borders")
    continents: List[str] = Field(alias="continents")

class Status(BaseModel):
    restcountries_status: str = Field(alias="restcountries_status")
    chuck_norris_status: str = Field(alias="chuck_norris_status")
    version: str = Field(alias="version")
    uptime: int = Field(alias="uptime")
    chuck_norris_quote: str = Field(alias="chuck_norris_quote")