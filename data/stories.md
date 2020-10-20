## happy path
* greet
  - action_greet
* chitchat_pricing
  - utter_chitchat_pricing
* chitchat_smart_personal_explainer
  - utter_chitchat_smart_personal_explainer  
* request_contact
  - utter_contact_summary
  - form_contact
  - form{"name":"form_contact"}
  - form{"name":null} 
* goodbye
  - action_bye

## bot challlenge
* out_of_scope
    - action_default_fallback

## bot question
* chitchat_bot
  - utter_chitchat_bot

## path of being smart

* greet
  - action_greet
* chitchat_bot
  - form_smart
  - form{"name":"form_smart"}
  - form{"name":null}
  - utter_chitchat_pricing
