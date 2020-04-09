python early:

    #goto - this acts like jump, except it saves the previous screen, clears all sprites, and resets the TextBuffer
    #goto newtag oldtag
    def parse_goto(lex):
        newtag = lex.simple_expression()
        oldtag = lex.simple_expression()
        return(newtag, oldtag)


    def execute_goto(o):
        global LastScreen
        global TextBuffer
        LastScreen = str(o[1])
        TextBuffer = ""
        renpy.hide('sprite')
        renpy.jump (str(o[0]))

    def lint_goto(o):
        try:
            renpy.check_text_tag (o.newtag)
        except:
            renpy.error("ERROR: newtag tag not valid" % o)
        try:
            renpy.check_text_tag (o.newtag)
        except:
            renpy.error("ERROR: oldtag tag not valid" % o)

    renpy.register_statement("goto", parse = parse_goto, execute = execute_goto, lint = lint_goto)

    #trans - transitions to a new background with fade in only if coming from a different background.
    #trans imagename
    def parse_trans(lex):
        file = lex.rest()
        return(file)


    def execute_trans(o):
        renpy.show('black', at_list = [fadeout])
        i = str(o)
        if CurrentScreen != LastScreen:
            renpy.show(i,  at_list = [fadein])
        else:
            renpy.show(i)

    def lint_trans(o):
        i = str(o) + ".png"
        renpy.try_compile("trans", i)
        renpy.check_text_tag(o[1])

    renpy.register_statement("trans", parse = parse_trans, execute = execute_trans, lint = lint_trans)
