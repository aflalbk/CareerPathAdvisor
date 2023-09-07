import random

# list of 100 Occupations.
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

# replay based on answer.
answer = input("Do you want a suggestion to help you select your dream job? (answer yes or no)")
answer = answer.lower()
if answer == "yes":
    # print a random Occupation from the list
    print(random.choice(occupations_list))
elif answer == "no":
    print("That's perfectly fine! If you ever change your mind or have any questions in the future, feel free to "
          "reach out. I'm here to help.")
else:
    print("Please enter yes or no")
