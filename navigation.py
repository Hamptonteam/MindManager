

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
                    text: "Home Page"
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "home"

                OneLineListItem:
                    text: "Grade Predictor"
                    icon: 'magnify'
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "grade"
                OneLineListItem:
                    text: "Stress Tips"
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "stress"
                OneLineListItem:
                    text: "Calendar"
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "cal"
                
            ScrollView:

Screen:    
    

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: 'EduAssistance'
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        MDIconButton:
            icon: "cogs"
            pos_hint: {"center_x":0.8, "center_y":0.5}
            theme_text_color: "Custom"
            text_color: .8, .8, .8, 1
            on_release:
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_date_picker()
                

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager


            Screen:
                name: 'home'

                MDLabel:
                    text: "Welcome!"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.80}
                    font_style: 'H4'
                    size_hint: (1,1)
                MDLabel:
                    id: feelButton
                    text: "How are you feeling?"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.60}
                    font_style: 'H6'
                    size_hint: (1,1)
                    
                MDIconButton:
                    id: neutral
                    icon: "emoticon-neutral"
                    pos_hint:{"center_x":0.5, "center_y":0.40}
                    theme_text_color: "Custom"
                    text_color: .8, .8, 0, 1
                    user_font_size: "52sp"
                    on_release:
                        feelButton.text = "Well I hope that turns green!"
                        neutral.user_font_size = "64sp"
                    on_release:
                        neutral.user_font_size = "52sp"
                        happy.opacity=0
                        sad.opacity=0
                        sad.disabled = True
                        happy.disabled = True
                MDIconButton:
                    id: happy
                    icon: "emoticon-happy"
                    pos_hint:{"center_x":0.25, "center_y":0.40}
                    theme_text_color: "Custom"
                    text_color: 0, .8, 0, 1
                    user_font_size: "52sp"
                    on_release:
                        feelButton.text = "That's great to hear!"
                        happy.user_font_size = "64sp"
                    on_release:
                        happy.user_font_size = "52sp"
                        sad.opacity=0
                        neutral.opacity=0
                        sad.disabled = True
                        neutral.disabled = True
                        
                MDIconButton:
                    id: sad
                    icon: "emoticon-sad"
                    pos_hint:{"center_x":0.75, "center_y":0.40}
                    theme_text_color: "Custom"
                    text_color: .8, 0, 0, 1
                    user_font_size: "52sp"
                    on_release:
                        feelButton.text = "I'm sorry to hear that."
                        sad.user_font_size = "64sp"
                    on_release:
                        sad.user_font_size = "52sp"
                        happy.opacity=0
                        neutral.opacity=0
                        neutral.disabled = True
                        happy.disabled = True
                    
                        

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
            
            Screen:
                name: 'cal'
                
                ScrollView:
                    BoxLayout:
                        MDList:
                            id: myList
                            pos_hint: {"center_x":0.5, "center_y":.5}
                            ScrollView:
                
                MDLabel:
                    text: "Calendar"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.80}
                    font_style: 'H4'
                    size_hint: (1,1)
                MDLabel:
                    text: "Set Date of Next Test"
                    pos_hint: {"center_x":.5, "center_y":0.25}
                    halign: 'center'
                    font_style: 'H6'
                MDTextField:
                    text: "DD"
                    id: userMonth
                    pos_hint: {"center_x":0.3, "center_y":0.20}
                    size_hint_x: None
                    width:40
                MDLabel:
                    text: "/"
                    pos_hint: {"center_x":.9, "center_y":0.20}
                    
                MDTextField:
                    text: "MM"
                    id: userDay
                    pos_hint: {"center_x":0.5, "center_y":0.20}
                    size_hint_x: None
                    width:40
                MDLabel:
                    text: "/"
                    pos_hint: {"center_x":1.1, "center_y":0.20}
                    
                MDTextField:
                    text: "YYYY"
                    id: userYear
                    pos_hint: {"center_x":0.7, "center_y":0.20}
                    size_hint_x: None
                    width:40
                MDTextField:
                    text: "assignment"
                    id: assignment
                    pos_hint: {"center_x":0.5, "center_y":0.30}
                    size_hint_x: None
                    width:120
                
                MDRectangleFlatButton:
                    text: "Set Date"
                    pos_hint: {"center_x":0.5, "center_y":0.10}
                    on_release:
                        app.addListItem(myList,assignment.text, userMonth.text + "/" + userDay.text+ "/" +userYear.text, "hello World")
                        
                        
                        
                
                    
                    
            
            Screen:
                name: 'set'

                MDLabel:
                    text: "Settings"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.80}
                    font_style: 'H4'
                    size_hint: (1,1)
            
                        


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
"""
