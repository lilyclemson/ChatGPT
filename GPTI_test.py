import OpenAI
import GPTI

def accumuluatetest():
    """
    Checks the different accumulate functions
    """
    tempGPT=GPTI.GPT()
    print("before call log = ", tempGPT.acumulate)
    testar=[{"role":"user","content":"what is my name?"}]
    tempGPT.Completion(testar,"Y")
    print("After call log = ", tempGPT.acumulate)
    tempGPT.clearacumulate()
    print("after a clear call log = ", tempGPT.acumulate)


accumuluatetest()#works!

def convocontinued():
    """
    checks to see if the model recognizes the previous request response
    """
    tempGPT=GPTI.GPT()
    testar=[{"role":"user","content":"my name is Carlos"}]
    answer1=tempGPT.Completion(testar,)
    print(answer1)
    testar1=[{"role":"user","content":"what is my name?"}]
    answer2=tempGPT.Completion(testar1)
    print(answer2)
    

convocontinued()#works!









