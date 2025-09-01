from datetime import datetime
import reflex as rx
from podcast_platform_reflex.contact.models import ContactMessageModel


class ContactFormState(rx.State):
    form_data: dict = {}
    message: dict = {}
    has_error: bool = False

    def reset_form(self):
        self.has_error = False
        self.form_data = {}

    @rx.event
    def handle_reset_button(self):
        self.reset_form()
        self.message = {}


    @rx.event
    def handle_form_submit(self, form_data: dict):
        self.form_data = form_data
        with rx.session() as session:
            try:
                instance = ContactMessageModel.model_validate(form_data)
            except Exception as e:
                print(e.errors())
                self.has_error = True
                return
            

            self.has_error = False
            self.form_data = {}
            return
            session.add(instance)
            session.commit()
            session.refresh(instance)
            self.reset_form()
            self.message = instance.model_dump()


def contact_form():
    init_name_val = rx.cond(
        ContactFormState.form_data.get("name"),
        ContactFormState.form_data.get("name"),
        ""
    )
    init_message_val = rx.cond(
        ContactFormState.form_data.get("message"),
        ContactFormState.form_data.get("message"),
        ""
    )

    return rx.vstack(
        rx.cond(ContactFormState.has_error,
        rx.text("true value or has_error is true"),
        "false value"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Your name", 
                    defaul_value=init_name_val, 
                    name="name", 
                    type="text"),
                rx.text_area(
                    placeholder="Your message",
                    default_value=init_message_val,
                    name="message",
                ),
                rx.hstack(
                    rx.button("Send message", type="submit"),
                    rx.button("Reset", type="button", on_click=ContactFormState.handle_reset_button),
                )
            ),
            on_submit=ContactFormState.handle_form_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Input value"),
        rx.text(ContactFormState.message.to_string()),
    )
