# I take help of chatgpt while writting source code for Chat Template Formatter

from pyparsing import Literal, Word, alphas, alphanums, nestedExpr, ParseException

def format_template(input_text):
    

    user_start = "{{#user}}"#tags used to identify the starting and end seg of  paragraph where user and assistant speaks
    user_end = "{{/user}}"  ## 
    assistant_start = "{{#assistant}}"
    assistant_end = "{{/assistant}}"



    Gen_cmd = "{{gen" + nestedExpr("{{", "}}") + "}}"  #nestedexpr help to match nested expression in curly braces
    assistant = assistant_start + Gen_cmd + assistant_end 
    #combine gen cmd and assistant seg


    try:
        parsed = Gen_cmd.transformString(input_text)
        parsed = assistant.transformString(parsed)
    except ParseException:
        parsed = input_text
    #  if parsing fail indicated by parseexception the code falls back to using the original input text


    UserSeg = []
    assistSeg = ""
    #  lists holding user seg and assistant seg



    for seg in parsed.split(assistant_start):
        if assistant_end in seg:
            assistSeg = seg
        else:
            UserSeg.append(seg)
             
# if an assistant cmd is found inside a segm, the segm is considere part of the assistant response. else it is considered a user seg and added to the  user seg list



    if not assistSeg.endswith("{{gen 'write' }}{{/assistant}}"):
        assistSeg += "{{gen 'write' }}{{/assistant}}"
# if the assistant seg ends with a "{{gen 'write' }}{{/assistant}}" command. if it does not this command is added. This ensures that the assistant's response is properly concluded


    formatted_temp = " ".join([
        user_start + user_segment.strip() + user_end
        for user_segment in UserSeg
    ]) + " " + assistSeg
 

    return formatted_temp
# return formated template output
 
input_text = input("Enter the required text: ")
formated_output = format_template(input_text)
print("formated output : ", formated_output)
