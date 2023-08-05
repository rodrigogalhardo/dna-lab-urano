import pika
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurações de conexão RabbitMQ
credentials = pika.PlainCredentials('dsqngzqh', 'SdHCABNVg71QnRthoaLwb690ukLK58kX')
parameters = pika.ConnectionParameters(
    host='porpoise.rmq.cloudamqp.com',
    port=5672,
    virtual_host='dsqngzqh',
    credentials=credentials,
    ssl=True,
    ssl_options={
        "ssl_version": ssl.PROTOCOL_TLSv1_2
    }
)


@app.route('/send', methods=['POST'])
def send_to_queue():
    try:
        data = request.json
        message = data.get('message')

        if not message:
            return jsonify({'error': 'Missing message'}), 400

        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_publish(exchange='', routing_key='hello', body=message)
        print(f" [x] Sent '{message}'")

        connection.close()

        return jsonify({'message': 'Message sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9010)
