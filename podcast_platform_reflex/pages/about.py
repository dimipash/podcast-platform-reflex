import reflex as rx
from podcast_platform_reflex import ui
from podcast_platform_reflex.pages.layout import page_layout


@rx.page("/about")
def about_page() -> rx.Component:
    return page_layout(
        rx.text("This is the About Page, I will add to it later :)"),
        title="About Page",
    )
