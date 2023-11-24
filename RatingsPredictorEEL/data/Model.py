# import pickle

# class Model:
#     def __init__(self, rf_classifier):
#         self.rf_classifier = rf_classifier

#     def load_model(self, formdata):
#         # Load the model using pickle
#         with open('random_forest_model.pkl', 'rb') as file:
#             loaded_model = pickle.load(file)
#         rating_predict = loaded_model.predict(formdata)

# # Assuming rf_classifier is defined in the same module or script
# # Initialize the Model class with rf_classifier
# model_instance = Model(rf_classifier)

# # Save the model
# model_instance.save_model()

# # Load the model and make predictions
# # You need to pass the appropriate formdata to the load_model method
# formdata = ...
# model_instance.load_model(formdata)
