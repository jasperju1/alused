class Student:
    
    school = 'Kuressaare Ametikool'

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self._phone = phone

    def add_reason_for_absence(self, reason):
        self.reason = reason
        print(f'{self.first_name} {self.last_name} puudumise pohjus: {self.reason}')

    def get_phone(self):
        return self._phone
    
    def set_phone(self, phone):
        self._phone = phone

class AdultStudent(Student):
    
    def __init__(self, first_name, last_name, phone, occupation):
        super().__init__(first_name, last_name, phone)
        self.occupation = occupation

    def print_occupation(self):
        print(f'{self.first_name} amet on {self.occupation}')

student_one = Student('Retep', 'Live', '5782378')
student_two = Student('Jasper', 'Jahutaja', '56645423')
adult_student = AdultStudent('Ratep', 'Doog', '52008511', 'Autojuht')

print(f'1. opilane: {student_one.first_name} {student_one.last_name} - {student_one.school}')
print(f'2. opilane: {student_two.first_name} {student_two.last_name} - {student_two.school}')
print(f'3. opilane: {adult_student.first_name} {adult_student.last_name} - {adult_student.school}')
student_two.add_reason_for_absence('Jain magama')

#print(student_one._phone)

print(student_one.get_phone())
student_one.set_phone('52123456')
print(student_one.get_phone())

print(f'{adult_student.first_name} telefon on {adult_student.get_phone()}')
adult_student.print_occupation()

