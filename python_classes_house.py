class House():
    num_room=5
    bath_room=2
    def cost_evaluation(self):
        print(self.num_room)
        pass

house = House()
print(house.num_room)
print(House.num_room)
house.num_room=7
print(house.num_room)
print(House.num_room)
print(House.cost_evaluation())