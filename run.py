from neonextech import create_app
import os

config = os.environ.get("NEONEXTECH_CONFIG")  # e.g. neonextech.config.ProdConfig
app = create_app(config)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=app.config.get("DEBUG", False))



    