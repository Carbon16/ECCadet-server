#Turn the following data into a list of names, and if register = 1, put a tick next to their name, if register = 2, put a cross next to their name.

S = [
  {
"id": 'Nick Bukhantsov',
"title": 'Nick Bukhantsov',
  },
  {
"id": 'John Gartside',
"title": 'John Gartside',
  },
  {
"id": 'Isabel Henderson',
"title": 'Isabel Henderson',
  },
  {
"id": 'Bay Andreadis',
"title": 'Bay Andreadis',
  },
  {
"id": 'Anna McGrath',
"title": 'Anna McGrath',
  },
  {
"id": 'Luca Rushton',
"title": 'Luca Rushton',
  },
  {
"id": 'Samara Sarpong',
"title": 'Samara Sarpong',
  },
  {
"id": 'Alexander Pavry',
"title": 'Alexander Pavry',
  },
  {
"id": 'Lara Thurman',
"title": 'Lara Thurman',
  },
  {
"id": 'Taylor Schultheiss',
"title": 'Taylor Schultheiss',
  },
  {
"id": 'Bryce Whitley',
"title": 'Bryce Whitley',
  },
  {
"id": 'Isla Henwood',
"title": 'Isla Henwood',
  },
  {
"id": 'Kintario Gledstone',
"title": 'Kintario Gledstone',
  },
  {
"id": 'Zoe Moir',
"title": 'Zoe Moir',
  },
  {
"id": 'Thomas Lovett',
"title": 'Thomas Lovett',
  },
  {
"id": 'Alex Bukur',
"title": 'Alex Bukur',
  },
  {
"id": 'Sam Perry',
"title": 'Sam Perry',
  },
  {
"id": 'Florence Bates',
"title": 'Florence Bates',
  },
  {
"id": 'Ada Ucuncu',
"title": 'Ada Ucuncu',
  },
  {
"id": 'Hugo Handley',
"title": 'Hugo Handley',
  },
  {
"id": 'Izzy Hutton',
"title": 'Izzy Hutton',
  },
  {
"id": 'Clementine Curham',
"title": 'Clementine Curham',
  },
  {
"id": 'Sophia Moores',
"title": 'Sophie Moores',
  },
  {
"id": 'Archie Lycett',
"title": 'Archie Lycett',
  },
  {
"id": 'Tom Carter',
"title": 'Tom Carter', 
  },
  {
"id": 'Paddy Purves',
"title": 'Paddy Purves',
  }
]

