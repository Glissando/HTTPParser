current_index = 0
node_stack = []
node_table = []

def parse_html(str):
    index = current_index
    if(str[index] == '<'):
        node_stack.append(parse_opening_tag(str))
    elif(str[index] == '</'):
        node_stack.append(parse_closing_tag(str))
    elif(str[index - 1] == '>'):
        node_stack.append(parse_inner_html(str))

def parse_opening_tag(str):
    index = current_index
    while(str[index] != '>' and len(str) > index):
        index += 1
    return str[current_index:index] + 'O'

def parse_closing_tag(str):
    index = current_index
    while(str[index] != '>' and len(str) > index):
        index += 1
    return str[current_index:index] + 'E'

def parse_inner_html(str):
    index = current_index
    return

def parse_self_closing_tag(str):
    index = current_index

def parse_attribute(str):
    index = current_index
    
def skip_whitespace(str):
    index = current_index
    while(str[index] == ' '):
        index += 1
    current_index = index

def log_stack():
    while(node_stack.count != 0):
        print(node_stack.pop())