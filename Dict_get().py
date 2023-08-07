favorite_language = {
    'roshan' : 'python',
    'satyam' : 'java',
    'arun' : 'javascript',
    'prince' : 'C'
}
fav_language = favorite_language.get('navin','No key value present in dictionary')      # Using get() to avoid error
print(fav_language,"\n")

#print(favorite_language['navin'])                                                       # give key error:'navin'
