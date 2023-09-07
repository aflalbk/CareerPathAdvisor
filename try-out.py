occupation_text = """Teacher
Professor
Librarian
Doctor
Nurse
Dentist
Pharmacist
Pediatrician
Veterinarian
Paramedic
Dental Hygienist
Engineer
Electrician
Software Developer
Carpenter
Surveyor
Welder
Biomedical Engineer
Computer Programmer
Chef
Waiter/Waitress
Barista
Baker
Flight Attendant
Wedding Planner
Lawyer
Police Officer
Police Detective
Social Worker
Artist
Musician
Actor
Photographer
Graphic Designer
Makeup Artist
Fashion Designer
News Anchor
Museum Curator
Writer
Journalist
Accountant
Financial Analyst
Actuary
Firefighter
Scientist
Geologist
Astronomer
Archaeologist
Biologist
Forensic Scientist
Marine Biologist
Environmental Scientist
Musician
Actor
Psychologist
Carpenter
Plumber
Salesperson
Real Estate Agent
Social Media Manager
Farmer
Pilot
Flight Instructor
Historian
Landscaper
Surveyor
Translator
Welder
Chemist
Mathematician
Optometrist
Radiologist
Radiologic Technologist
Speech Therapist
Occupational Therapist
Physical Therapist
Chiropractor
Acupuncturist
Zoologist
Economist
Park Ranger
Museum Curator
Hairdresser
Forensic Scientist
Marine Biologist
Wedding Planner
News Anchor
Environmental Scientist
Personal Trainer
Human Resources Manager
Museum Curator
Speech Pathologist
"""
category_text = """Education and Teaching
Education and Teaching
Education and Teaching
Medical and Healthcare
Medical and Healthcare
Medical and Healthcare
Medical and Healthcare
Medical and Healthcare
Medical and Healthcare
Medical and Healthcare
Medical and Healthcare
Engineering and Technology
Engineering and Technology
Engineering and Technology
Engineering and Technology
Engineering and Technology
Engineering and Technology
Engineering and Technology
Engineering and Technology
Culinary and Hospitality
Culinary and Hospitality
Culinary and Hospitality
Culinary and Hospitality
Culinary and Hospitality
Culinary and Hospitality
Legal and Law Enforcement
Legal and Law Enforcement
Legal and Law Enforcement
Legal and Law Enforcement
Creative Arts and Media
Creative Arts and Media
Creative Arts and Media
Creative Arts and Media
Creative Arts and Media
Creative Arts and Media
Creative Arts and Media
Creative Arts and Media
Creative Arts and Media
Writing and Journalism
Writing and Journalism
Financial and Accounting
Financial and Accounting
Financial and Accounting
Emergency Services
Science and Research
Science and Research
Science and Research
Science and Research
Science and Research
Science and Research
Science and Research
Science and Research
Entertainment and Performing Arts
Entertainment and Performing Arts
Psychology and Counseling
Construction and Building
Construction and Building
Business and Sales
Business and Sales
Business and Sales
Agriculture and Farming
Aviation and Piloting
Aviation and Piloting
History and Research
Landscaping and Surveying
Landscaping and Surveying
Language and Communication
Metalworking and Construction
Chemistry and Research
Mathematics and Statistics
Optometry and Vision Care
Medical Imaging and Radiology
Medical Imaging and Radiology
Therapists and Healthcare
Therapists and Healthcare
Therapists and Healthcare
Therapists and Healthcare
Therapists and Healthcare
Zoology and Animal Science
Economics and Analysis:
Park and Wildlife Management
Museum and Curation
Other
Other
Other
Other
Other
Other
Other
Other
Other
Other"""

distinct_category_text = """Education and Teaching
Medical and Healthcare
Engineering and Technology
Culinary and Hospitality
Legal and Law Enforcement
Creative Arts and Media
Writing and Journalism
Financial and Accounting
Emergency Services
Science and Research
Entertainment and Performing Arts
Psychology and Counseling
Construction and Building
Business and Sales
Agriculture and Farming
Aviation and Piloting
History and Research
Landscaping and Surveying
Language and Communication
Metalworking and Construction
Chemistry and Research
Mathematics and Statistics
Optometry and Vision Care
Medical Imaging and Radiology
Therapists and Healthcare
Zoology and Animal Science
Economics and Analysis:
Park and Wildlife Management
Museum and Curation
Other"""

