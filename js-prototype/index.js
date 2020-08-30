const ItemProfile = require('./ItemProfile');
const UserProfile = require('./UserProfile');

const test_prof_1 = new ItemProfile(0.25,0.5,4)
const test_prof_2 = new ItemProfile(8.75,1,2)
const test_prof_3 = new ItemProfile(12.00,2,5)

const test_user_prof = new UserProfile([])
test_user_prof.addProfile(test_prof_1)
test_user_prof.addProfile(test_prof_2)
test_user_prof.addProfile(test_prof_3)

console.log(test_user_prof.getOptimalFreeTimes([0.25,0.5, 7.75, 8.5,9.5]))