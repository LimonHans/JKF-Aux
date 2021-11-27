###############################
#   HansLimon at 2021/09/21   #
#                             #
# Only for educational usage. #
#                             #
#     CopyLEFT Mongrokey®     #
###############################
from ScreenShow import ScreenShow
from win32api import ShellExecute

if __name__ == '__main__':
    userans = ScreenShow("达摩克利斯之剑", ["达摩克利斯之剑——模式选择：", "不重复之剑", "完全随机之剑"], "choose")
    print(userans)
    if userans == "不重复之剑":
        ShellExecute(0, 'open', '.\\NoneRepeatKiller.exe', '', '', 0)
    elif userans == "完全随机之剑":
        ShellExecute(0, 'open', '.\\Killer.exe', '', '', 0)