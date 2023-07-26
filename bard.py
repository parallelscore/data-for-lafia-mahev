import json
import csv

from fhir import Patient

# Get the number of patients in Tanzania
number_of_patients = len(Patient.all(params={"country": "Tanzania"}))

# Create a CSV file to export the data to
with open("patients_tanzania.csv", "w") as csvfile:

    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header row to the CSV file
    writer.writerow(["Resource Type", "ID", "Name"])

    # Iterate over the patients in Tanzania
    for patient in Patient.all(params={"country": "Tanzania"}):

        # Get the resource type of the patient
        resource_type = patient.resource_type

        # Get the ID of the patient
        id = patient.id

        # Get the name of the patient
        name = patient.name[0].text

        # Write the data to the CSV file
        writer.writerow([resource_type, id, name])
