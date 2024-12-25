from flask import Flask, jsonify
import solver

app = Flask(__name__)

@app.route('/solve')
async def async_view():
    response = await solver.solver("https://modrinth.com/auth/sign-up","0x4AAAAAAAHWfmKCm7cUG869");
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
