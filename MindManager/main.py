from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from navigation import navigation_helper
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
import random
import pickle
import os

import calendar
import sklearn

Window.size = (300, 500)


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class EduApp(MDApp):
    dialog = None
    h_indicator = 0

    def build(self):
        MainScreen = Screen()
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.secondary_palette = "Black"
        screen = Builder.load_string(navigation_helper)
        # MainScreen.add_widget(screen)
        return screen

    def on_start(self):
        self.root.ids.happy.opacity = 1
        self.root.ids.neutral.opacity = 1
        self.root.ids.sad.opacity = 1
        self.root.ids.feelButton.opacity = 1
        self.root.ids.eduTips.disabled = True
        self.root.ids.sad.disabled = False
        self.root.ids.happy.disabled = False
        self.root.ids.neutral.disabled = False

        self.h_indicator = pickle.load(open("happy_score.dat", "rb"))

    def on_stop(self):
        pickle.dump(self.h_indicator, open("happy_score.dat", "wb"))

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def show_time_picker(self):
        from datetime import datetime

        previous_time = datetime.strptime("03:20:00", '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        time_dialog.set_time(previous_time)
        time_dialog.open()

    def get_time(self, instance, time):
        return time

    def get_date(self, date):
        pass

    def show_date_picker1(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def get_data(self, grade_1, grade_2, failures, studytime):
        if self.check_data(grade_1, grade_2, failures, studytime):
            test_data = self.pre_process(grade_1, grade_2, failures, studytime)
            reg = pickle.load(open("reg_algo.pickle", "rb"))
            prediction = reg.predict([test_data])
            prediction *= 5
            prediction = str(prediction)

            prediction = prediction[1:5] + "%"

            close_button = MDFlatButton(text="Close", on_release=self.close_dialog)

            self.dialog = MDDialog(text="" + prediction, title="Your Test Prediction:",
                                   size_hint=(.75, 1),
                                   buttons=[close_button])
            self.dialog.open()

        else:
            close_button = MDFlatButton(text="Close", on_release=self.close_dialog)

            self.dialog = MDDialog(text="Please enter numeric values.", title="Invalid Inputs",
                                   size_hint=(.75, 1),
                                   buttons=[close_button])
            self.dialog.open()

    def pre_process(self, grade_1, grade_2, failures, studytime):

        grade_1 = float(grade_1) / 5
        grade_2 = float(grade_2) / 5
        failures = int(failures)
        studytime = int(studytime)
        if failures <= 3:
            failures = failures
        else:
            failures = 4
        if studytime < 2:
            studytime = 1
        elif studytime >= 2 and studytime <= 5:
            studytime = 2
        elif studytime > 5 and studytime <= 10:
            studytime = 3
        else:
            studytime = 4
        return [failures, studytime, grade_1, grade_2]

    def check_data(self, grade_1, grade_2, failures, studytime):
        # checks to see if entries are valid
        try:
            grade_1 = float(grade_1)
        except:
            return False
        try:
            grade_2 = float(grade_2)
        except:
            return False
        try:
            failures = int(failures)
        except:
            return False
        try:
            studytime = round(float(studytime))
        except:
            return False

        if (isinstance(grade_1, int) or isinstance(grade_1, float)) and (
                isinstance(grade_2, int) or isinstance(grade_2, float)) and (isinstance(failures, int)) and (
                isinstance(studytime, int) or isinstance(studytime, float)):
            return True
        else:
            return False

    def rand_tips(self):
        tips = ["Avoid Caffeine, Alcohol, and Nicotine :)",
                "Indulge in Physical Activity",
                "Get some sleep!", "Try Some Relaxation Techniques!",
                "Talk to someone!", "Take Control!",
                "Create a fresh start - Clean your room",
                "Rest!", "Keep a positive attitude!", "Try some yoga!",
                "Be the assertive person I know you are!", "If you smoke, stop.",
                "Take responsibility", "Hug a loved one ;)",
                "Write down a goal."]
        n = random.randrange(0, len(tips))
        return tips[n]

    def change_tip(self):
        self.root.ids.eduTips.text = self.rand_tips()

    def get_name(self, text):
        self.root.ids.welcome_text.text = f"Welcome, {text}"

    def show_settings(self):
        self.ContentNavigationDrawer.screen_manager.current = "settings"

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=2020,
            month=8,
            day=22,
        )

        date_dialog.open()

    def monthValue(self, monthss):
        if (
                monthss == 1 or monthss == 3 or monthss == 5 or monthss == 7 or monthss == 8 or monthss == 10 or monthss == 12):
            return 31
        elif (monthss == 4 or monthss == 6 or monthss == 9 or monthss == 11):
            return 30
        else:
            return 29

    ### Whole month crap
    def checkDate(self, days, months, years):
        MDDatePicker(
            callback=self.get_date,
            year=2020,
            month=8,
            day=22,
        )
        yearsAway = 1
        monthsAway = 1
        daysAway = 1
        if (float(years) >= float(MDDatePicker.today.year)):

            if (float(months) - float(MDDatePicker.today.month) < 0):

                monthsAway = float(months) - float(MDDatePicker.today.month) + 12
                print(monthsAway)
            else:
                monthsAway = float(months) - float(MDDatePicker.today.month)

                print(monthsAway)
            if (float(days) - float(MDDatePicker.today.day) < 0):
                daysAway = float(days) - float(MDDatePicker.today.day) + self.monthValue(float(months))

                print(daysAway)
            else:
                daysAway = float(days) - float(MDDatePicker.today.day) + self.monthValue(float(months))
                print(daysAway)

            if float(months) <= float(MDDatePicker.today.month):
                if (float(days) < float(MDDatePicker.today.day)):
                    yearsAway = float(years) - float(MDDatePicker.today.year) - 1
                    print(yearsAway)

                else:
                    yearsAway = float(years) - float(MDDatePicker.today.year)
                    print(yearsAway)

            else:
                yearsAway = float(years) - float(MDDatePicker.today.year)
                print(yearsAway)
        return str(monthsAway), str(daysAway), str(yearsAway)

    ### Adds items to the list
    def addListItem(self, list, item1, item2):
        dates = TwoLineListItem(text=item1, secondary_text=item2)
        list.add_widget(dates)

    def send_happieness(self, num):
        self.root.ids.eduTips.opacity = 1
        self.root.ids.eduTips.disabled = False
        self.root.ids.tip_btn.opacity = 1
        self.root.ids.tip_btn.disabled = False
        num = float(num)
        self.h_indicator += num
        if self.h_indicator <= -3 and self.root.ids.friend_email.text:
            # send email to friend
            pass

    def check_study_data(self, level, course_count, desired):
        if level != "E" or level != "M" or level != "H":
            return False
        elif desired != "A" or desired != "B" or desired != "C":
            return False
        else:
            return course_count.isnumeric()

    def study_time(self, level, course_count, desired):
        if self.check_study_data(level, course_count, desired):
            course_count = int(course_count)
            if level == "E":
                if desired == "A":
                    time = (course_count * 3)
                elif desired == "B":
                    time = (course_count * 2)
                elif desired == "C":
                    time = (course_count * 1)
            elif level == "M":
                if desired == "A":
                    time = (course_count * 3) + 2
                elif desired == "B":
                    time = (course_count * 2.5) + 2
                elif desired == "C":
                    time = (course_count * 2) + 2
            elif level == "H":
                if desired == "A":
                    time = (course_count * 3) + 3
                elif desired == "B":
                    time = (course_count * 2.7) + 3
                elif desired == "C":
                    time = (course_count * 2.5) + 3

            time = time / course_count
            if time > 60:
                hours = time / 60
                minutes = time % 60
                time = f"{hours} hours, and {minutes} per week"
            else:
                minutes = time

                time = f"{minutes} min. per week"

            close_button = MDFlatButton(text="Close", on_release=self.close_dialog)

            self.dialog = MDDialog(text=time, title="Your Study-Time:",
                                   size_hint=(.75, 1),
                                   buttons=[close_button])
            self.dialog.open()

        else:
            close_button = MDFlatButton(text="Close", on_release=self.close_dialog)

            self.dialog = MDDialog(text="Please enter appropriate values.", title="Invalid Inputs",
                                   size_hint=(.75, 1),
                                   buttons=[close_button])
            self.dialog.open()


app = EduApp().run()
import bugs

bugs.fixBugs()
app.run()
