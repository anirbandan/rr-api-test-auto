import logging
import yaml
import jsonpath
import json

logging.basicConfig(level=logging.INFO)
def get_test_configuration():
    with open('../../src/test_config.yaml', 'rt') as config_file:
        config=yaml.safe_load(config_file.read())
    config_file.close()
    return config

def get_test_data():
    test_data_file = open("../../src/test_data.json", 'r')
    test_data = test_data_file.read()
    return json.loads(test_data)

def get_response_details(response, tag):
    json_response = json.loads(response.content)
    return jsonpath.jsonpath(json_response, tag)[0]