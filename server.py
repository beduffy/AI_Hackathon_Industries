from flask import Flask, url_for, request, send_from_directory, render_template
app = Flask(__name__, static_url_path='')

#url_for('static', filename='output_file.json')

@app.route('/')
def index():
    return render_template('current_call_report.html')

@app.route('/intermediate_data/<path:path>')
def send_intermediate_data(path):
    return send_from_directory('intermediate_data', path)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':

    print app
    app.run()
