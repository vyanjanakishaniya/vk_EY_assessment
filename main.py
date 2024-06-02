from fastapi import FastAPI
from app_views import addition

app = FastAPI()

app.include_router(addition.router)

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
