from datashack_sdk import StreamingTable, Column

Users = StreamingTable(
    "users",
    "db1"
)
Users['id'] = Column('string')
Users['age'] = Column('int')
Users['name'] = Column('string')

UserEvents = StreamingTable(
    "users_events",
    "db1"
)
UserEvents['c1'] = Column('string')
UserEvents['c2'] = Column('int')
UserEvents['c3'] = Column('string', partition=True)
UserEvents['c4'] = Column('string')
UserEvents['c5'] = Column('double', partition=True)



