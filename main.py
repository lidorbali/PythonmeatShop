from distutils.command.install import value

import function as f

obj_list = f.create_obj()
user_choose = None
while user_choose != 5:
    user_choose = int(input(f"""
בחר מהאופציות מוצגות מטה לביצוע פעולות
     [1] - הצגת מלאיי בשר
        [2] - עדכון מלאיי
   [3] - שינוי מחיר למוצר
[4] - הוספת מוצר חדש     
               [5] -יציאה
"""))
    try:
        if user_choose == 1:
            f.show_product(obj_list)
    except:
        print("press nothing")
        continue
    try:
        if user_choose == 2:
            print(f.edit_amount(obj_list))
    except:
        print("press nothing")
        continue

    try:
        if user_choose == 3:
            f.set_new_price(obj_list)
    except:
            print("press nothing")
            continue

    try:
        if user_choose == 4:
            f.add_new_product(obj_list)
    except:
        print("press nothing")
        continue
    try:
        if user_choose == 5:
            f.update_file(obj_list)
            print("bye bye motek")
            quit()
    except valuer:
        print("press nothing")
        continue