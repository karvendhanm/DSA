let nestedObject = {
    id: 28802695164,
    date: 'December 31, 2016',
    data: {
        totalUsers: 99,
        online: 80,
        onlineStatus: {
            active: 67,
            away: 13,
            busy: 8
        }
    }
};

console.log(nestedObject.data.onlineStatus['busy']);