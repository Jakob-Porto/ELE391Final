# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pickle # he turned himself into a, funniest thing I ever
import pip
pip.main(['install','scikit-learn'])
def minMax(val:float,min:float,max:float)->float:
    return (val-min)/(max-min)
def returnNeural():
    with open("isBrokenNeural.pkl", "rb") as f:
        neuralModel=pickle.load(f)


def main():
    with open("isBrokenNeural.pkl", "rb") as f:
        neuralModel=pickle.load(f)
    with open("isBrokenKNN.pkl", "rb") as f:
        KNNModel = pickle.load(f)
    with open("isBrokenRandomForrest.pkl", "rb") as f:
        RandomForestModel=pickle.load(f)
    tempSTR:str=input("Do you want to predict a value, type Y for yes and n for no: ")
    while tempSTR=="Y":
        tempMod:int=int(input("Please select the model, 0 for Neural network, 1 for KNN, and 2 for Random Forrest: "))
        airTemp: float = minMax(float(input("Enter the air temperature: ")), 295.3, 304.5)
        procTemp: float = minMax(float(input("Enter the process temperature: ")), 305.7, 313.8)
        rot: float = minMax(float(input("Enter the rotational speed: ")),1168,2076)
        torque: float = minMax(float(input("Enter the torque: ")),16.7,68.9)
        tool: float = minMax(float(input("Enter the tool use: ")),0,253)
        type: str = input("Enter the type, H for high, M for medium, and L for low: ")
        lis=[]
        if type=="H":
            lis=[1,0,0]
        elif type=="M":
            lis=[0,0,1]
        elif type=="L":
            lis=[0,1,0]
        else:
            lis=[0,0,0]


        if tempMod==0:
            results=neuralModel.predict([[airTemp,procTemp,rot,torque,tool]+lis])
        elif tempMod==1:
            results=KNNModel.predict([[airTemp,procTemp,rot,torque,tool]+lis])
        elif tempMod==2:
            neuralModel.RandomForestModel.predict([[airTemp,procTemp,rot,torque,tool]+lis])
        print(int(results[0]))
        tempSTR: str = input("Do you want to predict another value, type Y for yes and n for no: ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
