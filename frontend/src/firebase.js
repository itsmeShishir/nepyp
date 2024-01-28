
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
    apiKey: "AIzaSyCeC0xNUc7PMjoedghTR7O4n4-j4Cv1UOg",
    authDomain: "newsletter-demo-fb3f7.firebaseapp.com",
    projectId: "newsletter-demo-fb3f7",
    storageBucket: "newsletter-demo-fb3f7.appspot.com",
    messagingSenderId: "53433028074",
    appId: "1:53433028074:web:d564559fc994257f303693"
};

const firebaseApp = initializeApp(firebaseConfig);
const db = getFirestore(firebaseApp);

export default db;


