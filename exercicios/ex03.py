a = str( input('Digite alguma coisa: '))
print('Primitivo:    ', type(a),
      '\nExiste espaços :    |', a.isspace(),
      '\nÉ um numero?:       |', a.isnumeric(),
      '\nÉ alfa bético:      |', a.isalpha(),      
      '\nÉ alfa numerico:    |', a.isalnum(),      
      '\nÉ decimal:          |', a.isdecimal(),
      '\nEsta em maiusculas: |', a.isupper(),
      '\nEsta em minúscula:  |', a.islower() ,
      '\nEsta capitalizado:  |', a.istitle())
