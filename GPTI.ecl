import python3 as python;
IMPORT internal.openaiGPT;


EXPORT GPTI := MODULE

    // initiate a chatGPT session
    EXPORT UNSIGNED getSession(STRING api_key='', STRING who='user', 
                                        STRING model='gpt-3.5-turbo', INTEGER temp=1) := FUNCTION
        sessID := openaiGPT.init(who := who, model := model, temp := temp, api_key := api_key);
        RETURN sessID;
    END;

    // return a response from ChatGPT based on a prompt
    EXPORT STRING getCompletion(INTEGER session, STRING prompt, 
                                                        BOOLEAN cont=False, 
                                                        REAL temperature = -1,
                                                        REAL topP=1, 
                                                        INTEGER max_tokens=70, 
                                                        REAL F_penalty=1.2,
                                                        REAL P_penalty=1) :=
                                                            EMBED(Python: globalscope('ChatGPT'), 
                                                                                    persist('global'))
        try:
            chatGPT = GPTList[session-1]
            if temperature == -1:
                temperature = None
            finalPrompt={"role":chatGPT.who, "content":prompt}
            result = chatGPT.Completion(prompt=finalPrompt, cont=cont,
                                            temp=temperature, topP=topP, max_tokens=max_tokens, 
                                                            F_penalty=F_penalty, P_penalty=P_penalty)
            return result
        except:
            import traceback as tb 
            exc = tb.format_exc()
            assert False, exc
    ENDEMBED;

END;

