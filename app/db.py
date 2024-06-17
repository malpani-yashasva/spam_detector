
from . import config
import pathlib
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection

settings = config.get_settings()

DB_CLIENT_ID = settings.astra_db_client_id
DB_CLIENT_SECRET = settings.astra_db_client_secret

BASE_DIR = pathlib.Path(__file__).resolve().parent
SCB_PATH = BASE_DIR / "ignored" / "db_connect.zip"


cluster = Cluster(
    cloud = {"secure_connect_bundle" : SCB_PATH},
    auth_provider= PlainTextAuthProvider(DB_CLIENT_ID, DB_CLIENT_SECRET)
)

def get_session():
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    return session
