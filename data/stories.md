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

## path of being smart

* greet
  - action_greet
* chitchat_bot
  - form_smart
  - form{"name":"form_smart"}
  - form{"name":null}
  - utter_chitchat_pricing

## New Story

* greet
    - action_greet
* chitchat_bot
    - form_smart
    - form{"name":"form_smart"}
    - slot{"requested_slot":"number"}
* out_of_scope{"number":30}
    - slot{"number":30}
    - slot{"number":30}
    - form_smart
    - slot{"number":30}
    - slot{"number":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_chitchat_pricing
    - slot{"number":30}
* chitchat_smart_personal_explainer
    - utter_chitchat_smart_personal_explainer
* request_contact
    - utter_contact_summary
    - form_contact
    - form{"name":"form_contact"}
    - slot{"requested_slot":"email"}
* out_of_scope{"email":"kkiarie4@gmail.com"}
    - slot{"email":"kkiarie4@gmail.com"}
    - slot{"email":"kkiarie4@gmail.com"}
    - form_contact
    - slot{"email":"kkiarie4@gmail.com"}
    - slot{"requested_slot":"phone-number"}
* out_of_scope{"phone-number":"(+25) 4715295492"}
    - slot{"phone-number":"(+25) 4715295492"}
    - slot{"phone-number":"(+25) 4715295492"}
    - form_contact
    - slot{"phone-number":"(+25) 4715295492"}
    - slot{"phone-number":null}
    - slot{"email":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - slot{"number":30}
    - slot{"email":"kkiarie4@gmail.com"}
    - slot{"phone-number":"(+25) 4715295492"}
    - action_bye

## New Story

* request_contact
    - utter_contact_summary
    - form_contact
    - form{"name":"form_contact"}
    - slot{"requested_slot":"email"}
* out_of_scope{"email":"it@mail.com"}
    - slot{"email":"it@mail.com"}
    - slot{"email":"it@mail.com"}
    - form_contact
    - slot{"email":"it@mail.com"}
    - slot{"requested_slot":"phone-number"}
* out_of_scope{"phone-number":"(+25) 4710010000"}
    - slot{"phone-number":"(+25) 4710010000"}
    - slot{"phone-number":"(+25) 4710010000"}
    - form_contact
    - slot{"phone-number":"(+25) 4710010000"}
    - slot{"phone-number":null}
    - slot{"email":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - slot{"email":"it@mail.com"}
    - slot{"phone-number":"(+25) 4710010000"}
    - action_bye

## New Story

* greet
    - action_greet
* chitchat_bot
    - form_smart
    - form{"name":"form_smart"}
    - slot{"requested_slot":"number"}
* out_of_scope{"number":14}
    - slot{"number":14}
    - form_smart
    - slot{"number":14}
    - slot{"number":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_chitchat_pricing
* request_contact
    - utter_contact_summary
    - form_contact
    - form{"name":"form_contact"}
    - slot{"requested_slot":"email"}
* out_of_scope{"email":"kelvin.kiarie@mayfair.co.ke"}
    - slot{"email":"kelvin.kiarie@mayfair.co.ke"}
    - form_contact
    - slot{"email":"kelvin.kiarie@mayfair.co.ke"}
    - slot{"requested_slot":"phone-number"}
* out_of_scope{"phone-number":"(+25) 4715295492"}
    - slot{"phone-number":"(+25) 4715295492"}
    - form_contact
    - slot{"phone-number":"(+25) 4715295492"}
    - slot{"phone-number":null}
    - slot{"email":null}
    - form{"name":null}
    - slot{"requested_slot":null}

## New Story

* intergration_of_smart_assistant
    - utter_application_response

## New Story

* development_cycle
    - utter_time_for_development
* billing_integration
    - utter_billing_platforms
