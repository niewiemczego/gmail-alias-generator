from typing import Literal

from pydantic import BaseModel, EmailStr, Field

ALLOWED_ALIASES_VALUES = (128, 256, 512, 1024, 2048, 4096)


class AliasBase(BaseModel):
    email: EmailStr
    use_dot: bool = True
    use_plus: bool = False
    page: int = Field(
        ..., gt=0, description="Number of 'page' to show from list of all aliases depending on aliases_per_page"
    )
    aliases_per_page: Literal[128, 256, 512, 1024, 2048, 4096] = Field(
        default=128,
        description=f"Allowed number of aliases: {ALLOWED_ALIASES_VALUES}",
    )
