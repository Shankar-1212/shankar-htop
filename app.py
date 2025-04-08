from flask import Flask
import getpass
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Shankar"
    username = getpass.getuser()

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
        top_output = "\n".join(top_output.splitlines()[:10])
    except Exception as e:
        top_output = f"Error getting top output: {e}"

    return f"""
    <h1>/htop Report</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
