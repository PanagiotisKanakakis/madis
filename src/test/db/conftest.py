import psycopg2
import pytest


@pytest.fixture(scope='session')
def db_connection(docker_services, docker_ip):
    """
    :param docker_services: pytest-docker plugin fixture
    :param docker_ip: pytest-docker plugin fixture
    :return: psycopg2 connection class
    """
    db_settings = {
        'database': 'test_database',
        'user': 'postgres',
        'host': docker_ip,
        'password': '',
        'port': docker_services.port_for('database', 5432),
        'application_name': 'your-app'
    }
    dbc = psycopg2.connect(**db_settings)
    dbc.autocommit = True
    return dbc


@pytest.fixture(autouse=True)
def _mock_db_connection(mocker, db_connection):
    """
    This will alter application database connection settings, once and for all the tests
    in unit tests module.
    :param mocker: pytest-mock plugin fixture
    :param db_connection: connection class
    :return: True upon successful monkey-patching
    """
    mocker.patch('db.database.dbc', db_connection)
    return True
