from django.db import models

Create your models here.
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
class Countryy(models.Model):
    cuntry = models.CharField(max_length=25)
    def __str__(self):
     return self.cuntry
class Statee(models.Model):
    stat = models.CharField(max_length=25)
    def __str__(self):
     return self.stat
class Cityy(models.Model):
    cty = models.CharField(max_length=25)
    def __str__(self):
     return self.cty
class Agee(models.Model):
    ag = models.IntegerField()
    def __str__(self):
        return self.ag
class Religionn(models.Model):
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
    Pobcity = models.ForeignKey(Cityy,on_delete=models.CASCADE)
    Fatherstatus = models.CharField(max_length=30)
    Motherstatus = models.CharField(max_length=30)
    NoofBrothers = models.CharField(max_length=20)
    Brothersmarried = models.CharField(max_length=25)
    NoofSisters = models.CharField(max_length=25)
    Sistersmarried = models.CharField(max_length=30)
    Familylocation = models.CharField(max_length=30)
    Contactno = models.IntegerField()
    Ancestralorigin = models.CharField(max_length=30)
    Hobbies_interes=models.CharField(max_length=500)
    others=models.CharField( max_length=50)
    FavouriteMusic=models.CharField(max_length=50)
    Others=models.CharFiled(max_length=50)
    Sportsfi=models.CharField(max_length=50)
    Otherss=models.CharFiled(max_length=50)
    spokenLang=models.CharField(max_length=50)
    otherss=models.CharFiled(max_length=50)
    prefredage=models.IntegerField()
    Matritalstatus=models.CharField(max_length=50)
    Have_childeren=models.CharField(max_length=50)
    prefredheigth=models.CharField(max_length=50)()
    Physical_status=models.CharField(max_length=50)
    Eatinghabits=models.CharField(max_length=50)
    Drinkinghabits=models.CharField(max_length=50)
    Smokinghabit=models.CharField(max_length=50)
    Religion=models.ForeignKey(Religion,on_delete=models.CASCADE)
    Religion_Castee=models.Foreignkey(cast,on_delete=models.CASCADE)
    kujaDosham=models.CharField(max_length=50)
    star=models.Foreignkey(Starr,on_delete=models.CASCADE)

   def __str__(self):
        return self.fname

