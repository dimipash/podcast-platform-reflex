import reflex as rx
from podcast_platform_reflex.ui.nav import navbar



def root_layout(child: rx.Component, *args, **kwargs):
    return rx.container(
        navbar(),
        rx.fragment(child), rx.logo(), width="100%", id="my-root-layout"
    )
