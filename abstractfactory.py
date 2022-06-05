# contoh script implementasi abstract factory
# kasusnya adalah : terdapat beberapa 3-4 mata kuliah / course , suatu saat akan ada penambahan--
# mata kuliah atau course baru , dimana object/entitas/instance pada class sebelumnya sudah di inisiasiakan
import random
class Course_At:
    "kelas ini untuk abstract factory mata kuliah "

    def __init__(self, course_factory=None):
        self.course_factory = course_factory

    def show_course(self):
        "method untuk menampilkan mata kuliah dengan abstract factory"

        course = self.course_factory()
        print(f'nama mata kuliah yang diselenggarakan adalah {course}')
        

class PBO:
    "ini mata kuliah PBO "
    def ruang(self):
        return 11
    def __str__(self):
        return "Pemrograman Berorientasi Objek"

class KI:
    "ini mata kuliah keamanan informasi"
    def ruang(self):
        return 12
    def __str__(self):
        return "Keamanan Informasi"
class Jarkom:
    "ini mata kuliah Jaringan Komputer"
    def ruang(self):
        return 13
    def __str__(self):
        return "Jaringan Komputer"

if __name__ =="__main__":
   PBO = PBO() #object untuk class PBO
   KI = KI()  # object untuk class KI
   Jarkom = Jarkom() #object untuk class Jarkom

   print(f'nama mata kuliah {PBO} dilaksanakan di ruang {PBO.ruang()}')
   print(f'nama mata kuliah {KI} dilaksanakan di ruang {KI.ruang()}')
   print(f'nama mata kuliah {Jarkom} dilaksanakan di ruang {Jarkom.ruang()}')

def random_course():
    "pemanggilan/ instansiasi subclass"

    return random.choice([PBO,KI,Jarkom])

if __name__ == "__main__":
    course = Course_At(random_course)
    for i in range (5):
        course.show_course()
