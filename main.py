from flask import Flask, render_template, request
from splunk_search import fetch_results
from sendmail import sendmail

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["POST"])
def search():
    msg = "No Search Results"
    if request.method == "POST":
        try:
            server_ip = request.form['server_ip']
            username = request.form['username']
            password = request.form['password']
            searchQry = request.form['searchQry']
            timeRange = request.form['timeRange']
            email = request.form['email']

            # Call Splunk Search API and get the results 
            resp_json = fetch_results(server_ip, username, password,
                                        searchQry, timeRange)
            print(resp_json)
            sendmail("Splunk Search Results", "PFA JSON Results", email, resp_json)
            msg = "Search Results sent as JSON to the reciever email address."
            return render_template("home.html", msg=msg)
        except Exception as e:
            msg = "Exception raised while processing request " + str(e)
            return render_template("home.html", msg=msg)
    else:
        return "Unauthorized Request"

if __name__ == "__main__":
    app.run(debug=True)
