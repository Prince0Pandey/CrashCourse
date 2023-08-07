def make_shirt(size,message):
    prompt = f"The size of the shirt: {size}\n"
    prompt += f"Message written on shirt: {message}\n"
    print(prompt)
make_shirt('small','do what you do!')
make_shirt(size='large',message='workhard')