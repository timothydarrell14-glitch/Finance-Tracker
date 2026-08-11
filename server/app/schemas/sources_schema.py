from extensions import ma
from models.sources import Sources

class SourcesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sources
        load_instance = True
        include_fk = True
        unknown = ma.EXCLUDE

source_schema = SourcesSchema()
sources_schema = SourcesSchema(many=True)