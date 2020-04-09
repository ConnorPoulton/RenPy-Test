init python:
    GotOrbBlue = False
    GotOrbGreen = False
    FlagTest = True

menu Inventory:
    "green orb" if GotOrbGreen == True:
        return "green orb"
    "test flag" if FlagTest == True:
        return "test flag"
    "blue orb" if GotOrbBlue == True:
        return "blue orb"
    "return":
        return
