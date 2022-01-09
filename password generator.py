import string as s
import random
ch=s.ascii_letters+s.digits+s.punctuation
password=''.join(random.choice(ch) for i in range(random.randint(5,20)))
print("GENERATED PASSWORD IS :",password)
