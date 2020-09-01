const ItemProfile = require('./ItemProfile');
const UserProfile = require('./UserProfile');

const item1 = new ItemProfile(0.25,0.5,4)
const item2 = new ItemProfile(8.75,1,2)
const item3 = new ItemProfile(12.00,2,5)

const user = new UserProfile([])
user.addProfile(item1)
user.addProfile(item2)
user.addProfile(item3)

console.log(user.getOptimalFreeTimes([0.25,0.5, 7.75, 8.5,9.5]))

const str = user.toString();
const fromStrTest = UserProfile.fromString(str)
console.log(fromStrTest.getOptimalFreeTimes([0.25,0.5, 7.75, 8.5,9.5]))