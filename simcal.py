from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import BoxLayout


class SimpleCalculator(MDApp):
    def build(self):
        Window.size=(350,180)
        screen = MDScreen()
        layout = BoxLayout(orientation="vertical")
        self.b_9=MDRaisedButton(text="9",on_press=self.insert_text)
        self.b_8=MDRaisedButton(text="8",on_press=self.insert_text)
        self.b_7=MDRaisedButton(text="7",on_press=self.insert_text)
        self.b_6=MDRaisedButton(text="6",on_press=self.insert_text)
        self.b_5=MDRaisedButton(text="5",on_press=self.insert_text)
        self.b_4=MDRaisedButton(text="4",on_press=self.insert_text)
        self.b_3=MDRaisedButton(text="3",on_press=self.insert_text)
        self.b_2=MDRaisedButton(text="2",on_press=self.insert_text)
        self.b_1=MDRaisedButton(text="1",on_press=self.insert_text)
        self.b_zero=MDRaisedButton(text="0",on_press=self.insert_text)
        self.b_equals=MDRaisedButton(text="=",on_press=self.equals)
        self.b_CLR=MDRaisedButton(text="CLR",on_press=self.clear_text)
        self.b_plus=MDRaisedButton(text="+",on_press=self.addition)
        self.b_minus=MDRaisedButton(text="-",on_press=self.sub)
        self.b_mul=MDRaisedButton(text="*",on_press=self.mul)
        self.b_Div=MDRaisedButton(text="/",on_press=self.div)
        self.text_field = MDTextFieldRect(text="",size_hint=(1, None),height="30dp",pos_hint={'centr_x':0,'center_y':0.96})
        gl = GridLayout(cols=4)
        layout.add_widget(self.text_field)

        lis=[self.b_9,self.b_8,self.b_7,self.b_plus,self.b_6,self.b_5,self.b_4,self.b_minus,self.b_3,self.b_2,self.b_1,self.b_mul,self.b_CLR,self.b_zero,self.b_equals,self.b_Div]
        for k in lis:
            gl.add_widget(k)
        
        
        layout.add_widget(gl)
        return layout

    def insert_text(self,obj):
        self.text_field.text=self.text_field.text + obj.text
    
    def clear_text(self,obj):
        self.text_field.text=""
    
    def addition(self,obj):
        self.operand1 = float(self.text_field.text)
        self.text_field.text=""
        self.oprator='+'

    def div(self,obj):
        self.operand1 = float(self.text_field.text)
        self.text_field.text=""
        self.oprator='/'

    def sub(self,obj):
        if self.text_field.text!="":
            self.operand1 = float(self.text_field.text)
            self.text_field.text=""
            self.oprator='-'
        else:
            self.text_field.text="-"

    def mul(self,obj):
        self.operand1 = float(self.text_field.text)
        self.text_field.text=""
        self.oprator='*'
    
    def equals(self,obj):
        self.operand2 = float(self.text_field.text)
        if self.oprator=='+':
            self.text_field.text=str(self.operand1+self.operand2)
        elif self.oprator=='-':
            self.text_field.text=str(self.operand1-self.operand2)
        elif self.oprator=='*':
            self.text_field.text=str(self.operand1*self.operand2)
        else:
            if self.operand2!=0: 
                self.text_field.text=str(self.operand1/self.operand2)
            else:
                self.text_field.text="ZeorDivisionError(CLR to continue)"
                    
    
SimpleCalculator().run()