import re
ftext = "sdngsjddsfmsdlkf.mdsksddad 2313dasd2@ffakf.com"
proverka_email = re.search(r'[0-9A-Za-z]- {,40}@\w{,40}\.\w{2,9}', ftext)


print(proverka_email)
