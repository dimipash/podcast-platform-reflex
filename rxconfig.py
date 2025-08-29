import os
import reflex as rx
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
print(DATABASE_URL)

config = rx.Config(
    app_name="podcast_platform_reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),        
    ],
    db_url=DATABASE_URL,
)