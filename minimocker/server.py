"""
MiniMocker – FastAPI server setup and dynamic route builder

© 2025 SkillSetPRO – All rights reserved under the MIT License.
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from .jwt_mock import verify_token
from .utils import log
import time

app = FastAPI()

config = {}

async def make_handler(route):
    async def handler(request: Request):
        if route.get("auth"):
            token = request.headers.get("Authorization", "").replace("Bearer ", "")
            if not verify_token(token, config.get("jwt_secret", "")):
                raise HTTPException(status_code=401, detail="Invalid or missing token")

        delay = route['response'].get("delay", 0)
        if delay:
            time.sleep(delay / 1000.0)

        return JSONResponse(
            status_code=route['response'].get("status", 200),
            content=route['response'].get("body", {})
        )
    return handler

def load_routes(conf):
    global config, app
    config = conf
    app.routes.clear()
    for route in conf.get("routes", []):
        handler = make_handler(route)
        app.add_api_route(route['path'], handler, methods=[route['method']])
        log(f"Loaded route {route['method']} {route['path']}")
