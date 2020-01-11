# PlaneAI
PlaneAI is a learning project used for recognizing fighter jet aircraft using an artificial intelligence. 

The project will use the resources listed below to build the system.
* https://towardsdatascience.com/train-image-recognition-ai-with-5-lines-of-code-8ed0bdd8d9ba
* https://www.pyimagesearch.com/2018/09/10/keras-tutorial-how-to-get-started-with-keras-deep-learning-and-python/

The models are placed within the train directory and then the aircraft name, so ./train/F-22/etc. Models will not be included due to _legal reasons_.

# Setup
```
sudo apt-get install python
sudo apt update
sudo apt install python3-dev python3-pip
sudo pip3 install -U virtualenv  # system-wide install
virtualenv --system-site-packages -p python3 ./venv
pip3 install --upgrade pip
pip3 install --upgrade tensorflow
pip3 install --upgrade opencv-python
pip3 install --upgrade keras
pip3 install --upgrade imageai --upgrade
```

Ensure python3 is used.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
