from sqlalchemy import Column, Integer, String

import db


class InterfaceMap(db.Base):
    __tablename__ = 'interfacemap'

    id = Column(Integer, primary_key=True)
    vrf = Column(String)
    export_map = Column(String)

    def __init__(self, vrf, export_map):
        self.vrf = vrf
        self.export_map = export_map

    def __str__(self):
        return f'{self.id} | {self.vrf} | {self.export_map}'
