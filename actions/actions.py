import webbrowser, re, json, requests
import pandas as pd
from actions.zipcodeApi import *
import pathlib
from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

names = pathlib.Path("data/names.txt").read_text().split("\n")
column_names = ["zip"]
df = pd.read_csv("data/uszips.csv", usecols=column_names)
zip = df.zip.to_list()
with open('organization.json') as f:
    data = json.load(f)


class GetJobsOnZipcode(Action):

    def name(self) -> Text:
        return "action_ask_interested_job"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        zipcode = tracker.get_slot("zipcode")
        if zipcode:
            getZipRadius(zipcode)
            dispatcher.utter_message(text="no job found in this zipcode, found these jobs in 50 miles radius")
            dispatcher.utter_message(response="utter_interested_job")

        return []


class AskQuestion1BasedOnJob(Action):
    def name(self) -> Text:
        return "action_ask_Question1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        job_type = tracker.get_slot("interested_job")
        if data["orgId"] == "Cadient":
            if job_type:
                dispatcher.utter_message(text=data["configuration"][0]["questions"][0])
        return []


class AskQuestion2BasedOnJob(Action):

    def name(self) -> Text:
        return "action_ask_Question2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        job_type = tracker.get_slot("interested_job")
        if data["orgId"] == "Cadient":
            if job_type:
                dispatcher.utter_message(text=data["configuration"][0]["questions"][1])
        return []


class AskQuestion3BasedOnJob(Action):

    def name(self) -> Text:
        return "action_ask_Question3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        job_type = tracker.get_slot("interested_job")
        if data["orgId"] == "Cadient":
            if job_type:
                dispatcher.utter_message(text=data["configuration"][0]["questions"][2])
        return []


class AskQuestion4BasedOnJob(Action):

    def name(self) -> Text:
        return "action_ask_Question4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        job_type = tracker.get_slot("interested_job")
        if data["orgId"] == "Cadient":
            if job_type:
                dispatcher.utter_message(text=data["configuration"][0]["questions"][3])
        return []


class AskQuestion5BasedOnJob(Action):

    def name(self) -> Text:
        return "action_ask_Question5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        job_type = tracker.get_slot("interested_job")
        if data["orgId"] == "Cadient":
            if job_type:
                dispatcher.utter_message(text=data["configuration"][0]["questions"][4])
        return []


