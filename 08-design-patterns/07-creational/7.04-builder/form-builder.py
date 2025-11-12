from abc import ABC, abstractmethod


class FormField:
    def __init__(self, field_type, label, name, placeholder=""):
        self.field_type = field_type
        self.label = label
        self.name = name
        self.placeholder = placeholder

    def render(self):
        return f'<label>{self.label}</label><input type="{self.field_type}" name="{self.name}" placeholder="{self.placeholder}"/>'

class FormButton:
    def __init__(self, label, name):
        self.label = label
        self.name = name

    def render(self):
        return f'<button type="submit" name="{self.name}">{self.label}</button>'

class Builder(ABC):

    @abstractmethod
    def add_text_field(self, label: str, name: str, placeholder: str = "") -> Builder:
        pass

    @abstractmethod
    def add_email_field(self, label: str, name: str, placeholder: str = "") -> Builder:
        pass

    @abstractmethod
    def add_password_field(self, label: str, name: str, placeholder: str = "") -> Builder:
        pass

    @abstractmethod
    def add_button(self, label: str, name: str) -> Builder:
        pass

    @abstractmethod
    def build(self) -> str:
        pass

class HTMLFormBuilder(Builder):
    def __init__(self):
        self.fields = []

    def add_text_field(self, label: str, name: str, placeholder: str = "") -> Builder:
        self.fields.append(FormField("text", label, name, placeholder))
        return self

    def add_email_field(self, label: str, name: str, placeholder: str = "") -> Builder:
        self.fields.append(FormField("email", label, name, placeholder))
        return self

    def add_password_field(self, label: str, name: str, placeholder: str = "") -> Builder:
        self.fields.append(FormField("password", label, name, placeholder))
        return self

    def add_button(self, label: str, name: str) -> Builder:
        self.fields.append(FormButton(label, name))
        return self

    def build(self) -> str:
        form_html = "<form>"
        content = "\n\t".join(field.render() for field in self.fields)
        return f'{form_html}\n\t{content}\n{form_html}'

class HtmlFormDirector:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct_login_form(self) -> str:
        return (self.builder
                .add_email_field("Email", "email", "Enter your email")
                .add_password_field("Password", "password", "Enter your password")
                .add_button("Login", "login")
                .build())

if __name__ == "__main__":
    builder = HTMLFormBuilder()
    director = HtmlFormDirector(builder)
    login_form_html = director.construct_login_form()
    print(login_form_html)
