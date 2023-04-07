
class save:
    file_name = ""
    save_file = None
    
    def __init__(self, n: str):
        self.file_name = n
        self.save_file = open(self.file_name, "r+")
    
    #Record points by players
    def save(self, scores: dict):
        file_str = ""
        for g,s in scores.items():
            if(len(s) == 2):
                file_str += f"{g} {s[0]},{s[1]}\n"
            else:
                file_str += f"{g} {s[0]}\n"
        
        self.save_file.seek(0)
        self.save_file.write(file_str)
        self.save_file.truncate()
    
    #Get scores from file
    def load(self) -> dict:
        save_data = {}
        for line in self.save_file:
            ls = line.split(" ")
            ls2 = []
            for i in ls[1].replace('\n','').split(","):
                ls2.append(int(i))
            save_data.update({ls[0]: ls2})
            
        return save_data
        #self.save_file.seek(0)
    
    def close(self):
        self.save_file.close()

'''
s = save("log.txt")
s.save("test", [1,2])
print(s.load("test"))
s.close()
'''