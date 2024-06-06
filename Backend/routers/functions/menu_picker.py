import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.menu_picker import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_acrostic_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    return OutputModel(
        output=chain.invoke({
            'input_context': f'''
                # About User
                * When i want to eat: {model.meal}
                * How much i am hungry: {model.how_much_are_you_hungry}
                * What i want to eat: {model.type_of_food}
                * Where i live in: {model.location}
                * Scope to search from where I live in: {model.scope}
                * How much i can pay for meal : {model.budget}

                # Environments
                * Target Language: Korean
            ''',
        }),
    )
