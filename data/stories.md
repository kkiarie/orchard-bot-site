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
  - action_restart
* goodbye
  - action_bye

## bot challlenge
* bot_challenge
    - action_default_fallback

## bot question
* chitchat_bot
  - utter_chitchat_bot

## Story from conversation with a874810377d64b65880417b70c5482e2 on October 17th 2020

* greet
    - action_greet
* positive
    - utter_positive
* chitchat_pricing
    - utter_chitchat_pricing
* request_contact
    - utter_contact_summary
    - form_contact
    - form{"name":"form_contact"}
    - slot{"requested_slot":"email"}
* deny{"email":"kevin@mayfair.co.ke"}
    - slot{"email":"kevin@mayfair.co.ke"}
    - slot{"email":"kevin@mayfair.co.ke"}
    - form_contact
    - slot{"email":"kevin@mayfair.co.ke"}
    - slot{"requested_slot":"phone-number"}
* goodbye{"phone-number":"(+25) 4715295492"}
    - slot{"phone-number":"(+25) 4715295492"}
    - slot{"phone-number":"(+25) 4715295492"}
    - form_contact
    - slot{"email":"kevin@mayfair.co.ke"}
    - slot{"phone-number":"(+25) 4715295492"}

## Story Request contact

* request_contact
    - utter_contact_summary
    - form_contact
    - form{"name":"form_contact"}
    - slot{"requested_slot":"email"}
* chitchat_pricing{"email":"tabbi@gmail.com"}
    - slot{"email":"tabbi@gmail.com"}
    - form_contact
    - slot{"email":"tabbi@gmail.com"}
    - slot{"requested_slot":"phone-number"}
* greet{"phone-number":"(+25) 4710712167"}
    - slot{"phone-number":"(+25) 4710712167"}
    - form_contact
    - slot{"phone-number":"(+25) 4710712167"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - action_bye
