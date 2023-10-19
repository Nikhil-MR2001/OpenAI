import openai

openai.api_key = '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'


def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        message = [{
            'role': 'user',
            'content': prompt
            }]
    )


    return response.choices[0].message.content.strip()


if __name__ == '__main__':
    while True:
        user_input = input("You : ")
        if user_input.lower() in ['quit', 'exit']:
            break

        response = chat_with_openai(user_input)
        print("Bot : ", response)

