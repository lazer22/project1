print "Let\'s get started!"
spy_name = raw_input("Provide your name here : ")

#check whether spy has input something or not
if len(spy_name) > 0 :
    #code block if the condition is true.
    # concatenation of salutation and name
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
    spy_salutation = raw_input("What should we call you ? : ")
    spy_age = raw_input("Enter your age : ")
    print type(spy_age)
    spy_age = int(spy_age)
    print type(spy_age)
    spy_name = spy_salutation + " " + spy_name
    print 'Welcome ' + spy_name + ' glad to have you back with us.'
    print "Alright " + spy_name + " I\'d like to know little bit more about you before we proceed further."
else:
    print "Invalid input, please try again."