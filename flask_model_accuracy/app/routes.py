from flask import Blueprint, render_template, request
from .utils import process_file  # Assuming process_file function exists

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            return "No file uploaded", 400

        # Optionally, you can also get target_column from form data:
        # target_column = request.form.get("target_column")
        # For this example, we let process_file choose the last column by default:
        results = process_file(file)  # or process_file(file, target_column)

        return render_template("result.html", results=results)
    return render_template("upload.html")


@main.route("/generate_accuracy", methods=["POST"])
def generate_accuracy():
    # You can implement the logic for generating accuracy here
    return "Accuracy generated successfully!"  # Modify as per your logic
