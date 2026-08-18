import os
from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN", "arn:aws:sns:us-east-1:123456789012:TrafficAlerts")
sns_client = boto3.client("sns", region_name="us-east-1")

@app.route("/traffic-data", methods=["POST"])
def process_traffic():
    data = request.get_json()
    camera_id = data.get("camera_id", "CAM_01")
    vehicle_count = data.get("vehicle_count", 0)

    threshold = 80
    if vehicle_count > threshold:
        message = f"ALERT: High traffic congestion detect at the camera {camera_id}! Vehicle count: {vehicle_count}"
        try:
            sns_client.publish(
                TopicArn=SNS-TOPIC_ARN,
                Message=message,
                Subject="Smart City Traffic Alert"
            )
            return jsonify({"status": "ALERT_SENT", "message":message}), 200
        except Exception as e:
            return jsonify({"status" : "FAILED_TO_SEND_ALERT", "ERROR" : str(e)}), 500
        return jsonify({"status" : "NORMAL", "vehicle_count" : vehicle_count}), 200
    if __name__ == "__main__":
        app.run(host="0..0.0.0", port=5001)
        
