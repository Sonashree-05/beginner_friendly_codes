email = input("Enter you email: ").strip()   #strip function will take out the spaces(before/after the input) for eg:example@gmail.com  strip() will convert it into example@gmail.com
username = email[:email.index('@')]        #This start from example and ends before @ (email[start:end]) starts and ends before index 7. index will help to find the index of @ -> [:7] 
domain = email[email.index('@')+1:]        #can also write as email.index('g'), here this starts with index [7+1:] till end. 
sliced = (f"Your username is '{username}' and domain is '{domain}'")    #f refers to formatter
print(sliced)



'''An email slicer is the best Python project for beginners. The project retrieves the username and domain of an email and prints a message with this information to send to the host.  

Steps to create an Email Slicer in Python-

Get the email from the user with the input method. 
With the strip() method we will get the characters we want, that is, only the email address.
Then separate the username and domain name.
Save the extracted username and domain name in a single statement.
Using print() the message with the username and domain name will be sent to the host.'''
