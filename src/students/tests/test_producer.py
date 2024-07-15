import pytest
from unittest.mock import patch
from src.students.services.producer import send_message

@pytest.fixture
def mock_pika_connection():
    with patch('src.students.services.producer.pika.BlockingConnection') as mock_connection:
        yield mock_connection

@pytest.mark.django_db
def test_send_message(mock_pika_connection):
    mock_connection_instance = mock_pika_connection.return_value
    mock_channel = mock_connection_instance.channel.return_value
    student_data = {
        'name': 'John Doe',
        'age': 25,
        'course': 'Computer Science'
    }

    with patch('builtins.print') as mock_print:
        send_message(student_data)
        mock_pika_connection.assert_called_once()
        mock_channel.queue_declare.assert_called_with(queue='create_student')
        mock_channel.basic_publish.assert_called_with(exchange='', routing_key='create_student', body='{"name": "John Doe", "age": 25, "course": "Computer Science"}')
        mock_connection_instance.close.assert_called_once()
        mock_print.assert_called_with(' [x] Sent {"name": "John Doe", "age": 25, "course": "Computer Science"}')
