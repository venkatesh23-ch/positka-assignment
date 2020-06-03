import json
import splunklib.client as client
import splunklib.results as results

# Install pycrypto for installing splunklib http://www.voidspace.org.uk/python/pycrypto-2.6.1/
# Install splunk-sdk instead of splunklib for python3

def fetch_results(server_ip, username, password, search_qry, time_range):
    try:
        session = client.connect(host=server_ip, port=8089,
                           username=username, password=password, autologin=True)
    except Exception as e:
        return "Error"# + str(e)
    else:
        kwargs_export = {"earliest_time": "-%sh" % time_range,
                         "latest_time": "now",
                         "search_mode": "normal"}
        exportsearch_results = session.jobs.export("search " + search_qry, **kwargs_export)

        # Get the results using the ResultsReader and convert to json serialzable data
        reader = results.ResultsReader(exportsearch_results)
        search_result = filter(lambda result: isinstance(result, dict), reader)
        search_result = json.dumps({"data": list(search_result)})
        session.logout()
        return search_result

# if __name__ == '__main__':
#     out_json = fetch_results('13.126.96.126', 'admin', 'password', 
#         'index=_internal | top sourcetype', '12')
#     print(out_json)