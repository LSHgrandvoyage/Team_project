import os
import dotenv
from fastapi import FastAPI

import routers

# Load environment variables from dotenv file
dotenv.load_dotenv()

OPENAI_API_KEY="my_api_key"

app = FastAPI(
    root_path=os.environ.get('BASE_URL', ''),
)

# Register all available routers
app.include_router(routers.functions.menu_picker.router)
app.include_router(routers.health.router)
app.include_router(routers.home.router)
