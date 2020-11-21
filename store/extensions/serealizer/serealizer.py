from store.extensions.serealizer import ma
from store.extensions.database.models import Shoes

class ShoeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Shoes
        include_relationships = True
        load_instance = True