import reflex as rx
from podcast_platform_reflex import ui
from podcast_platform_reflex.layout import root_layout


def page_layout(
    children: rx.Component, title: str = "Podcast Platform"
) -> rx.Component:
    return root_layout(
        rx.container(         
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
    )
