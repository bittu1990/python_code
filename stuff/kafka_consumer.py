from kafka import KafkaConsumer
import sys
import pandas as pd


def consumer_app():
    """
    This will create a Kafka Consumer to access the data published over the required topic
    :param self: No parameters
    :return: List of JSON
    """
    bootstrap_servers = ['localhost:9092']
    topicName = 'DurstexpreesTopic'
    consumer = KafkaConsumer(topicName, group_id='group1', bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='earliest', consumer_timeout_ms=2000)
    json_list = []
    for message in consumer:
        consumer.commit()
        # print(message.value.decode('ascii'))
        json_list.append(message.value.decode('ascii'))
    # consumer.close()

    return json_list


def main_data_process():
    """
    This is to process data received from Kafka consumer as JSON list
    """
    json_data = consumer_app()
    print(len(json_data))
    df_user_data = pd.DataFrame(json_data)
    print(len(df_user_data['id'].unique()))


main_data_process()
