let userobj={username:"Ana", 
               password: "123" }
let database = [userobj]

let newsfeed=[{username:"aa", timline:"1"},{username:"bb", timline:'23'}, {username:'cc', timline:'5'} ]


const people = ["Greg", "Mary", "Devon", "James"];
people.shift()
console.log(people)

people[2]="Jason"
console.log(people)

people[people.length]='Elena'
console.log(people)
console.log(people.indexOf('Mary'))
mary_ind=people.indexOf('Mary')
me_ind=people.indexOf('Elena')

let people1=people.slice(mary_ind+1,me_ind)
console.log(people1)
console.log(people1.indexOf('Foo'))

last=people[people.length-1]
console.log(last)

for (let i=0; i<people.length; i++){
    console.log(people[i]);
}
let i=0
while (people[i] != "Jason") {
    console.log(people[i]);
    i++;
}
let colors = ['red', 'blue', 'white', 'black', 'green']
let suff=['st', 'nd', 'rd', 'th', 'th', 'th']

=================================================//
for (let i=0; i<colors.length; i++) {
console.log('M
do {
let user_numb = prompt('what is the number?');
var user_numb_num = Number(user_numb)} while (user_numb_num< 10)


or//
let user_numb
do {
    user_numb = prompt('what is the number?')} while (Number(user_numb)< 10)
=============================================//

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log('the number of floors: ', building['numberOfFloors']);
console.log('apartments quantity at floor 1: ', building['numberOfAptByFloor']['firstFloor']);
console.log('apartments quantity at floor 3: ', building['numberOfAptByFloor']['thirdFloor']);
console.log("name and rooms' quantity: ", building['nameOfTenants'][1], building['numberOfRoomsAndRent']['dan'][0])

let rent_s=building['numberOfRoomsAndRent']['sarah'][1]
let rent_d=building['numberOfRoomsAndRent']['dan'][1]
let rent_dav=building['numberOfRoomsAndRent']['david'][1]

if (rent_s+rent_dav>rent_d){
    rent_d=1200;
}

console.log(rent_d)

========================//

family = {'mother': "Taty",
        'father': 'Serg',
        'child': 'Alex',
        'grandchild': 'Dan'}

for (let i in family) {console.log (i, family [i])};
===============================================================

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  let a =""
  for (let i in details) {a = a+ " " +i+" "+ details[i]};
  console.log(a)
==============================================================

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let names_l=[]
for (let i=0; i<names.length; i++) {
names_l[i] = names[i][0];
};
let j=names_l.sort().join("");

console.log(j)
