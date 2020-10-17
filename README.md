# Snake_game_using_Neural_Nets
AI plays snake game!


Here, I've used neural nets on a game. The network is trained using a 'Feed forward neural net'. Process for data generaton is as follow:-

The process to successfully generate the training data, Use it to train and then use this trained model for prediction is given below:-

1)Make a directory with the name of your choice.
2)Place new_snake_game.py, training_script_snake.py and snake_implementation.py in the same directory.
3)Run the (new_snake_game.py) script to generate the data. (Note:- you have to play the game more than 20 times to generate the data manually. The more you play, The better it will be for our neural network). Pickle will store the training data list in the same directory after data is generated. 

4)Navigate to your working directory, Run training_script_snake.py) script. This script will generate the model, You can monitor the training process and accuracy while it's being trained. If accuracy is not up to the mark, Try learning about what batch_size is, Epochs, learning_rate. Tweak them or play with them or increase the amount of data generated and train again until you get accuracy greater than 80%. The trained model will be saved in the same directory.

5)Run the snake_implementaion.py script and voila!. Enjoy!.


Here are few links you should refer to understand why batch_size plays an important role in training a model and increasing it's accuracy:-

https://machinelearningmastery.com/how-to-control-the-speed-and-stability-of-training-neural-networks-with-gradient-descent-batch-size/


PS:- I had three solutions for the problem:-
    1)Feed forward neural net (I've used this, Generated data manually by playing a lot of games)
    2)Reinforcement learning  (Can be used to solve problems where data cannot be generated easily)
    3)Using genetic algos(When you have absolute no knowledge of anything)
    
   
