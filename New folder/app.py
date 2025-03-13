from flask import Flask, render_template, request, send_file
import pdfkit

app = Flask(__name__)

# Route for the landing page
@app.route('/')
def index():
    return render_template('index.html')

# Route for form page
@app.route('/create')
def form():
    return render_template('form.html')

# Route to handle form data and generate resume
@app.route('/generate', methods=['POST'])
def generate_resume():
    data = {
        "name": request.form['name'],
        "email": request.form['email'],
        "phone": request.form['phone'],
        "objective": request.form['objective'],
        "experience": request.form['experience'].split('\n'),
        "skills": request.form['skills'].split(','),
        "education": request.form['education'].split('\n'),
    }

    # Render the resume template with user data
    rendered_html = render_template('resume_template1.html', data=data)

    # Generate PDF
    pdf_path = "generated_resume.pdf"
    pdfkit.from_string(rendered_html, pdf_path)

    # Send PDF as download
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)


