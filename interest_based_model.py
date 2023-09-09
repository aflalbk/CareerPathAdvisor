import random
import time
import sys


#
# list of occupation and its category
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

occupation_responses = [
    "That's wonderful! Education and teaching play a crucial role in shaping future generations.",
    "Impressive choice! Medical and healthcare professionals make a significant impact on people's lives.",
    "Great pick! Engineering and technology drive innovation and progress in our world.",
    "Excellent! Culinary and hospitality bring joy through food and service.",
    "Very commendable! Legal and law enforcement uphold justice and safety.",
    "Fantastic! Creative arts and media inspire and entertain us.",
    "Terrific! Writing and journalism are powerful means of communication.",
    "Impressive! Financial and accounting expertise fuels businesses and economies.",
    "Bravo! Emergency services are vital in times of crisis.",
    "Outstanding! Science and research expand our understanding of the world.",
    "Amazing choice! Entertainment and performing arts bring joy and creativity.",
    "Well done! Psychology and counseling offer valuable support and insights.",
    "Impressive! Construction and building shape our physical environment.",
    "Excellent! Business and sales drive economic growth and innovation.",
    "Great selection! Agriculture and farming ensure our food supply.",
    "Impressive! Aviation and piloting explore the skies and connect the world.",
    "Fascinating! History and research uncover the past's treasures.",
    "Well done! Landscaping and surveying enhance outdoor spaces.",
    "Superb choice! Language and communication bridge understanding.",
    "Excellent! Metalworking and construction craft with precision.",
    "Impressive! Chemistry and research delve into the world of molecules.",
    "Outstanding! Mathematics and statistics are the universal language.",
    "Great pick! Optometry and vision care preserve eye health.",
    "Well done! Medical imaging and radiology offer vital insights.",
    "Bravo! Therapists and healthcare professionals aid in healing and well-being.",
    "Impressive! Zoology and animal science explore the wonders of nature.",
    "Great choice! Economics and analysis unravel market dynamics.",
    "Outstanding! Park and wildlife management protect our natural heritage.",
    "Excellent! Museum and curation preserve our cultural treasures.",
    "That's intriguing! 'Other' opens up a world of possibilities for exploration."
]


def slow_type(text, delay=0.00):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)


# replay based on answer.
answer = input("Do you want a suggestion to help you select your dream job? (answer yes or no)")
answer = answer.lower()
if answer == "yes":
    slow_type("Okay, choose your interested category from the list and enter its number \n", 0.03)

    # printing one by one category in the category-list (typing style).
    for category in distinct_category_list:
        slow_type(category,0.01)
        time.sleep(0.01)
        print()

    # taking the number of category from user
    num_cato = int(input())

    # handling input above 30.
    while num_cato > 30:
        num_cato = int(input("Please select a number from the list."))

    # finding the matching category in the list
    num_selected_cato = distinct_category_list[num_cato - 1]
    # removing number part from the num_selected_cato
    if num_cato < 10:
        selected_cato = num_selected_cato[3:]
    else:
        selected_cato = num_selected_cato[4:]
    # simple personalized appreciation for choosing the category (typing style).
    slow_type(occupation_responses[num_cato - 1], 0.03)
    print()
    # set a boolean to avoid unnecessary looping
    find = False
    # set an empty list for stor occupation of selected category
    selected_occupation = []
    for occupation_category in occupation_category_list:
        # appending matching values to the selected_occupation.
        if occupation_category[1] == selected_cato:
            selected_occupation.append(occupation_category[0])
            find = True
        else:
            if not find:
                continue
            else:
                break

    # print a random Occupation from the list
    slow_type(f"If you have a passion for the {selected_cato} category, I have a wonderful recommendation for you."
              f" Consider pursuing a career as a {random.choice(selected_occupation)}.", 0.03)
elif answer == "no":
    slow_type("That's perfectly fine! If you ever change your mind or have any questions in the future, feel free to "
              "reach out. I'm here to help.", 0.03)
else:
    print("Please enter yes or no")
