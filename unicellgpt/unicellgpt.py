import re
import openai

def msg():
    print(
    """感谢使用单元格ChatGPT外接机器人
    指令前缀：
    
    -c 输入开始对话
    -rs 重置对话上下文文本
    -e 退出
------------------------------"""
    )

def errormsg():
    print(
    """似乎这个命令没有前缀无法被识别呢，请参考下方的指令前缀：
    
    -c 输入开始对话
    -rs 重置对话上下文文本
    -e 退出
------------------------------"""
    )

def chat():
    global messages
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("我说：")
        if user_input.startswith("-c "):
            prompt = user_input[3:]
            c(prompt)
        elif user_input == "-rs":
            rs()
        elif user_input == "-e":
            # 清除API密钥
            openai.api_key = None
            break
        else:
            errormsg()

def c(prompt):
    openai.api_key = api_key

    global messages
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = messages + [{"role": "user", "content": prompt}]
    )
    messages = messages + [{"role": "assistant", "content": response.choices[0].message.content}]

    print("GPT小珞：" + response.choices[0].message.content)
    print("------------------------------")

def rs():
    global messages
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

def get_api_key():
    while True:
        api_key = input("请输入API密钥：")
        if not re.match(r"^[A-Za-z0-9\-]+$", api_key):
            print("API密钥只能由数字和英文字母组成，请重新输入！")
            print("------------------------------")
        else:
            openai.api_key = api_key
            try:
                openai.Completion.create(
                  engine="text-davinci-002",
                  prompt="Hello",
                  temperature=0.5,
                  max_tokens=1
                )
                print("API密钥输入正确！")
                print("------------------------------")
                return api_key
            except openai.error.AuthenticationError:
                print("API密钥错误，请重新输入！")
                print("------------------------------")

def start():
    api_key = get_api_key()
    msg()
    chat()

if __name__ == '__main__':
    start()
