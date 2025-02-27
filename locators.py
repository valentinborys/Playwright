
class RegistrationLocators:
    ENTRANCE_LOCATOR = 'text=Войти'
    REGISTRATION_LOCATOR = "text=Регистрация"
    LAST_NAME_LOCATOR = "//input[@name='lastName']"
    FIRST_NAME_LOCATOR = "(//input[@class='_vrmZib'])[9]"
    PHONE = "//input[@name='phone']"
    EMAIL = "(//input[@ type='email'])[2]"
    PASSWORD = "(//input[@type='password'])[1]"
    PASSWORD_CONFIRM = "(//input[@type='password'])[2]"
    SUCCESS_BUTTON = "//button[@class='_etcHyp _W7H2r6 _WuoKbT']"
