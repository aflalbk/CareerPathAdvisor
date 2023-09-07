import time
import sys

occupations_list = ['Teacher', 'Doctor', 'Engineer', 'Chef', 'Police Officer', 'Nurse', 'Artist', 'Lawyer',
                    'Accountant', 'Firefighter', 'Writer', 'Electrician', 'Dentist', 'Architect', 'Musician',
                    'Scientist', 'Pharmacist', 'Plumber', 'Actor', 'Psychologist', 'Librarian', 'Waiter/Waitress',
                    'Farmer', 'Pilot', 'Photographer', 'Software Developer', 'Hairdresser', 'Carpenter',
                    'Graphic Designer', 'Journalist', 'Veterinarian', 'Barista', 'Baker', 'Salesperson', 'Chef',
                    'Electrician', 'Geologist', 'Makeup Artist', 'Astronomer', 'Paramedic', 'Real Estate Agent',
                    'Biologist', 'Pediatrician', 'Social Worker', 'Mechanic', 'Flight Attendant', 'Historian',
                    'Archaeologist', 'Landscaper', 'Surveyor', 'Translator', 'Welder', 'Chemist', 'Mathematician',
                    'Optometrist', 'Radiologist', 'Pharmacist', 'Financial Analyst', 'Archaeologist',
                    'Speech Therapist', 'Event Planner', 'Fashion Designer', 'Zoologist', 'Economist',
                    'Archaeologist', 'News Anchor', 'Park Ranger', 'Electrician', 'Accountant',
                    'Social Media Manager', 'Surveyor', 'Paramedic', 'Forensic Scientist', 'Flight Instructor',
                    'Wedding Planner', 'Marine Biologist', 'Economist', 'Librarian', 'Radiologic Technologist',
                    'Veterinarian', 'Acupuncturist', 'Graphic Designer', 'Landscaper', 'Nurse Practitioner',
                    'Architect', 'Dental Hygienist', 'Actuary', 'Biomedical Engineer', 'Computer Programmer',
                    'Personal Trainer', 'Environmental Scientist', 'Physical Therapist', 'Astronomer', 'Hairdresser',
                    'Chiropractor', 'Police Detective', 'Human Resources Manager', 'Museum Curator',
                    'Occupational Therapist', 'Speech Pathologist']
"""
for text in occupations_list:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
        # Adjust the sleep duration to control the typing speed
    time.sleep(0.2)
    print()

print()  # To move to the next line after typing
"""
import time
import random
import sys


def slow_type(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


text_to_type = "This is text being typed out."
for text in occupations_list:
    slow_type(text)
    time.sleep(0.2)
    print()
print()  # To move to the next line after typing
