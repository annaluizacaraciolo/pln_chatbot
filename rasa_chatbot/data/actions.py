from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionConfirmFlightDetails(Action):
    def name(self) -> Text:
        return "action_confirm_flight_details"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Retrieve information from slots
        departure_location = tracker.get_slot("location")
        arrival_location = tracker.get_slot("location")
        date_range = tracker.get_slot("time")
        passengers = tracker.get_slot("amount_people")

        # Customize the confirmation message based on extracted details
        confirmation_message = (
            f"Sure! I will search for round-trip flights from {departure_location} to {arrival_location} "
            f"for the dates {date_range} with {passengers} passengers."
        )

        # Confirm the flight details
        dispatcher.utter_message(text=confirmation_message)

        return []
