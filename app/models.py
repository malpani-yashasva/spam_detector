from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
import uuid

class SpamInference(Model):
    __keyspace__ = "spam_inference"
    uuid = columns.UUID(primary_key=True, default = uuid.uuid1)
    query = columns.Text()
    label = columns.Text()
   