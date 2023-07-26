import json
from faker import Faker
import random
from datetime import timedelta
import pandas as pd

fake = Faker('en_US')

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

def generate_encounter_data(num_encounters):
    encounters = []
    for _ in range(num_encounters):
        encounter = {}
        encounter['resourceType'] = 'Encounter'
        encounter['id'] = str(_+1)
        encounter['status'] = random.choice(['planned', 'arrived', 'triaged', 'in-progress', 'onleave', 'finished', 'cancelled'])
        encounter['subject'] = {'reference': 'Patient/' + str(_+1)}
        encounters.append(encounter)
    return encounters

def generate_condition_data(num_conditions):
    conditions = []
    for _ in range(num_conditions):
        condition = {}
        condition['resourceType'] = 'Condition'
        condition['id'] = str(_+1)
        condition['subject'] = {'reference': 'Patient/' + str(_+1)}
        conditions.append(condition)
    return conditions

def generate_procedure_data(num_procedures):
    procedures = []
    for _ in range(num_procedures):
        procedure = {}
        procedure['resourceType'] = 'Procedure'
        procedure['id'] = str(_+1)
        procedure['status'] = random.choice(['completed', 'in-progress', 'not-done'])
        procedure['subject'] = {'reference': 'Patient/' + str(_+1)}
        procedures.append(procedure)
    return procedures

def generate_immunization_data(num_immunizations):
    immunizations = []
    for _ in range(num_immunizations):
        immunization = {}
        immunization['resourceType'] = 'Immunization'
        immunization['id'] = str(_+1)
        immunization['status'] = 'completed'
        immunization['patient'] = {'reference': 'Patient/' + str(_+1)}
        immunizations.append(immunization)
    return immunizations

def generate_observation_data(num_observations):
    observations = []
    for _ in range(num_observations):
        observation = {}
        observation['resourceType'] = 'Observation'
        observation['id'] = str(_+1)
        observation['status'] = 'final'
        observation['subject'] = {'reference': 'Patient/' + str(_+1)}
        observations.append(observation)
    return observations

def generate_location_data(num_locations):
    locations = []
    for _ in range(num_locations):
        location = {}
        location['resourceType'] = 'Location'
        location['id'] = str(_+1)
        location['status'] = 'active'
        locations.append(location)
    return locations

def generate_practitioner_data(num_practitioners):
    practitioners = []
    for _ in range(num_practitioners):
        practitioner = {}
        practitioner['resourceType'] = 'Practitioner'
        practitioner['id'] = str(_+1)
        practitioner['active'] = True
        practitioner['name'] = [{'use': 'official', 'family': fake.last_name(), 'given': [fake.first_name()]}]
        practitioners.append(practitioner)
    return practitioners

def generate_careteam_data(num_careteams):
    careteams = []
    for _ in range(num_careteams):
        careteam = {}
        careteam['resourceType'] = 'CareTeam'
        careteam['id'] = str(_+1)
        careteam['status'] = 'active'
        careteam['subject'] = {'reference': 'Patient/' + str(_+1)}
        careteams.append(careteam)
    return careteams

def generate_appointment_data(num_appointments):
    appointments = []
    for _ in range(num_appointments):
        appointment = {}
        appointment['resourceType'] = 'Appointment'
        appointment['id'] = str(_+1)
        appointment['status'] = 'booked'
        appointment['start'] = str(fake.future_datetime(end_date='+30d', tzinfo=None))
        appointment['end'] = str(fake.future_datetime(end_date='+30d', tzinfo=None) + timedelta(hours=1))
        appointment['participant'] = [{'actor': {'reference': 'Patient/' + str(_+1)}, 'status': 'accepted'}]
        appointments.append(appointment)
    return appointments


def generate_synthetic_data(num_patients=100, num_encounters=100, num_conditions=100, num_procedures=100, num_immunizations=100, num_observations=100, num_locations=10, num_practitioners=10, num_careteams=10, num_appointments=10):
    # Generate synthetic patient data
    patients_data = generate_patient_data(num_patients)
    
    # Generate synthetic encounter (hospital admission) data
    encounters_data = generate_encounter_data(num_encounters)
    
    # Generate synthetic condition (diagnosis) data
    conditions_data = generate_condition_data(num_conditions)
    
    # Generate synthetic procedure data
    procedures_data = generate_procedure_data(num_procedures)
    
    # Generate synthetic immunization data
    immunizations_data = generate_immunization_data(num_immunizations)
    
    # Generate synthetic observation (test result) data
    observations_data = generate_observation_data(num_observations)
    
    # Generate synthetic location (hospital bed) data
    locations_data = generate_location_data(num_locations)
    
    # Generate synthetic practitioner data
    practitioners_data = generate_practitioner_data(num_practitioners)
    
    # Generate synthetic care team data
    careteams_data = generate_careteam_data(num_careteams)
    
    # Generate synthetic appointment data
    appointments_data = generate_appointment_data(num_appointments)
    
    # Combine all data into one dictionary
    all_data = {
        'patients': patients_data,
        'encounters': encounters_data,
        'conditions': conditions_data,
        'procedures': procedures_data,
        'immunizations': immunizations_data,
        'observations': observations_data,
        'locations': locations_data,
        'practitioners': practitioners_data,
        'careteams': careteams_data,
        'appointments': appointments_data
    }
    
    return all_data

# Generate synthetic data
synthetic_data = generate_synthetic_data()

# convert to csv
# df = pd.DataFrame(synthetic_data)
# df.to_csv('synthetic_data.csv', index=False)


# Save synthetic data to a JSON file
with open('synthetic_data.json', 'w') as f:
    json.dump(synthetic_data, f, indent=4)
