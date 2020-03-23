import requests


class getData():

    def __init__(self):
        self.CLIENT_ID = "0f6332f4-c060-49fc-bcf6-548982d56569"
        self.CLIENT_SECRET = "ux@CJAaxCD85A9psm-Wdb?x3/Z4c6gp9"
        self.SCOPE = "https://gosh-fhir-synth.azurehealthcareapis.com/.default"
        self.FHIR_BASE_URL = "https://gosh-fhir-synth.azurehealthcareapis.com"
        self.payload = "grant_type=client_credentials&client_id={}&client_secret={}&scope={}".format(self.CLIENT_ID, self.CLIENT_SECRET, self.SCOPE)
        self.url = "https://login.microsoftonline.com/ca254449-06ec-4e1d-a3c9-f8b84e2afe3f/oauth2/v2.0/token"
        self.headers = {'content-type': "application/x-www-form-urlencoded"}
        self.access_token = self.get_access_token()
        self.auth_header = self.make_auth_header(self.access_token)

    def get_access_token(self):
        res = requests.post(self.url, self.payload, headers=self.headers)
        if res.status_code == 200:
            response_json = res.json()
            return response_json.get('access_token', None)

    def make_auth_header(self, access_token):
        return {'Authorization': 'Bearer {}'.format(access_token), 'Content-Type': 'application/fhir+json'}

    def get_patient_total_number(self):
        raw = requests.get('{}/Patient?_summary=count'.format(self.FHIR_BASE_URL), headers=self.auth_header)
        patient_total = raw.json()["total"]
        return patient_total

    def get_observation_total_number(self):
        raw = requests.get('{}/Observation?_summary=count'.format(self.FHIR_BASE_URL), headers=self.auth_header)
        observation_total = raw.json()["total"]
        return observation_total


    def get_microsoft_fhir_server_version(self):
        raw = requests.get('{}/metadata'.format(self.FHIR_BASE_URL), headers=self.auth_header)
        version = raw.json()["version"]
        return version

    def get_fhir_version(self):
        raw = requests.get('{}/metadata'.format(self.FHIR_BASE_URL), headers=self.auth_header)
        version = raw.json()["fhirVersion"]
        return version



