# Importing some useful functions. 
from random import random
from random import randrange

def getRandomWeight():
    '''
        purpose: generate random value between -1 and 1 and return it.
        parms: None
        return: Range: -1 to 1 
    '''
    r_no = random()
    neg = randrange(1,11,1)
    if neg <= 5:
        return round(r_no,2)
    return round(r_no * -1,2)

class perceptron:
    '''
        Mimic the perperties of the Bilogical neuron.
        Constructor:
            + __init__(no_of_inputs, learning_rate,threshold) 
        Instance Methods: 
            + train(input_data, output_data, iterations)
            + predict(test_data)
            + set_weights(weights) 
    '''
    def __init__(self, no_of_inputs, learning_rate,threshold):
        self.no_of_inputs = no_of_inputs
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.weights = [getRandomWeight() for x in range(no_of_inputs)]
    def train(self, input_data, output_data, iterations):
        for iteration in range(iterations): # For each iteration defined.
            out_data_index = 0 # Pointer for output_data [list]
            for input_row in input_data: # For each row in matrix.
                sum_ = self._cal_sum(input_row) # Calculate sum for each input row.
                actual_out = self._activation_function(sum_)
                if actual_out != output_data[out_data_index]: # If actual_out does't equals to espected output
                    error = output_data[out_data_index] - actual_out
                    new_weights = self._compute_new_weights(input_row,error)
                    self.weights = new_weights # Assign new Weights
                out_data_index = out_data_index + 1 # After each iteration increment it by One. 
    def predict(self, test_data):
        if len(test_data[0]) != len(self.weights):
            # Raise the excpetion if the test data shape did not match with the trained data sahpe.
            raise Exception(f'Test Data Length did not match: test_data_size= {test_data[0]} != train_data_size= {len(self.weights)}')
        result = []
        for test_row in test_data:
            sum_ = self._cal_sum(test_row)
            out_ = self._activation_function(sum_)
            result.append(out_) 
        return result
    def _cal_sum(self, inputs):
        sum_ = 0
        corr_weight_index = 0 # Corresponding Weight Index
        for no_ in inputs:
            sum_ = sum_ +  no_ * self.weights[corr_weight_index]
            corr_weight_index = corr_weight_index + 1
        return sum_    
    def _activation_function(self,cal_sum):
        return 1 if cal_sum > self.threshold else 0 # unit step Function  	
    def _compute_new_weights(self, inputs, error):  
        new_weights = []
        corr_weight_index = 0 # Corresponding weight index
        for input_val in inputs:
            wi = self.weights[corr_weight_index]
            new_weights.append(round(wi + (self.learning_rate*input_val*error),2)) 
        return new_weights
    def set_weights(self,weights): # Assign your own weights
        self.weights = weights    
    def __str__(self):
        return f'Perceptron(learning_rate{self.learning_rate}, threshold={self.threshold}, weights={self.weights})'


def main():
    # ------------Traning for OR Gate------------
    print('-------OR Gate Traning-------')
    OR_perceptron = perceptron(no_of_inputs=2,learning_rate=0.1,threshold=0)
    print('Before Traning: ',OR_perceptron)
    train_data = [ [0,0],[0,1],[1,0],[1,1] ]
    target_data = [0, 1, 1, 1]
    OR_perceptron.train(train_data, target_data, iterations=3)
    print('After Traning: ',OR_perceptron)
    test_data = [[1,1],[0,0],[1,0],[0,1]]
    predicted = OR_perceptron.predict(test_data)
    for index in range(len(test_data)):
        print(test_data[index],' -> ', predicted[index])
    print()    
    # ------------Traning for AND Gate------------
    print('-------AND Gate Traning-------')    
    AND_perceptron = perceptron(no_of_inputs=2,learning_rate=0.1,threshold=0.2)
    print('Before Traning: ',AND_perceptron)
    train_data = [ [0,0],[0,1],[1,0],[1,1] ]
    target_data = [0, 0, 0, 1]
    AND_perceptron.train(train_data, target_data, iterations=12)
    print('After Traning: ',AND_perceptron)
    test_data = [[1,1],[0,0],[1,0],[0,1]]
    predicted = AND_perceptron.predict(test_data)
    for index in range(len(test_data)):
        print(test_data[index],' -> ', predicted[index])

    # ------------Traning for 2x2 Image to identify black or white pixel------------
    print('')
    print('-------[2x2] Black and White pixel Traning-------')
    PIXEL_perceptorn = perceptron(no_of_inputs=4,learning_rate=0.1,threshold= 0.1)
    print('Before Traning: ',PIXEL_perceptorn)
    train_data = [  [0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],
                    [0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],
                    [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],
                    [1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
    target_data = [0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1]
    PIXEL_perceptorn.train(train_data, target_data, iterations=100)
    print('After Traning: ',PIXEL_perceptorn)
    test_data = [[0,1,1,0],[0,1,0,0]]
    predicted = PIXEL_perceptorn.predict(test_data)
    for index in range(len(test_data)):
        print(test_data[index],' -> ', predicted[index])

if __name__ == '__main__':
	main()
