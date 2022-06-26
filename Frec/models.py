from django.db import models
 
def student_directory(instance, filename): 
    name, ext = filename.split(".")
    name = instance.firstname + instance.lastname
    filename = name +'.'+ ext 
    return 'studentImages/' + name + '/' + '{}'.format(filename)

class Student(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    nim = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to=student_directory ,null=True, blank=True)
    def __str__(self):
        return str(self.firstname + " " + self.lastname + " " + str(self.nim))

class Major(models.Model):
    OPEN = "Open"
    CLOSED = "Closed"
    statusOptions = ((OPEN,"Open"), (CLOSED,"Closed"))
    major = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=10, choices=statusOptions, default= OPEN)
    def __str__(self):
        return str(self.major + " " + self.status)

class Attendence(models.Model):
    PRESENT = "Present"
    ABSENT = "Absent"
    statusOptions = ((PRESENT,"Present"), (ABSENT,"Absent"))
    Current_Major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True)
    Student_name =  models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add = True, null = True)
    time = models.TimeField(auto_now_add=True, null = True)
    status = models.CharField(max_length=10, choices=statusOptions, default=ABSENT)

    def __str__(self):
        return str(self.Student_name.firstname + " " +  self.Student_name.lastname + " "  + str(self.status) + " " + self.Current_Major.major + " " + str(self.date) + " " + str(self.time))