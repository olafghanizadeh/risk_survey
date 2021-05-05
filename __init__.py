from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'risk_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
        
    risk_1 = models.IntegerField(
        widget=widgets.RadioSelect,
        label=
        "Risco de o montante a receber pelo investidor vir a ser inferior ao capital investido",
        choices=[1,2,3,4,5]
        )
    risk_2 = models.IntegerField(
        widget=widgets.RadioSelect,
        label=
        "Risco de o valor dos ativos, ou dos ativos subjacentes no caso de Produtos Financeiros Complexos, variar e tal ter impacto na rentabilidade do investimento",
        choices=[1,2,3,4,5]
        )





# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['risk_1', 'risk_2']


page_sequence = [Demographics, CognitiveReflectionTest]
