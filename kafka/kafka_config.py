import os

SECURITY_PROTOCOL = "SASL_SSL"
SSL_MACHENISM = "PLAIN"
API_KEY = "M7AF5MHWTEHMM42X"
ENDPOINT_SCHEMA_URL = "https://poi-4qwer.us-central1.gcp.confluent.cloud"
API_SECRET_KEY = "8VvGLYI2keS9ZFGFNaGfq7uUk0oWLbkxFr9lSzkbAca9lfxDPPjTKk/234dfghl"
BOOTSTRAP_SERVER = "plm-fgbhn.us-west4.gcp.confluent.cloud:9092"
SCHEMA_REGISTRY_API_KEY = "3NMBHCDFG67U8I"
SCHEMA_REGISTRY_API_SECRET = "UXlUK633aEEp3aX2jjienBc0AfnoF/Fe33AaWRaCVGHTYU71nEakg8WA5kfQHu"


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 'bootstrap.servers': BOOTSTRAP_SERVER,
                 'security.protocol': SECURITY_PROTOCOL,
                 'sasl.username': API_KEY,
                 'sasl.password': API_SECRET_KEY
                 }
    return sasl_conf


def schema_config():
    return {'url': ENDPOINT_SCHEMA_URL,

            'basic.auth.user.info': f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

            }
