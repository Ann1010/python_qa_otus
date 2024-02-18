from subprocess import run, PIPE
import os


def pars_ps_aux():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    res = run(["ps aux"], shell=True, stdout=PIPE).stdout.decode('utf-8').split('\n')
    res = [list(filter(None, row.replace('\n', '').split(" "))) for row in res if row]
    dict_ps = {}
    for el in res[0]:
        dict_ps[el] = []
    for i in range(1, len(res)):
        if res[i][0][0] != '_':
            dict_ps['USER'].append(res[i][0])
            dict_ps['%CPU'].append(float(res[i][2]))
            dict_ps['%MEM'].append(float(res[i][3]))
            dict_ps['COMMAND'].append(res[i][10])
    for i in range(1, len(res)):
        if res[i][0][0] != "_":
            if res[i][0] in dict_ps:
                dict_ps[res[i][0]] += 1
            else:
                dict_ps[res[i][0]] = 1
    return dict_ps


def max_mem_ps(dict_ps):
    """Определение названия процесса с максимальной используемой памятью"""
    max_index = dict_ps['%MEM'].index(max(dict_ps['%MEM']))
    return dict_ps['COMMAND'][max_index][:20]


def max_cpu_ps(dict_ps):
    """Определение названия процесса с максимальной используемым CPU"""
    max_index = dict_ps['%CPU'].index(max(dict_ps['%CPU']))
    return dict_ps['COMMAND'][max_index][:20]


def write_res(ps_dict):
    with open("report_ps_aux.txt", "w") as file:
        file.write(f"Отчёт о состоянии системы: \n"
                   f"Пользователи системы: {set(ps_dict['USER'])}\n"
                   f"Процессов запущено: {len(ps_dict['USER'])}\n"
                   f"\r\n"
                   f"Пользовательских процессов:\n")
        for el in set(ps_dict['USER']):
            file.write(f"{el}: {ps_dict[el]}\n")
        file.write(f"\r\n"
                   f"Всего памяти используется: {round(sum(ps_dict['%MEM']), 2)}% \n"
                   f"Всего CPU используется: {round(sum(ps_dict['%CPU']), 2)}% \n"
                   f"Больше всего памяти использует: {max_mem_ps(ps_dict)}\n"
                   f"Больше всего CPU использует: {max_cpu_ps(ps_dict)}")


if __name__ == "__main__":
    write_res(pars_ps_aux())
