from ast import literal_eval

def isLiteral(s): #Detect if s represents a literal
    if isdigit(s) or ((s[0] == '"' and s[-1] == '"') or (s[0] == '\'' and s[-1] == '\'')):
        return True
    return False

def lex(script): #Lex a script
    script = script.replace('\n', '')
    x = 0  #Iterator
    r = [] #Return value
    d = -1 #Splitter bracket depth
    lastcomma = 0 #Last comma encountered by the splitter
    while x < len(script):
        if script[x] == '[':
            d += 1
        elif script[x] == ']':
            d -= 1
        
        if d == 0:
            if script[x] == ',':
                r.append(script[lastcomma+1:x])
                lastcomma = x
        x += 1
    r.append(script[lastcomma+1:x])

    for x in range(len(r)):
        r[x] = tuple(r[x].split(':', 1))

    r2 = {}
    for x in r:
        r2[x[0]] = x[1]
    return r2

