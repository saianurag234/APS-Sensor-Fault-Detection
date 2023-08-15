import os

SECURITY_PROTOCOL = "SASL_SSL"
SSL_MACHENISM = "PLAIN"
API_KEY = "M7AF5MHWTEHMM42X"
ENDPOINT_SCHEMA_URL = "https://psrc-4nrnd.us-central1.gcp.confluent.cloud"
API_SECRET_KEY = "8VvGLYI2keS9ZFGFNaGfq7uUk0oWLbkxFr9lSzkbAca9lfxDPPjTKk/1o+NrSsJ4"
BOOTSTRAP_SERVER = "pkc-6ojv2.us-west4.gcp.confluent.cloud:9092"
SCHEMA_REGISTRY_API_KEY = "3NMBHCKPYMUP6EPE"
SCHEMA_REGISTRY_API_SECRET = "UXlUK633aEEp3aX2jjienBc0AfnoF/Fe33AaWRaKvW99CyfkT1nEakg8WA5kfQHu"


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
