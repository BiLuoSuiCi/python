
#直接用kv代码预先定义控件(如按钮)的行为有时不能满足我们的需求，于是我们可能需要临时改变按钮的行为：
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from time import gmtime, strftime # this equls cv codes #...

Builder.load_string("""
#:import gmtime time.gmtime
#:import strftime time.strftime

<RootWidget>
    BoxLayout:
        orientation: 'vertical'
        Button:
            id: change_itself
            text: 'I can change myself'
            on_release: root.ids['change_itself'].text = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        Button:
            id: change_all
            text: 'I can change our behavior'
            on_release: root.change_all()
""")

class RootWidget(Screen):
    def change_all(self):
        print(self.ids)
        for instance_class in self.ids.values():
            print(instance_class)
            instance_class.text = 'Exit'
            instance_class.bind(on_release=exit)
    def d_y(self):
        print('22222')

class TestApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    TestApp().run()



#作者：yingshaoxo
#链接：https://www.jianshu.com/p/f95576c03f5b
#來源：简书
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。