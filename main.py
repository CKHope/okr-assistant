import google.generativeai as genai
from time import sleep
import streamlit as st
from config import *

st.title("🤖Generative AI OKR helper")
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyDejiC_S0NiWQWy6aqPBVuXaCBJ56ktWmw'
genai.configure(api_key=GOOGLE_API_KEY)    

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
# chat

#! display option to help with Objectives or Key result
st.warning("🪶Premium assistant: Hi boss, I am your Premium assistant! I can help you to give hints about your OKR ideas (both Objective and Key result). Which do you want me to help, boss?")
option = st.selectbox(
   "",
   ("OKR-Objectives", "OKR-Key results"),
   index=None,
   placeholder="please select one, boss...",
)

userinput=st.chat_input("Please input what you want to achieve with your OKR here, boss...")

if option:
    st.warning(f'🪶Premium assistant: Hi boss, you ordered me to help with: {option}. Roger!~~~')
    st.warning(f'🪶Premium assistant: Please input in the box at the bottom, boss...')
if userinput:
    st.warning(f'🪶Premium assistant: Hi boss, you asked me to give some hints on the objective: "{userinput}"')
    all_flows={
    "OKR-Objectives":OKR_O_helper(userinput),
    "OKR-Key results":OKR_KR_helper(userinput)
    }

    active_flow=all_flows[option]
    
    for index,message in enumerate(active_flow):
        with st.spinner(f'🪶Premium assistant:🚀🚀🚀 Generating hint no# {index+1} at max speed...'):
            response = chat.send_message(message,stream=True)
        
        with st.chat_message(name="Premium assitant",avatar= '🪶'):
            if response:
                st.success(f'hint no# {index+1}')
                message_placeholder = st.empty()
                full_response = ''
                assistant_response = response
                        # Streams in a chunk at a time
                for chunk in response:
                    # Simulate stream of chunk
                    # TODO: Chunk missing `text` if API stops mid-stream ("safety"?)
                    for ch in chunk.text.split(' '):
                        full_response += ch + ' '
                        sleep(0.05)
                        # Rewrites with a cursor at end
                        message_placeholder.write(full_response + '🪶')
                # Write full message with placeholder
                #TODO: keep history
                message_placeholder.write(full_response)

# st.write(chat.history)
#TODO: add OKR helper on Lark database with gemini
