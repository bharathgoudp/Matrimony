
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
    class Meta:
        model=Step2
        fields="__all__"

class Step3_Form(forms.ModelForm):
    class Meta:
        model=Step3
        fields="__all__"

class Step4_Form(forms.ModelForm):
    class Meta:
        model=Step4
        fields="__all__"                

