from flask import Flask, request, render_template_string
import logging

app = Flask(__name__)

# Configure logging to save results to a log file
logging.basicConfig(filename='flask_app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# HTML template for the addition page
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Addition</title>
</head>
<body>
    <h1>Addition of Two Numbers</h1>
    <form method="POST">
        <label for="num1">Enter the first number: </label>
        <input type="text" name="num1" id="num1"><br><br>
        
        <label for "num2">Enter the second number: </label>
        <input type="text" name="num2" id="num2"><br><br>
        
        <input type="submit" value="Add">
    </form>
    
    {% if result %}
    <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2

        # Log the result to both console and file
        log_message = f"Result: {result}"
        logging.info(log_message)
    else:
        result = None

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
