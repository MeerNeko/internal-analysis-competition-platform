from pathlib import Path
import streamlit.web.cli as stcli

def streamlit_run():
    # pyinstallerでは絶対パスでの指定が必要
    ex_file = Path.cwd() / 'home.py'
    sys.argv=['streamlit', 'run', ex_file, '--global.developmentMode=false', '--server.port=8501']
    sys.exit(stcli.main())

if __name__ == "__main__":
    streamlit_run()