from abc import ABC, abstractmethod

# define Visitor interface
class Exporter(ABC):
    @abstractmethod
    def export_paragraph(self, paragraph): ...

    @abstractmethod
    def export_image(self, image): ...

    @abstractmethod
    def export_heading(self, heading): ...


class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Exporter): ...

class HTMLExporter(Exporter):
    def export_paragraph(self, paragraph):
        return f"<p>{paragraph.text}</p>"

    def export_image(self, image):
        return f'<img src="{image.url}" alt="{image.alt}"/>'

    def export_heading(self, heading):
        return f"<h{heading.level}>{heading.text}</h{heading.level}>"


class PDFExporter(Exporter):
    def export_paragraph(self, paragraph):
        return f"PDF Paragraph: {paragraph.text}"

    def export_image(self, image):
        return f"PDF Image: [src={image.url}, alt={image.alt}]"

    def export_heading(self, heading):
        return f"PDF Heading Level {heading.level}: {heading.text}"


class Heading(Element):
    def __init__(self, level):
        self.level = level
        self.text = f"Heading Level {level}"

    def accept(self, visitor: Exporter):
        return visitor.export_heading(self)

class Paragraph(Element):
    def __init__(self, text):
        self.text = text

    def accept(self, visitor: Exporter):
        return visitor.export_paragraph(self)

class Image(Element):
    def __init__(self, url, alt):
        self.url = url
        self.alt = alt

    def accept(self, visitor: Exporter):
        return visitor.export_image(self)

class HTMLDocument:
    def __init__(self):
        self.elements = []

    def add_element(self, element: Element):
        self.elements.append(element)

    def export(self, exporter: Exporter):
        return [element.accept(exporter) for element in self.elements]

def print_exported_content(exported_content):
    for content in exported_content:
        print(content)

if __name__ == "__main__":
    elements = [
        Heading(1),
        Paragraph("This is the first paragraph."),
        Image("image1.png", "An image"),
        Heading(2),
        Paragraph("This is the second paragraph."),
    ]

    document = HTMLDocument()
    for element in elements:
        document.add_element(element)

    html_exporter = HTMLExporter()
    exported_content = document.export(html_exporter)
    print_exported_content(exported_content)

    print("\n---\n")
    pdf_exporter = PDFExporter()
    exported_content = document.export(pdf_exporter)
    print_exported_content(exported_content)
