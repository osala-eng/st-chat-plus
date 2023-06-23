# st-chat-plus

Streamlit Component, for a Chat-bot UI, [example app](https://share.streamlit.io/osala-eng/st-chat-plus/main/examples/chatbot.py)


## Installation

Install `streamlit-chat-plus` with pip
```bash
pip install streamlit-chat-plus 
```

usage, import the `message` function from `streamlit_chat_plus`
```py
import streamlit as st
from streamlit_chat_plus import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right

### To use markdown in the message
message("Hello bot!", is_user=True, allow_html=True) 
"""
This Enables markdown in the message and allows you to use html tags
By default this will open links in a new tab, to disable this set `open_links_externally` to False
"""
```
   
### Screenshot

![sample-page](https://github.com/osala-eng/st-chat-plus/assets/64925863/b61c75e9-1a3a-4388-9bf2-0bc534c8fb17)


authors - [@osala-eng](https://github.com/osala-eng) [@yashppawar](https://github.com/yashppawar)  [@YashVardhan-AI](https://github.com/yashvardhan-ai)  