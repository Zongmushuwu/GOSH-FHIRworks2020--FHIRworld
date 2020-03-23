import requests

import patient as patient

from datetime import datetime


class getData():

    def __init__(self):
        self.CLIENT_ID = "0f6332f4-c060-49fc-bcf6-548982d56569"
        self.CLIENT_SECRET = "ux@CJAaxCD85A9psm-Wdb?x3/Z4c6gp9"
        self.SCOPE = "https://gosh-fhir-synth.azurehealthcareapis.com/.default"
        self.FHIR_BASE_URL = "https://gosh-fhir-synth.azurehealthcareapis.com"
        self.payload = "grant_type=client_credentials&client_id={}&client_secret={}&scope={}".format(self.CLIENT_ID,
                                                                                                     self.CLIENT_SECRET,
                                                                                                     self.SCOPE)
        self.url = "https://login.microsoftonline.com/ca254449-06ec-4e1d-a3c9-f8b84e2afe3f/oauth2/v2.0/token"
        self.headers = {'content-type': "application/x-www-form-urlencoded"}
        self.access_token = self.get_access_token()
        self.auth_header = self.make_auth_header(self.access_token)
        self.all_patient = self.get_all_patient()

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

    def get_all_patient(self):
        raw = requests.get('{}/Patient'.format(self.FHIR_BASE_URL), headers=self.auth_header)
        all_patient = []
        self.get_all_patient_nextpage(raw, all_patient)

        patients = []
        for raw_patient_data in all_patient:
            for patient_data in raw_patient_data["entry"]:
                patients.append(patient.parsePatient().parse_patient_info(patient_data))
        print(len(patients))
        print(patients)
        return patients

    def get_all_patient_nextpage(self, raw, all_patient):
        json = raw.json()
        if json is not None:
            all_patient.append(json)
        else:
            return
        relation = json["link"][0]["relation"]
        if relation == "next":
            print("nextpage")
            next_url = json["link"][0]["url"]
            next_raw = requests.get(next_url, headers=self.auth_header)
            return self.get_all_patient_nextpage(next_raw, all_patient)
        else:
            return

    def get_gender_number(self, gender):
        patients = self.all_patient
        number = 0
        for patient in patients:
            if patient.gender == gender:
                number = number + 1
        return number

    def get_country_patient_number(self, country):
        patients = self.all_patient
        number = 0
        for patient in patients:
            if patient.country == country:
                number = number + 1
        return number

    def get_age_number(self, age):
        patients = self.all_patient
        current_year = datetime.now().year
        number = 0
        for patient in patients:
            if int(current_year) - int(patient.birth_year) == age:
                number = number + 1
        return number

    def get_age_range_number(self, age_begin, age_end):
        # include age_begin but not age_end
        age_between = age_end - age_begin - 1
        number = 0
        for a in range (0, age_between):
            number = number + self.get_age_number(age_begin + a)
        return number

    def get_maritalStatus_patient_number(self, maritalStatus):
        patients = self.all_patient
        number = 0
        for patient in patients:
            if patient.maritalStatus == maritalStatus:
                number = number + 1
        return number

    def get_communication_patient_number(self, communication):
        patients = self.all_patient
        number = 0
        for patient in patients:
            if patient.communication == communication:
                number = number + 1
        return number
