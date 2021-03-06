import os
def load_config():
    if (os.environ.get('MODE')):
        mode = os.environ.get('MODE')
    else:
        # change here to switch environments locally.
        mode = 'development'
    try:
        if mode == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'TESTING':
            from .testing import TestingConfig
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .development import DevelopmentConfig
        return DevelopmentConfig