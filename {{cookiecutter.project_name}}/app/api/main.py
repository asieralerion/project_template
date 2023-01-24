""" REST API interface to get images quality parameters.

Functions:
    get_quality(image_dataset: ImageDataset, image_qa_service: ImageQAService) -> List[ImageQuality]
"""
import os
import sys
from pathlib import Path
from typing import List

from fastapi import FastAPI, Depends
import uvicorn
from dotenv import load_dotenv


def load_environment_variables(env_path: Path):
    if not env_path.exists():
        print(f".env file not found in {str(env_path.resolve())}, please create it and run the server again.")
        sys.exit(1)

    load_dotenv(dotenv_path=env_path)

dotenv_path = Path(Path(__file__).parent.parent.parent, '.env.api')
load_environment_variables(dotenv_path)

app = FastAPI()


if __name__ == "__main__":
    print("Starting api.")

    uvicorn.run(
        "main:app",
        host=os.getenv("HOST"),
        reload=int(os.getenv("RELOAD")),
        port=int(os.getenv("PORT")),
        workers=int(os.getenv("WEB_CONCURRENCY"))
    )
