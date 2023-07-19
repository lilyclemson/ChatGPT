import Emotionset
import random
testingset=Emotionset.emotionSetter("the student")
# Anger Happy Fear Confusion
testemotions=[(random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3)),
              (random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3)),
              (random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3)),
              (random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3)),
              (random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3)),]
for test in testemotions:
    Anger,Happy,Fear,Confusion=test
    result=testingset.generate_greeting(Anger,Happy,Fear,Confusion)
    print("Anger={Ang},Happy={Hap},Fear={Fea},Confusion={Con},Result={res}".format(Ang=Anger,Hap=Happy,Con=Confusion,Fea=Fear,res=result))


