from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse

"""
This view handles the messaging between the
whatsapp user and the Twilio sandbox.
"""
account_sid = 'ACcd5ff20cc0ef9cf2eeff5f8f3132ad5e'
auth_token = '5362783749d08632d988f4d56bcf5df6'
client = Client(account_sid, auth_token)


@csrf_exempt
def twilio_bot(request):
    # Receive message from whatsapp user
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')

    # Send a response to the user

    if message == 'Hi' or 'Hey' or 'Hello':
        response = MessagingResponse()
        response.message('Hi there! What do you think'
                         ' is the best sauce for a '
                         'sandwich?\n'
                         '1. Mayonaise\n'
                         '2. Sweet chilli\n'
                         '3. BBQ')

        reply = MessagingResponse()

        """
        Since reply is in xml, I should figure
        out a way to extract the message from the
        xml tags, and have it ready to be stored
        in a database.
        """

        if message == 'Mayonaise':
            reply.message('You like the sandwich rich and creamy!')
            return HttpResponse(str(reply))
        if message == 'Sweet chilli':
            reply.message('Hot but not too hot, huh?')
            return HttpResponse(str(reply))
        if message == 'BBQ':
            reply.message('You never go wrong with BBQ!')
            return HttpResponse(str(reply))

        return HttpResponse(str(response))

    return HttpResponse(twilio_bot)
