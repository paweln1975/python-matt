from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("hello.html")

items = [str(i) for i in range(10)]

parameters = {
    "title": "Hello World",
    "items": items
}
print(template.render(parameters))
