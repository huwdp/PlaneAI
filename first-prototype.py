# Code taken from https://towardsdatascience.com/train-image-recognition-ai-with-5-lines-of-code-8ed0bdd8d9ba
# Not tested yet!!!

from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()

model_trainer.setModelTypeAsResNet()

model_trainer.setDataDirectory("planeai")

model_trainer.trainModel(num_objects=10, num_experiments=200, enhance_data=True, batch_size=32, show_network_summary=True)
