#Step1 : pip install requests
#Step2 : Open Google form and get the pre-filled link and identify the inputs requires (eg_link) https://docs.google.com/forms/d/e/1FAIpQLSdEpKD5qTGuRricxRp1p48Agjk8nR0wGbrdxRD5Fqw7OlW3Fw/viewform?usp=pp_url&entry.305685618=Option+1&entry.704311461=janub78@gmail.com&entry.60239828=Janu+Basil&entry.2128855103=Working+Professional&entry.1791362013=17-24&entry.824953496=Male&entry.100361457=15000+-+25000&entry.1393506013=Always&entry.692832308=Agree&entry.500419387=Sadness&entry.1117779231=Sometimes&entry.1435977934=Yes&entry.1860442754=Very+Effective&entry.1603822592=Yes,+somewhat&entry.1859443271=Emotional+Storytelling&entry.295802879=Rarely&entry.1403180056=Neutral&entry.1924770571=Yes&entry.1062432079=Sometimes&entry.2048070578=Disagree&entry.1828168511=Likely&entry.29275047=Agree&entry.2127042845=Social+Media&entry.1663764009=Yes&entry.1168960511=Yes,+clearly&entry.2051398078=Email+Marketing&entry.1543516883=Neutral&entry.1400134732=Wow
#Step3 : write the data block with entry.ID like below
#Step4 : run the python script

import requests  # Importing the requests module to send HTTP requests

# URL of the Google Form 'formResponse' endpoint
url = "https://docs.google.com/forms/d/e/1FAIpQLSdEpKD5qTGuRricxRp1p48Agjk8nR0wGbrdxRD5Fqw7OlW3Fw/formResponse"

# List of names and emails to be submitted to the form
names_and_emails = [
    # List of name-email pairs to submit to the form
    ("ravi", "ravi123@gmail.com"),
    ("sundar", "sundar456@gmail.com"),
    # Add more names and emails here as needed...
]

# Loop through each name and email pair in the list
for name, email in names_and_emails:
    # Prepare the form data with appropriate field names and values
    data = {
        "entry.305685618": "Option 1",  # Selecting "Option 1" for a specific question
        "entry.704311461": email,       # Submitting the email for the respective user
        "entry.60239828": name,         # Submitting the name for the respective user
        "entry.2128855103": "Working Professional",  # Choosing an option for occupation
        "entry.1791362013": "17-24",    # Choosing an age group
        "entry.824953496": "Male",      # Choosing gender
        "entry.100361457": "15000 - 25000",  # Submitting salary range
        "entry.1393506013": "Always",  # Frequency option
        "entry.692832308": "Agree",    # Agreeing to a specific statement
        "entry.500419387": "Sadness",  # Emotion selection
        "entry.1117779231": "Sometimes",  # Frequency option for another question
        "entry.1435977934": "Yes",     # Choosing "Yes" for a specific question
        "entry.1860442754": "Very Effective",  # Rating a particular statement
        "entry.1603822592": "Yes, somewhat",  # Rating a different statement
        "entry.1859443271": "Emotional Storytelling",  # Choosing a storytelling style
        "entry.295802879": "Rarely",   # Frequency selection
        "entry.1403180056": "Neutral",  # Submitting a neutral response
        "entry.1924770571": "Yes",     # Choosing "Yes" for another question
        "entry.1062432079": "Sometimes",  # Frequency selection for another question
        "entry.2048070578": "Disagree",  # Choosing "Disagree"
        "entry.1828168511": "Likely",  # Likelihood selection
        "entry.29275047": "Agree",     # Agreement with a statement
        "entry.2127042845": "Social Media",  # Choosing "Social Media" for a specific question
        "entry.1663764009": "Yes",     # Choosing "Yes"
        "entry.1168960511": "Yes, clearly",  # Agreeing to clarity
        "entry.2051398078": "Email Marketing",  # Selecting "Email Marketing"
        "entry.1543516883": "Neutral",  # Rating as "Neutral"
        "entry.1400134732": "Wow"      # Reaction to a statement
    }

    # Sending a POST request to the Google Form with the data
    response = requests.post(url, data=data)

    # Checking if the form submission was successful (status code 200 or 302)
    if response.status_code in [200, 302]:
        print(f"Form submitted successfully for {name} ({email})!")
    else:
        # If submission failed, print the error status code
        print(f"Failed to submit form for {name} ({email}). Status code: {response.status_code}")
