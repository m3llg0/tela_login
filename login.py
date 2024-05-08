from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen


class TelaLogin(Screen):
    def build(self):
        self.orientation = 'vertical'
        self.padding = [50, 20]
        self.spacing = 10
        
        # Definindo a cor de fundo para preto
        Window.clearcolor = (0, 0, 0, 1)
        
        # Adicionando uma imagem
        self.add_widget(Image(source='/Users/aluno.sesipaulista/Downloads/3736502.png'))
        
        # Adicionando um rótulo
        self.add_widget(Label(text=" .:: L O G I N ::.", font_size=24))
        
        # Adicionando campos de entrada de texto
        
        self.user_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.username_label = Label(text="U S U Á R I O", font_size=18, size_hint=(None, None), size=(450, 50))
        self.username_input = TextInput(hint_text='Digite aqui...', multiline=False, size_hint=(None, None), size=(450, 50))
        self.user_layout.add_widget(self.username_label)
        self.user_layout.add_widget(self.username_input)
        self.add_widget(self.user_layout)
        
        self.pass_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.password_label = Label(text="S E N H A", font_size=18, size_hint=(None, None), size=(450, 50))
        self.password_input = TextInput(hint_text='Digite aqui...', multiline=False, size_hint=(None, None), size=(450, 50))
        self.pass_layout.add_widget(self.password_label)
        self.pass_layout.add_widget(self.password_input)
        self.add_widget(self.pass_layout)
        
        # Adicionando botões de login e cadastro
        self.buttons = BoxLayout(padding=[0, 10], spacing=10)
        self.entrar = Button(text='E n t r a r', color=(0, 0, 0, 1), size_hint=(None, None), size=(450, 50), background_color=(100, 100, 100, 100))
        self.cadastrar = Button(text='C a d a s t r e - s e', color=(0, 0, 0, 1), size_hint=(None,None), size=(450, 50), background_color=(100, 100, 100, 100))
        self.buttons.add_widget(self.entrar)
        #self.buttons.add_widget(self.abrir_tela_cadastro)
        self.add_widget(self.buttons)
        self.cadastrar.bind(on_press=self.abrir_tela_cadastro)
        self.add_widget(self.cadastrar)
        
    
        return self
    
+ 


class TelaCadastro(App):        
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=[50, 20], spacing=10)
        
        # Definindo a cor de fundo para preto
        Window.clearcolor = (0, 0, 0, 1)
        
        # Adicionando um rótulo
        self.root.add_widget(Label(text=" .:: C A D A S T R O ::.", font_size=24))
        
        # Adicionando campos de entrada de texto
        
        # Nome
        self.name_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.name_label = Label(text="N O M E", font_size=18, size_hint=(None, None), size=(450, 50))
        self.name_input = TextInput(hint_text='Digite aqui...', multiline=False, size_hint=(None, None), size=(450, 50))
        self.name_layout.add_widget(self.name_label)
        self.name_layout.add_widget(self.name_input)
        self.root.add_widget(self.name_layout)
        
        # Email
        self.email_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.email_label = Label(text="E M A I L", font_size=18, size_hint=(None, None), size=(450, 50))
        self.email_input = TextInput(hint_text='Digite aqui...', multiline=False, size_hint=(None, None), size=(450, 50))
        self.email_layout.add_widget(self.email_label)
        self.email_layout.add_widget(self.email_input)
        self.root.add_widget(self.email_layout)
        
        # Celular
        self.cll_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.cll_label = Label(text="C E L U L A R", font_size=18, size_hint=(None, None), size=(450, 50))
        self.cll_input = TextInput(hint_text='Digite aqui...', multiline=False, size_hint=(None, None), size=(450, 50))
        self.cll_layout.add_widget(self.cll_label)
        self.cll_layout.add_widget(self.cll_input)
        self.root.add_widget(self.cll_layout)
        
        # Senha
        self.pass_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.password_label = Label(text="S E N H A", font_size=18, size_hint=(None, None), size=(450, 50))
        self.password_input = TextInput(hint_text='Digite aqui...', multiline=False, size_hint=(None, None), size=(450, 50))
        self.pass_layout.add_widget(self.password_label)
        self.pass_layout.add_widget(self.password_input)
        self.root.add_widget(self.pass_layout)
        
        # Adicionando botão de cadastro
        self.cadastrar = Button(text='C a d a s t r e - s e', color=(0, 0, 0, 1), size_hint=(None,None), size=(450, 50), background_color=(100, 100, 100, 100))
        self.cadastrar.bind(on_press=self.abrir_tela_login)
        self.root.add_widget(self.cadastrar)
        
        return self.root
        
    def abrir_tela_login(self, instance):
        self.root.clear_widgets()  # Limpa os widgets atuais
        tela_login = TelaLogin()  # Cria uma nova instância da tela de login
        self.root.add_widget(tela_login)  # Adiciona a nova tela à raiz

if __name__ == '__main__':
    TelaLogin().run()
