users = {
    'roshaniya' : {
        'first' : 'roshan',
        'last'  : 'chaurasia',
        'location' : 'nallasopara'
    },
    'shivaay005' : {
        'first' : 'satyam',
        'last'  : 'tiwari',
        'location' : 'andheri'
    },
    'hemant007' : {
        'first' : 'hemant',
        'last'  : 'yadav',
        'location' : 'bandra'
    }
}

for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\n User name : {username}")
    print(f"\t Full name : {full_name.title()}")
    print(f"\t Location : {location.title()}")