import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import json
import csv

fake = Faker('en_US')

# Function to generate patient data
def generate_patient_data(num_patients):
    patients = []
    for _ in range(num_patients):
        patient = {}
        patient['resourceType'] = 'Patient'
        patient['id'] = str(_+1)
        patient['name'] = [{'family': fake.last_name(), 'given': [fake.first_name()]}]
        patient['gender'] = random.choice(['male', 'female'])
        patient['birthDate'] = str(fake.date_of_birth(minimum_age=1, maximum_age=80))
        patient['managingOrganization'] = {'reference': 'Organization/' + str(_+1)}
        patient['identifier'] = [{'system': 'https://fhir-opensrp.lafia.io/Patient', 'value': str(_+1)}]
        patients.append(patient)
    return patients

# Function to generate encounter data
def generate_encounter_data(num_encounters):
    encounters = []
    for _ in range(num_encounters):
        encounter = {}
        encounter['resourceType'] = 'Encounter'
        encounter['id'] = str(_+1)
        encounter['status'] = random.choice(['planned', 'arrived', 'triaged', 'in-progress', 'onleave', 'finished', 'cancelled'])
        encounter['patient'] = 'Patient/' + str(_+1)
        encounter['period'] = json.dumps({'start': str(fake.past_datetime(start_date='-1y', tzinfo=None)), 'end': str(fake.past_datetime(start_date='-1d', tzinfo=None))})
        encounters.append(encounter)
    return encounters

# Function to generate condition data
def generate_condition_data(num_conditions):
    conditions = []
    for _ in range(num_conditions):
        condition = {}
        condition['resourceType'] = 'Condition'
        condition['id'] = str(_+1)
        condition['clinicalStatus'] = json.dumps({'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical', 'code': random.choice(['active', 'recurrence', 'inactive', 'remission', 'resolved']), 'display': 'clinical status'}]})
        condition['verificationStatus'] = json.dumps({'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/condition-ver-status', 'code': random.choice(['unconfirmed', 'confirmed', 'refuted', 'entered-in-error']), 'display': 'verification status'}]})
        condition['subject'] = 'Patient/' + str(_+1)
        condition['onsetDateTime'] = str(fake.past_datetime(start_date='-1y', tzinfo=None))
        conditions.append(condition)
    return conditions

# Function to generate procedure data
def generate_procedure_data(num_procedures):
    procedures = []
    for _ in range(num_procedures):
        procedure = {}
        procedure['resourceType'] = 'Procedure'
        procedure['id'] = str(_+1)
        procedure['status'] = random.choice(['preparation', 'in-progress', 'not-done', 'on-hold', 'stopped', 'completed', 'entered-in-error', 'unknown'])
        procedure['subject'] = 'Patient/' + str(_+1)
        procedure['performedDateTime'] = str(fake.past_datetime(start_date='-1y', tzinfo=None))
        procedures.append(procedure)
    return procedures

# Function to generate immunization data
def generate_immunization_data(num_immunizations):
    immunizations = []
    for _ in range(num_immunizations):
        immunization = {}
        immunization['resourceType'] = 'Immunization'
        immunization['id'] = str(_+1)
        immunization['status'] = 'completed'
        immunization['patient'] = 'Patient/' + str(_+1)
        immunization['occurrenceDateTime'] = str(fake.past_datetime(start_date='-1y', tzinfo=None))
        immunizations.append(immunization)
    return immunizations

# Function to generate observation data
def generate_observation_data(num_observations):
    observations = []
    for _ in range(num_observations):
        observation = {}
        observation['resourceType'] = 'Observation'
        observation['id'] = str(_+1)
        observation['status'] = random.choice(['registered', 'preliminary', 'final', 'amended', 'corrected', 'cancelled', 'entered-in-error', 'unknown'])
        observation['subject'] = 'Patient/' + str(_+1)
        observation['effectiveDateTime'] = str(fake.past_datetime(start_date='-1y', tzinfo=None))
        observation['valueQuantity'] = json.dumps({'value': fake.random_number(digits=2), 'unit': 'mg/dL', 'system': 'http://unitsofmeasure.org', 'code': 'mg/dL'})
        observations.append(observation)
    return observations