N = [
  {
    "id": "AL SA'DI, Sanad",
    "title": "AL SA'DI, Sanad"
  },
  {
    "id": "ALLISON, Isabelle",
    "title": "ALLISON, Isabelle"
  },
  {
    "id": "BARRETT, Marcus",
    "title": "BARRETT, Marcus"
  },
  {
    "id": "BEDFORD, James",
    "title": "BEDFORD, James"
  },
  {
    "id": "BUIJS, Catharina",
    "title": "BUIJS, Catharina"
  },
  {
    "id": "CALLAGHAN, Seren",
    "title": "CALLAGHAN, Seren"
  },
  {
    "id": "CATTERALL, Thomas",
    "title": "CATTERALL, Thomas"
  },
  {
    "id": "CLARK, Sophie",
    "title": "CLARK, Sophie"
  },
  {
    "id": "ELLIOTT, Jacob",
    "title": "ELLIOTT, Jacob"
  },
  {
    "id": "ELLIS, Charlie",
    "title": "ELLIS, Charlie"
  },
  {
    "id": "GRAU-HERNANDEZ, Pep",
    "title": "GRAU-HERNANDEZ, Pep"
  },
  {
    "id": "HANSSON, Philip",
    "title": "HANSSON, Philip"
  },
  {
    "id": "HARPER, Sebastian",
    "title": "HARPER, Sebastian"
  },
  {
    "id": "HUGHES, Georgina",
    "title": "HUGHES, Georgina"
  },
  {
    "id": "JAMES, Sophie",
    "title": "JAMES, Sophie"
  },
  {
    "id": "JONES, Harry",
    "title": "JONES, Harry"
  },
  {
    "id": "JUSTICE, Holly",
    "title": "JUSTICE, Holly"
  },
  {
    "id": "KOUSETTA, Kenan",
    "title": "KOUSETTA, Kenan"
  },
  {
    "id": "KWOK, Sophia",
    "title": "KWOK, Sophia"
  },
  {
    "id": "LAWSON SMITH, Tom",
    "title": "LAWSON SMITH, Tom"
  },
  {
    "id": "LUNG, Sean",
    "title": "LUNG, Sean"
  },
  {
    "id": "LUTTIG, Zach",
    "title": "LUTTIG, Zach"
  },
  {
    "id": "MACGREGOR",
    "title": "MACGREGOR"
  },
  {
    "id": "WATSON, Isla",
    "title": "WATSON, Isla"
  },
  {
    "id": "MACMILLAN, Hector",
    "title": "MACMILLAN, Hector"
  },
  {
    "id": "NORTHOVER, William",
    "title": "NORTHOVER, William"
  },
  {
    "id": "PATEL, Rohan",
    "title": "PATEL, Rohan"
  },
  {
    "id": "PINNES, Isabella",
    "title": "PINNES, Isabella"
  },
  {
    "id": "Popeta, Vladimir",
    "title": "Popeta, Vladimir"
  },
  {
    "id": "REID, George",
    "title": "REID, George"
  },
  {
    "id": "SECKER, Jacob",
    "title": "SECKER, Jacob"
  },
  {
    "id": "SHARMA, Dev",
    "title": "SHARMA, Dev"
  },
  {
    "id": "SIRAH, Jeevan",
    "title": "SIRAH, Jeevan"
  },
  {
    "id": "SMITH, Reuben",
    "title": "SMITH, Reuben"
  },
  {
    "id": "VOWLES, Finn",
    "title": "VOWLES, Finn"
  },
  {
    "id": "WILLIAMS, Destiny",
    "title": "WILLIAMS, Destiny"
  },
  {
    "id": "XANTHAKOS, Pan",
    "title": "XANTHAKOS, Pan"
  },
  {
    "id": "ZHENG, Eason",
    "title": "ZHENG, Eason"
  }
]

B = [
    {
      "id": "Annalise Dixon",
      "title": "Annalise Dixon"
    },
    {
      "id": "Stepan Kasperskiy",
      "title": "Stepan Kasperskiy"
    },
    {
      "id": "Lucie Jones",
      "title": "Lucie Jones"
    },
    {
      "id": "Freddie Hawkins",
      "title": "Freddie Hawkins"
    },
    {
      "id": "Sasha Patient",
      "title": "Sasha Patient"
    },
    {
      "id": "Spencer McHarg",
      "title": "Spencer McHarg"
    },
    {
      "id": "Isabella Sharp",
      "title": "Isabella Sharp"
    },
    {
      "id": "Jasper Cole",
      "title": "Jasper Cole"
    },
    {
      "id": "Jamie Williams",
      "title": "Jamie Williams"
    },
    {
      "id": "Victor Muangman",
      "title": "Victor Muangman"
    },
    {
      "id": "Dara Spasova",
      "title": "Dara Spasova"
    },
    {
      "id": "Esme Jordan",
      "title": "Esme Jordan"
    },
    {
      "id": "Ronnie Hickling",
      "title": "Ronnie Hickling"
    },
    {
      "id": "Sophia Pirrie",
      "title": "Sophia Pirrie"
    },
    {
      "id": "Nathan Farmer",
      "title": "Nathan Farmer"
    },
    {
      "id": "Beth Fryer",
      "title": "Beth Fryer"
    },
    {
      "id": "Harry Swan",
      "title": "Harry Swan"
    },
    {
      "id": "Bea Scott",
      "title": "Bea Scott"
    },
    {
      "id": "Maria Pontes",
      "title": "Maria Pontes"
    },
    {
      "id": "Erin Speed",
      "title": "Erin Speed"
    },
    {
      "id": "Imogen Martin-Webb",
      "title": "Imogen Martin-Webb"
    },
    {
      "id": "Will James",
      "title": "Will James"
    },
    {
      "id": "Riccardo Figna",
      "title": "Riccardo Figna"
    },
    {
      "id": "Alex Okonkwo",
      "title": "Alex Okonkwo"
    },
    {
      "id": "Alisha Hakata",
      "title": "Alisha Hakata"
    },
    {
      "id": "Harry Wearne",
      "title": "Harry Wearne"
    },
    {
      "id": "Alfie Webb",
      "title": "Alfie Webb"
    }
]

