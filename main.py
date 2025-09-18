from pyscript import document, display

def information(event=None):
    info1 = str(document.getElementById("input1").value) #Name
    info2 = str(document.getElementById("input2").value) #Age
    info3 = str(document.getElementById("input3").value) #School Name
    message = "Hello, I\'m " + str(info1)
    message2 = "I\'m " + str(info2) + " years old."
    message3 = "I studied in " + str(info3)

    display(message + ".\n" + message2 + "\n" + message3 + ".",target="message")