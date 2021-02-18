from threading import Thread

s_fw = True
s_st = 0

def main():
    global s_fw, s_st
    from time import sleep
    import RPi.GPIO as GPIO
    import sys

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    # PIN-Zuweisung am Raspberry
    A=8
    B=10
    C=12
    D=16
    time = 0.001#default: 0.001  //Min: 0.0008
    # PINS definieren
    GPIO.setup(A,GPIO.OUT)
    GPIO.setup(B,GPIO.OUT)
    GPIO.setup(C,GPIO.OUT)
    GPIO.setup(D,GPIO.OUT)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)

    # Ansteuerung der Spulen des Motors
    def Step1():
        print("step1")
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(D, True)
        sleep (time)
        GPIO.output(D, False)

    def Step2():
        print("step2")
        GPIO.output(D, True)
        GPIO.output(C, True)
        sleep (time)
        GPIO.output(D, False)
        GPIO.output(C, False)

    def Step3():
        print("step3")
        GPIO.output(C, True)
        sleep (time)
        GPIO.output(C, False)

    def Step4():
        print("step4")
        GPIO.output(B, True)
        GPIO.output(C, True)
        sleep (time)
        GPIO.output(B, False)
        GPIO.output(C, False)
    def Step5():
        print("step5")
        GPIO.output(B, True)
        sleep (time)
        GPIO.output(B, False)
    def Step6():
        print("step6")
        GPIO.output(A, True)
        GPIO.output(B, True)
        sleep (time)
        GPIO.output(A, False)
        GPIO.output(B, False)
    def Step7():
        print("step7")
        GPIO.output(A, True)
        sleep (time)
        GPIO.output(A, False)
    def Step8():
        print("step8")
        GPIO.output(D, True)
        GPIO.output(A, True)
        sleep (time)
        GPIO.output(D, False)
        GPIO.output(A, False)
    # Eine komplette Umdrehung starten


    def forward(degrees):
        for i in range (degrees):
            Step1()
            Step2()
            Step3()
            Step4()
            Step5()
            Step6()
            Step7()
            Step8()

    def backward(degrees):
        for i in range (degrees):
            Step8()
            Step7()
            Step6()
            Step5()
            Step4()
            Step3()
            Step2()
            Step1()

    #360 Grad = 512 ste
        
        
    def runner():
        GPIO.setup(A,GPIO.OUT)
        GPIO.setup(B,GPIO.OUT)
        GPIO.setup(C,GPIO.OUT)
        GPIO.setup(D,GPIO.OUT)
        GPIO.output(A, False)
        GPIO.output(B, False)
        GPIO.output(C, False)
        GPIO.output(D, False)
        
        global s_fw, s_st
        while True:
            #print("s_st:"+str(s_st))
            if s_st!=1:
                if s_fw:
                    forward(10)
                else:
                    backward(10)
                sleep(s_st)

    movement(0)


    runner()


def movement(value):
    global s_fw, s_st
    print("Move: "+str(value))
    forward = (value>0)
    if(value<0):
        value*=-1
    stoptime=(1-value)
    s_fw = forward
    s_st = float(stoptime)


    
t = Thread(target=main)
t.daemon = True
t.start()




