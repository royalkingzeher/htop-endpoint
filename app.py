from flask import Flask
import getpass
import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual name
    username = getpass.getuser()
    ist_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], stderr=subprocess.STDOUT, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    html = f"""
    <html>
        <head><title>/htop</title></head>
        <body>
            <h2>Name: {name}</h2>
            <h2>Username: {username}</h2>
            <h2>Server Time (IST): {ist_time}</h2>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
