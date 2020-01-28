from django.db import models

# Create your models here.
class MotherTonguee(models.Model):
    locallang = models.CharField(max_length=30)
    def __str__(self):
     return self.locallang
class Castee(models.Model):
    cst = models.CharField(max_length=10)
    def __str__(self):
     return self.cst
class Subcastee(models.Model):
    subcst = models.CharField(max_length=20)
    def __str__(self):
     return self.subcst
class Heightt(models.Model):
    hgt = models.CharField(max_length=10)
    def __str__(self):
     return self.hgt
class Weightt(models.Model):
    wght = models.CharField(max_length=10)
    def __str__(self):
     return self.wght
class Starr(models.Model):
    chukka = models.CharField(max_length=30)
    def __str__(self):
     return self.chukka
class Raasii(models.Model):
    rasi = models.CharField(max_length=30)
    def __str__(self):
     return self.rasi
class Member(models.Model):
    residing_cuntry = models.CharField(max_length=50)
    residing_stat = models.CharField(max_length=50)
    residing_cty = models.CharField(max_length=50)
class Countryy(models.Model):
    cuntry = models.CharField(max_length=25)
    def __str__(self):
     return self.cuntry
class Statee(models.Model):
    stat = models.CharField(max_length=25)
    country = models.ForeignKey(Countryy)
    def __str__(self):
     return self.stat
class Cityy(models.Model):
    cty = models.CharField(max_length=25)
    city = models.ForeignKey(Cityy)
    def __str__(self):
     return self.cty
class Agee(models.Model):
    ag = models.IntegerField()
    def __str__(self):
        return self.ag
class Religion(models.Model):
    relig = models.CharField(max_length=25)
    def __str__(self):
        return self.relig
class Matridata(models.Model):
    Name = models.CharField(max_length=25)
    CreateProfile = models.CharField(max_length=20)
    Gender = models.CharField(max_length=15)
    MotherTongue = models.ForeignKey(MotherTonguee,on_delete=models.CASCADE)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Caste = models.ForeignKey(Castee,on_delete=models.CASCADE)
    Subcaste = models.ForeignKey(Subcastee,on_delete=models.CASCADE)
    Dosham = models.CharField(max_length=20)
    MaritalStatus = models.CharField(max_length=25)
    NoofChildren = models.CharField(max_length=20)
    Height = models.ForeignKey(Heightt,on_delete=models.CASCADE)
    FamilyStatus = models.CharField(max_length=20)
    FamilyType = models.CharField(max_length=20)
    FamilyValues = models.CharField(max_length=25)
    AnyDisability = models.CharField(max_length=25)
    HighestEducation = models.CharField(max_length=30)
    Occupation = models.CharField(max_length=25)
    Bodytype = models.CharField(max_length=25)
    Weight = models.ForeignKey(Weightt,on_delete=models.CASCADE)
    Educationdetail = models.CharField(max_length=35)
    Occupationdetail = models.CharField(max_length=35)
    Eatinghabit = models.CharField(max_length=35)
    Drinkinghabit = models.CharField(max_length=35)
    Smokinghabit = models.CharField(max_length=35)
    Star = models.ForeignKey(Starr,on_delete=models.CASCADE)
    Raasi = models.ForeignKey(Raasii,on_delete=models.CASCADE)
    Birthtime = models.DateTimeField()
    Pobcountry = models.ForeignKey(Countryy,on_delete=models.CASCADE)
    Pobstate = models.ForeignKey(Statee,on_delete=models.CASCADE)
    Pobcity = models.ForeignKey(City,on_delete=models.CASCADE)
    Fatherstatus = models.CharField(max_length=30)
    Motherstatus = models.CharField(max_length=30)
    NoofBrothers = models.CharField(max_length=20)
    Brothersmarried = models.CharField(max_length=25)
    NoofSisters = models.CharField(max_length=25)
    Sistersmarried = models.CharField(max_length=30)
    Familylocation = models.CharField(max_length=30)
    Contactno = models.IntegerField()
    Ancestralorigin = models.CharField(max_length=30)
