Full_name = input('What is your name? ')
age = input('What is your age? ')
# int(age)
D_O_B = input('What is your birth date? ')
# int(D_O_B)
P_O_B = input('Where/Which is your birth place? ')
Gender = input('What is your gender? ')
Fathers_name = input("What is your father's name? ")
Mothers_name = input("What is your mother's name? ")
Siblings = input('How many siblings do you have? ')
try:
    int(Siblings)
except Exception:
    print('please enter numerical value')
    Siblings = input('How many siblings do you have? ')
    int(Siblings)
# do some stuff
# Flat_no = input('What is your flat no.? ')
# int(Flat_no)
# Floor_no = input('What is your floor no.? ')
# int(Floor_no)
# Bldg_or_Apt_name = input('What is your building or apartment name? ')
# LM = input('What is landmark for your address? ')
# Road = input('What is your nearest road? ')
# Area = input('What is your Area? ')
# City = input('What is your city name? ')
Pin_code = input('What is your area pincode? ')
int(Pin_code)
State = input('What is your state name? ')
# Address = (Flat_no + ', ' + Floor_no + 'th floor ' + ', ' + Bldg_or_Apt_name + ', ' + LM + ', ' + Road + ', ' + Area + ', ' + City + '-' + Pin_code + ', ' + State + '.')
coma = ','
th = 'th floor'
dash = '-'
dot = '.'
# Address = f'{Flat_no}{coma} {Floor_no}{th}{coma} {Bldg_or_Apt_name}{coma} {LM}{coma} {Road}{coma} {Area}{coma} {City}{dash}{Pin_code}{coma} {State}{dot}'
Address = input('What is your address? ')
Email_Id = input('What is your email address? ')
Phone_No = input('What is your phone number? ')
int(Phone_No)
print('Full_name' + '     : ' + Full_name.upper())
print('age' + '           : ' + age + ' years')
print('D_O_B' + '         : ' + D_O_B)
print('P_O_B' + '         : ' + P_O_B)
print('Gender' + '        : ' + Gender)
print('Fathers_name' + '  : ' + Fathers_name)
print('Mothers_name' + '  : ' + Mothers_name)
print('Siblings' + '      : ' + Siblings)
print('Address' + '       : ' + Address)
print('Email_Id' + '      : ' + Email_Id)
print('Phone_No' + '      : ' + Phone_No)

def getNumericalValue():
    try:
        int(Siblings)
    except Exception:
        print('please enter numerical value')
        Siblings = input('How many siblings do you have? ')
        int(Siblings)
