from src.pass_gen import password_generator

if __name__ == "__main__":
    min_length = int(input("Enter the minimum length: "))
    number = input("Do you want to have number (y/n)? ").lower() =='y' 
    special_character = input("Do you want to have special character (y/n)? ").lower() =='y' 
    my_pass = password_generator(min_length = min_length, number = number, special_character = special_character)
    print(my_pass)
