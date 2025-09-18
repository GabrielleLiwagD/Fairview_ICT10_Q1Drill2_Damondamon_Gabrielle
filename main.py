from pyscript import document, display

def information(event=None):
    info1 = document.getElementById("input1").value #Name
    info2 = document.getElementById("input2").value #Age
    info3 = document.getElementById("input3").value #School Name
    info4 = document.getElementById("input4").value #School Address

    display(f'Hello, I\'m {info1}', target="output1")
    display(f'I\'m currently {info2}', target="output2")
    display(f'I study at {info3}', target="output3")
    display(f'My school is at {info4}', target="output4")
