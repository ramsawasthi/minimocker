"""
MiniMocker – CLI entry point for launching the mock server

© 2025 SkillSetPRO – All rights reserved under the MIT License.
"""


import argparse
import uvicorn
from .server import app, load_routes
from .config_loader import load_config, watch_config
from .utils import log

def main():
    parser = argparse.ArgumentParser(description="MiniMocker - Lightweight Mock Server")
    parser.add_argument("config", help="Path to mock_config.json")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the server on")
    args = parser.parse_args()

    config = load_config(args.config)
    load_routes(config)

    def reload():
        config = load_config(args.config)
        load_routes(config)

    watch_config(args.config, reload)
    log(f"Starting server at http://localhost:{args.port}")
    uvicorn.run(app, host="0.0.0.0", port=args.port)
