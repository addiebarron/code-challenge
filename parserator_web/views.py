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
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.

        address = request.query_params.get('address');

        try:
            address_components, address_type = self.parse(address);
            response = {
                'components': address_components,
                'type': address_type
            }
        except Exception as exception:
            exception_name = type(exception).__name__
            response = {
                'error': True,
                'exceptionName': exception_name,
                'detail': 'Unable to parse.'
                # Finer exception handling would be a nice next step I think
            }

        return Response(response)

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        address_components, address_type = usaddress.tag(address);

        return address_components, address_type
