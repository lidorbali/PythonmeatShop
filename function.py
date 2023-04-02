import __init__
import product_class


def create_obj():
    """
    creates list of lists
    :return:
    list of objects (products)
    """
    data_list = []
    for i in range(1, len(__init__.pre_list)):
        data_list.append(product_class.Product(__init__.pre_list[i].split(",")))
    return data_list


def update_file(obj_list):
    """
    update the file
    :return:
    updated file
    """
    check_file = open("meat_data.txt", 'w', encoding='utf-8')
    check_file.write(f"סוג בשר,שם המוצר,מצב שימור,מחיר,כמות\n")
    for product in obj_list:
        check_file.write(
            f"{product.get_type()},{product.get_name()},{product.get_condition()},{product.get_price()} ,{product.get_amount()}\n")
    check_file.close()


def add_amount(product, amount, obj_list):
    """
    adds the amount in the product
    :return:
    updated obj_list with new amount
    """
    obj_list[product].add(amount)

    return obj_list[product]


def sub_amount(product, amount, obj_list):
    """
    Reduces the amount from the product
    :return:
    updated obj_list with new amount
    """
    obj_list[product].sub(amount)
    update_file(obj_list)
    return obj_list[product]


def edit_amount(obj_list):
    """
    adds or reduces the amount according the user's choice with help of two other functions
    :return:
    updated obj_list with new amount
    """

    user_choise = int(input(f"""[1]-להוספת כמות 
[2]- להפחתת כמות"""))

    if user_choise == 1:
            show_product(obj_list)
            product_number = int(input(f"מספר המוצר שתרצה להוסיף ממנו "))
            amount = float(input(f"כמה להוסיף?"))
            print(add_amount(product_number, amount, obj_list))
    elif user_choise == 2:
            show_product(obj_list)
            product_number = int(input(f"מספר המוצר שתרצה להחסיר ממנו  "))
            amount = float(input(f"כמה להחסיר?"))
            print (sub_amount(product_number, amount, obj_list))
    else:
         print("ניתן לבחור רק מה מספרים שניתנו")
         edit_amount(obj_list)







def show_product(obj_list):
    """
    Prints the inventory according to the user's choice and show "almost out of stock" warning
    """

    user_choise = int(input(f"""סוג בשר שתרצה לראות? 
    [1]-בקר
    [2]-עוף
    [3]-כבש
    [4]-דגים
    [5]-הכל """))

    if user_choise == 1:
            print(f"בקר\n____")
            for meat in obj_list:
                if meat.get_type() == "בקר":
                    if meat.get_amount() == 0:
                        print(f"[{obj_list.index(meat)}]. {meat} (אזל במלאי !)       ")
                        print()
                    elif meat.get_amount() <= 30:
                        print(f"[{obj_list.index(meat)}]. {meat}(מוצר זה עומד להיגמר!)              ")
                        print()
                    else:
                        print(f"                          [{obj_list.index(meat)}]. {meat}", )
                        print()


    elif user_choise == 2:
            print(f"עוף\n____")
            for chicken in obj_list:
                if chicken.get_type() == "עוף":
                    if chicken.get_amount() == 0:
                        print(f"[{obj_list.index(chicken)}]. {chicken} (אזל במלאי !)       ")
                        print()
                    elif chicken.get_amount() <= 30:
                        print(f"[{obj_list.index(chicken)}]. {chicken}(מוצר זה עומד להיגמר!)          ")
                        print()
                    else:
                        print(f"                        [{obj_list.index(chicken)}]. {chicken}")
                        print()

    elif user_choise == 3:
                    print(f"כבש\n____")
                    for lamb in obj_list:
                        if lamb.get_type() == "כבש":
                            if lamb.get_amount() == 0:
                                print(f"[{obj_list.index(lamb)}]. {lamb} (אזל במלאי !)       ")
                                print()

                            elif lamb.get_amount() <= 30:
                                print(f"[{obj_list.index(lamb)}]. {lamb} (מוצר זה עומד להיגמר!)       ")
                                print()
                            else:
                                print(f"                          [{obj_list.index(lamb)}]. {lamb}")
                                print()
    elif user_choise == 4:
                        print(f"דגים\n____")
                        for fish in obj_list:
                            if fish.get_type() == "דגים":
                                if fish.get_amount() == 0:
                                    print(f"[{obj_list.index(fish)}]. {fish} (אזל במלאי !)       ")
                                    print()
                                elif fish.get_amount() <= 30:
                                    print(f"[{obj_list.index(fish)}]. {fish}(מוצר זה עומד להיגמר!)   ")
                                    print()
                                else:
                                    print(f"                          [{obj_list.index(fish)}]. {fish}")
                                    print()
    elif user_choise == 5:
                    for product in obj_list:
                        if product.get_amount() == 0:
                            print(f"[{obj_list.index(product)}]. {product} (אזל במלאי !)       ")
                            print()
                        elif product.get_amount() <= 30:
                            print(f"[{obj_list.index(product)}]. {product} (מוצר זה עומד להיגמר!)    ")
                            print()
                        else:

                                print(f"                          [{obj_list.index(product)}]. {product}")
                                print()
    else:
        print("ניתן לבחור רק מה מספרים שניתנו")
        show_product(obj_list)

def set_new_price(obj_list: list):
    """
    set new price to the product
    :return:
    updated obj_list with new price of specific object
    """

    show_product(obj_list)
    user_choise = int(input(f"בחר מספר מוצר "))
    if len(obj_list)-1<user_choise:
        print("ניתן לבחור רק מה מספרים שניתנו")
        set_new_price(obj_list)
    else:
        new_price = float(input(f"הקש מחיר חדש"))
        obj_list[user_choise].set_price(new_price)
        update_file(obj_list)
        print(obj_list[user_choise])




def add_new_product(obj_list:list):
    """
    add new product to the list
    :return:
    """

    meat_type=int(input(f"""מהו סוג הבשר החדש?
[1]-בקר
    [2]-כבש
    [3]-עוף
    [4]-דגים"""))

    if meat_type == 1:
        meat_type= "בקר"

    elif meat_type == 2:
        meat_type = "כבש"


    elif meat_type == 3:
        meat_type = "עוף"


    elif meat_type == 4:
        meat_type = "דגים"
    else:
        print(f"בחר רק מהאופציות המוצגות")
        add_new_product(obj_list)

    meat_product = input(f"שם המוצר החדש")

    meat_condition=int(input(f"אנא בחר מצב מוצר"
                            f"[1]-טרי "
                             f"[2]-קפוא"))
    if meat_condition == 1:
        meat_condition = "טרי"

    elif meat_condition == 2:
        meat_condition = "קפוא"
    else:
        print(f"בחר רק מהאופציות המוצגות")
        add_new_product(obj_list)
    price = float(input(f"הקש  מחיר למוצר "))
    amount= float(input(f"הקש  כמות המוצר"))
    new_product=product_class.Product([meat_type,meat_product,meat_condition,price,amount])
    obj_list.append(new_product)
    print(new_product)