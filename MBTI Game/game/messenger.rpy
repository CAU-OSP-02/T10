#################################################################################
# by sDextra
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################

#################################################################################
### Messenger Emulator
#################################################################################
init python:
#################################################################################
    display_aspect_ratio = 16.0 / 9.0
    yadj = ui.adjustment()

    messages = []

    message_time = False
    in_history = True
    choice_number = True
    click_to_continue = True
    under_messenger = True
    time_to_send_pm = 2.0
    time_to_send_am = 2.0

    typewriter = True
    typewriter_speed = 1
    typewriter_counter = 0

    interlocutor = "sDextra"
    interlocutor_online = True
    interlocutor_typing = True
    interlocutor_extra_time = 1
    interlocutor_typing_speed = 0.1
    interlocutor_typing_show = False
    interlocutor_sends = False

    audio_path = 'sfx/'
    audio_extension = '.mp3'

    def show_messenger():
        _window_hide()
        renpy.show_screen('messenger')
        renpy.pause(1.0, hard=True)
    def hide_messenger():
        renpy.hide_screen('messenger')
        renpy.pause(1.0, hard=True)
        _window_show()

    from mutagen.mp3 import MP3
    class Audio():
        def __init__(self, name, bar):
            self.file_name = name
            self.name = audio_path + self.file_name + audio_extension
            self.length = self.get_audio_length(self.name)
            self.duration = self.get_duration(self.length)
            self.bar = renpy.random.randint(1,9) if not bar else bar

        # get mp3 file length
        def get_audio_length(self, name):
            file = renpy.loader.transfn(name)
            audio = MP3(file)
            length = int(round(audio.info.length, 0))
            return length
        def play(self):
            renpy.play(self.name, channel='sound')
        def bar_idle(self):
            return 'messenger/audio/bar_'+str(self.bar)+'.png'
        def bar_hover(self):
            return color_brightness('messenger/audio/bar_'+str(self.bar)+'.png')
        # Audio's minutes and seconds
        def get_duration(self, d):
            m = d // 60
            m = '0'+str(m) if m < 10 else m
            s = d % 60
            s = '0'+str(s) if s < 10 and s != 0 else str(s)+'0' if s == 0 else s
            return "%s:%s"%(m,s)

    class Picture():
        def __init__(self, name, x):
            self.name = str(name)
            self.x = x # maximum 297
            # self.y = x
            self.y = int(x/display_aspect_ratio)
            # self.x = int(y/display_aspect_ratio)
            # self.y = y
        # Open picture to fulll screen
        def open_fullpic(self):
            renpy.show_screen('sc_fullpic', pic=self.name)

    from datetime import datetime
    class Message():
        def __init__(self, what, who, choices, audio, audio_bar, pic, pic_x, time):
            self.what = what
            self.who = who
            self.time_list = time
            self.choices = choices
            self.position = self.find_position(who)
            self.pic = Picture(pic, pic_x) if pic else False
            self.audio = Audio(audio, audio_bar) if audio else False
            self.time = self.format_time(time) if type(message_time) != bool else self.get_current_time() if time else False

        def find_position(self, who):
            position = 0.0 if who else .99
            return position

        # time from
        def get_current_time(self):
            now = datetime.now()
            time = datetime.strftime(now, "%H:%M")
            return time

        # Message time
        def format_time(self, time):
            h, m = time
            m = '0'+str(m) if m < 10 and m != 0 else str(m)+'0' if m == 0 else m
            h = '0'+str(h) if h < 10 and h != 0 else str(h)+'0' if h == 0 else h
            return "%s:%s"%(h,m)


    # New message
    def msg(what, who=0, choices=False, pic=False, pic_size=360, audio=False, audio_bar=0, status=False):
        if status:
            store.interlocutor_online = True if status == 'online' else interlocutor_online

        if who and what and interlocutor_typing:
            store.interlocutor_typing_show = True
            renpy.pause(interlocutor_extra_time, hard=True)
            speed = len(what) * interlocutor_typing_speed
            renpy.pause(speed, hard=True)
            store.interlocutor_typing_show = False

        if pic or audio:
            sends = 'status_picture' if pic else 'status_audio'
            time = time_to_send_pm if pic else time_to_send_am
            if who:
                store.interlocutor_sends = sends
                renpy.pause(time, hard=True)
                store.interlocutor_sends = False
            else:
                renpy.pause(time, hard=True)


        time_update()
        store.messages.append(Message(what, who, choices, audio, audio_bar, pic, pic_size, message_time))
        store.yadj.value = 9999*9999
        store.typewriter_counter = 0

        if status:
            store.interlocutor_online = False if status == 'offline' else interlocutor_online
        if in_history:
            add_history(who, what)
        if who:
            renpy.play(store.audio_path+'new_message'+store.audio_extension, 'audio')

        renpy.restart_interaction()
        if not click_to_continue:
            if who or not who and not typewriter:
                renpy.pause(1.0, hard=True)
            else:
                renpy.pause()
        else:
            renpy.pause()

        if choices:
            freeze()


    def find(what):
        temp = []
        if what == "":
            return temp
        for message in messages:
            # add usual message
            if message.what:
                if what.lower() in message.what.lower():
                    temp.append(message)
            else:
                # add pic
                if what == '#pic':
                    if message.pic:
                        temp.append(message)
                # add audio message
                elif what == '#audio':
                    if message.audio:
                        temp.append(message)
        return temp

    input_find = ""
    def find_change_func(value):
        store.input_find = value
        store.yadj.value = 0
        renpy.restart_interaction()
    def find_reset():
        store.input_find = ""
        store.yadj.value = 9999*9999

    # Add message to history
    def add_history(who, what):
        who = store.interlocutor if who == 1 else store.name
        if what:
            store.narrator.add_history(kind='adv', who=who, what=what)

    # Message time update
    def time_update(m=1):
        if type(message_time) != bool:
            hours, minutes = message_time
            if minutes + m >= 60:
                hours += 1
                if hours >= 24:
                    hours = 0
                minutes += m-60
            else:
                minutes += m
            store.message_time = [hours, minutes]

    def unpause():
        renpy.pause(.1)


    # Delete the last message
    def del_last_msg():
        if len(store.messages) > 0:
            del store.messages[-1]
    # Clear exluding the last message
    def del_previous_msg():
        del store.messages[:-1]
    # Clear all messages
    def del_all_msg():
        store.messages = []
    # Choice logic
    def die_is_cast(lbl):
        unfreeze()
        del_last_msg()
        renpy.jump(lbl)
    # Status
    def online():
        store.interlocutor_online = True
    # Status
    def offline():
        store.interlocutor_online = False
    # Block Skip
    def freeze():
        renpy.config.skipping = False
        store._skipping = False
        renpy.pause(9999, hard=True)
    # Unblock Skip
    def unfreeze():
        store._skipping = True

    # Tag for message time
    def time_tag(tag, argument, contents):
        size = 18
        color = store.style_gray
        return [ (renpy.TEXT_TAG, u"size={}".format(size)), (renpy.TEXT_TAG, u"color={}".format(color)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/size"), (renpy.TEXT_TAG, u"/color"), ]
    config.custom_text_tags["t"] = time_tag

    # input
    # is_input = False

# screen input_msg():
#     input default "?????? ?????? ??? ?????? ??????????" style 'txt_base' align .659, .934 xanchor 0 length 14 color '#fff'
#     $ is_input = True


    # my_msg = ""
    # def input_msg(value):
    #     # is_input = True
    #     my_msg = value

#################################################################################


#################################################################################
# Messenger Screen
#################################################################################
screen messenger():
    if under_messenger:
        add '#00000090' at blackout
    default find_enable = False
    key 'anykey' action NullAction()

    # Interlocutor's Avatar
    frame background None xysize (400,650) at move_messenger:
        add 'messenger/av/'+interlocutor.lower().replace(' ', '_')+'.png' pos (43,14)
        add 'messenger_background' pos (-6,-6)
        frame background None xysize (372, 525) align (0.1,0.58):
            viewport id 'vp_msg' mousewheel True  yadjustment yadj:
                vbox spacing 15 xsize 365 xalign 0.4 box_reverse True:
                    $ all_messages = find(input_find) if find_enable else messages[::-1]
                    for message in all_messages:
                        $ you = not message.who
                        $ complete_message = typewriter_counter >= len(message.what) if message.what else True
                        $ can_type = you and typewriter and message == messages[-1] and not complete_message and not interlocutor_typing_show
                        $ box = 'box_one' if you else 'box_two'
                        $ box_hover = 'hover_box' if you else 'hover_box_two'
                        if message.audio: # Audio
                            default played = False
                            default audio_sec = 0
                            $ playing = renpy.music.get_playing(channel='sound')
                            $ current_audio = audio_sec if message.audio.name == playing else 0
                            $ now_play = message.audio.name == playing
                            $ audio_idle = 'stop_idle' if now_play else 'play_idle'
                            $ audio_hover = 'stop_hover' if now_play else 'play_hover'
                            $ xoffset = 1.08 if you and played and now_play else 0 # because of the viewport bug~
                            frame background Frame(box, 25, 25) xalign message.position xysize 360,95:
                                hbox spacing -250 xalign message.position-xoffset:
                                    hbox spacing -50:
                                        button xysize 229,58 background audio_idle hover_background audio_hover action If (now_play, [Stop('sound')], [SetScreenVariable('played', True), SetScreenVariable('audio_sec', 0), Function(message.audio.play)]):
                                            text "{k=1.5}%s{/k}"%(message.audio.duration) style 'txt_base' align .26,.9 xanchor 0.0 size 22 color style_gray
                                        if message_time:
                                            text "{t}%s{/t}"%(message.time) style 'txt_time'
                                    if played and now_play:
                                        timer 0.05 repeat True action SetScreenVariable('audio_sec', audio_sec+0.05), If(audio_sec>=message.audio.length, [SetScreenVariable('audio_sec', 0), SetScreenVariable('played', False)])
                                    $ bar_xoffset = 140 if played and now_play else 0 # because of the viewport bug~
                                    bar value StaticValue(current_audio, message.audio.length) yalign .25 xpos bar_xoffset maximum (241, 29) thumb None left_bar message.audio.bar_hover() right_bar message.audio.bar_idle()
                        elif message.pic: # Picture
                            hbox spacing 0 xalign message.position:
                                $ bottom = 35 if message_time else 20
                                button xalign message.position xmaximum 200 xpadding 0 top_padding 20 bottom_padding bottom background Frame(box, 25, 25) hover_background Frame(box_hover, 25,25) action Function(message.pic.open_fullpic):
                                    add 'messenger/pic/'+message.pic.name+'.png' align .5,.5 size message.pic.x, message.pic.y
                                if message_time:
                                    text "{t}%s{/t}"%(message.time) style 'txt_time'
                        elif message.choices: # Menu
                            frame xalign message.position xmaximum 297 xpadding 20 ypadding 10 background Frame(box, 25, 25):
                                vbox:
                                    $ sort = sorted(message.choices.items(), key=lambda x: x)
                                    for k, v in sort:
                                        $ k = k+1
                                        $ txt = "%s"%(v.get('name', 'choice %s'%(k) )) # if not found - "choice 'number'"
                                        $ lbl = v.get('jump', 'start') # if not found - jump start
                                        $ t = "%s. %s"%(k, txt) if choice_number else "%s"%(txt)
                                        textbutton t hover_background '#5FB8D2' action Function(die_is_cast, lbl):
                                            text_size 20 text_font style_font text_xalign 1.0 text_color '#fff'
                                        if choice_number:
                                            key str(k) action Function(die_is_cast, lbl)
                        else: # Usual message
                            $ hm = message.time
                            $ txt = message.what
                            if can_type: # Typewriter
                                $ hm = "" # do not show time in last message
                                $ txt = message.what[:typewriter_counter]
                            $ bottom = 30 if message_time else 15
                            hbox spacing -60 xalign message.position:
                                button xalign message.position xmaximum 292 xpadding 20 top_padding 15 bottom_padding bottom background Frame(box, 25, 25):
                                    text "%s"%(txt) style 'txt_base'
                                if message_time:
                                    text "{t}%s{/t}"%(hm) style 'txt_time'
                                if can_type:
                                    key 'dismiss' action NullAction() # Block skip
                                    key 'anykey' action SetVariable('typewriter_counter', typewriter_counter+typewriter_speed)
        # input_find
        # Interlocutor's name & status
        $ status = 'status_typing' if interlocutor_typing_show else 'status_online' if interlocutor_online else 'status_offline'
        $ status = interlocutor_sends if interlocutor_sends else status
        text "%s"%(interlocutor) style 'txt_base' size 18 xalign 0.25 xanchor 0.0 yalign 0.025
        add status align 0.25, 0.06 xanchor 0.0

        # Arrow
        image 'arrow_idle' pos (9, 21)
        # Magnifier
        # if not is_input:
        $ magnifier_idle = 'magnifier_hover' if find_enable else 'magnifier_idle'
        imagebutton idle magnifier_idle hover 'magnifier_hover' pos (357, 20) action If(find_enable, [Function(find_reset), SetScreenVariable('find_enable', False)], SetScreenVariable('find_enable', True))

        if find_enable:
                input changed find_change_func style 'txt_base' length 14 align .12,.99 xanchor 0 color '#fff'
                key 'K_ESCAPE' action Function(find_reset), SetScreenVariable('find_enable', False)

        # Telegram bar
        vbar value YScrollValue('vp_msg') style 'bar_vert'

        # input_msg
        # if is_input:
        #     input default "?????? ?????? ??? ?????? ??????????" style 'txt_base' length 14 align .12,.99 xanchor 0 color '#fff' action SetVariable(my_msg, value)

#################################################################################
screen sc_fullpic(pic=False):
    modal True zorder 10
    add '#00000090' at blackout
    add 'messenger/pic/'+pic+'.png' at move_pic
    button background None action Hide('sc_fullpic')
#################################################################################

#################################################################################
# by sDextra
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################