# Function to generate location data
def generate_location_data(num_locations):
    locations = []
    for _ in range(num_locations):
        location = {}
        location['resourceType'] = 'Location'
        location['id'] = str(_+1)
        location['status'] = random.choice(['active', 'suspended', 'inactive'])
        location['name'] = fake.word(ext_word_list=['ICU', 'Surgery', 'Pediatrics', 'Emergency', 'Maternity'])
        location['description'] = 'Hospital ward'
        locations.append(location)
    return locations

# Function to generate practitioner data
def generate_practitioner_data(num_practitioners):
    practitioners = []
    for _ in range(num_practitioners):
        practitioner = {}
        practitioner['resourceType'] = 'Practitioner'
        practitioner['id'] = str(_+1)
        practitioner['active'] = True
        practitioner['gender'] = random.choice(['male', 'female'])
        practitioner['birthDate'] = str(fake.date_of_birth(minimum_age=25, maximum_age=65))
        practitioners.append(practitioner)
    return practitioners

# Function to generate care team data
def generate_careteam_data(num_careteams):
    careteams = []
    for _ in range(num_careteams):
        careteam = {}
        careteam['resourceType'] = 'CareTeam'
        careteam['id'] = str(_+1)
        careteam['status'] = random.choice(['proposed', 'active', 'suspended', 'inactive', 'entered-in-error'])
        careteam['subject'] = 'Patient/' + str(_+1)
        careteam['participant'] = json.dumps([{'member': {'reference': 'Practitioner/' + str(_+1)}}])
        careteams.append(careteam)
    return careteams

# Function to generate appointment data
def generate_appointment_data(num_appointments):
    appointments = []
    for _ in range(num_appointments):
        appointment = {}
        appointment['resourceType'] = 'Appointment'
        appointment['id'] = str(_+1)
        appointment['status'] = random.choice(['proposed', 'pending', 'booked', 'arrived', 'fulfilled', 'cancelled', 'noshow', 'entered-in-error'])
        appointment['start'] = str(fake.future_datetime(end_date='+30d', tzinfo=None))
        appointment['end'] = str(fake.future_datetime(end_date='+30d', tzinfo=None) + timedelta(hours=1))
        appointment['participant'] = json.dumps([{'actor': {'reference': 'Patient/' + str(_+1)}, 'status': 'accepted'}])
        appointments.append(appointment)
    return appointments
num_entries = 100

# Generate synthetic data
observations_data = generate_observation_data(num_entries)
locations_data = generate_location_data(num_entries)
practitioners_data = generate_practitioner_data(num_entries)
careteams_data = generate_careteam_data(num_entries)
appointments_data = generate_appointment_data(num_entries)

# Convert to pandas DataFrames
df_observations = pd.DataFrame(observations_data)
df_locations = pd.DataFrame(locations_data)
df_practitioners = pd.DataFrame(practitioners_data)
df_careteams = pd.DataFrame(careteams_data)
df_appointments = pd.DataFrame(appointments_data)


# Generate synthetic data
patients_data = generate_patient_data(num_entries)
encounters_data = generate_encounter_data(num_entries)
conditions_data = generate_condition_data(num_entries)
procedures_data = generate_procedure_data(num_entries)
immunizations_data = generate_immunization_data(num_entries)

# Convert to pandas DataFrames
df_patients = pd.DataFrame(patients_data)
df_encounters = pd.DataFrame(encounters_data)
df_conditions = pd.DataFrame(conditions_data)
df_procedures = pd.DataFrame(procedures_data)
df_immunizations = pd.DataFrame(immunizations_data)

# Save to CSV
df_patients.to_csv('csv_data/patients_data.csv', index=False)
df_encounters.to_csv('csv_data/encounters_data.csv', index=False)
df_conditions.to_csv('csv_data/conditions_data.csv', index=False)
df_procedures.to_csv('csv_data/procedures_data.csv', index=False)
df_immunizations.to_csv('csv_data/immunizations_data.csv', index=False)


# Save to CSV
df_observations.to_csv('csv_data/observations_data.csv', index=False)
df_locations.to_csv('csv_data/locations_data.csv', index=False)
df_practitioners.to_csv('csv_data/practitioners_data.csv', index=False)
df_careteams.to_csv('csv_data/careteams_data.csv', index=False)
df_appointments.to_csv('csv_data/appointments_data.csv', index=False)
