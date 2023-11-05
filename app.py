from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

def load_model():
    print("Loading model...")
    global model
    model = joblib.load('rfmodel.pkl')

    return None

load_model()

@app.route('/ping')
def ping():
    return 'pong'


@app.route('/predict')
def predict():
    # acc_max gyro_max acc_kurtosis gyro_kurtosis lin_max lin_kurtosis acc_skewness gyro_skewness post_gyro_max post_lin_max
    arr = []
    return 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)