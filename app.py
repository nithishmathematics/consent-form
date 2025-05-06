from flask import Flask, render_template, request, redirect
from fpdf import FPDF
from datetime import datetime
import os

app = Flask(__name__)
os.makedirs('submissions', exist_ok=True)

@app.route('/')
def form():
    return render_template('consent_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    guide = request.form['guide']
    consent = request.form.get('consent', 'No')
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="EEG Research Consent Form", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Guide: {guide}", ln=True)
    pdf.cell(200, 10, txt=f"Consent Given: {consent}", ln=True)
    pdf.cell(200, 10, txt=f"Submitted on: {date}", ln=True)

    filename = f"submissions/{name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(filename)

    return "<h3>Thank you for your submission. Your consent form has been saved.</h3>"

if __name__ == '__main__':
    app.run(debug=True)
