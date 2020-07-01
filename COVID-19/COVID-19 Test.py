print("||SELF SCREENING COVID-19||")

ask = input("Do you want to start your test.(yes/no)")

if ask == "yes":
    print("OK")

    name = str(input("enter your name..."))
    print("Hello!", name, )

    a = input("1 = Do you have fever above 101.4?\nکیا آپ کو تیز بخار ھے (4۔101 سے زیادہ) ؟\n(yes/no)")

    b = input("2 = Do you have cough - (dry cough)?\nکیا آپ کو خشک کھانسی ھے ؟\n(yes/no)")

    c = input("3 = Do you have Cough - (Wet Cough)?\nکیا آپ کو بلغمی کھانسی ھے ؟\n(yes/no)")

    d = input("4 = Do you have Shortness of Breath?\nکیا آپ کو سانس لینے میں تکلیف ہوتی ہے)\n(yes/no)")

    e = input("5 = Do you have Flu?\nکیا آپ کو نزلا ہے ؟\n(yes/no)")

    f = input("6 = Have you travelled abroad in the last 15 days?\nکیا آپ نے پچھلے 15 دنوں میں بیرون ملک سفر کیا ہے؟\n(yes/no)")

    g = input("7 = Have you been in contact with any person who has recently travelled internationally?\nکیا آپ کسی ایسے شخص سے رابطے میں ہیں جس نے حال ہی میں بین الاقوامی سفر کیا ہے ؟\n(yes/no)")

    h = input("8 = Do you have chest infection?\nکیا آپ کو سانس میں تکلیف کی بیماری ہے؟\n(yes/no)")

    i = input("9 = Is your age more than or equal to 60 years of age?\nکیا آپ کی عمر 60 سال سے زیادہ یا مساوی ہے؟\n(yes/no)")

    j = input("10 = Due to Co-morbidities, do you take any medicine?\nکیا آپ کو کوئی اور بیماری ہے جس کی وجہ سے آپ دوائی لیتے ہیں؟\n(yes/no)")


    permission = input("If you want to submit your test, type (submit)")

    if permission.lower() == "submit":
        print(name, "your test has been submitted")


        if a == "yes":
            if b == "yes":
                if d == "yes":
                    if f == "yes":
                        if g == "yes":
                            if i == "yes":
                                print(name, "Ooops! High Probability of Corona ! Test for Corona , Inform to Authorities ,\n Follow Govt Instructions\n Isolate at home")

        else:
            print(name, "CONGRATULATIONS! YOU ARE SAFE.")
        if a == "no":
            if b == "no":
                if c == "no":
                    if d == "no":
                        if e == "no":
                            if f == "no":
                                if g == "no":
                                    if h == "no":
                                        if i == "no":
                                            if j == "no":
                                                print(name, "You are safe from COVID-19")
        else:
            print(name, "Ooops! High probability of Corona.")


else:
    print("OK")