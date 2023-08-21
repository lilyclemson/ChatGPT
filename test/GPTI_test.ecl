IMPORT python3 as python;
IMPORT $.^.internal.openaiGPT;
IMPORT $.^.GPTI;


api_key := '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';

sess := GPTI.GetSession(api_key:=api_key);
msg := 'How are you? My name is Human';
response := GPTI.getCompletion(sess, msg, True);
OUTPUT(response);