R = [
  {
    "id": "Mary Elizabeth Baihinga",
    "title": "Mary Elizabeth Baihinga"
  },
  {
    "id": "Daniel Strange",
    "title": "Daniel Strange"
  },
  {
    "id": "Viktor Chistyakov",
    "title": "Viktor Chistyakov"
  },
  {
    "id": "Sam Clinton",
    "title": "Sam Clinton"
  },
  {
    "id": "Henry Dench",
    "title": "Henry Dench"
  },
  {
    "id": "Daniel Clatworthy",
    "title": "Daniel Clatworthy"
  },
  {
    "id": "Caroline Bartram",
    "title": "Caroline Bartram"
  },
  {
    "id": "Ching Wan (Joshua) Chu",
    "title": "Ching Wan (Joshua) Chu"
  },
  {
    "id": "Annebel English",
    "title": "Annebel English"
  },
  {
    "id": "Toby Lee",
    "title": "Toby Lee"
  },
  {
    "id": "Zak Scerri",
    "title": "Zak Scerri"
  },
  {
    "id": "Jack Wingate",
    "title": "Jack Wingate"
  },
  {
    "id": "George Gordon",
    "title": "George Gordon"
  },
  {
    "id": "Selina Han",
    "title": "Selina Han"
  },
  {
    "id": "Maja Maziuk",
    "title": "Maja Maziuk"
  },
  {
    "id": "Jacob (Jake) Barton",
    "title": "Jacob (Jake) Barton"
  },
  {
    "id": "Dejan Filpas",
    "title": "Dejan Filpas"
  },
  {
    "id": "Harry Hamlyn",
    "title": "Harry Hamlyn"
  },
  {
    "id": "Timofey Lomizov",
    "title": "Timofey Lomizov"
  },
  {
    "id": "Samuel Brown",
    "title": "Samuel Brown"
  },
  {
    "id": "Roscoe Crockett",
    "title": "Roscoe Crockett"
  },
  {
    "id": "Matthew Jarrett",
    "title": "Matthew Jarrett"
  },
  {
    "id": "Brandon McGuinness",
    "title": "Brandon McGuinness"
  },
  {
    "id": "Max Springett",
    "title": "Max Springett"
  },
  {
    "id": "Wai Lam (Miles) Wong)",
    "title": "Wai Lam (Miles) Wong)"
  },
  {
    "id": "Florence White",
    "title": "Florence White"
  },
  {
    "id": "Samuel Sheehan",
    "title": "Samuel Sheehan"
  },
  {
    "id": "Hugo Dowgierd ",
    "title": "Hugo Dowgierd "
  },
  {
    "id": "James Roberts",
    "title": "James Roberts"
  },
  {
    "id": "Aaron Patel",
    "title": "Aaron Patel"
  },
  {
    "id": "Rafi Darwish",
    "title": "Rafi Darwish"
  },
  {
    "id": "Po Yen (Felicia) Cheung",
    "title": "Po Yen (Felicia) Cheung"
  },
  {
    "id": "Mikhail (Misha) Davidenko",
    "title": "Mikhail (Misha) Davidenko"
  },
  {
    "id": "James Kirkman",
    "title": "James Kirkman"
  },
  {
    "id": "Diana Peters",
    "title": "Diana Peters"
  },
  {
    "id": "Zain Thaver",
    "title": "Zain Thaver"
  },
  {
    "id": "Qian Yu (Aloysius) Yeung",
    "title": "Qian Yu (Aloysius) Yeung"
  }
]

