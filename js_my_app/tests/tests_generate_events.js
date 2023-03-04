const Users = require('./my_app/models/users');
const { datashack_test } = require('datashack/testing');

datashack_test(function test_users() {
  const test_data = {
    'id': 'test',
    'name': 'test', 
    'email': 'test@test.com',
  };

  // publish new event!
  Users.insert(test_data);

  // should be saved!
  assert.deepStrictEqual(Users.list()[0], test_data);
});
