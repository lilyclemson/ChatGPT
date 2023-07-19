
import openai
import GPTI


class emotionSetter:
    def __init__(self  ,who="",context="",model="gpt-3.5-turbo",api_key="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"):
        """
        When an emotionSetter object is created a GPT Object is also created using the shared parameters.
        the "who" parameter is inserted to the prompt to provide more context 
        model controls what model is being used to complete the API request (only gpt-3.5-turbo for ChatCompletion)
        Context and "who" passed to GPT,developed here
        """
        self.gpt=GPTI.GPT(who=who,model=model,temp=1,api_key=api_key)
        self.who=who
        self.model=model
        self.api_key=api_key
      
    
   
    def categorizeA(self,Ang):
        """
        Ang is an int value between 1-3
        and is then used to determine what string to return
        """
        if Ang >2:
            Anger="Angry"
        if Ang<= 2:
            Anger=" "
        return Anger
    def categorizeF(self,Fea):
        """
        Fea is an int value between 1-3
        and is then used to determine what string to return
        """
        if Fea >2:
            Feamood="scared"
        if Fea<=2:
            Feamood =" "
        return Feamood
    def categorizeC(self,Con):
        """
        Con is an int value between 1-3
        and is then used to determine what string to return
        """
        if Con >2:
            Conf="confused"
        if Con<=2:
            Conf =" "
        return Conf
        
        
        
    def contracheck(self,Ang,Hap,Fea,Con):
        """
        All parameters are integers between 1-3
        contracheck returns the appropriate string that represents the happiness score however can also
        remove the string entirely to limit direct contradictions in emotions passed, to avoid situations like "I am Happy, Angry, Confused and Scared"
        """
        if ((Hap )<Ang)and Hap>=1:
            return ""
        if ((Hap )<Fea) and Hap>=1:
            return ""
        if ((Hap)<Con)and Hap>=1:
            return ""
        if (Hap)>1:
            return "Happy,"
        if (Hap)<=1:
            return "Depressed" 
    def neutralcheck(self,Ang,Hap,Fea,Con):
        """
        Neutralcheck is in theory an unnecessary function that just lets you know if the prompt is neutral
        (only the single emotion of happy) or not (anything else)
        """
        if Hap<=1:
            print("False: not neutral scenerio")
            return False
        if (Ang and Fea and Con)<=2:
            print("True: neutral response deployed")
            return True
    def neutralcat(self):
        """
        Only is called if neutralcheck is true and therefore only returns one string "Happy"
        """
        Hap="happy"
        return Hap
    def generate_greeting(self,Ang,Hap,Fea,Con):
        """
        Generate_greeting is the first function called when creating a call. Uses an emotion setter object along with four neccesary parameters
        The four parameters are ints between 1-3 though not strict as in the code wont break if its above or below those numbers
        A list is passed to the call itself as a JSON
        """
        prompt=self.generate_prompt(Ang,Hap,Fea,Con)
        ex=self.gpt
        messages=[ 
             ("system", "You are a helpful assistant"),
             ("user", "I feel happy.  Give me an approptiate greeting in reference to my mood."),
             ("assistant", "Hello, you seem well how is your day?"),
             ("user", "I feel  depressed. Give me an an appropriate greeting in reference to my mood."),
             ("assistant", "You dont seem to be doing so well today what has got you down?"),
             ("user", "I feel Angry. Give me an appropriate greeting in reference to my mood."),
             ("assistant","You seem riled up today, what is angering you today?"),
             ("user", "I feel Angry, Scared and Confused. Give me an appropriate greeting in reference to my mood."),
             ("assistant","Hello, it sounds like you're experiencing a mix of emotions right now, how can I help you?"),
             ("user",(prompt)+"Give me an appropriate greeting in reference to my mood."),
                  ]
        outJSON=[]
        for m in messages:
            outOBJ={'role':m[0],'content':m[1]}
            outJSON.append(outOBJ)
            
        result=ex.Completion(outJSON,"Y")
        return result
  
    
    def generate_prompt(self,Ang,Hap,Fea,Con): 
        """
        Uses the four parameters to fill in a prestructured string to be used as a prompt
        """
        print(Hap,Fea,Con,Ang)
        if(self.neutralcheck(Ang,Hap,Fea,Con)):
            tempP= (": I feel " + self.neutralcat() +'.' )
            model= "GPT-3.5"
            print(model)
            print(tempP)
            
        else:
            tempP= (": I feel " + self.contracheck(Ang,Hap,Fea,Con) +" , "+ self.categorizeA(Ang) + ", " + self.categorizeF(Fea) + " and " + self.categorizeC(Con)+'.')
            model= "GPT-3.5"
            print(model)
            print(tempP)
        print("tempP=",tempP)    
        return tempP
    


#document these functions for future use in ECL bundle
#look at GNN bundle ECL by dev roger