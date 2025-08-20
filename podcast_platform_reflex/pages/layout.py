import reflex as rx
from podcast_platform_reflex import ui


def page_layout(
    children: rx.Component, title: str = "Podcast Platform"
) -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            ui.page_heading(title),
            rx.box(
                children,
            ),
            rx.link(
                rx.button("Home"),
                href="/",
                is_external=False,
            ),
            rx.link(
                rx.button("Contact"),
                href="/contact",
                is_external=False,
            ),
            rx.link(
                rx.button("About"),
                href="/about",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
