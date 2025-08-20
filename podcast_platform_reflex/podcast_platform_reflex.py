"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from podcast_platform_reflex.contact import *
from podcast_platform_reflex.pages import *


class State(rx.State):
    """The app state."""

    title: str = "Welcome to Reflex!"
    new_title: str = "Welcome to Podcast Platform!"

    @rx.event
    def handle_click_event(self):
        self.title = self.new_title


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(State.title, size="9", on_click=State.handle_click_event),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                on_mouse_over=State.handle_click_event,
                size="5",
            ),
            rx.link(
                rx.button("Contact US!"),
                href="/contact",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index, route="/")
