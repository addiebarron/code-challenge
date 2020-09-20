import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        '''Process a request to this API endpoint and return data representing the results of processing.'''

        # Grab the address from our request data
        address = request.query_params.get('address');

        try:
            # Parse the address
            address_components, address_type = self.parse(address);

            # Return the results of a successful parse
            response = {
                'inputString': address,
                'components': address_components,
                'type': address_type
            }
        except Exception as exception:
            # Grab the name of the exception as a string
            exception_name = type(exception).__name__

            # Send a response describing the error
            response = {
                'error': True,
                'exceptionName': exception_name,
                'detail': 'Unable to parse.'
                # Finer exception handling would be a nice next step I think - wasn't able to find documentation on the other types of exceptions thrown by usaddress.
            }

        return Response(response)

    def parse(self, address):
        '''Use the usaddress module to parse a given address into two fields: the type of the address as a string, and its tagged component parts as an OrderedDict.'''

        address_components, address_type = usaddress.tag(address);

        return address_components, address_type
