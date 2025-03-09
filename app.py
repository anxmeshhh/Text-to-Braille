from flask import Flask, render_template, request
import alphaToBraille, brailleToAlpha  # Your existing modules

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None  # To store translation output

    if request.method == "POST":
        input_text = request.form.get("text")
        conversion_type = request.form.get("conversion_type")

        if conversion_type == "braille_to_text":
            result = brailleToAlpha.translate(input_text)
        elif conversion_type == "text_to_braille":
            result = alphaToBraille.translate(input_text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
