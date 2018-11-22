from sqlalchemy import Column, String, Integer

from modules.database.base import BaseModel


class Board(BaseModel):
    __tablename__ = 'OT_BOARD_T'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    bg_color = Column(String(10))
    active = Column(Integer)
    user_id = Column(Integer)

    def __init__(self, name='', bg_color='', active=1):
        self.name = name
        self.bg_color = bg_color
        self.active = active

    def __repr__(self):
        return '<Board: name={} bg_color={}>'.format(self.name, self.bg_color)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'bg_color': self.bg_color,
            'active' : self.active
        }

    @staticmethod
    def deserialize(json_obj):
        if type(json_obj) is type({}):
            b = Board()
            if 'name' in json_obj:
                b.name = json_obj['name']
            if 'bg_color' in json_obj:
                b.bg_color = json_obj['bg_color']
            if 'active' in json_obj:
                b.active = json_obj['active']
            return b