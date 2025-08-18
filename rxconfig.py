import reflex as rx

config = rx.Config(
    app_name="podcast_platform_reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)