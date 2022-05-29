# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionGetPincode(Action):

    def name(self) -> Text:
        return "action_get_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}")
        dispatcher.utter_message(f"Your state for the pincode is {res.json()[0]['PostOffice'][0]['State']}")
        return []


class ActionGetState(Action):

    def name(self) -> Text:
        return "action_get_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}")
        dispatcher.utter_message(f"you City name is {res.json()[0]['PostOffice'][0]['Name']}")
        return []


class ActionGetDistrict(Action):

    def name(self) -> Text:
        return "action_get_district"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}")
        dispatcher.utter_message(f"Your district name is {res.json()[0]['PostOffice'][0]['District']}")
        return []
