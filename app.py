from flask import Flask
import subprocess

app = Flask(__name__)

# Route for "/"
@app.route('/')
def main_app():
    return "Hello from Python main App"

# Route for "/time"
@app.route('/time')
def get_time():
    # Execute the `date` command to get current date and time
    current_time = subprocess.check_output(["date"]).decode("utf-8")
    return f"Current time from date command: {current_time}"

# Route for "/store"
@app.route('/store')
def store_app():
    return "Hello from Application Store"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
