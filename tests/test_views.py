import pytest


@pytest.mark.parametrize(
    'address,expected_status,expected_data',
    [
        (
            '123 main st chicago il',
            200,
            {
                'status': 'success',
                'inputString': '123 main st chicago il',
                'components': {
                    'AddressNumber':        '123',
                    'StreetName':           'main',
                    'StreetNamePostType':   'st',
                    'PlaceName':            'chicago',
                    'StateName':            'il',
                },
                'type': 'Street Address',
            }
        ),
        (
            '123 main st chicago il 123 main st',
            500,
            {
                'status': 'error',
                'error': 'RepeatedLabelError',
                'message': 'The server encountered an error parsing that address.',
            },
        ),
    ],
)
def test_api_parse(client, address, expected_data, expected_status):
    '''Test that the API handles both a valid and an invalid address string and returns data in the correct structure as well as a correct status code.'''

    response = client.get('/api/parse/', {'address': address})

    assert response.data == expected_data and response.status_code == expected_status
