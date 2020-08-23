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
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.list import MDList, ThreeLineListItem

import calendar
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
    def get_data(self, text1,text2,text3,text4):
        print(text1,text2,text3,text4)
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        more_button = MDFlatButton(text="More")

        self.dialog = MDDialog(text='Predicted Grade:', title="Grade Prediction",
            size_hint=(.75, 1),
            buttons=[close_button, more_button])
        self.dialog.open()

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
            #if

    def change_tip(self):
        self.root.ids.eduTips.text = self.rand_tips()

    def change_size(self,emotion):
        self.root.ids.emotion.user_font_size = "64sp"

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
    def show_date_picker(self):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=2020,
            month=8,
            day=22,
        )

        date_dialog.open()

    def monthValue(self,monthss):
        if (monthss == 1 or monthss == 3 or monthss == 5 or monthss == 7 or monthss == 8 or monthss == 10 or monthss == 12):
            return 31
        elif (monthss == 4 or monthss == 6 or monthss == 9 or monthss == 11):
            return 30
        else:
            return 29
    def checkDate(self,days,months,years):
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
    def addListItem(self,list,item1,item2,item3):
        dates = ThreeLineListItem(text=item1, secondary_text = item2, tertiary_text= item3)
        list.add_widget(dates)
    def removeListItem(self,list):
        for dates in list.children:
            list.remove_widget(dates)




EduApp().run()