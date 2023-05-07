from django import forms

NUMS= [
    ('F', 'F'),
    ('I', 'I'),
    ('L', 'L'),
    ('N', 'N'),
    ('P', 'P'),
    ('T', 'T'),
    ('U', 'U'),
    ('V', 'V'),
    ('W', 'W'),
    ('X', 'X'),
    ('Y', 'Y'),
    ('Z', 'Z'),

    ]
class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))