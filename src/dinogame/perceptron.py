import random
n_input=3 #number of inputs & weights
weights = [random.uniform(-1,1) for x in range(n_input)] #list of weights
inputs = [1]+[int(input("input?")) for x in range(n_input-1)]#how to automate input? 

#print(weights)
print(inputs)

#activation function
def sign(n):
    if n >= 0:
        return 1
    if n < 0:
        return -1



class Perceptron:
    def _init_(self, n_input, func): #extra argument: actfunc?
        self.n_input = n_input
        self.activation_function = func 
       
#make a guess based on input and weight
    def guess(self, inputs):
        Sum = 0.0
        for i in range(self.n_input):
            Sum += float(inputs[i])*float(weights[i])
        # output = sign(Sum)
        output = self.activation_function()
        print(output)
        

    guess(inputs)
            


p = Perceptron(2, sign )
p.guess()
