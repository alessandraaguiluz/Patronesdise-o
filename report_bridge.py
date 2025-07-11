from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, content):
        pass

class PDFExporter(Exporter):
    def export(self, content):
        print(f"Exporting {content} to PDF...")

class HTMLExporter(Exporter):
    def export(self, content):
        print(f"Exporting {content} to HTML...")

class Report(ABC):
    def __init__(self, exporter):
        self.exporter = exporter

    @abstractmethod
    def generate(self):
        pass

class UserReport(Report):
    def generate(self):
        self.exporter.export("User Report")

class SalesReport(Report):
    def generate(self):
        self.exporter.export("Sales Report")

if __name__ == "__main__":
    pdf = PDFExporter()
    html = HTMLExporter()

    user_report = UserReport(pdf)
    sales_report = SalesReport(html)

    user_report.generate()
    sales_report.generate()
