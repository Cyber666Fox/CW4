from project.config import config
from project.models.models import Genre,Director,Movies,User 
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movies": Movies,
        "User": User,
    }


if __name__ == "__main__":
    app.run(host = "localgost", port=8080, debug=True)