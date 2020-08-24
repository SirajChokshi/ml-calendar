import math

class ItemProfile(object):

    def __init__(self, start_time, duration, rating):
        self.start_time = start_time
        self.duration = duration
        self.rating = rating

    def get_start_time(self):
        return self.start_time

    def get_duration(self):
        return self.duration

    def get_rating(self):
        return self.rating

class UserProfile(object):

    def __init__(self, item_profiles):
        start_time_dict = {}
        duration_dict = {}

        current = 0
        for i in range(96):
            start_time_dict[current] = 0
            # duration_dict[current] = 0
            current = 0.25 + current
        
        duration_dict[0.25] = 0
        duration_dict[0.5] = 0
        duration_dict[1] = 0
        duration_dict[2] = 0
        
        for item_profile in item_profiles:
            curr_time = item_profile.get_start_time()
            curr_duration = item_profile.get_duration()

            rating = (item_profile.get_rating() - 3) * (item_profile.get_rating() - 3)
            if item_profile.get_rating() < 3:
                rating = 0 - rating

            curr_val_1 = start_time_dict[curr_time]
            curr_val_2 = duration_dict[curr_duration]

            start_time_dict[curr_time] = curr_val_1 + rating
            duration_dict[curr_duration] = curr_val_2 + rating
        
        self.start_time_dict = start_time_dict
        self.duration_dict = duration_dict

    # now the dictionaries are complete

    def add_new_item(self, item_profile):
        prof_start = item_profile.get_start_time()
        prof_duration = item_profile.get_duration()

        rating = (item_profile.get_rating() - 3) * (item_profile.get_rating() - 3)
        if item_profile.get_rating() < 3:
            rating = 0 - rating

        curr_val_1 = self.start_time_dict[prof_start]
        curr_val_2 = self.duration_dict[prof_duration]

        self.start_time_dict[prof_start] = curr_val_1 + rating
        self.duration_dict[prof_duration] = curr_val_2 + rating



    def get_optimal_vectors(self):
        sort_start_times = sorted(self.start_time_dict.items(), key=lambda x: x[1], reverse=True)
        sort_durations = sorted(self.duration_dict.items(), key=lambda x: x[1], reverse=True)

        print(type(sort_start_times))
        print(sort_start_times)

        optimal_vectors = []

        for i in range(3):
            for j in range(3):
                curr_start = sort_start_times[i]
                curr_duration = sort_durations[j]

                #print(curr_start)
                #print(curr_duration)

                new_vector = [curr_start[0],curr_duration[0]]
                optimal_vectors.append(new_vector)


        # print(optimal_vectors)

        return optimal_vectors

    def compute_cosine_similarity(self, item_start_time, item_duration):
        vectors = self.get_optimal_vectors()

        print(f"ITEM START TIME: {item_start_time}")

        min_diff = 1

        item_start_time = self.convert_time_to_circle(item_start_time)

        item_magnitude = math.sqrt(item_start_time * item_start_time + item_duration * item_duration)
        print(f"ITEM START CIRCLE: {item_start_time}")
        print(f"ITEM DURATION: {item_duration}")
        print(f"ITEM MAGNITUDE: {item_magnitude}")

        for vector in vectors:
            vector_start = self.convert_time_to_circle(vector[0])
            vector_duration = vector[1]

            #print(f"VECTOR START: {vector_start}")
            #print(f"VECTOR DURATION: {vector_duration}")

            vector_magnitude = math.sqrt(vector_start * vector_start + vector_duration * vector_duration)

            dot_product = vector_start * item_start_time + vector_duration * item_duration
            total_magnitude = item_magnitude * vector_magnitude

            angle = abs(dot_product / total_magnitude)

            if abs(angle) < min_diff:
                min_diff = abs(angle)
        
        return min_diff

    def get_optimal_free_times(self, blocked_off_times):
        optimal_events = []
        current_time = 0
        current_duration = 0.25
        for i in range(96):
            for j in range(4):
                if current_time not in blocked_off_times and current_time + current_duration not in blocked_off_times:
                    angle = abs(self.compute_cosine_similarity(current_time, current_duration))
                    print(f"ANGLE: {angle}")
                    if abs(angle) < 0.002:
                        print(f"APPENDING {current_time}, {current_duration}")
                        optimal_events.append([current_time, current_duration])
                #DO SOMETHING
                current_duration = 2 * current_duration
                if current_duration == 2:
                    current_duration = 0.25
            
            current_time = current_time + 0.25
        
        print(optimal_events)
        print(len(optimal_events))
        return optimal_events

    def convert_time_to_circle(self, time):
        angle = time * math.pi / 12
        return math.cos(angle)


        