from src.main import create_app
application = create_app("config/config.json")

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=80, debug = True)