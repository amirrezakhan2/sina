class CustomStr:
    def __init__ (self,text):
        self.text = text
    
    def custom_split (self ,*splitt):
        
        result=[self.text]

        for i in splitt:
            n=[]
            for j in result:
                n.extend(j.split(i))
            result = n
        

        final_result=[]

        for item in result:

            if item:
             final_result.append(item)
        
        return final_result
    
    def remove_duplicate(self):

        result=[*self.text]

        none_string = ''

        for i in result:

            if i not in none_string:
                none_string += i
        return none_string


    def set(self,indexx,word):
        result = [*self.text]
        result[indexx] = word

        final_result=''

        for i in result:
            final_result += i

        return final_result

a=CustomStr('sina')
b=a.set(2,'a')
print(b)