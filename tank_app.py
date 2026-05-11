import webview
import os
import sys

def get_html_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'index.html')
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

if __name__ == '__main__':
    html_path = get_html_path()
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    webview.create_window('坦克大战', html=html, width=800, height=860,
                          resizable=False, fullscreen=False, confirm_close=True)
    webview.start()
