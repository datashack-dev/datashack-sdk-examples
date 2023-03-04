const { StreamingTable, Column } = require('datashack_sdk_js');

const Users = new StreamingTable(
  "users",
  "db1"
);
Users.addColumn('id', 'string');
Users.addColumn('age', 'int');
Users.addColumn('name', 'string');

const UserEvents = new StreamingTable(
  "users_events",
  "db1"
);
UserEvents.addColumn('c1', 'string');
UserEvents.addColumn('c2', 'int');
UserEvents.addColumn('c3', 'string', { partition: true });
UserEvents.addColumn('c4', 'string');
UserEvents.addColumn('c5', 'double', { partition: true });