'''
occupation_list = occupation_text.splitlines()
category_list = category_text.splitlines()
distinct_category_list = distinct_category_text.splitlines()
print(occupation_list, '\n', category_list)
print(len(occupation_list), len(category_list))
print(distinct_category_list)

occupation_category_list = []
for x in range(len(occupation_list)):
    occupation_category_list.append([occupation_list[x], category_list[x]])

distinct_category_list_with_number = []
for x in range(len(distinct_category_list)):
    distinct_category_list_with_number.append(f"{x+1}. " + distinct_category_list[x])

print(distinct_category_list_with_number)

print(occupation_category_list)
print(len(occupation_category_list))

ans = ["golden 234", "gryt rutyh", "ehrtg erjt"]
adt = ans[1]
print(adt[3:])

'''
import random

occupation_category_list = [['Teacher', 'Education and Teaching'], ['Professor', 'Education and Teaching'],
                            ['Librarian', 'Education and Teaching'], ['Doctor', 'Medical and Healthcare'],
                            ['Nurse', 'Medical and Healthcare'], ['Dentist', 'Medical and Healthcare'],
                            ['Pharmacist', 'Medical and Healthcare'], ['Pediatrician', 'Medical and Healthcare'],
                            ['Veterinarian', 'Medical and Healthcare'], ['Paramedic', 'Medical and Healthcare'],
                            ['Dental Hygienist', 'Medical and Healthcare'], ['Engineer', 'Engineering and Technology'],
                            ['Electrician', 'Engineering and Technology'],
                            ['Software Developer', 'Engineering and Technology'],
                            ['Carpenter', 'Engineering and Technology'], ['Surveyor', 'Engineering and Technology'],
                            ['Welder', 'Engineering and Technology'],
                            ['Biomedical Engineer', 'Engineering and Technology'],
                            ['Computer Programmer', 'Engineering and Technology'], ['Chef', 'Culinary and Hospitality'],
                            ['Waiter/Waitress', 'Culinary and Hospitality'], ['Barista', 'Culinary and Hospitality'],
                            ['Baker', 'Culinary and Hospitality'], ['Flight Attendant', 'Culinary and Hospitality'],
                            ['Wedding Planner', 'Culinary and Hospitality'], ['Lawyer', 'Legal and Law Enforcement'],
                            ['Police Officer', 'Legal and Law Enforcement'],
                            ['Police Detective', 'Legal and Law Enforcement'],
                            ['Social Worker', 'Legal and Law Enforcement'], ['Artist', 'Creative Arts and Media'],
                            ['Musician', 'Creative Arts and Media'], ['Actor', 'Creative Arts and Media'],
                            ['Photographer', 'Creative Arts and Media'],
                            ['Graphic Designer', 'Creative Arts and Media'],
                            ['Makeup Artist', 'Creative Arts and Media'],
                            ['Fashion Designer', 'Creative Arts and Media'], ['News Anchor', 'Creative Arts and Media'],
                            ['Museum Curator', 'Creative Arts and Media'], ['Writer', 'Writing and Journalism'],
                            ['Journalist', 'Writing and Journalism'], ['Accountant', 'Financial and Accounting'],
                            ['Financial Analyst', 'Financial and Accounting'], ['Actuary', 'Financial and Accounting'],
                            ['Firefighter', 'Emergency Services'], ['Scientist', 'Science and Research'],
                            ['Geologist', 'Science and Research'], ['Astronomer', 'Science and Research'],
                            ['Archaeologist', 'Science and Research'], ['Biologist', 'Science and Research'],
                            ['Forensic Scientist', 'Science and Research'],
                            ['Marine Biologist', 'Science and Research'],
                            ['Environmental Scientist', 'Science and Research'],
                            ['Musician', 'Entertainment and Performing Arts'],
                            ['Actor', 'Entertainment and Performing Arts'],
                            ['Psychologist', 'Psychology and Counseling'], ['Carpenter', 'Construction and Building'],
                            ['Plumber', 'Construction and Building'], ['Salesperson', 'Business and Sales'],
                            ['Real Estate Agent', 'Business and Sales'], ['Social Media Manager', 'Business and Sales'],
                            ['Farmer', 'Agriculture and Farming'], ['Pilot', 'Aviation and Piloting'],
                            ['Flight Instructor', 'Aviation and Piloting'], ['Historian', 'History and Research'],
                            ['Landscaper', 'Landscaping and Surveying'], ['Surveyor', 'Landscaping and Surveying'],
                            ['Translator', 'Language and Communication'], ['Welder', 'Metalworking and Construction'],
                            ['Chemist', 'Chemistry and Research'], ['Mathematician', 'Mathematics and Statistics'],
                            ['Optometrist', 'Optometry and Vision Care'],
                            ['Radiologist', 'Medical Imaging and Radiology'],
                            ['Radiologic Technologist', 'Medical Imaging and Radiology'],
                            ['Speech Therapist', 'Therapists and Healthcare'],
                            ['Occupational Therapist', 'Therapists and Healthcare'],
                            ['Physical Therapist', 'Therapists and Healthcare'],
                            ['Chiropractor', 'Therapists and Healthcare'],
                            ['Acupuncturist', 'Therapists and Healthcare'], ['Zoologist', 'Zoology and Animal Science'],
                            ['Economist', 'Economics and Analysis:'], ['Park Ranger', 'Park and Wildlife Management'],
                            ['Museum Curator', 'Museum and Curation'], ['Hairdresser', 'Other'],
                            ['Forensic Scientist', 'Other'], ['Marine Biologist', 'Other'],
                            ['Wedding Planner', 'Other'], ['News Anchor', 'Other'],
                            ['Environmental Scientist', 'Other'], ['Personal Trainer', 'Other'],
                            ['Human Resources Manager', 'Other'], ['Museum Curator', 'Other'],
                            ['Speech Pathologist', 'Other']]
