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

        time_and_duration_dict = {}

        current = 0
        for i in range(96):
            time_and_duration_dict[(current, 0.25)] = 0
            time_and_duration_dict[(current, 0.5)] = 0
            time_and_duration_dict[(current, 1)] = 0
            time_and_duration_dict[(current, 2)] = 0
            # duration_dict[current] = 0
            current = 0.25 + current
        
        for item_profile in item_profiles:
            curr_time = item_profile.get_start_time()
            curr_duration = item_profile.get_duration()

            curr_key = (curr_time, curr_duration)

            rating = item_profile.get_rating() - 3

            if curr_key not in time_and_duration_dict.keys():
                time_and_duration_dict[curr_key] = rating
            else:
                curr_val = time_and_duration_dict[curr_key]
                time_and_duration_dict[curr_key] = curr_val + rating
        
        self.time_and_duration_dict = time_and_duration_dict

    # now the dictionary is complete

    def add_new_item(self, item_profile):
        prof_start = item_profile.get_start_time()
        prof_duration = item_profile.get_duration()

        curr_key = (prof_start, prof_duration)

        


        surrouding_keys = [(prof_start, prof_duration * 2), (prof_start, prof_duration / 2)]

        if prof_start == 0:
            surrouding_keys.append((0.25, prof_duration))
            surrouding_keys.append((23.75, prof_duration))
        elif prof_start == 0.25:
            surrouding_keys.append((0, prof_duration))
            surrouding_keys.append((0.5, prof_duration))
        elif prof_start == 23.75:
            surrouding_keys.append((0, prof_duration))
            surrouding_keys.append((23.5, prof_duration))
        else:
            surrouding_keys.append((prof_start + 0.25, prof_duration))
            surrouding_keys.append((prof_start - 0.25, prof_duration))


        rating = item_profile.get_rating() - 3

        if curr_key not in self.time_and_duration_dict.keys():
            self.time_and_duration_dict[curr_key] = rating
        else:
            curr_val = self.time_and_duration_dict[curr_key]
            self.time_and_duration_dict[curr_key] = curr_val + rating

        for key in surrouding_keys:
            if key not in self.time_and_duration_dict.keys():
                self.time_and_duration_dict[key] = rating / 2
            else:
                val = self.time_and_duration_dict[key]
                self.time_and_duration_dict[key] = val + rating/2

        print(self.time_and_duration_dict)



    def get_vectors(self):
        sort_vectors = sorted(self.time_and_duration_dict.items(), key=lambda x: x[1], reverse=True)

        print(sort_vectors)

        return sort_vectors

        '''

        for i in range(3):
            for j in range(3):
                curr_start = sort_start_times[i]
                curr_duration = sort_durations[j]

                #print(curr_start)
                #print(curr_duration)

                new_vector = [curr_start[0],curr_duration[0]]
                optimal_vectors.append(new_vector)

        '''

    '''

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

    '''

    def get_optimal_free_times(self, blocked_off_times):
        vectors = self.get_vectors()

        optimal_events = []

        count = 0

        for vector in vectors:
            print(f"VECTOR: {vector}")
            curr_time = vector[0][0]
            curr_duration = vector[0][1]

            if curr_time not in blocked_off_times and curr_time + curr_duration not in blocked_off_times:
                optimal_events.append(vector)
                count = 1 + count
                if count == 5:
                    return optimal_events
        
        print(optimal_events)
        return optimal_events
        
        '''
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
        '''

    def convert_time_to_circle(self, time):
        angle = time * math.pi / 12
        return math.cos(angle)


        