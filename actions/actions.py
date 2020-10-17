# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
import requests


class FormContact(FormAction):

    def name(self) -> Text:
        return "form_contact"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["email","phone-number"]        

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        data = {
            "phone_number":tracker.get_slot("phone-number"),
            "email":tracker.get_slot("email"),
            # "message":tracker.get_slot("message"),
         
        }
        requests.post("http://thecreativeorchards.com/c-bot/public/bot/contact", json=data)

        dispatcher.utter_message(template="utter_form_thankyou")

        return [SlotSet("phone-number", None),SlotSet("email", None)]


class ActionBye(Action):

    def name(self) -> Text:
        return "action_bye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.request("GET","http://thecreativeorchards.com/c-bot/public/bot/bye")
        json_data = response.json()
        feeback =json_data["message"]
        dispatcher.utter_message(text= feeback)

        return []



class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.request("GET","http://thecreativeorchards.com/c-bot/public/bot/greeting")
        json_data = response.json()
        feeback =json_data["message"]
        dispatcher.utter_message(text= feeback)

        return []
