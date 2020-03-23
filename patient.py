class Patient:

    def __init__(self):
        self.gender = ""
        self.country = ""
        self.birth_year = ""
        self.maritalStatus = ""
        self.communication = ""


class parsePatient():
    def __init__(self):
        self.Patient = Patient()

    def parse_patient_info(self, json):
        resource = json["resource"]
        if resource is not None and resource["resourceType"] == "Patient":
            try:
                self.Patient.gender = resource["gender"]
            except KeyError:
                pass

            try:
                self.Patient.country = resource["address"][0]["country"]
            except KeyError:
                pass

            try:
                self.Patient.birth_year = resource["birthDate"].split("-")[0]
            except KeyError:
                pass

            try:
                self.Patient.maritalStatus = resource["maritalStatus"]["text"]
            except KeyError:
                pass

            try:
                self.Patient.communication = resource["communication"][0]["language"]["text"]
            except KeyError:
                pass

        return self.Patient