class AskQuestion6BasedOnJob(Action):

    def name(self) -> Text:
        return "action_ask_Question6"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        job_type = tracker.get_slot("interested_job")
        if data["orgId"] == "Cadient":
            if job_type:
                dispatcher.utter_message(text=data["configuration"][0]["questions"][5])
        return []


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_details_form_2"

    def validate_firstname(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `firstname` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")

        if len(slot_value) <= 2 or slot_value not in names:
            # dispatcher.utter_message(response="utter_name_spelled_correctly")
            # z = tracker.latest_message['text']
            # print(z)

            dispatcher.utter_message(text=f"That's a very short name or I'm assuming you mis-spelled.")
            return {"firstname": None}
        else:
            return {"firstname": slot_value}

    def validate_lastname(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Last name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"lastname": None}
        else:
            return {"lastname": slot_value}

    def validate_job_pos(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        return {"job_pos": slot_value}

    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        if re.search(regex, slot_value):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"this email is not validate !!")
            return {"email": None}

    def validate_zipcode(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the zipcode is super short, it might be wrong.
        print(f"given zipcode = {slot_value}")

        if int(slot_value) in zip:
            return {"zipcode": slot_value}
        else:
            dispatcher.utter_message(text=f"no job found in this zipcode !!")
            return {"zipcode": None}

    def validate_interested_job(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        return {"interested_job": slot_value}

    def validate_submit(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        FirstName = tracker.get_slot("firstname")
        LastName = tracker.get_slot("lastname")
        JobPosition = tracker.get_slot("job_pos")
        Email = tracker.get_slot("email")
        ZipCode = tracker.get_slot("zipcode")
        Interested_Job = tracker.get_slot("interested_job"),
        Question1 = tracker.get_slot("Question1")
        Question2 = tracker.get_slot("Question2")
        Question3 = tracker.get_slot("Question3")
        Question4 = tracker.get_slot("Question4")
        Question5 = tracker.get_slot("Question5")
        Question6 = tracker.get_slot("Question6")

        response = {
            "text": "Thanks for providing the given details....",
            "FirstName": FirstName,
            "LastName": LastName,
            "JobPosition": JobPosition,
            "Email": Email,
            "ZipCode": ZipCode,
            "Interested_Job": Interested_Job,
            "Question1": Question1,
            "Question2": Question2,
            "Question3": Question3,
            "Question4": Question4,
            "Question5": Question5,
            "Question6": Question6
        }

        if slot_value == "yes":
            json_object = json.dumps(response, indent=4)
            with open("data.json", "w") as outfile:
                outfile.write(json_object)

            dispatcher.utter_message(response="utter_details2_thanks",
                                     FirstName=tracker.get_slot("firstname"),
                                     LastName=tracker.get_slot("lastname"),
                                     JobPosition=tracker.get_slot("job_pos"),
                                     Email=tracker.get_slot("email"),
                                     ZipCode=tracker.get_slot("zipcode"),
                                     Interested_Job=tracker.get_slot("interested_job"),
                                     Question1=tracker.get_slot("Question1"),
                                     Question2=tracker.get_slot("Question2"),
                                     Question3=tracker.get_slot("Question3"),
                                     Question4=tracker.get_slot("Question4"),
                                     Question5=tracker.get_slot("Question5"),
                                     Question6=tracker.get_slot("Question6"))
        else:
            dispatcher.utter_message(text="Thank you for your interest")


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_details_form"

    async def required_slots(
            self,
            slots_mapped_in_domain: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> Optional[List[Text]]:

        firstname = tracker.slots.get("firstname")
        # lastname = tracker.slots.get("lastname")
        if firstname is not None:
            if firstname not in names:
                return ["name_spelled_correctly"] + slots_mapped_in_domain

        return slots_mapped_in_domain

    async def extract_name_spelled_correctly(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        intent = tracker.get_intent_of_latest_message()
        print("intent:", intent)
        return {"name_spelled_correctly": intent == "affirm"}

    def validate_name_spelled_correctly(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `firstname` value."""
        print("spell check:", tracker.get_slot("name_spelled_correctly"))
        if tracker.get_slot("name_spelled_correctly"):
            return {"firstname": tracker.get_slot("firstname"), "name_spelled_correctly": True}
        return {"firstname": None, "name_spelled_correctly": None}

    def validate_firstname(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `firstname` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")

        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"firstname": None}
        else:
            return {"firstname": slot_value}

    def validate_lastname(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Last name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"lastname": None}
        else:
            return {"lastname": slot_value}

    def validate_job_pos(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        return {"job_pos": slot_value}

    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if re.search(regex, slot_value):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"this email is not validate !!")
            return {"email": None}

    def validate_zipcode(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the zipcode is super short, it might be wrong.
        print(f"given zipcode = {slot_value}")

        if int(slot_value) in zip:
            return {"zipcode": slot_value}
        else:
            dispatcher.utter_message(text=f"no job found in this zipcode !!")
            return {"zipcode": None}

    def validate_submit(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        if slot_value == "yes":
            dispatcher.utter_message(response="utter_details_thanks",
                                     FirstName=tracker.get_slot("firstname"),
                                     LastName=tracker.get_slot("lastname"),
                                     Email=tracker.get_slot("email"),
                                     ZipCode=tracker.get_slot("zipcode"),
                                     Job=tracker.get_slot("job"))
        else:
            dispatcher.utter_message(text="Thank you for your interest")

# class ValidateCandidateForm(Action):
#     def name(self) -> Text:
#         return "user_details_form"

# def run(
#     self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
# ) -> List[EventType]:
#     required_slots = ["firstname", "lastname", "email", "zipcode", "job"]

#         for slot_name in required_slots:
#             print( tracker.slots.get(slot_name))
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]

#         submit = tracker.get_slot("submit")
#         print(submit)

#         if submit == 'y':
#             return [SlotSet("requested_slot", None)]
#         else:
#             dispatcher.utter_message(text="Thank you for your interest")

# dispatcher.utter_message(response="utter_details_thanks",
#                      FirstName=tracker.get_slot("firstname"),
#                      LastName=tracker.get_slot("lastname"),
#                      Email=tracker.get_slot("email"),
#                      ZipCode=tracker.get_slot("zipcode"),
#                      Job=tracker.get_slot("job"))


# All slots are filled.
