#! python3
#
# regular expression lesson from how to automate the boring stuff
#
#You can use a kind of regular expressions even in word and libre office to search for things!
#
#
all_NZ_phone_numbers = r'''

NZ phone lines courtesy of Wikipedia
https://en.wikipedia.org/wiki/Telephone_numbers_in_New_Zealand

Land Line
Town/City 			number
Whangarei 	 		(09) 43x-xxxx
New Plymouth 		(06) 75x-xxxx
Upper Hutt			(04) 52x-xxxx
Porirua				(04) 23x-xxxx
Lower Hutt			(04) 56x-xxxx
Wellington north		(04) 47x-xxxx
Wellington south		(04) 38x-xxxx
Nelson 	 			(03) 54x-xxxx
Kaikoura 		 	(03) 319-xxxx
Dunedin 	 			(03) 4xx-xxxx
Invercargill 		(03) 21x-xxxx 

Mobile Phone
Prefix 	Network 							Number length 		Notes
0201 	Orcon 		
0202 	Orcon 		
0203 	Voyager 												Formerly owned by Accelero
0204 	Skinny 							6 or 7 digits 	
0205 	Vodafone 		
0206 	Voyager Internet 		
021 	Vodafone 						6 to 8 digits 		6 digits originally assigned to on account customers only and 7 digits assigned to prepay customers only
022 	2degrees 						7 digits 			2degrees was launched in August 2009.
023 	Unused 												Owned by Vodafone
024 	Unused 												Protected by Management Committee 30.01.09 to preserve the potential code expansion option.
025 	Unused 							6-7 digits 			Was used by Telecom New Zealand until it was shut down on 31 March 2007. All numbers have now migrated to 027 (7-digit), with older 025 numbers prefixed with 4 (e.g. 027-4xx-xxxx).
026 	Spark New Zealand,Team Talk 		7 digits 			Used for calling Fleetlink or other trunked radios from a phone line
027 	Spark New Zealand 				7 digits 			Formerly Telecom New Zealand
028 0 	Compass Communications 		
028 	CallPlus or BLACK + WHITE 		
028 4 	Warehouse Mobile 									Owned by The Warehouse group, this network launched on 28 November 2015 as an MVNO on 2Degrees Mobile
028 85 	Vodafone 											Previously allocated to M2 Limited and was transferred to Vodafone on 6/11/13
028 86 	Vodafone 											Previously allocated to M2 Limited and was transferred to Vodafone on 6/11/13
028 89 	2Talk 							7 digits 	
028 96 	NOW 												Previously called Airnet NZ Ltd
029 	TelstraClear (Vodafone) 								Vodafone acquired TelstraClear in 2012 


Ways people write phone numbers:
(04)1234567
(04) 123 4567
(04) 1234 567
041234567
04 1234567


One way to solve this is to strip all brackets and special characters from the message, except maybe commas
Then to the regex to find the patterns

in general, prefix is 2 to 5 numbers, phone number is an additional 6 to 8 numbers
There are patterns for the prefixes, we can work out the length of the remaining number by the prefix
'''

#How RE works
#you compile a search method
#then you search some text to make a match object (the searth results)
#then you call the match objects group() to get the matched strings
#RE does greedy matches, that means it tries to match the most possile in it's result, can also do non greedy but need to specify it "?"


# \d  -digit numeric character class
# \D  -character that is not a numeric digit
# \w  -Word Characters, letters and underscores
# \W  -non letter or underscore characters
# \s  -white space characters, space, tabs, newline
# \S  -non-white space characters
# .   -wild card character, could be anything

# YOU CAN MAKE YOUR OWN CLASSES!!!
# vowelRegex = re.compile(r'[aeiouAEIOU]+[a-zA-Z0-9_.+-]+') don't need |
# 		vowelRegex.search(string)
# letterRegex = re.compile(r'[a-zA-Z]') can use ranges
# nonLetterRegex = re.compile(r'[^a-zA-Z]') "^" shows every text character that isn't a letter

#| pipe character, lets you specify options
#   r'Bat(man|mobile|copter|car)'
#  ^hello at the start to show result has to be at beginning of string
#  bye$ to match with this string at the end of the text
#
#  r'Bat(wo)?man'  search for Batman or Batwoman
#  r'02(01|02|03|04|05|06|1|2|3|4|5|6|7|8|84|85|89|9|96){1}\d\d\d\d\d\d(\d)?'   search for all mobile phone numbers
#  r'(03|04|06|09){1}\d\d\d\d\d\d\d'   search for all land line phone numbers
#
#  r'Da(na)* Batman!'    searches for na 0 to any number of times
#  r'First Name: (.*) Last Name: (.*)'  #searches up to the new line character
#  r'First Name: (.*) Last Name: (.*)', re.DOTALL   #searches actually everything
#  r'First Name: (.*) Last Name: (.*)', re.IGNORECASE   #searches amd ognores case os search
#  r'Bat(woman|man)+'
#
# object.search() --finds the first one
# object.findall() --finds them all
import re, pprint

#search, using the VERBOSE option I can add comments and it ignores white spaces, others there as reference
areaCodes_regex = re.compile(r'''((03|04|06|09|   #all the land line area codes
02(01|02|03|04|05|06|1|2|3|4|5|6|7|8|80|84|85|89|9|96))  #all the mobile phone digit codes start with 02, then there are some options
\D{,2} 					#something non numeric that goes in the middle between the area code and main number, between zero and 2 characters
(\d\d\d\d\d\d(\d){,2}))	#the number could be 6 to 8 digits long
''', re.VERBOSE | re.DOTALL | re.IGNORECASE)

#text string
message='Call me on (021) 1234567, or 021-1234567. If you want to \'have fun\' call me at home on 09x623456\nI tell people I don\'t like a fake phone number, 04 1234567891 or 02212345.\nMy old number was 0280-1234567.'
print(message)

#search for phone numbers
match_object = areaCodes_regex.findall(message)

#check if I found anything then print it or else a message
if match_object != None: 
	for find in match_object:
		print(find[1] + ' ' + find[3])
else:
	print('Nothing was found')

