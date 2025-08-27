import reflex as rx
from podcast_platform_reflex import ui
from podcast_platform_reflex.pages.layout import page_layout


@rx.page("/pricing")
def pricing_page() -> rx.Component:
    return page_layout(
        rx.text("This is the pricing page, I will add to it later :)"),
        title="Pricing Page",
    )
