from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def run_task(request):
    SECRET_TEXT = "It's fine to celebrate success but it is more important to heed the lessons of failure. By Bill Gates"
    output = "";
    if request.method == "POST" and request.body:
        output = validate_text(request.body.decode('utf-8'), SECRET_TEXT)
    else:
        output = "You should pass the variable value as POST"
    return HttpResponse(output)

# Create your views here.
def validate_text(input, text):
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