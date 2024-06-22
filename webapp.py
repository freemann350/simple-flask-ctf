from flask import Flask, render_template_string
import os
import base64

app = Flask(__name__)
scenario = os.getenv('SCENARIO', '1')

@app.route('/')
def index():
    if scenario == '1':
        content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CTF Challenge</title>
        </head>
        <body>
            <h1>Welcome to the CTF challenge!</h1>
            <!-- The flag is hidden in this comment: {{ flag }} -->
        </body>
        </html>
        """
    elif scenario == '2':
        content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CTF Challenge</title>
        </head>
        <body>
            <h1>Welcome to the CTF challenge!</h1>
            <script>
                console.log("The flag is hidden in this script: {{ flag }}");
            </script>
        </body>
        </html>
        """
    elif scenario == '3':
        content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CTF Challenge</title>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body>
            <h1>Welcome to the CTF challenge!</h1>
        </body>
        </html>
        """
    elif scenario == '4':
        content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CTF Challenge</title>
        </head>
        <body>
            <h1>Welcome to the CTF challenge! Find the flag.</h1>
        </body>
        </html>
        """
    elif scenario == '5':
        encoded_flag = base64.b64encode(os.getenv('FLAG', 'No flag set').encode()).decode()
        content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CTF Challenge</title>
        </head>
        <body>
            <h1>Welcome to the CTF challenge!</h1>
            <p>The encoded flag is: {{ encoded_flag }}</p>
        </body>
        </html>
        """
        return render_template_string(content, encoded_flag=encoded_flag)
    else:
        content = "Invalid scenario"

    return render_template_string(content, flag=os.getenv('FLAG', 'No flag set'))

if scenario == '3':
    @app.route('/static/style.css')
    def style():
        flag = os.getenv('FLAG', 'No flag set')
        return f"""
        body {{
            background-color: #f0f0f0;
        }}
        /* Flag: {flag} */
        """

if scenario == '4':
    @app.route('/hidden-endpoint')
    def hidden_flag():
        flag = os.getenv('FLAG', 'No flag set')
        return f"The flag is: {flag}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
