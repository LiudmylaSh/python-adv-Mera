import json
from abc import ABC


class Model(ABC):

    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file, "r")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    def generate_dict(self):
        return self.__dict__

    @classmethod
    def get_all(cls):
        data = cls.get_data()
        if len(data) > 0:
            fields = data[0].keys()
            for el in data:
                for field in fields:
                    if field == "id":
                        continue
                    print(el[field])

    @classmethod
    def print_object(cls, objects: list):
        if len(objects) > 0:
            fields = objects[0].keys()
            for ob in objects:
                for field in fields:
                    if field == "id":
                        continue
                    print(ob[field])

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data()
        counter = 0
        if len(data) > 0:
            for el in data:
                if id == el["id"]:
                    return el
                counter+=1
                if counter == len(el):
                    print("Not found element with this id")

    @staticmethod
    def save_to_file(path_to_file, data):
        file = open(path_to_file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    @classmethod
    def delete(cls, id):
        elements = cls.get_data()
        for i in range(len(elements)):
            if elements[i]["id"] == id:
                del elements[i]
                break

        cls.save_to_file("database/" + cls.file, elements)

    @classmethod
    def get_employees_work(cls, id, place_of_work, data):
        employees_work = []
        if len(data) > 0:
            for el in data:
                if id == int(el["object_id"]) and el["type_of_work"] == place_of_work:
                    employees_work.append(el)
        return employees_work


    def save(self):
        data = self.get_data()
        new_el = self.generate_dict()
        if len(data) > 0:
            new_el["id"] = data[-1]["id"] + 1
        else:
            new_el["id"] = 1
        data.append(new_el)
        self.save_to_file("database/" + self.file, data)