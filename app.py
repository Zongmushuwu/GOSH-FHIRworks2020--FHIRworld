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

    female = datas.get_gender_number("female")
    male = datas.get_gender_number("male")
    age010 = datas.get_age_range_number(0, 10)
    age1020 = datas.get_age_range_number(10, 20)
    age2030 = datas.get_age_range_number(20, 30)
    age3040 = datas.get_age_range_number(30, 40)
    age4050 = datas.get_age_range_number(40, 50)
    age5060 = datas.get_age_range_number(50, 60)
    age6070 = datas.get_age_range_number(60, 70)
    age70120 = datas.get_age_range_number(70, 120)
    country = datas.get_country_patient_number("US")
    commE = datas.get_communication_patient_number("English")
    commS = datas.get_communication_patient_number("Spanish")
    married = datas.get_maritalStatus_patient_number("M")
    notmarried = datas.get_maritalStatus_patient_number("Never Married")


    return render_template("index.html", fhir_version=fhir_version, microsoft_fhir_server_version=microsoft_fhir_server_version,
                           patient_total_number=patient_total_number, observation_total_number=observation_total_number,
                           female = female, male = male, age010 = age010, age1020 = age1020, age2030 = age2030, age3040 = age3040,
                           age4050 = age4050, age5060 = age5060, age6070 = age6070, age70120 = age70120, country = country, commE = commE,
                           commS = commS, married = married, notmarried = notmarried)




if __name__ == '__main__':
    app.run()
