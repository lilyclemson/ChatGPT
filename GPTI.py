import random
import Emotionset
import openai

#GPT Object includes a who, context, model, message, and api_key attribute all with default values
class GPT:
    def __init__(self,who="",model="gpt-3.5-turbo",temp=1,api_key="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"): 
        """
        api_key is necessary to create a call to the API
        temp controls the randomness of the responses, has a default value of 1 can be overidden both in the constructor or function call
        model controls what model does the completion, default is gpt-3.5-turbo, wont be changing

        """
        self.api_key=api_key
        self.temperature=temp
        self.who=who
        self.model=model
        self.acumulate=[]

    #
    def Completion(self, prompt, cont=False, temp=None, topP=1, max_tokens=70, F_penalty=1.2, P_penalty=1 ):
        """
        prompt is a dictionary list of messages 
        cont controls whether the conversation is recorded to be used in the next call, default is false, it will not record
        temp is a form of randomness control, default is set to 1 can be between 0-2
        TopP is a form of randomness control, controls how much of a node is samples for a response, default is set to 1, between 0-2
        max_tokens controls the length of the prompt in characters, not exact but approximate, default is 70 tokens
        F_penalty controls the frecuency penalty modifier a higher penalty means the response will include more new ideas, between 0-2, default is 1.2
        P_penalty controls how often the response will include the same words verbatim, between 0-2, default is 1
        """
        openai.api_key = self.api_key
        fullprompt = self.generate_fullprompt(prompt)
        if temp is None:
            temp = self.temperature
        Chat_Completion = openai.ChatCompletion.create(
            
            model = self.model,
            messages = fullprompt,
            temperature = temp,
            top_p = topP, 
            max_tokens= max_tokens,
            frequency_penalty=F_penalty,
            presence_penalty=P_penalty,
        )
        if cont =="Y":
            responsedict={"role":Chat_Completion.choices[0].message.role,"content":Chat_Completion.choices[0].message.content}
            self.continueconvo(fullprompt+[responsedict]) 
        else: 
            self.clearacumulate()
        
        return Chat_Completion.choices[0].message["content"]
    
    
            
        
        
       
    def generate_fullprompt(self,prompt):
        """
        Function appends the previous conversation to the beginning of next call allowing the conversations to be "remembered" by the ChatCompletion call 
        """

        prompted=self.acumulate+prompt

        return prompted
    
    
    
    def continueconvo(self,content):
        """
        Adds to the accumulate "log" of previous conversations
        """
        self.acumulate += content
        
    
    def clearacumulate(self):
        """
        Clears the accumulate or "log" of previous conversations
        """
        self.acumulate=[]



#
#Finish emotionset /yes
#add previous conversations YES
#Figure out how to do fewshot learning/Yes
#meaningfull responses/yes....
#getting more than one response at once/ Yes
#Refine the interface so lili can wrapper ECL....