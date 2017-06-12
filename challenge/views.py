from django.shortcuts import render


# Create your views here.
def validate_text(input, text):
#    secret_key = "Voce conseguiu resolver o desafio"
    output = ""
    for i in range(len(text)):
        if len(input) <= i:
            return output
            output += "?"
        elif input[i] == text[i]:
            output += input[i]
        elif input[i] in text:
            output += "-"
        else:
            output +=  "*"

    return output