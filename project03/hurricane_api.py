from flask import Flask, request
import numpy as np
app = Flask(__name__)
import tensorflow as tf

model = tf.keras.models.load_model('models/hurricane.keras')

@app.route('/models/hurricane/v1', methods=['GET'])
def model_info():
   return {
      "version": "v1",
      "name": "hurricane",
      "description": "Classify images as containing damaged or non-damaged buildings",
      "number_of_parameters": 3453634
   }


def preprocess_input(im):
   """
   Converts user-provided input into an array that can be used with the model.
   This function could raise an exception.
   """
   # convert to a numpy array
   d = np.array(im)
   return(d.reshape(32, 150, 150, 3))

@app.route('/models/hurricane/v1', methods=['POST'])
def classify_damage_image():
   im = request.get_json("image")['image']
   if not im:
      return {"error": "The `image` field is required"}, 404
   try:
      data = preprocess_input(im)
   except Exception as e:
      return {"error": f"Could not process the `image` field; details: {e}"}, 404
   return { "result": model.predict(data).tolist()}


# start the development server
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')