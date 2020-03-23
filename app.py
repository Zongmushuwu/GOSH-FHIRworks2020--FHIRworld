from flask import Flask, render_template
from method import getData






app = Flask(__name__)


@app.route('/')
def index():
    datas = getData()
    fhir_version = datas.get_fhir_version()
    microsoft_fhir_server_version = datas.get_microsoft_fhir_server_version()
    patient_total_number = datas.get_patient_total_number()
    observation_total_number = datas.get_observation_total_number()

    return render_template("index.html", fhir_version=fhir_version, microsoft_fhir_server_version=microsoft_fhir_server_version,
                           patient_total_number=patient_total_number, observation_total_number=observation_total_number)




if __name__ == '__main__':
    app.run()
