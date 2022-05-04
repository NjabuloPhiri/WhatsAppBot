# WhatsAppBot

A simple program to make conversations possible between a WhatsApp user and the Twilio API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python, Django and Twilio.

```bash
pip install python
```

```bash
pip install twilio
```

```bash
pip install Django
```

## Usage

```python
from twilio.twiml.messaging_response import MessagingResponse

# returns reply from Twilio Sandbox
reply = MessagingResponse()

if message == 'my message':
   reply.message('Sandbox reply')
   return HttpResponse(str(reply))
```

## Demo 1
This is a very basic version of the solution. From being able to send messages between the Sandbox and a WhatsApp user, the next step is manipulating the response from the user -- which comes as XML -- such that it is stripped of the XML tags and only the message string is left. The string can then be added onto a database, from which it can later be called to present a summary of the responses from the user.

## License
[MIT](https://choosealicense.com/licenses/mit/)
