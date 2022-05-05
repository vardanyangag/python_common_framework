class Config:
    def __init__(self, env, api, browser):
        self.base_url = {
            'qa': 'https://letskodeit.teachable.com/',
            'windows': 'WINDOWS MACHINE IP'
        }[env]

        self.admin_port = {
            'qa': '',
            'windows': '9999'
        }[env]

        self.api_url = {
            'api_env': 'SOME URI FOR API',
        }[api]

        self.browser = {
            'api': 'api',
            'chrome': 'chrome',
            'firefox': 'firefox',
            'ie': 'ie',
            'notepad': 'notepad'
        }[browser]