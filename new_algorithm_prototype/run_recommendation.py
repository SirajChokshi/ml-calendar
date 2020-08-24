from itemprofile import ItemProfile
from itemprofile import UserProfile

def run():
    test_prof_1 = ItemProfile(0.25,0.5,4)
    test_prof_2 = ItemProfile(8.75,1,2)
    test_prof_3 = ItemProfile(12.00,2,5)

    test_user_prof = UserProfile([])
    test_user_prof.add_new_item(test_prof_1)
    test_user_prof.add_new_item(test_prof_2)
    test_user_prof.add_new_item(test_prof_3)

    test_user_prof.get_optimal_vectors()

    test_user_prof.get_optimal_free_times([0.25,0.5, 7.75, 8.5,9.5])

if __name__ == "__main__":
    run()