from typing import Literal

from pydantic import BaseModel, Field


class InputModel(BaseModel):
    meal: Literal[
        'breakfast',
        'brunch',
        'lunch',
        'dinner',
        'midnight snack',
    ] = Field(
        default='dinner',
    )
    how_much_are_you_hungry: Literal[
        "I'm starving",
        'Hungry',
        'Soso',
        "I'm full",
    ] = Field(
        default='Hungry',
    )
    type_of_food: Literal[
        'Korean',
        'Chinese',
        'Japanese',
        'Western',
        'Others',
    ] = Field(
        default='Chinese',
    )
    location: str = Field(
        default='광주광역시 첨단과기로123 대학기숙사 A동',
    )
    scope: float = Field(
        default='1.5',
        ge='0.5',
        le='7.0',
        )
    budget: str = Field(
        description="최대 사용 가능한 돈",
        default='15000',
    )

    llm_type: Literal['chatgpt'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description=' ',
    )
