
from django import forms
from matriapp.models import Step1,Step2,Step3,Step4
from django.forms.widgets import Media,MediaDefiningClass,Widget,TextInput,NumberInput,EmailInput,URLInput,PasswordInput,HiddenInput,MultipleHiddenInput,FileInput,ClearableFileInput,Textarea,DateInput,DateTimeInput,TimeInput,CheckboxInput,Select,NullBooleanSelect,SelectMultiple,RadioSelect,CheckboxSelectMultiple,MultiWidget,SplitDateTimeWidget,SplitHiddenDateTimeWidget,SelectDateWidget


dosham=(
    ('yes',"YES"),
    ('no','NO'),
    ("don't","Don't know")
)
meritalstatus=(
    ('Never Married ','Never Married '),
    ('Widowed ','Widowed '),
    ('Divorced','Divorced'),
    ('Awaiting divorce','Awaiting divorce')
)
Noofchildren=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4')
)
familystatus=(
    ('Middle class','Middle class'),
    ('Upper middle class ','Upper middle class '),
    ('Rich','Rich'),
    ('Affluent','Affluent')
)
familytype=(
    ('Joint','joint'),
    ('Nuclear','Nuclear')
)
familyvalues=(
    ('Orthodox','Orthodox'),
    ('Traditional','Traditional'),
    ('Moderate','Moderate'),
    ('Liberal','Liberal')
)
anydisability=(
    ('Normal','Normal'),
    ('Physically challenged','Physically challenged')
)
employedin=(
    ('Government','Government'),
    ('Private','Private'),
    ('Business','Business'),
    ('Defence','Defence'),
    ('Self Employed','Self Employed'),
    ('Not working','Not working')
)
# step2 radiobuttons
Bodytype=(
    ('Slim','Slim'),
    ('Average','Average'),
    ('Athletic','Athletic'),
    ('Heavy','Heavy')
)

Eatinghabbit=(
    ('Vegetarian','Vegetarian'),
    ('Non-Vegetarian','Non-Vegetarian'),
    ('Eggetarian','Eggetarian')
)

Drinkinghabit=(
    ('No','No'),
    ('Drinks Socially','Drinks Socially'),
    ('Yes','Yes')
)

smokinghabit=(
    ('No','No'),
    ('Occasionally','Occasionally'),
    ('Yes','Yes')
)
FamilyLocation=(
    ('Same as my Location','Same as my Location'),
    ('Different Location','Different Location')
)

# step3 radio buttons

hobbies=(
    ('Cooking','Cooking'),
    (' Nature',' Nature'),
    (' Dancing',' Dancing'),
    ('Photography','Photography'),
    ('Dancing','Dancing'),
    ('Painting','Painting'),
    ('pets',' Pets'),
    ('Playing Musical Instruments','Playing Musical Instruments'),
    (' Puzzles',' Puzzles'),
    ('Gardening /Landscaping','Gardening /Landscaping'),
    ('Art / Handicraft','Art / Handicraft'),
    ('Listening to Music','Listening to Music'),
    (' Movies',' Movies'),
    ('Internet Surfing','Internet Surfing'),
    ('Traveling','Traveling')
)


favouriteMusic=(
    ('Film songs','Film songs'),
    ('Indian /Classical Music','Indian /Classical Music'),
    (' Western Music',' Western Music')
)
sportesFItness=(
    ('Cricket','Cricket'),
    ('Carrom','Carrom'),
    ('Chess','Chess'),
    (' Jogging',' Jogging'),
    ('Badminton','Badminton'),
    ('Swimming','Swimming'),
    ('Tennis','Tennis'),
    ('Football','Football')
    
)

spokenlangauge=(
    ('English','English'),
    ('Hindi','Hindi'),
    ('Tamil','Tamil'),
    ('Telugu','Telugu'),
    ('Malayalam','Malayalam'),
    ('Kannada','Kannada'),
    ('Gujarati','Gujarati'),
    ('Marathi','Marathi'),
    ('Urdu','Urdu')
    
)


class Step1_Form(forms.ModelForm):
    Dosham=forms.ChoiceField(choices=dosham, widget=forms.RadioSelect(attrs={'class': 'special'}))
    MaritalStatus=forms.ChoiceField(choices=meritalstatus,widget=forms.RadioSelect(attrs={'class':'special'}))
    NoofChildren=forms.ChoiceField(choices=Noofchildren, widget=forms.RadioSelect(attrs={'class':'special'}))
    FamilyStatus=forms.ChoiceField(choices=familystatus, widget=forms.RadioSelect(attrs={'class':'special'}))
    FamilyType=forms.ChoiceField(choices=familytype, widget=forms.RadioSelect(attrs={'class':'special'}))
    FamilyValues=forms.ChoiceField(choices=familyvalues, widget=forms.RadioSelect(attrs={'class':'special'}))
    AnyDisability=forms.ChoiceField(choices=anydisability, widget=forms.RadioSelect(attrs={'class':'special'}))
    EmployedIn=forms.ChoiceField(choices=employedin, widget=forms.RadioSelect(attrs={'class':'special'}))
    class Meta:
        model=Step1
        fields = "__all__"
        

class Step2_Form(forms.ModelForm):
    Bodytype=forms.ChoiceField(choices=Bodytype,widget=forms.RadioSelect(attrs={'class':'special'}))
    Eatinghabit=forms.ChoiceField(choices=Eatinghabbit,widget=forms.RadioSelect(attrs={'class':'special'}))
    Drinkinghabit=forms.ChoiceField(choices=Drinkinghabit,widget=forms.RadioSelect(attrs={'class':'special'}))
    Smokinghabit=forms.ChoiceField(choices=smokinghabit,widget=forms.RadioSelect(attrs={'class':'special'}))
    Familylocation=forms.ChoiceField(choices=FamilyLocation,widget=forms.RadioSelect(attrs={'class':'special'}))
    class Meta:
        model=Step2
        fields="__all__"

class Step3_Form(forms.ModelForm):
    Hobbies=forms.ChoiceField(choices=hobbies,widget=forms.CheckboxSelectMultiple(attrs={'class':'special'}))
    FavouriteMusic=forms.ChoiceField(choices=favouriteMusic,widget=forms.CheckboxSelectMultiple(attrs={'class':'special'}))
    Sportsfi=forms.ChoiceField(choices=sportesFItness,widget=forms.CheckboxSelectMultiple(attrs={'class':'special'}))
    spokenLang=forms.ChoiceField(choices=spokenlangauge,widget=forms.CheckboxSelectMultiple(attrs={'class':'special'}))
    class Meta:
        model=Step3
        fields="__all__"

class Step4_Form(forms.ModelForm):

    class Meta:
        model=Step4
        fields="__all__"                

