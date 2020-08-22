from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from navigation import navigation_helper
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import random
import pickle
import sklearn
Window.size = (300, 500)


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass

class EduApp(MDApp):

    def build(self):
        MainScreen = Screen()
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.secondary_palette = "Black"
        screen = Builder.load_string(navigation_helper)
        #MainScreen.add_widget(screen)
        return screen

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def get_data(self, grade_1, grade_2, failures, studytime):
        if self.check_data(grade_1, grade_2, failures, studytime):
            test_data = self.pre_process(grade_1, grade_2, failures, studytime)
            reg = pickle.load(open("reg_algo.pickle", "rb"))
            prediction = reg.predict[test_data]
            prediction *= 100
            prediction = str(prediction)
            prediction = prediction[:5] + "%"

            close_button = MDFlatButton(text="Close", on_release=self.close_dialog)

            self.dialog = MDDialog(text=prediction, title="Your Test Prediction:",
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
        if studytime <= 4:
            studytime = -studytime
        else:
            studytime = -4
        return [grade_1, grade_2, failures, studytime]


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
                   "Get some sleep!", "Try Relaxation Techniques",
                   "Talk to someone!", "Take Control!",
                   "Create a fresh start - Clean your room",
                   "Rest!", "Keep a positive attitude!", "Try some yoga!",
                   "Be the assertive person I know you are!", "If you smoke, stop.",
                   "Take responsibility", "Hug a loved one ;)",
                   "Write down a goal."]
           n = random.randrange(0,len(tips))
           return tips[n]
        #def checkForNumbers(self,a,b,c,d):
            #for i in range 3:
                #if a
    def change_tip(self):
        self.root.ids.eduTips.text = self.rand_tips()



EduApp().run()