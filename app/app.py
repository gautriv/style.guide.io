from flask import Blueprint, request, jsonify, render_template
import markdown
from .mstp_rules import analyze_content

main = Blueprint('main', __name__)

feedback_list = []
document_content = ""

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    global document_content
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        content = file.read().decode('utf-8')
        document_content = content
        html_content = markdown.markdown(content)
        suggestions = analyze_content(content)
        return jsonify({"message": "File uploaded successfully", "content": html_content, "suggestions": suggestions})

@main.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    feedback = data.get('feedback')
    feedback_list.append(feedback)
    return jsonify({"message": "Feedback submitted successfully", "feedback_list": feedback_list})

@main.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    return jsonify({"feedback_list": feedback_list})
