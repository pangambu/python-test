class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house =  house
        
    

    def __str__(self):
        return f"{self.name} is from {self.house}"
    #getter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")


    #getter
    @property
    def house(self):
        return self._house
    #setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house  

    
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐴"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russel terrier":
    #             return "🐕"
    #         case _:
    #             return "🪄"





def main():
    student = get_student()
    print(student)

 
def get_student():
    
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    


if __name__ == "__main__":
    main()