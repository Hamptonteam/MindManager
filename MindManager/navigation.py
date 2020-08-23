navigation_helper = """

<ContentNavigationDrawer>:
    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            
           #put in picture or something
            
            MDLabel:
                text: "MindManager"
                halign: 'left'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: 'Assisting you and your mind in your academic career.'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
                halign: 'left'
            
          
            MDList:
                TwoLineListItem:
                    text: "Home"
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "home"

                TwoLineListItem:
                    text: "Grade Predictor"
                    icon_right: 'magnify'
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "grade"

                TwoLineListItem:
                    text: "Studytime Calculator"
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "studytime_calc"                        
                        

                TwoLineListItem:
                    text: "Assignment Planner"
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "assignment_planner"
            
            ScrollView:

Screen:    

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: 'MindManager'
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [('cogs', lambda x: setattr(app.root.ids.screen_manager, 'current', 'settings'))]
        

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager


            Screen:
                name: 'home'
            
                MDLabel:
                    id: welcome_text
                    text: "Welcome!"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.80}
                    font_style: 'H4'
                    size_hint: (1,1)
                    
                
                        
            
                MDLabel:
                    id: eduTips
                    text: app.rand_tips()
                    halign: 'center'
                    pos_hint: {"center_x":0.5, "center_y":0.5}
                    opacity: 0
                    disabled: True
                MDRectangleFlatButton:
                    id: tip_btn
                    text: "New Tip!"
                    pos_hint: {"center_x":0.5, "center_y":0.25}
                    on_release: app.change_tip()
                    disabled: True
                    opacity: 0
                        
                MDLabel:
                    id: feelButton
                    text: "How are you feeling?"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.60}
                    font_style: 'H6'
                    size_hint: (1,1)
                  
                  
                MDIconButton:
                    id: sad
                    icon: "emoticon-sad"
                    pos_hint:{"center_x":0.75, "center_y":0.40}
                    theme_text_color: "Custom"
                    text_color: .8, 0, 0, 1
                    user_font_size: "52sp"
                    on_press:
                        #feelButton.text = "I'm sorry to hear that."
                        sad.user_font_size = "64sp"
                    on_release:
                        sad.user_font_size = "52sp"
                        happy.opacity=0
                        neutral.opacity=0
                        sad.opacity=0
                        feelButton.opacity = 0
                        sad.disabled = True
                        happy.disabled = True
                        neutral.disabled = True
                        app.send_happieness(-1)
                
                
                
                MDIconButton:
                    id: happy
                    icon: "emoticon-happy"
                    pos_hint:{"center_x":0.25, "center_y":0.40}
                    theme_text_color: "Custom"
                    text_color: 0, .8, 0, 1
                    user_font_size: "52sp"
                    
                    on_press:
                        #feelButton.text = "That's great to hear!"
                        happy.user_font_size = "64sp"
                    on_release:
                        happy.user_font_size = "52sp"
                        happy.opacity=0
                        neutral.opacity=0
                        sad.opacity=0
                        feelButton.opacity = 0
                        sad.disabled = True
                        happy.disabled = True
                        neutral.disabled = True
                        app.send_happieness(1)
                
                 
                MDIconButton:
                    id: neutral
                    icon: "emoticon-neutral"
                    pos_hint:{"center_x":0.5, "center_y":0.40}
                    theme_text_color: "Custom"
                    text_color: .8, .8, 0, 1
                    user_font_size: "52sp"
                    
                    on_press:
                        #feelButton.text = "Well I hope that turns green!"
                        neutral.user_font_size = "64sp"
                        
                    on_release:
                        neutral.user_font_size = "52sp"
                        happy.opacity=0
                        neutral.opacity=0
                        sad.opacity=0
                        feelButton.opacity = 0
                        sad.disabled = True
                        happy.disabled = True
                        neutral.disabled = True
                        app.send_happieness(0)
                

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
                name: "assignment_planner"

                MDLabel:
                    text: "Upcoming Deadlines"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.80}
                    font_style: 'H6'
                    size_hint: (1,1)
                
                MDTextField:
                    hint_text: "MM"
                    required: True
                    id: userMonth
                    pos_hint: {"center_x":0.3, "center_y":0.20}
                    size_hint_x: None
                    width:40
                MDLabel:
                    text: "/"
                    pos_hint: {"center_x":.9, "center_y":0.20}
                    
                MDTextField:
                    hint_text: "DD"
                    required: True
                    id: userDay
                    pos_hint: {"center_x":0.5, "center_y":0.20}
                    size_hint_x: None
                    width:40
                MDLabel:
                    text: "/"
                    pos_hint: {"center_x":1.1, "center_y":0.20}
                    
                MDTextField:
                    hint_text: "YYYY"
                    required: True
                    id: userYear
                    pos_hint: {"center_x":0.7, "center_y":0.20}
                    size_hint_x: None
                    width:40
                MDTextField:
                    hint_text: "Assignment"
                    required: True
                    id: assignment
                    pos_hint: {"center_x":0.5, "center_y":0.30}
                    size_hint_x: None
                    width:120
                
                MDRectangleFlatButton:
                    text: "Set Date"
                    pos_hint: {"center_x":0.5, "center_y":0.10}
                    on_release:
                        app.addListItem(myList,assignment.text, userMonth.text + "/" + userDay.text+ "/" +userYear.text)
                ScrollView:

                    pos_hint: {"center_x":0.5, "center_y":0.55}
                    size_hint: (1, .4)
                    max: 3
                
                    MDList:
                        id: myList
                        pos_hint: {"center_x":0.5, "center_y":0.4}            
            
            
            Screen:
                name: "settings"
                MDLabel:
                    text: "Settings"
                    text_color: app.theme_cls.primary_palette
                    pos_hint: {"center_x":0.165, "center_y":0.8}
                    halign: "center"
                    font_style: "H5"
                
                MDTextFieldRound:
                    id: enter_name
                    hint_text: "Enter Name"
                    helper_text: "Enter your name"
                    helper_text_mode: "on_focus"
                    required: True
                    icon_left: "account-arrow-right"
                    pos_hint: {"center_x":0.51, "center_y":0.7}
                    max_text_length: 10
                    on_focus:
                        app.get_name(enter_name.text)
            
                
                MDTextFieldRound:
                    id: enter_email
                    hint_text: "Personal Email"
                    helper_text: "example@domain.com"
                    icon_left: "email"
                    helper_text_mode: "on_focus"
                    required: True
                    pos_hint: {"center_x":0.51, "center_y":0.6}
                
                MDTextFieldRound:
                    id: friend_email
                    hint_text: "Friends Email"
                    helper_text: "example@domain.com"
                    icon_left: "email"
                    helper_text_mode: "on_focus"
                    required: True
                    pos_hint: {"center_x":0.51, "center_y":0.5}
                    
                MDRectangleFlatButton:
                    text: "Change Theme"
                    on_release: app.show_theme_picker()
                    pos_hint: {"center_x":0.5, "center_y":0.4}
                    
                MDRectangleFlatButton:
                    text: "Change Date"
                    on_release: app.show_date_picker1()
                    pos_hint: {"center_x":0.5, "center_y":0.3}
                    
            Screen:
                name: "studytime_calc"
                MDLabel:
                    text: "Study-time Calculator"
                    text_color: app.theme_cls.primary_palette
                    pos_hint: {"center_x":0.5, "center_y":0.8}
                    halign: "center"
                    font_style: "H5"

                MDLabel:
                    text: "Calculate your optimal study-time, for effecient time management."
                    pos_hint: {"center_x":0.5, "center_y":0.7}
                    height: self.texture_size[1]
                    halign: 'center'

                MDTextField:
                    id: level
                    pos_hint: {"center_x":0.35, "center_y":0.5}
                    hint_text: "Level: HS/College/Graduates/"
                    size_hint_x: None
                    width:50

                MDTextField:
                    id: course_count
                    pos_hint: {"center_x":0.35, "center_y":0.4}
                    hint_text: "# of classes"
                    size_hint_x: None
                    width:50

                MDTextField:
                    id: desired
                    pos_hint: {"center_x":0.7, "center_y":0.3}
                    hint_text: "Desired Letter Grade "
                    helper_text: "A, B, or C"
                    width:50

                MDRectangleFlatButton:
                    id: studyCalcButton
                    text: "Calculate"
                    halign: "center"
                    pos_hint: {"center_x":0.5, "center_y":0.1}
                    on_press:
                        app.study_time(level.text, course_count.text, desired.text)  
                
            
            
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                

"""
