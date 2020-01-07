import numpy as np
from tensorflow.keras.models import load_model


model = load_model('baseline_model.h5')

test = np.array([[3.0, 4.0, 78704]])

pred = model.predict(test)

print(pred[0][0])