import reflex as rx
from podcast_platform_reflex.ui.nav import navbar

from podcast_platform_reflex import providers


def root_layout(child: rx.Component, *args, **kwargs):
    return providers.my_clerk_provider(
        rx.container(
            navbar(), rx.fragment(child), rx.logo(), width="100%", id="my-root-layout"
        )
    )
