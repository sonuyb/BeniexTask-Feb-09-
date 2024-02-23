class Cypher:
    def __init__(self, input_string):
        self.input_string = input_string
 
    @classmethod
    def convert_string(cls, string):
       
        """Converting string"""
       
        cypher_string = ""
        for char in string:
            if char.isdigit():
                new_char = str((int(char) + 1) % 10)
            elif char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                new_ord = (ord(char) - base + 2) % 26 + base
                new_char = chr(new_ord)
                new_char = new_char.swapcase()  
            else:
                new_char = char
            cypher_string += new_char
        return cypher_string
 
    def create_cypher(self):
       
        """Calls the class method to perform the conversion."""
       
        return self.convert_string(self.input_string)
 
input_string = "ABcD1293Z"
cypher_obj = Cypher(input_string)
cypher_text = cypher_obj.create_cypher()
print(cypher_text)