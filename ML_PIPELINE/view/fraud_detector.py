import joblib
from os import system
model = None


def load_model() -> None:
    global model

    model = joblib.load('../model/fraud-detector.pkl')


if __name__ == '__main__':
    print('loading model... please wait 😀')
    load_model()
    
    system('cls')
    print("fraud perdiction----------------------")
    distance_from_home=float(input("give the distance of transaction from home: "))
    distance_from_last_transaction=float(input("Give the distance from where last transaction happened:"))
    repeat_retailer=int(input("Have you repeated retailer write yes(1) or no(0):"))
    used_card=int(input("Mode of payment is card write yes(1) or no(0):"))
    used_pin=int(input("used pin or not write yes(1) or no(0):"))
    online_order=int(input("you place order online write yes(1) or no(0):"))
    perdicted_value=model.predict([[distance_from_home,distance_from_last_transaction,repeat_retailer,
    used_card,used_pin,online_order]])
    print(perdicted_value[0])
    if(perdicted_value[0]):
        print("you are in danger of credit card fraud")
    else:
        print("you are safe from credit card fraud")    