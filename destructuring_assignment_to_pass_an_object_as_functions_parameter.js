const profileData = {
    name:'Karvendhan',
    age:36,
    nationality:'Indian',
    location:'TamilNadu'
}

// function useProfileData(obj) {
//     const {name, age, nationality, location} = obj;
//     console.log('the name, age, nationality, location is: ', name, age, nationality, location);
// }

// const useProfileData = (obj) => {
//     const {name, age, nationality, location} = obj;
//     console.log('the name, age, nationality, location is: ', name, age, nationality, location);
// }

const useProfileData = ({name, age, nationality, location}) => {
    console.log('the name, age, nationality, location is: ', name, age, nationality, location);
}

useProfileData(profileData);