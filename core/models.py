class Teacher(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ClassQuerySet(models.QuerySet):
    def current_year(self):
        current_year = datetime.now().year
        return self.filter(year=current_year)
    

class Class(models.Model):
    class_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    is_active = models.BooleanField(default=True)
    year = models.IntegerField(default=datetime.now().year)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ClassQuerySet.as_manager()

    def __str__(self):
        return self.class_name
    

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    


    def __str__(self):
        return f"{self.student.name} - {self.grade}"
    

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()

    def __str__(self):
        return f"{self.student.name} - {self.date}"
    
