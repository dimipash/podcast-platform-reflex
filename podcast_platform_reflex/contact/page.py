import reflex as rx
from podcast_platform_reflex import ui
from podcast_platform_reflex.pages.layout import page_layout

from .forms import contact_form


@rx.page("/contact")
def contact_page() -> rx.Component:
    return page_layout(
        rx.vstack(
            rx.text("This is the Contact Page, I will add to it later :)"),
            contact_form(),
        ),
        title="Contact Page",
    )
