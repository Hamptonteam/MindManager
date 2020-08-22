

navigation_helper = """
<ContentNavigationDrawer>:
    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Stress Tabs'
                halign: 'center'
                font_style: 'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: 'Predict your next test score and find out ways to deal with stress or how to study'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
                halign: 'center'
            MDList:
                OneLineListItem:
                    text: "Welcome!"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "home"

                OneLineListItem:
                    text: "Grade Predictor"
                    icon: 'magnify'
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "grade"
                OneLineListItem:
                    text: "Stress Tips"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "stress"
            ScrollView:

Screen:    

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: 'EduAssistance'
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager


            Screen:
                name: 'home'

                MDLabel:
                    text: "Edu Assistant"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.80}
                    font_style: 'H4'
                    size_hint: (1,1)
                MDLabel:
                    text: "In this app, you can schedule upcoming tests, learn how to deal with stress and prepare for upcoming tests, and even predict the score of your next test!"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.50}
                    font_style: 'H6'
                    size_hint: (.8,1)

            Screen:
                name: 'grade'

                MDLabel:
                    text: "Grade Predictor"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.80}
                    font_style: 'H4'
                MDLabel:
                    text: "Feeling stressed for the next test? Use this calculator to predict what your score will be based on previous test scores, failures, and study time!"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.65}
                    font_style: 'Caption'
                    size_hint_x: None
                    width:250
                MDLabel:
                    text: "Past Grade 1 (%)"
                    halign: "center"
                    pos_hint: {"center_x":0.35, "center_y":0.5}
                    font_style: 'H5'
                MDTextField:
                    id: TF1
                    pos_hint: {"center_x":0.85, "center_y":0.5}
                    size_hint_x: None
                    width:50
                MDLabel:
                    text: "Past Grade 2 (%)"
                    halign: "center"
                    pos_hint: {"center_x":0.35, "center_y":0.4}
                    font_style: 'H5'
                MDTextField:
                    id: TF2
                    pos_hint: {"center_x":0.85, "center_y":0.4}
                    size_hint_x: None
                    width:50
                MDLabel:
                    text: "Failures (#)"
                    halign: "center"
                    pos_hint: {"center_x":0.35, "center_y":0.3}
                    font_style: 'H5'
                MDTextField:
                    id: TF3
                    pos_hint: {"center_x":0.85, "center_y":0.3}
                    size_hint_x: None
                    width:50
                MDLabel:
                    text: "Study Time (hr)"
                    halign: "center"
                    pos_hint: {"center_x":0.35, "center_y":0.2}
                    font_style: 'H5'
                MDTextField:
                    id: TF4
                    pos_hint: {"center_x":0.85, "center_y":0.2}
                    size_hint_x: None
                    width:50
                MDRectangleFlatButton:
                    id: calcButton
                    text: "Calculate"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.1}
                    on_press:
                        app.get_data(TF1.text,TF2.text,TF3.text,TF4.text)
                        
                
            Screen:
                name: 'stress'
                MDLabel:
                    id: eduTips
                    text: app.rand_tips()
                    halign: 'center'
                    pos_hint: {"center_x":0.5, "center_y":0.5}
                MDRectangleFlatButton:
                    text: "New Tip!"
                    pos_hint: {"center_x":0.5, "center_y":0.25}
                    on_release: app.change_tip()
                        
                        


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
"""
