from django import forms

Choises = (
    ('Распространненый', 'Распространненый'),
    ('Полунезависимый', 'Полунезависимый'),
    ('Встроенный', 'Встроенный'),
)

Choises_coco = (
    ('Предварительная', 'Предварительная'),
    ('Детальная', 'Детальная')
)

Rating = (
    ('Очень низкий', 'Очень низкий'),
    ('Низкий', 'Низкий'),
    ('Средний', 'Средний'),
    ('Высокий', 'Высокий'),
    ('Очень высокий', 'Очень высокий'),
    ('Критический', 'Критический'),
)

Rating_low = (
    ('Критически низкий', 'Критически низкий'),
    ('Очень низкий', 'Очень низкий'),
    ('Низкий', 'Низкий'),
    ('Средний', 'Средний'),
    ('Высокий', 'Высокий'),
    ('Очень высокий', 'Очень высокий'),
    ('Критический', 'Критический'),
)
class base_coco(forms.Form):
    size = forms.FloatField()
    sh = forms.CharField(widget=forms.Select(choices=Choises))

class coco2(forms.Form):
    size = forms.FloatField()
    sh = forms.CharField(widget=forms.Select(choices=Choises_coco))

class PoProperties(forms.Form):
    save_po = forms.CharField(widget=forms.Select(choices=Rating))
    size_bd = forms.CharField(widget=forms.Select(choices=Rating))
    prod_lev = forms.CharField(widget=forms.Select(choices=Rating))


class ApparatPropeties(forms.Form):
    speed = forms.CharField(widget=forms.Select(choices=Rating))
    memory = forms.CharField(widget=forms.Select(choices=Rating))
    virtual = forms.CharField(widget=forms.Select(choices=Rating))
    times = forms.CharField(widget=forms.Select(choices=Rating))


class PersonalPropeties(forms.Form):
    analiz = forms.CharField(widget=forms.Select(choices=Rating))
    oput = forms.CharField(widget=forms.Select(choices=Rating))
    sposobnost = forms.CharField(widget=forms.Select(choices=Rating))
    oput_virtual = forms.CharField(widget=forms.Select(choices=Rating))
    oput_language = forms.CharField(widget=forms.Select(choices=Rating))


class ProjectPropeties(forms.Form):
    method = forms.CharField(widget=forms.Select(choices=Rating))
    instruments = forms.CharField(widget=forms.Select(choices=Rating))
    treb = forms.CharField(widget=forms.Select(choices=Rating))


class SizeForm(forms.Form):
    prec = forms.CharField(widget=forms.Select(choices=Rating))
    flex = forms.CharField(widget=forms.Select(choices=Rating))
    resl = forms.CharField(widget=forms.Select(choices=Rating))
    team = forms.CharField(widget=forms.Select(choices=Rating))
    pmat = forms.CharField(widget=forms.Select(choices=Rating))


class WorkForm(forms.Form):
    pers = forms.CharField(widget=forms.Select(choices=Rating_low))
    prex = forms.CharField(widget=forms.Select(choices=Rating_low))
    rcpx = forms.CharField(widget=forms.Select(choices=Rating_low))
    ruse = forms.CharField(widget=forms.Select(choices=Rating_low))
    pdif = forms.CharField(widget=forms.Select(choices=Rating_low))
    fcil = forms.CharField(widget=forms.Select(choices=Rating_low))
    sced = forms.CharField(widget=forms.Select(choices=Rating_low))


class ErrorMultForm(forms.Form):
    acap = forms.CharField(widget=forms.Select(choices=Rating))
    aexp = forms.CharField(widget=forms.Select(choices=Rating))
    pcap = forms.CharField(widget=forms.Select(choices=Rating))
    pcon = forms.CharField(widget=forms.Select(choices=Rating))
    pexp = forms.CharField(widget=forms.Select(choices=Rating))
    ltex = forms.CharField(widget=forms.Select(choices=Rating))

    rely = forms.CharField(widget=forms.Select(choices=Rating))
    data = forms.CharField(widget=forms.Select(choices=Rating))
    cplx = forms.CharField(widget=forms.Select(choices=Rating))
    ruse = forms.CharField(widget=forms.Select(choices=Rating))
    docu = forms.CharField(widget=forms.Select(choices=Rating))

    time = forms.CharField(widget=forms.Select(choices=Rating))
    stor = forms.CharField(widget=forms.Select(choices=Rating))
    pvol = forms.CharField(widget=forms.Select(choices=Rating))

    tool = forms.CharField(widget=forms.Select(choices=Rating))
    site = forms.CharField(widget=forms.Select(choices=Rating))
    sced = forms.CharField(widget=forms.Select(choices=Rating))