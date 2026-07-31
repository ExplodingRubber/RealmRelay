from api.server import app

import uvicorn


HOST = "0.0.0.0"
PORT = 42069


def main():
    print("RealmRelay Agent starting...")
    print(f"Listening on http://{HOST}:{PORT}")

    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()