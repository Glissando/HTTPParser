class Dom():
    def __init__(self, nodes):
        self.nodes = nodes
        pass
    
    def constructDom(self, html):
        parser = HtmlParser()
        parser.parse_html(html)
        stack = parser.get_stack()
    
    def parse_node(self, stack):
        tokenEnd = Node(stack.pop())
        while(len(stack) > 0):
            tokenOpen = stack.top()
            if not tokenOpen.isOpen():
                tokenEnd.append(self.parse_node(stack))
            elif tokenOpen.value == tokenEnd.token.value:
                return Node(stack.pop())
                

class HtmlParser():
    def __init__(self):
        self.node_stack = []
        self.node_table = []
        self.current_index = 0

    def get_stack(self):
        return self.node_stack

    #Parses an entire html file and returns the tags in a stack
    def parse_html(self, str):
        while(len(str) - 2 > self.current_index):
            self.skip_whitespace(str)
            index = self.current_index
            if(str[index] == '<' and str[index + 1] != '/'):
                self.node_stack.append(self.parse_opening_tag(str))
                index = self.current_index
            if(str[index] == '<' and  str[index + 1] == '/'):
                self.node_stack.append(self.parse_closing_tag(str))
        
        self.log_stack()
        return self.node_stack
        

    #Parses <Example key1=value1 key2=value2>
    def parse_opening_tag(self, str):
        self.current_index += 1
        index = self.current_index
        while(str[index] != '>' and str[index] != ' ' and len(str) - 1 > index):
            index += 1

        element = str[self.current_index:index]
        self.current_index = index
        attributes = self.parse_attributes(str)
        innerHtml = self.parse_inner_html(str)

        return Token(element, True, innerHtml, attributes)

    #Parses </Example>
    def parse_closing_tag(self, str):
        self.current_index += 2
        index = self.current_index
        while(str[index] != '>' and  str[index] != ' ' and len(str) - 1 > index):
            index += 1
        
        element = str[self.current_index:index]
        self.current_index = index
        self.skip_whitespace(str)
        self.current_index += 1
        return Token(element, False)

    #Parses >InnerHTML<
    def parse_inner_html(self, str):
        self.current_index += 1
        index = self.current_index
        while(len(str) - 1 > index and str[index] != '<'):
            index += 1
        element = str[self.current_index:index]
        self.current_index = index
        return element.strip()

    #Parses </Example>
    def parse_self_closing_tag(self, str):
        index = self.current_index

    #Parses key1=value1 key2=value2
    def parse_attributes(self, str):
        attributes = {}
        self.skip_whitespace(str)
        while(str[self.current_index] != '>' and len(str) - 1 > self.current_index):
            self.parse_attribute(str, attributes)
            self.skip_whitespace(str)
        return attributes

    #Parses key=value
    def parse_attribute(self, str, attributes):
        index = self.current_index
        #Parse key
        while(len(str) - 1 > index and str[index] != '=' and str[index] != ' ' and str[index] != '>'):
            index += 1
        
        key = str[self.current_index:index]
        if(str[index] == '='):
            index += 1
        self.skip_whitespace(str)
        self.current_index = index
        #Parse value
        while(str[index] != ' ' and str[index] != '>' and len(str) - 1 > index):
            index += 1
        value = str[self.current_index:index]
        attributes[key] = value
        self.current_index = index

    def skip_whitespace(self, str):
        index = self.current_index
        while(str[index] == ' '):
            index += 1
        self.current_index = index

    def log_stack(self):
        for token in self.node_stack:
            if token.isOpen():
                print(token)
                print(f'innerHtml: {token.innerHtml}')
                print('--Attributes--')
                for attr in token.attributes:
                    print(f'{attr}: {token.attributes[attr]}')
                print()


    def reset_index(self):
        self.current_index = 0

class Token:
    def __init__(self, value, open, innerHtml=None, attributes=None):
        self.value = value
        if open == True:
            self.attributes = attributes
            self.innerHtml = innerHtml
        self.open = open

    def __str__(self):
        return str(self.value)

    def isOpen(self):
        return self.open

    def getValue(self):
        return self.value

class Node:
    def __init__(self, token):
        self.token = token
        self.children = []

    def append(self, node):
        self.children.append(node)

def loadIndex():
    data = ''
    with open('index.html', 'r') as file:
        data = file.read().replace('\n', '')
    parser = HtmlParser()
    parser.parse_html(data)

loadIndex()