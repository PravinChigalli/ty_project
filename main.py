#joke
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from helpers import screen_helper
from kivy.uix.screenmanager import ScreenManager
from emailverfication import email_ver
from sql import search_data, profile_data
from local_app_data import save_theme, load_theme, load_primary, load_accent, check_status, set_status, get_profile

Window.size = (360, 600)


class HomeScreen(Screen):
    pass


class SearchScreen(Screen):
    pass


class SettingsScreen(Screen):
    f = 0


class FaqsScreen(Screen):
    pass


class FeedbackScreen(Screen):
    pass


class ProfileScreen1(Screen):
    no = 0


class ProfileScreen2(Screen):
    pass


class ReportUrlScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(SearchScreen(name='profile'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(FaqsScreen(name='faqs'))
sm.add_widget(FeedbackScreen(name='feedback'))
sm.add_widget(ProfileScreen1(name='profile1'))
sm.add_widget(ProfileScreen2(name='profile2'))
sm.add_widget(ReportUrlScreen(name='report'))


class Demo(MDApp):
    picker = None
    valid = 0

    def build(self):

        self.theme_cls.theme_style = load_theme()
        self.theme_cls.primary_palette = load_primary()
        self.theme_cls.accent_palette = load_accent()

        screen = Builder.load_string(screen_helper)
        # urL = MDTextField(text='Enter url', pos_hint={'center_x': 0.5, 'center_y': 0.6}, size_hint={})
        # btn1 = MDRectangleFlatButton(text='Search', pos_hint={'center_x': 0.8, 'center_y': 0.5}, size_hint=(0.045, 0.05))
        # btn2 = MDFloatingActionButton(icon='plus', pos_hint={'center_x': 0.9, 'center_y': 0.1})
        # url = Builder.load_string(url_helper)
        # screen.add_widget(url)
        # screen.add_widget(btn1)
        # screen.add_widget(btn2)
        return screen

    def go_back(self, screen_name):
        self.root.current = screen_name

    def show_themepicker(self):
        self.picker = MDThemePicker()
        self.picker.open()

    def store_theme(self, f):
        if f == 1:
            save_theme(self.picker.theme_cls.theme_style, self.picker.theme_cls.primary_palette,
                       self.picker.theme_cls.accent_palette)
            self.toast_text(8)
        else:
            self.toast_text(9)

    def get_url(self):
        Link = self.root.get_screen('home').ids.link.text
        users = search_data(self, Link)
        # print(users)
        user = None
        for user in users:
            pass
        self.root.get_screen('search').ids.label1.text = Link

        if user == None:
            self.root.get_screen('search').ids.label2.text = "NOT FAKE"
        else:
            self.root.get_screen('search').ids.label2.text = "FAKE"

    def register(self):
        strng1 = self.root.get_screen('profile1').ids.name.text
        strng2 = self.root.get_screen('profile1').ids.mail.text
        if self.valid == 0:
            self.toast_text(5)
        elif len(strng1) == 0:
            self.toast_text(6)
        else:
            self.root.current = 'profile2'
            profile_data(self)
            set_status(1, strng2, strng1)
            self.root.get_screen('profile2').ids.username.text = self.root.get_screen('profile1').ids.name.text
            self.root.get_screen('profile2').ids.emailid.text = self.root.get_screen('profile1').ids.mail.text
            self.toast_text(7)

    def get_mail(self):
        no = 0
        strng = self.root.get_screen('profile1').ids.mail.text
        if strng.endswith("gmail.com"):
            no = email_ver(strng)
            self.toast_text(1)
        else:
            self.toast_text(2)
        return no

    def toast_text(self, p):
        if p == 0:
            toast("Sending Otp...!")
        elif p == 1:
            toast("OTP Sent...!")
        elif p == 2:
            toast("Couldn't send OTP. Please Enter a valid Gmail ID...!")
        elif p == 3:
            toast("OTP Verification Successful...!")
        elif p == 4:
            toast("Invalid OTP.Verification Unsuccessful...!")
        elif p == 5:
            toast("First Verify your gmail id using OTP...!")
        elif p == 6:
            toast("Please Enter your name...!")
        elif p == 7:
            toast("Successfully Registered...!")
        elif p == 8:
            toast("Changes Saved...!")
        elif p == 9:
            toast("Theme already saved...!")

    def validate_otp(self, no):
        if no == self.root.get_screen('profile1').ids.otp.text:
            self.toast_text(3)
            self.valid = 1
        else:
            self.toast_text(4)
            self.valid = 0

    def profile_status(self, s):
        strng = ""
        strng1 = ""
        if s == 0:
            status = check_status()
            if status == 0:
                self.root.current = 'profile1'
            else:
                self.root.get_screen('profile2').ids.emailid.text = get_profile(0)
                self.root.get_screen('profile2').ids.username.text = get_profile(1)
                self.root.current = 'profile2'
        elif s == 2:
            set_status(0, strng, strng1)

    def float(self):
        if check_status() == 0:
            self.root.current = 'profile1'
        else:
            self.root.current = 'report'


Demo().run()