T = [
  {
    "id": "Edward Armstrong",
    "title": "Edward Armstrong"
  },
  {
    "id": "Tilly Craggs",
    "title": "Tilly Craggs"
  },
  {
    "id": "Rufus Ford",
    "title": "Rufus Ford"
  },
  {
    "id": "Kiran Gopikumar",
    "title": "Kiran Gopikumar"
  },
  {
    "id": "Sadie Hyde",
    "title": "Sadie Hyde"
  },
  {
    "id": "Edward Lyons",
    "title": "Edward Lyons"
  },
  {
    "id": "Graham Mills",
    "title": "Graham Mills"
  },
  {
    "id": "Isla Perkins",
    "title": "Isla Perkins"
  },
  {
    "id": "Lara Sennaro",
    "title": "Lara Sennaro"
  },
  {
    "id": "Coco Veillard",
    "title": "Coco Veillard"
  },
  {
    "id": "Chiamaka Brown",
    "title": "Chiamaka Brown"
  },
  {
    "id": "William Digance",
    "title": "William Digance"
  },
  {
    "id": "Charles Francis",
    "title": "Charles Francis"
  },
  {
    "id": "Fleur Veillard",
    "title": "Fleur Veillard"
  },
  {
    "id": "Stefan Ilic",
    "title": "Stefan Ilic"
  },
  {
    "id": "Harriet Mathers",
    "title": "Harriet Mathers"
  },
  {
    "id": "Joseph Morley",
    "title": "Joseph Morley"
  },
  {
    "id": "Edward Pike",
    "title": "Edward Pike"
  },
  {
    "id": "Lucile Soin",
    "title": "Lucile Soin"
  },
  {
    "id": "Oscar Dale-Essex",
    "title": "Oscar Dale-Essex"
  },
  {
    "id": "Charlotte Burgess",
    "title": "Charlotte Burgess"
  },
  {
    "id": "Ruby Edwards",
    "title": "Ruby Edwards"
  },
  {
    "id": "Ho Sum (Isabel) Fung",
    "title": "Ho Sum (Isabel) Fung"
  },
  {
    "id": "Nadia Gyamfi",
    "title": "Nadia Gyamfi"
  },
  {
    "id": "Amelia Jallot",
    "title": "Amelia Jallot"
  },
  {
    "id": "Casper Maxwell-Randeria",
    "title": "Casper Maxwell-Randeria"
  },
  {
    "id": "Ariana Newton",
    "title": "Ariana Newton"
  },
  {
    "id": "Sienna Raincock",
    "title": "Sienna Raincock"
  },
  {
    "id": "Gabrielle Stowe",
    "title": "Gabrielle Stowe"
  },
  {
    "id": "Jack Warner",
    "title": "Jack Warner"
  },
  {
    "id": "Daisy Craggs",
    "title": "Daisy Craggs"
  },
  {
    "id": "Eva Fitzhugh",
    "title": "Eva Fitzhugh"
  },
  {
    "id": "Cheuk Ying (Lea) Yuen",
    "title": "Cheuk Ying (Lea) Yuen"
  },
  {
    "id": "Alivia Hakata",
    "title": "Alivia Hakata"
  },
  {
    "id": "Arun Joshi",
    "title": "Arun Joshi"
  },
  {
    "id": "Tana McCall",
    "title": "Tana McCall"
  },
  {
    "id": "Isabella Penino Vinas",
    "title": "Isabella Penino Vinas"
  },
  {
    "id": "Henry Reid",
    "title": "Henry Reid"
  },
  {
    "id": "William Thomson",
    "title": "William Thomson"
  },
  {
    "id": "Kate Coursey",
    "title": "Kate Coursey"
  }
]

