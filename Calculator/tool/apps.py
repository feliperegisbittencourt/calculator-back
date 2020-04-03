from django.apps import AppConfig
from corsheaders import CORS

application= Django(__name__)
app = application
cors = CORS(app, resources={r"/report/":{"origins":"*"}})
os.environ["NLS_LANG"] = ".UTF8"

class ToolConfig(AppConfig):
    name = 'tool'
