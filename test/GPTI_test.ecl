IMPORT python3 as python;
IMPORT $.^.internal.openaiGPT;
IMPORT $.^.GPTI;


api_key := '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';

sess := GPTI.GetSession(api_key:=api_key);
msg := 'How are you? My name is Human';
response := GPTI.getCompletion(sess, msg, True);
OUTPUT(response);



