email = input("Enter you email: ").strip()   #strip function will take out the spaces(before/after the input) for eg:example@gmail.com  strip() will convert it into example@gmail.com
username = email[:email.index('@')]        #This start from example and ends before @ (email[start:end]) starts and ends before index 7. index will help to find the index of @ -> [:7] 
domain = email[email.index('@')+1:]        #can also write as email.index('g'), here this starts with index [7+1:] till end. 
sliced = (f"Your username is '{username}' and domain is '{domain}'")    #f refers to formatter
print(sliced)
