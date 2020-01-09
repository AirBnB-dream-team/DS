import numpy as np
import pickle
from tensorflow.keras.models import load_model
class Predictor():


    def __init__(self):

        # Loading the encoder
        self.pickle_in = open('encoder.pickle', 'rb')
        self.encoder = pickle.load(pickle_in)
        self.pickle_in.close()

        # Loading the model
        self.model = load_model('final_model.h5')


    def get_pred(bedrooms: int=2,
                bathrooms: int=2,
                zipcode: int=78702,
                property_type: str='House',
                room_type: str='Entire home/apt'):
                
        """
        Takes 5 inputs and returns a numeric prediction:

        Keyword args:
            bedrooms: int, number of bedrooms
            bathrooms: int, number of bathrooms
            zipcode: int, zipcode of location
            property_type: string, type of property
            room_type: string, type of room
        """

        num_array = np.array([[bedrooms, bathrooms]])
        cat_array = np.array([[zipcode, property_type, room_type]])

        encoded_cat = self.encoder.transform(cat_array)
        encoded_cat = encoded_cat.toarray()

        array_final = np.concatenate((num_array, encoded_cat), axis=1)

        pred = self.model.predict(array_final)

        return round(pred[0][0], 2)
