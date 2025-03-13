from flask import Flask, render_template, request, redirect, url_for, send_file
import pdfkit
import os

app = Flask(__name__)

# PDFKit configuration (Windows path setup)
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")


# Serve the index.html directly from root folder
@app.route("/")
def index():
    return open("index.html").read()


# Form route for user details
@app.route("/create", methods=["GET", "POST"])
def create_resume():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "objective": request.form["objective"],
            "experience": request.form["experience"].split(","),
            "skills": request.form["skills"].split(","),
            "education": request.form["education"].split(","),
        }

        # Render the resume template
        rendered_html = render_template("resume_template1.html", data=data)

        # Generate PDF file
        pdf_path = "generated_resume.pdf"
        pdfkit.from_string(rendered_html, pdf_path, configuration=PDFKIT_CONFIG)

        return send_file(pdf_path, as_attachment=True)

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
