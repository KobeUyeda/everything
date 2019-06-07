import kivy

from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button

from kivy.core.window import Window

from kivy.clock import Clock



class stuff(FloatLayout):

    def __init__(self):

        super().__init__()

        self.t = 0

        Clock.schedule_interval(self.update, .01)

        self.displayOne = Label(text='', halign="left")
        self.displayOne.size_hint = (1, .1)
        self.displayOne.font_size = 40
        self.displayOne.text_size = (Window.width - 30, 0)
        self.displayOne.pos_hint = {'top': .925}
        self.displayOne.halign = ('right')
        self.add_widget(self.displayOne)

        self.display = Label(text='0')
        self.display.size_hint = (1, .1)
        self.display.font_size = 90
        self.display.text_size = (Window.width - 30, 0)
        self.display.halign = ('right')
        self.display.pos_hint = {'top': .725, 'right': 1}
        self.add_widget(self.display)

        self.l = Button(text="(.)", background_color=(.5, .5, .5, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.4943, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': .525, 'right': .497}
        self.l.bind(on_press=self.dec)
        self.add_widget(self.l)

        self.l = Button(text="=", background_color=(.2, .7, 1, 0.94))
        self.l.background_normal = ('')
        self.l.size_hint = (.4943, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': .525, 'right': .9959}
        self.l.bind(on_press=self.equal)
        self.add_widget(self.l)

        self.l = Button(text="9", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.42, 'right': .7471}
        self.l.bind(on_press= lambda x:self.input(self, str(9)))
        self.add_widget(self.l)

        self.l = Button(text="8", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.42, 'right': .497}
        self.l.bind(on_press=lambda x: self.input(self, str(8)))
        self.add_widget(self.l)

        self.l = Button(text="7", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.42, 'right': .2484}
        self.l.bind(on_press=lambda x: self.input(self, str(7)))
        self.add_widget(self.l)

        self.l = Button(text="x", background_color=(.5, .5, .5, .8))
        self.l.background_normal = ('')
        self.l.pos_hint = {'top': 0.42, 'right': .99595}
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.bind(on_press=lambda x: self.add(self, str(' * ')))
        self.add_widget(self.l)

        self.l = Button(text="6", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.315, 'right': .7471}
        self.l.bind(on_press=lambda x: self.input(self, str(6)))
        self.add_widget(self.l)

        self.l = Button(text="5", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.315, 'right': .497}
        self.l.bind(on_press=lambda x: self.input(self, str(5)))
        self.add_widget(self.l)

        self.l = Button(text="4", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.pos_hint = {'top': 0.315, 'right': .2484}
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.bind(on_press=lambda x: self.input(self, str(4)))
        self.add_widget(self.l)

        self.l = Button(text="÷", background_color=(.5, .5, .5, .8))
        self.l.background_normal = ('')
        self.l.pos_hint = {'top': 0.315, 'right': .99595}
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.bind(on_press=lambda x: self.add(self, str(' / ')))
        self.add_widget(self.l)

        self.l = Button(text="3", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.21, 'right': .7471}
        self.l.bind(on_press=lambda x: self.input(self, str(3)))
        self.add_widget(self.l)

        self.l = Button(text="2", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.pos_hint = {'top': 0.21, 'right': .497}
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.bind(on_press=lambda x: self.input(self, str(2)))
        self.add_widget(self.l)

        self.l = Button(text="1", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.pos_hint = {'top': 0.21, 'right': .2484}
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.bind(on_press=lambda x: self.input(self, str(1)))
        self.add_widget(self.l)

        self.l = Button(text="+", background_color=(.5, .5, .5, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.pos_hint = {'top': 0.21, 'right': .99595}
        self.l.font_size = 25
        self.l.bind(on_press=lambda x: self.add(self, str(' + ')))
        self.add_widget(self.l)

        self.l = Button(text="(-)", background_color=(.5, .5, .5, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.105, 'right': .2484}
        self.l.bind(on_press=self.negative)
        self.add_widget(self.l)

        self.l = Button(text="0", background_color=(.3, .3, .3, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.105, 'right': .497}
        self.l.bind(on_press=lambda x: self.input(self, str(0)))
        self.add_widget(self.l)

        self.clear = Button(text="C", background_color=(.5, .5, .5, .8))
        self.clear.background_normal = ('')
        self.clear.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.clear.pos_hint = {'top': 0.105, 'right': .7471}
        self.clear.bind(on_press=self.cle)
        self.add_widget(self.clear)

        self.l = Button(text="-", background_color=(.5, .5, .5, .8))
        self.l.background_normal = ('')
        self.l.size_hint = (.2455, .1)
        self.l.font_size = 25
        self.l.pos_hint = {'top': 0.105, 'right': .99595}
        self.l.bind(on_press=lambda x: self.add(self, str(' - ')))
        self.add_widget(self.l)

    def update(self, f):
        self.display.text_size = (Window.width - 30, 0)
        self.displayOne.text_size = (Window.width - 30, 0)

    def input(self, f, input):
        p = self.displayOne.text
        if p != "":
            try:
                if p[-2] == '=':
                    o = True
                else:
                    o = False
                if o == True:
                    self.displayOne.text = (" ")
                    self.display.text = ("")
            except IndexError:
                d = True
        if self.display.text == '0':
            self.display.text = str(input)
        else:
            p = self.display.text
            self.display.text = (p + str(input))

    def negative(self, f):
        p = self.display.text
        if float(p) > 0:
            self.display.text=('-' + p)

    def add(self, f, input):
        p = self.displayOne.text
        if p != "":
            try:
                if p[-2] == '=':
                    o = True
                else:
                    o = False
                if o == True:
                    self.displayOne.text = (" ")
            except IndexError:
                d = True
        p = self.displayOne.text
        l = self.display.text
        n = len(p)
        self.displayOne.text = (p + l + input)
        self.display.text = (str(0))

    def dec(self, f):
        p = self.display.text
        l = (p + '.')
        try:
            float(l)
            o = True
        except ValueError:
            o = False
        if o == True:
            self.display.text = (p + '.')

    def cle(self, f):
        self.display.text = str(0)
        self.displayOne.text = ""

    def equal(self, f):
        l = self.displayOne.text
        n = self.display.text
        p = self.displayOne.text = (l + n)
        l = self.displayOne.text = (p + ' = ')
        if l[-2] == '=':
            try:
                t = eval(p)
                self.display.text = str(t)
            except ZeroDivisionError:
                self.display.text = str(0)
            except:
                self.display.text = ('Error')
                self.displayOne.text = ""



class Calculator(App):

    def build(self):
        self.icon = "c03428568.jpg"
        Window.clearcolor = (0.2, 0.2, .2, 1)
        return stuff()



if __name__ == "__main__":

    Calculator().run()