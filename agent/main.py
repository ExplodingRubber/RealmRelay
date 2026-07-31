from api.server import app
from config.settings import API_HOST, API_PORT

import uvicorn


def main():
    print("RealmRelay Agent starting...")
    print(f"Listening on http://{API_HOST}:{API_PORT}")

    uvicorn.run(app, host=API_HOST, port=API_PORT)


if __name__ == "__main__":
    main()