# list of categories.
distinct_category_list = ['1. Education and Teaching', '2. Medical and Healthcare', '3. Engineering and Technology',
                          '4. Culinary and Hospitality', '5. Legal and Law Enforcement', '6. Creative Arts and Media',
                          '7. Writing and Journalism', '8. Financial and Accounting', '9. Emergency Services',
                          '10. Science and Research', '11. Entertainment and Performing Arts',
                          '12. Psychology and Counseling', '13. Construction and Building', '14. Business and Sales',
                          '15. Agriculture and Farming', '16. Aviation and Piloting', '17. History and Research',
                          '18. Landscaping and Surveying', '19. Language and Communication',
                          '20. Metalworking and Construction', '21. Chemistry and Research',
                          '22. Mathematics and Statistics', '23. Optometry and Vision Care',
                          '24. Medical Imaging and Radiology', '25. Therapists and Healthcare',
                          '26. Zoology and Animal Science', '27. Economics and Analysis:',
                          '28. Park and Wildlife Management', '29. Museum and Curation', '30. Other']

print("okay, Choose you interested category from the list, and enter the numer of it \n")
# printing one by one category in the category-list.
for category in distinct_category_list:
    print(category)
# taking the number of category from user
num_cato = int(input())
print(num_cato)
# finding the matching category in the list
num_selected_cato = distinct_category_list[num_cato - 1]
print(num_selected_cato)
# removing number part from the num_selected_cato
if num_cato < 10:
    selected_cato = num_selected_cato[3:]
else:
    selected_cato = num_selected_cato[4:]
print(selected_cato)
find = False
selected_occupation = []
for occupation_category in occupation_category_list:
    if occupation_category[1] == selected_cato:
        selected_occupation.append(occupation_category[0])
        find = True
    else:
        if not find:
            continue
        else:
            break

print(selected_occupation)
# print a random Occupation from the list
print(random.choice(selected_occupation))
