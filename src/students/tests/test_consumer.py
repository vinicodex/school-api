import pytest
from unittest.mock import patch, MagicMock
from src.students.services.consumer import consume_messages, callback

@pytest.fixture
def mock_pika_connection():
    with patch('src.students.services.consumer.pika.BlockingConnection') as mock_connection:
        yield mock_connection

def test_callback():
    mock_channel = MagicMock()
    mock_method = MagicMock()
    mock_properties = MagicMock()
    body = b'Test message'

    with patch('builtins.print') as mock_print:
        callback(mock_channel, mock_method, mock_properties, body)
        mock_print.assert_called_with(' [x] Received b\'Test message\'')

@pytest.mark.django_db
def test_consume_messages(mock_pika_connection):
    mock_connection_instance = mock_pika_connection.return_value
    mock_channel = mock_connection_instance.channel.return_value

    with patch('builtins.print') as mock_print:
        consume_messages()
        mock_pika_connection.assert_called_once()
        mock_channel.queue_declare.assert_called_with(queue='create_student')
        mock_channel.basic_consume.assert_called_with(queue='create_student', on_message_callback=callback, auto_ack=True)
        mock_channel.start_consuming.assert_called_once()
        mock_print.assert_any_call(' [*] Waiting for messages. To exit press CTRL+C')
