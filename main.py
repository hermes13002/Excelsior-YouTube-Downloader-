from kivymd.app import MDApp
from kivy.lang import Builder
from pytube import *
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.utils import platform
import os
import webbrowser



kv = '''
MDScreen:
    name: "main"
    title: title
    label: label
    thumbnail: thumbnail
    MDFloatLayout:
        #md_bg_color: 53/255, 56/255, 60/255, 1''
        MDFloatLayout:
            size_hint: .9, .097
            pos_hint: {'center_x': .5, 'center_y': .84}
            canvas:
                Color:
                    rgb: 238/255, 238/255, 238/255, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
            TextInput:
                id: url_textinput
                hint_text: 'Enter The Video URL/Link'
                size_hint: 1, None
                pos_hint: {'center_x': .5, 'center_y': .5}
                height: self.minimum_height
                multiline: False
                cursor_color: 0, 0, 0, 1
                cursor_width: '2sp'
                background_color: 0, 0, 0, 0 
                padding: 15
                font_size: '23sp'
        Button:
            text: 'Save'
            size_hint: .9, .065
            pos_hint: {'center_x': .5, 'center_y': .67}
            background_color: 30, 144, 255, 0
            font_size: '23sp'
            color: 1, 1, 1, 1
            on_press: app.downloading_video(url_textinput.text)
            canvas.before:
                Color:
                    rgb: 30/255, 144/255, 255/255, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [7]
        MDLabel:
            id: title
            pos_hint: {'center_x': .5, 'center_y': .55}
            font_size: '20sp'
            theme_text_color: 'Custom'
            text_color: 1, 0, 0, 1
            halign: "center"
        AsyncImage:
            id: thumbnail
            source: ""
            pos_hint: {"center_x": .5, "center_y": .30}
            size_hint_y: .35
            size_hint_x: .70
            background_color: 0, 0, 0, 0
        MDLabel:
            id: label
            pos_hint: {'center_x': .5, 'center_y': .07}
            font_size: '26sp'
            theme_text_color: 'Custom'
            text_color:  30/255, 144/255, 255/255, 1
            halign: "center"
            
            
            
    MDToolbar:
        id: toolbar
        title:  'Excelsior YT Downloader'
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open") ]]
        elevation: 10
        pos_hint: {"x": 0, "top": 1}
        size_hint_y: .065
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '20dp'
            padding: '20dp'
            MDRectangleFlatButton:
                text: "DARK MODE"
                size_hint: .9, .095
                on_press: self.theme_cls.theme_style = "Dark"
                pos_hint: {"center_x": .5, "center_y": .7}
            MDRectangleFlatButton:
                text: "LIGHT MODE"
                size_hint: .9, .095
                on_press: self.theme_cls.theme_style = "Light"
                pos_hint: {"center_x": .5, "top": 1}
            MDLabel:
                text: "CONTACT ME"
                font_size: '30sp'
                font_style: "Button"
                size_hint_y: None
                height: self.texture_size[1]
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 30/255, 144/255, 255/255, 1
            MDRectangleFlatButton:
                text: "DISCORD"
                size_hint: .9, .095
                on_release: app.contact_discord()
                pos_hint: {"center_x": .5, "center_y": .7}
            MDRectangleFlatButton:
                text: "WHATSAPP"
                size_hint: .9, .095
                on_release: app.contact_whatsapp()
                pos_hint: {"center_x": .5, "center_y": .7}
            MDRectangleFlatButton:
                text: "MY WEBSITE"
                size_hint: .9, .095
                on_release: app.contact_website()
                pos_hint: {"center_x": .5, "center_y": .7}
            MDRectangleFlatButton:
                text: "EXIT"
                size_hint: .9, .095
                on_release: app.win_exit()
                pos_hint: {"center_x": .5, "center_y": .7}
            ScrollView:
'''



class YouTube_Downloader(MDApp):
    image = False
    if platform == 'android':
          from android.storage import primary_external_storage_path
          dir = primary_external_storage_path()
          download_dir_path = os.path.join(dir, 'Download')


    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("splash.kv"))
        screen_manager.add_widget(Builder.load_string(kv))
        return screen_manager
        #kvstring = Builder.load_string(kv)
        #return kvstring

    def on_start(self):
        Clock.schedule_once(self.main, 10)

    def main(self, *args):
        screen_manager.current = "main"

    def assets(self, thumbnail, title):
        screen_manager.get_screen('main').thumbnail.source=thumbnail
        screen_manager.get_screen('main').title.text='VIDEO TITLE: '+ title

    def download_video(self, stream):
        if self.image_loaded == True:
              stream.download(self.download_dir_path)
        screen_manager.get_screen('main').label.text= "Download Complete"


    def downloading_video(self, url):
        video = YouTube(url)
        self.assets(video.thumbnail_url, video.title)
        self.image_loaded = True
        Clock.schedule_once(lambda x: self.download_video(video.streams.get_highest_resolution()), 4)
        screen_manager.get_screen('main').label.text = "Video Downloading"
    
    
    def contact_discord(self):
        webbrowser.open_new('www.discordapp.com/users/Excelsior01#0442')
    def contact_whatsapp(self):
        webbrowser.open_new('https://api.whatsapp.com/send?phone=2347050250008')
    def contact_website(self):
        webbrowser.open_new('https://hermes13002.github.io/My-Portfolio-Website/')
    
    def win_exit(self):
          exit()



YouTube_Downloader().run()