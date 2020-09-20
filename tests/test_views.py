import pytest


def test_api_parse_succeeds(client):
    '''Test that the API parses a valid address string successfully and returns data in the correct structure.'''
    
    address_string = '123 main st chicago il'
    
    response = client.get('/api/parse/', {'address': address_string })
    
    assert response.data == {
        'inputString': address_string,
        'components': {
            'AddressNumber':        '123',
            'StreetName':           'main',
            'StreetNamePostType':   'st',
            'PlaceName':            'chicago',
            'StateName':            'il',
        }, 
        'type': 'Street Address'
    }


def test_api_parse_raises_error(client):
    '''Test that the API returns an exception when parsing an invalid string string successfully and returns the correct exception name.'''
    
    address_string = '123 main st chicago il 123 main st'
    
    response = client.get('/api/parse/', {'address': address_string})
    # Could this call ^ be fixturized for DRYer code? 
    
    assert response.data['error'] == True and response.data['exceptionName'] == 'RepeatedLabelError'