L = [
  {
    "id": "Alysha Advani",
    "title": "Alysha Advani"
  },
  {
    "id": "Luke Bermejo",
    "title": "Luke Bermejo"
  },
  {
    "id": "Lottie Edwards",
    "title": "Lottie Edwards"
  },
  {
    "id": "Joshua Hadley",
    "title": "Joshua Hadley"
  },
  {
    "id": "Olivia Key",
    "title": "Olivia Key"
  },
  {
    "id": "George Walkden",
    "title": "George Walkden"
  },
  {
    "id": "Madeleine O’Brien",
    "title": "Madeleine O’Brien"
  },
  {
    "id": "Arran Blevins",
    "title": "Arran Blevins"
  },
  {
    "id": "Charissa Kwok",
    "title": "Charissa Kwok"
  },
  {
    "id": "Eleanor Vetch",
    "title": "Eleanor Vetch"
  },
  {
    "id": "Georgina Carrington",
    "title": "Georgina Carrington"
  },
  {
    "id": "Harry Feltham",
    "title": "Harry Feltham"
  },
  {
    "id": "Alice Griffiths",
    "title": "Alice Griffiths"
  },
  {
    "id": "Wai Ching Lee (Cedric)",
    "title": "Wai Ching Lee (Cedric)"
  },
  {
    "id": "Isabella Mitchell",
    "title": "Isabella Mitchell"
  },
  {
    "id": "George Scott-Williams",
    "title": "George Scott-Williams"
  },
  {
    "id": "Isabella Matson",
    "title": "Isabella Matson"
  },
  {
    "id": "James Mathews",
    "title": "James Mathews"
  },
  {
    "id": "Lucy Hughes",
    "title": "Lucy Hughes"
  },
  {
    "id": "Susanna Christie",
    "title": "Susanna Christie"
  },
  {
    "id": "Noah Fairclough",
    "title": "Noah Fairclough"
  },
  {
    "id": "Marigold Jones",
    "title": "Marigold Jones"
  },
  {
    "id": "Rory Mathers",
    "title": "Rory Mathers"
  },
  {
    "id": "Nicola Peters",
    "title": "Nicola Peters"
  },
  {
    "id": "Louis Simmons",
    "title": "Louis Simmons"
  },
  {
    "id": "Phoebe Witten",
    "title": "Phoebe Witten"
  },
  {
    "id": "Theo Maxwell-Randeria",
    "title": "Theo Maxwell-Randeria"
  },
  {
    "id": "Janice Leung",
    "title": "Janice Leung"
  }
]


names = [{"title":"PATEL, Rohan","id":"PATEL, Rohan","reg":1,"authorised":"Kousetta "},{"title":"CLARK, Sophie","id":"CLARK, Sophie","reg":1,"authorised":"Kousetta "},{"title":"LUNG, Sean","id":"LUNG, Sean","reg":1,"authorised":"Kousetta "},{"title":"MACGREGOR","id":"MACGREGOR","reg":1,"authorised":"Kousetta "},{"title":"LUTTIG, Zach","id":"LUTTIG, Zach","reg":2,"authorised":"Kousetta "},{"title":"Jack Wingate","id":"Jack Wingate","reg":1,"authorised":"Flt Sgt Crockett"},{"title":"Harry Hamlyn","id":"Harry Hamlyn","reg":1,"authorised":"Flt Sgt Crockett"},{"title":"Zoe Moir","id":"Zoe Moir","reg":2,"authorised":"Leo"},{"title":"Ronnie Hickling","id":"Ronnie Hickling","reg":2,"authorised":"Leo"},{"title":"Zain Thaver","id":"Zain Thaver","reg":1,"authorised":"Flt Sgt Crockett"},{"title":"Imogen Martin-Webb","id":"Imogen Martin-Webb","reg":1,"authorised":"Leo"},{"title":"SIRAH, Jeevan","id":"SIRAH, Jeevan","reg":2,"authorised":"Kousetta "},{"title":"BUIJS, Catharina","id":"BUIJS, Catharina","reg":1,"authorised":"Izzy"},{"title":"Lara Sennaro","id":"Lara Sennaro","reg":1,"authorised":"Leo"},{"title":"Ariana Newton","id":"Ariana Newton","reg":1,"authorised":"Leo"},{"title":"Sienna Raincock","id":"Sienna Raincock","reg":1,"authorised":"Leo"},{"title":"Charles Francis","id":"Charles Francis","reg":1,"authorised":"Leo"},{"title":"Jack Warner","id":"Jack Warner","reg":1,"authorised":"Leo"},{"title":"William Digance","id":"William Digance","reg":1,"authorised":"Leo"},{"title":"Daisy Craggs","id":"Daisy Craggs","reg":1,"authorised":"Leo"},{"title":"Ruby Edwards","id":"Ruby Edwards","reg":1,"authorised":"Leo"},{"title":"Nadia Gyamfi","id":"Nadia Gyamfi","reg":1,"authorised":"Leo"},{"title":"Oscar Dale-Essex","id":"Oscar Dale-Essex","reg":1,"authorised":"Leo"},{"title":"Tilly Craggs","id":"Tilly Craggs","reg":1,"authorised":"Leo"},{"title":"Chiamaka Brown","id":"Chiamaka Brown","reg":1,"authorised":"Leo"}]

