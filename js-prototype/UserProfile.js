module.exports = class UserProfile {
    
    constructor(itemProfiles) {

        const timeDurationMap = new Map();
        let current = 0;

        for (let i = 0; i < 96; i++) {

            timeDurationMap[this.constructor.getKeyFromArray(current, 0.25)] = 0;
            timeDurationMap[this.constructor.getKeyFromArray(current, 0.5)] = 0;
            timeDurationMap[this.constructor.getKeyFromArray(current, 1)] = 0;
            timeDurationMap[this.constructor.getKeyFromArray(current, 2)] = 0;

            current += 0.25;

        }

        for (const profile of itemProfiles) {

            const key = this.constructor.getKeyFromArray(profile.startTime, profile.duration);

            // subtract 3 to zero-center ratings
            const rating = profile.rating - 3;

            if (!timeDurationMap.has(key)) {
                timeDurationMap.set(key, rating);
            } else {
                const prevRating = timeDurationMap.get(key);
                timeDurationMap.set(key, prevRating + rating);
            }

        }

        this.timeDurationMap = timeDurationMap;

    }

    addProfile(itemProfile) {

        const start = itemProfile.startTime, duration = itemProfile.duration;

        const key = this.constructor.getKeyFromArray(start, itemProfile.duration);

        const prevKey = this.constructor.getKeyFromArray(start, itemProfile.duration * 2);
        const nextKey = this.constructor.getKeyFromArray(start, itemProfile.duration / 2);

        const surroundingKeys = [prevKey, nextKey];

        switch (start) {
            case 0:
                surroundingKeys.push(this.constructor.getKeyFromArray(0.25, duration));
                surroundingKeys.push(this.constructor.getKeyFromArray(23.75, duration));
                break;
            case 0.25:
                surroundingKeys.push(this.constructor.getKeyFromArray(0, duration));
                surroundingKeys.push(this.constructor.getKeyFromArray(0.5, duration));
                break;
            case 23.75:
                surroundingKeys.push(this.constructor.getKeyFromArray(0, duration));
                surroundingKeys.push(this.constructor.getKeyFromArray(23.5, duration));
                break;
            default:
                surroundingKeys.push(this.constructor.getKeyFromArray(start - 0.25, duration));
                surroundingKeys.push(this.constructor.getKeyFromArray(start + 0.25, duration));
                break;
        } 

        const rating = itemProfile.rating - 3;

        if (!this.timeDurationMap.has(key)) {
            this.timeDurationMap.set(key, rating);
        } else {
            const prevRating = this.timeDurationMap.get(key);
            this.timeDurationMap.set(key, prevRating + rating);
        }

        for (const surroundingKey of surroundingKeys) {
            if (!this.timeDurationMap.has(surroundingKey)) {
                this.timeDurationMap.set(surroundingKey, rating / 2);
            } else {
                const prevRating = this.timeDurationMap.get(surroundingKey);
                this.timeDurationMap.set(surroundingKey, prevRating + rating / 2);
            }
        }

        // console.log(this)

    }

    getOptimalFreeTimes(blockedOffTimes) {

        function getVectors(map) {

            function byRating(a, b) {
                if (a[1] === b[1]) {
                    return 0;
                }
                else {
                    return (a[1] > b[1]) ? -1 : 1;
                }
            }

            return [...map].sort(byRating);

        }

        const vectors = getVectors(this.timeDurationMap), optimalEvents = [];

        for (const vector of vectors) {

            const key = this.constructor.getArrayFromKey(vector[0])

            const time = key[0];
            const duration = key[1];
        
            if (!blockedOffTimes.includes(time) && !blockedOffTimes.includes(time + duration)) {

                optimalEvents.push(vector);

                if (optimalEvents.length >= 5) {
                    return optimalEvents;
                }
            }
        }

        return optimalEvents;

    }

    static convertTimeToCircle(time) {
        const angle = time * Math.PI / 12;
        return Math.cos(angle);
    }

    static getKeyFromArray(start, duration) {
        return [start, duration].toString();
    }

    static getArrayFromKey(key) {
        return key.split(",").map(x => Number(x));
    }

    toString() {
        return [...this.timeDurationMap].join('\n')
    }
}