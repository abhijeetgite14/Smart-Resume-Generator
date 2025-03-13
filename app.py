from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

# Ensure wkhtmltopdf is properly configured
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

# Home route — shows "Generate Resume" button
@app.route('/')
def index():
    return render_template('index.html')

# Form route — shows the form
@app.route('/create', methods=['GET', 'POST'])
def create_resume():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "objective": request.form['objective'],
            "experience": request.form['experience'].split(','),
            "skills": request.form['skills'].split(','),
            "education": request.form['education'].split(',')
        }

        # Choose a template (default to template1)
        selected_template = request.form.get('template', 'resume_template1.html')
        rendered_html = render_template(selected_template, data=data)

        # Generate the PDF
        pdf_path = "generated_resume.pdf"
        pdfkit.from_string(rendered_html, pdf_path, configuration=PDFKIT_CONFIG)

        return send_file(pdf_path, as_attachment=True)

    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)





