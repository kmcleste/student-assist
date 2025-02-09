# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from emoji import emojize


class ActionHaystackSearch(Action):

    def name(self) -> Text:
        return "action_info_retrieval"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# call hs api get the response and return it in dispatcher
        dispatcher.utter_message(text="Calling haystack and returning search results....")

        return []

class ActionDefaultAskAffirmation(Action):
    def name(self):
        return "action_default_ask_affirmation"
    
    async def run(self, dispatcher, tracker, domain):
        # select the top 2 intents from the tracker        
        # ignore the first one -- nlu fallback
        #predicted_intents = tracker.latest_message["intent_ranking"][1:3]
        
        # A prompt asking the user to select an option
        message = "Sorry! I am not able to understand you. Can you rephrase or do you want to intelligent search CCI?"
        
        # # a mapping between intents and user friendly wordings
        # intent_mappings = {
        #     "supply_contact_info": "Supply Contact Information",
        #     "affirm": "Agree",
        #     "deny": "Disagree",
        #     "goodbye": "End conversation"
        # }
        # # show the top three intents as buttons to the user
        # buttons = [
        #     {
        #         "title": intent_mappings[intent['name']],
        #         "payload": "/{}".format(intent['name'])
        #     }
        #     for intent in predicted_intents
        # ]
        buttons = [
            {
                "title": 'Yes ' + emojize(":thumbs_up:"),
                "payload": "/info_retrieval"
            },
            {
                "title": 'No ' +  emojize(":thumbs_down:"),
                "payload": "/deny_info_retrieval"
            }
            
        ]
        
        # add a "none of these button", if the user doesn't
        # agree when any suggestion
        buttons.append({
            "title": "Helpdesk",
            "payload": "/helpdesk"
        })
        dispatcher.utter_message(text=message, buttons=buttons)
        return []