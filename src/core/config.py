import os
from gitea import Gitea
from ..utils.language_validator import LanguageValidator

class Config:
    GITEA_URL = os.environ.get('GITEA_URL', '')
    OPENAI_BASE_URL = os.environ.get('OPENAI_BASE_URL', '')
    GITEA_TOKEN = os.environ.get('GITEA_TOKEN')
    API_KEY = os.environ.get('API_KEY')
    AI_MODEL = os.environ.get('AI_MODEL', 'Qwen/Qwen2.5-Coder-32B-Instruct-AWQ')
    
    _raw_language: str = os.environ.get('HUMAN_LANGUAGE', 'zh')
    HUMAN_LANGUAGE = LanguageValidator.validate_language(_raw_language)
    
    @classmethod
    def initialize_clients(cls):
        gitea_client = Gitea(cls.GITEA_URL, cls.GITEA_TOKEN)
        return gitea_client
