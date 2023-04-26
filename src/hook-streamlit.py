# For create .exe
from PyInstaller.utils.hooks import copy_metadata
datas = copy_metadata('streamlit')