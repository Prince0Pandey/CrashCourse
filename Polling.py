favorite_language = {
    'roshan' : 'python',
    'satyam' : 'java',
    'arun' : 'javascript',
    'prince' : 'C'
}
poll = ['roshan','hemant','satyam','shubham','prince','arti']

for name in poll:
    if name in favorite_language.keys():
        print(f"{name.title()} Thank you for taking poll.")
    else:
        print(f"{name.title()} You should take a poll.")