#If names[i] are in S, B, T, N or R, then assign them the label of the list they are in. If names[i].reg = 1, then put a tick next to their name, if names[i].reg = 2, put a cross next to their name.

for i in range(len(names)):
  for j in range(len(S)):
    if names[i]['title'] == S[j]['title']:
      names[i]['status'] = 'S'
  for k in range(len(B)):
    if names[i]['title'] == B[k]['title']:
      names[i]['status'] = 'B'
  for l in range(len(T)):
    if names[i]['title'] == T[l]['title']:
      names[i]['status'] = 'T'
  for m in range(len(N)):
    if names[i]['title'] == N[m]['title']:
      names[i]['status'] = 'N'
  for n in range(len(R)):
    if names[i]['title'] == R[n]['title']:
      names[i]['status'] = 'R'
  for o in range(len(L)):
    if names[i]['title'] == L[o]['title']:
      names[i]['status'] = 'L'
  if names[i]['reg'] == 1:
    names[i]['tick'] = '✔'
  elif names[i]['reg'] == 2:
    names[i]['tick'] = '✘'

#Print all the names with the lable R in alphabetical order, with teh tick or cross next to their name.

Brad = []
Scott = []
Tranining = []
R = []
Naval = []
Leadership = []

for i in range(len(names)):
  if names[i]['status'] == 'B':
    Brad.push(names[i]['tick'] + ' ' + names[i]['title'])
  
for i in range(len(names)):
  if names[i]['status'] == 'S':
    Scott.push(names[i]['tick'] + ' ' + names[i]['title'])

for i in range(len(names)):
  if names[i]['status'] == 'T':
    Tranining.push(names[i]['tick'] + ' ' + names[i]['title'])

for i in range(len(names)):
  if names[i]['status'] == 'N':
    Naval.push(names[i]['tick'] + ' ' + names[i]['title'])

for i in range(len(names)):
  if names[i]['status'] == 'R':
    R.push(names[i]['tick'] + ' ' + names[i]['title'])
  
for i in range(len(names)):
  if names[i]['status'] == 'L':
    Leadership.push(names[i]['tick'] + ' ' + names[i]['title'])


#return a count of the number of names in each list.

S_count = 0
B_count = 0
T_count = 0
N_count = 0
R_count = 0
L_count = 0

for i in range(len(names)):
  if names[i]['status'] == 'S':
    S_count += 1
  elif names[i]['status'] == 'B':
    B_count += 1
  elif names[i]['status'] == 'T':
    T_count += 1
  elif names[i]['status'] == 'N':
    N_count += 1
  elif names[i]['status'] == 'R':
    R_count += 1
  elif names[i]['status'] == 'L':
    L_count += 1

print('Scott: ' + str(S_count))
print('Bradford: ' + str(B_count))
print('Training: ' + str(T_count))
print('Navy: ' + str(N_count))
print('RAF: ' + str(R_count))
print('Total: ' + str(len(names)))