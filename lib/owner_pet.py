class Owner:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name):
        self.name = name
        Owner.all.append(self)
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type.")

        if pet.pet_type not in Owner.PET_TYPES:
            raise Exception("Invalid pet type.")

        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet(Owner):
    all = []

    def __init__(self, name, pet_type, owner=None):
        super().__init__(name)
        self.pet_type = pet_type
        self.owner = owner
        self.validate_pet_type(pet_type)
        Pet.add_pet(self)
        if owner:
            owner.add_pet(self)

    def validate_pet_type(self, pet_type):
        if pet_type not in Owner.PET_TYPES:
            raise Exception(f"Invalid pet type.")

    @classmethod
    def add_pet(cls, pet):
        cls.all.append(pet)
