from my_app.models.users import Users
from datashack.testing import datashack_test

@datashack_test
def test_users():
    test_data = {
        'id': 'test',
        'name': 'test', 
        'email': 'test@test.com',
    }

    # publish new event!
    Users.insert(test_data)

    # should be saved!
    assert Users.list()[0] == test_data
