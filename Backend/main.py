import os
import dotenv
from fastapi import FastAPI

import routers

# Load environment variables from dotenv file
dotenv.load_dotenv()

OPENAI_API_KEY="sk-proj-uj3I1vE7ZrLXzEALrqNWT3BlbkFJUmM9fvC3VhtON4Y3ySRB"

app = FastAPI(
    root_path=os.environ.get('BASE_URL', ''),
)

# Register all available routers
app.include_router(routers.functions.menu_picker.router)
app.include_router(routers.health.router)
app.include_router(routers.home.router)
