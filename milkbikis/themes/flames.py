# these symbols for now have to be set directly in powerline-shell.py:
#class Powerline:
#    symbols = {
#        # flames (flamey)
#        'patched': {
#            'lock': u'\uE0A2',
#            'network': u'\uE0A2',
#            'separator': u'\uE0C0',
#            'separator_thin': u'\uE0C1'
#        }
#    }

# flame colors (Work in progress)!

class Color(DefaultColor):
    USERNAME_FG = 250
    #USERNAME_BG = 240
    USERNAME_BG = 226
    #USERNAME_ROOT_BG = 124
    USERNAME_ROOT_BG = 160

    HOSTNAME_FG = 250
    HOSTNAME_BG = 238

    HOME_SPECIAL_DISPLAY = True
    #HOME_BG = 31  # blueish
    HOME_BG = 208  # blueish
    HOME_FG = 15  # white
    #PATH_BG = 237  # dark grey
    PATH_BG = 166 # dark grey
    #PATH_FG = 250  # light grey
    PATH_FG = 15  # light grey
    #CWD_FG = 254  # nearly-white grey
    CWD_FG = 15 # nearly-white grey
    #SEPARATOR_FG = 244
    SEPARATOR_FG = 15

    #READONLY_BG = 124
    READONLY_BG = 160
    READONLY_FG = 254

    SSH_BG = 166 # medium orange
    SSH_FG = 254

    REPO_CLEAN_BG = 148  # a light green color
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 161  # pink/red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 39
    JOBS_BG = 238

    #CMD_PASSED_BG = 236
    CMD_PASSED_BG = 160
    CMD_PASSED_FG = 15
    #CMD_FAILED_BG = 161
    CMD_FAILED_BG = 160
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = 148
    SVN_CHANGES_FG = 22  # dark green

    VIRTUAL_ENV_BG = 35  # a mid-tone green
    VIRTUAL_ENV_FG = 00
