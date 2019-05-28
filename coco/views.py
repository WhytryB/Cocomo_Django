from django.shortcuts import render
from .forms import *
from django.views.generic import View
# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse

global q


def posts_coco_list(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

class BaseCocoView(View):
    template = 'base.html'

    def get(self, request):
        form = base_coco()
        return render(request, self.template,
                      context={"form":form})

    def post(self, request):
        form = base_coco(request.POST)
        if form.is_valid():
            Size = form.cleaned_data['size']
            ai, b, c, d = 0, 0, 0, 0
            if form.cleaned_data['sh'] == "Распространненый":
                ai = 2.4
                b = 1.05
                c = 2.5
                d = 0.38
            elif form.cleaned_data['sh'] == "Полунезависимый":
                ai = 3.0
                b = 1.12
                c = 2.5
                d = 0.35
            elif form.cleaned_data['sh'] == "Встроенный":
                ai = 3.6
                b = 1.20
                c = 2.5
                d = 0.32
            PM = ai * (Size ** b)
            TM = c * (PM ** d)
            return render(request, 'base.html', context={'form': form, 'PM': PM, "TM": TM})


from functools import reduce
import collections

def genrate_dict(dicts, dict_znach_pred):
    spisok_data_pred = collections.defaultdict(set)
    for d in dicts:
        for k, v in d.items():  # d.items() in Python 3+
            spisok_data_pred[v].add(k)
    print(spisok_data_pred)
    spisok_znach_pred = []
    for i, j in (spisok_data_pred.items()):
        print(i, j, "--")
        if str(spisok_data_pred.get(i)) == "{'Очень низкий'}":
            spisok_znach_pred.append(dict_znach_pred.get(i)[0])
        elif str(spisok_data_pred.get(i)) == "{'Низкий'}":
            spisok_znach_pred.append(dict_znach_pred.get(i)[1])
        elif str(spisok_data_pred.get(i)) == "{'Средний'}":
            spisok_znach_pred.append(dict_znach_pred.get(i)[2])
        elif str(spisok_data_pred.get(i)) == "{'Высокий'}":
            spisok_znach_pred.append(dict_znach_pred.get(i)[3])
        elif str(spisok_data_pred.get(i)) == "{'Очень высокий'}":
            spisok_znach_pred.append(dict_znach_pred.get(i)[4])
        elif str(spisok_data_pred.get(i)) == "{'Критический'}":
            spisok_znach_pred.append(dict_znach_pred.get(i)[5])
        else:
            pass
    print(spisok_znach_pred)
    return spisok_znach_pred


class PromLevelView(View):
    template = 'promlevel.html'

    def get(self, request):
        po_form = PoProperties()
        ap_form = ApparatPropeties()
        pe_form = PersonalPropeties()
        pr_form = ProjectPropeties()
        form = base_coco()
        return render(request, self.template,
                      context={"pe_form":pe_form, "ap_form": ap_form, "po_form":po_form, "pr_form":pr_form, "form":form})

    def post(self, request):
        po_form = PoProperties(request.POST)
        ap_form = ApparatPropeties(request.POST)
        pe_form = PersonalPropeties(request.POST)
        pr_form = ProjectPropeties(request.POST)
        form = base_coco(request.POST)
        if po_form.is_valid() and ap_form.is_valid() and pe_form.is_valid() and pr_form.is_valid() and form.is_valid():
            Size = form.cleaned_data['size']

            save_po = {po_form.cleaned_data['save_po']: "save_po"}
            size_bd = {po_form.cleaned_data['size_bd']: "size_bd"}
            prod_lev = {po_form.cleaned_data['prod_lev']: "prod_lev"}

            speed = {ap_form.cleaned_data['speed']: "speed"}
            memory = {ap_form.cleaned_data['memory']: "memory"}
            virtual = {ap_form.cleaned_data['virtual']: "virtual"}
            times ={ap_form.cleaned_data['times']: "times"}

            analiz  = {pe_form.cleaned_data['analiz']: "analiz"}
            oput = {pe_form.cleaned_data['oput']: "oput"}
            sposobnost ={ pe_form.cleaned_data['sposobnost']: "sposobnost"}
            oput_virtual = {pe_form.cleaned_data['oput_virtual']: "oput_virtual"}
            oput_language = {pe_form.cleaned_data['oput_language']: "oput_language"}

            method = {pr_form.cleaned_data['method']: "method"}
            instruments = {pr_form.cleaned_data['instruments']: "instruments"}
            treb = {pr_form.cleaned_data['treb']: "treb"}

            dict_znach = {"save_po":[0.75, 0.88, 1.00, 1.15, 1.40, 1], "size_bd":[1, 0.94, 1.00, 1.08, 1.16, 1],
                          "prod_lev":[0.70, 0.85, 1.00, 1.15, 1.30, 1.65], "speed":[1,1,1.00,1.11,1.30,1.66],
                          "memory":[1,1,1.00,1.06,1.21,1.56], "virtual":[1,0.87,1.00, 1.15, 1.30, 1],
                          "times":[1,0.87, 1.00, 1.07, 1.15,1], "analiz":[1.46, 1.19,1.00, 0.86, 0.71, 1],
                          "oput":[1.29,1.13, 1.00, 0.91,0.82, 1], "sposobnost":[1.42,1.17,1.00,0.86,0.70, 1],
                          "oput_virtual":[1.21,1.10,1.00,0.90, 1,1], "oput_language":[1.14,1.07,1.00,0.95, 1, 1],
                          "method":[1.24,1.10,1.00,0.91, 0.82,1], "instruments":[1.24,1.10,1.00,0.91,0.83,1],
                          "treb":[1.23,1.08,1.00,1.04,1.10,1]}
            dicts = [save_po ,size_bd ,
                          prod_lev , speed ,
                          memory , virtual ,
                          times , analiz ,
                          oput , sposobnost,
                          oput_virtual , oput_language ,
                         method , instruments , treb]

            spisok_znach = genrate_dict(dicts, dict_znach)

            znach = reduce(lambda x, y: x * y, spisok_znach)


            ai, b, c, d = 0, 0, 0, 0
            if form.cleaned_data['sh'] == "Распространненый":
                ai = 3.2
                b = 1.05

            elif form.cleaned_data['sh'] == "Полунезависимый":
                ai = 3.0
                b = 1.12

            elif form.cleaned_data['sh'] == "Встроенный":
                ai = 2.8
                b = 1.20
            PM = 0
            PM = znach * ai * (Size ** b)
            return render(request, self.template, context={"pe_form":pe_form, "ap_form": ap_form, "po_form":po_form,
                                                            "pr_form":pr_form, "form":form, 'PM': PM})
        else:
            return HttpResponse(u'Куда прёшь?')




class Cocomo2View(View):
    template = 'cocomo2.html'

    def get(self, request):
        size_form = SizeForm()
        work_form = WorkForm()
        error_form = ErrorMultForm()
        form = coco2()
        return render(request, self.template,
                      context={"error_form": error_form, "work_form": work_form, "size_form":size_form, "form":form})

    def post(self, request):
        size_form = SizeForm(request.POST)
        work_form = WorkForm(request.POST)
        error_form = ErrorMultForm(request.POST)
        form = coco2(request.POST)
        if size_form.is_valid() and work_form.is_valid() and error_form.is_valid() and form.is_valid():
            Size = form.cleaned_data['size']

            pers = {work_form.cleaned_data['pers']: "pers"}
            prex = {work_form.cleaned_data['prex']: "prex"}
            rcpx = {work_form.cleaned_data['rcpx']: "rcpx"}
            ruse = {work_form.cleaned_data['ruse']: "ruse"}
            pdif = {work_form.cleaned_data['pdif']: "pdif"}
            fcil = {work_form.cleaned_data['fcil']: "fcil"}
            sced = {work_form.cleaned_data['sced']: "sced"}

            prec = {size_form.cleaned_data['prec']: "prec"}
            flex = {size_form.cleaned_data['flex']: "flex"}
            resl = {size_form.cleaned_data['resl']: "resl"}
            team = {size_form.cleaned_data['team']: "team"}
            pmat = {size_form.cleaned_data['pmat']: "pmat"}

            acap = {error_form.cleaned_data['acap']: "acap"}
            aexp = {error_form.cleaned_data['aexp']: "aexp"}
            pcap = {error_form.cleaned_data['pcap']: "pcap"}
            pcon = {error_form.cleaned_data['pcon']: "pcon"}
            pexp = {error_form.cleaned_data['pexp']: "pexp"}
            ltex = {error_form.cleaned_data['ltex']: "ltex"}
            rely = {error_form.cleaned_data['rely']: "rely"}
            data = {error_form.cleaned_data['data']: "data"}
            cplx = {error_form.cleaned_data['cplx']: "cplx"}
            ruse1 = {error_form.cleaned_data['ruse']: "ruse1"}
            docu = {error_form.cleaned_data['docu']: "docu"}
            time = {error_form.cleaned_data['time']: "time"}
            stor = {error_form.cleaned_data['stor']: "stor"}
            pvol = {error_form.cleaned_data['pvol']: "pvol"}
            tool = {error_form.cleaned_data['tool']: "tool"}
            site = {error_form.cleaned_data['site']: "site"}
            sced1 = {error_form.cleaned_data['sced']: "sced1"}

            ai, b, c, d = 0, 0, 0, 0
            if form.cleaned_data['sh'] == 'Предварительная':
                dict_znach_pred = {"pers": [2.12, 1.62, 1.26, 1.00, 0.83, 0.63, 0.50],
                              "prex": [1.59, 1.33, 1.22, 1.00, 0.87, 0.74, 0.62],
                              "rcpx": [0.49, 0.60, 0.83, 1.00, 1.33, 1.91, 2.72],
                              "ruse": [1, 1, 0.95, 1.00, 1.07, 1.15, 1.24],
                              "pdif": [1, 1, 0.87, 1.00, 1.29, 1.81, 2.61],
                              "fcil": [1.43, 1.30, 1.10, 1.00, 0.87, 0.73, 0.62],
                              "sced": [1, 1.43, 1.14, 1.00, 1.00, 1, 1]}
                print('Предварительная')
                print(dict_znach_pred)

                dicts = [pers, prex,
                               rcpx,
                               ruse,
                               pdif,
                               fcil,
                               sced]

                spisok_znach_pred = genrate_dict(dicts, dict_znach_pred)

                znach = reduce(lambda x, y: x * y, spisok_znach_pred)
                print(znach)
                A = 2.94
            else:
                dict_znach_detail = {"acap": [1.42, 1.29, 1.00, 0.85, 0.71, 1],
                              "aexp": [1.22, 1.10, 1.00, 0.88, 0.81, 1],
                              "pcap": [1.34, 1.15, 1.00, 0.88, 0.76, 1],
                              "pcon": [1.29, 1.12, 1.00, 0.90, 0.81, 1],
                              "pexp": [1.19, 1.09, 1.00, 0.91, 0.85, 1],
                              "ltex": [1.20, 1.09, 1.00, 0.91, 0.84, 1],
                              "rely": [0.84, 0.92, 1.00, 1.10, 1.26, 1],
                              "data": [1, 0.23, 1.00, 1.14, 1.28, 1],
                              "cplx": [0.73, 0.87, 1.00, 1.17, 1.34, 1.74],
                              "ruse1": [1, 0.95, 1.00, 1.07, 1.15, 1.24],
                              "docu": [0.81, 0.91, 1.00, 1.11, 1.23, 1],
                              "time": [1, 1, 1.00, 1.11, 1.29, 1.63],
                              "stor": [1, 1, 1.00, 1.05, 1.17, 1.46],
                              "pvol": [1, 0.87, 1.00, 1.15, 1.30, 1],
                              "tool": [1.17, 1.09, 1.00, 0.90, 0.78, 1],
                              "site": [1.22, 1.09, 1.00, 0.93, 0.86, 0.80],
                              "sced1": [1.43, 1.14, 1.00, 1.00, 1.00, 1]}

                dicts = [acap,
                        aexp,
                        pcap,
                        pcon,
                        pexp,
                          ltex,
                        rely,
                         data,
                         cplx,
                       ruse1,
                        docu,
                      time,
                      stor,
                      pvol,
                       tool,
                       site,
                       sced1]

                spisok_znach_detail= genrate_dict(dicts, dict_znach_detail)
                znach = reduce(lambda x, y: x * y, spisok_znach_detail)
                print(znach)
                A = 2.45


            dict_znach = {"prec":[6.20, 4.96, 3.72,2.48,1.24,0.00],
                        "flex":[5.07,4.05,3.04,2.03,1.01,0.00],
                        "resl":[7.07,5.65,4.24,2.83,1.41,0.00],
                        "team":[5.48,4.38,3.29,2.19,1.10,0.00],
                         "pmat":[7.80,6.24,4.68,3.12,1.56,0.00]}
            dicts = [prec,
                           flex,
                           resl,
                           team,
                           pmat]

            spisok_znach = genrate_dict(dicts, dict_znach)

            znach_sum = reduce(lambda x, y: x + y, spisok_znach)

            E = 0.91 + (0.01 * znach_sum)
            PM = znach * A * (Size ** E)
            return render(request, self.template, context={"error_form": error_form, "work_form": work_form,
                                                                     "size_form":size_form, "form":form, 'PM': PM})
        else:
            return HttpResponse(u'Куда прёшь?')