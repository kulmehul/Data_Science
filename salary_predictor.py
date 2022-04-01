import joblib

model = joblib.load("salary_model.pk1")

print("enter ur exp : " , end='')
exp =  input() 

p = model.predict([[ exp ]])
print(p)

