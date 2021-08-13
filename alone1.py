input_id = input ("ID\n")
input_pw = input ("PW\n")
real_sushi = "sushi"
real_sashimi = "sashimi"
real_sushi_pw = "1111"
real_sashimi_pw = "1234"

if real_sushi == input_id and real_sushi_pw == input_pw:
    print ("Hello! Sushi!")
elif real_sashimi == input_id and real_sashimi_pw == input_pw:
    print ("Hello! Sashimi!")
else:
    print ("Wrong Id or PW!")
