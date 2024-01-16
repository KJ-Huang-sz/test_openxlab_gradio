import gradio as gr

# 输入name字符串，输出Hello {name}!字符串
def greet(name):
    return "Hello " + name + "!"
import time
import gradio as gr

def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "You typed: " + message[: i+1]

gr.ChatInterface(slow_echo).launch()
demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
    outputs="text",
    allow_flagging="never",
)
if __name__ == "__main__":
    demo.launch()
