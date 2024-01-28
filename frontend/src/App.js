import React, { useState, useEffect } from 'react';
import { FaFacebook, FaInstagram } from "react-icons/fa";
import { FaLinkedinIn } from "react-icons/fa6";
import "./app.css";
import img from "./assets/nfilili.png";
import { collection, addDoc, serverTimestamp } from 'firebase/firestore';
import db from './firebase';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const App = () => {
  const [input, setInput] = useState("");

   const getInitialTime = () => {
    const storedTime = localStorage.getItem('countdownTimerInitialTime');
    return storedTime ? parseInt(storedTime, 10) : (11 * 24 * 60 * 60); // 11 days in seconds by default
  };

  const getRemainingSeconds = () => {
    const storedSeconds = localStorage.getItem('countdownTimerRemainingSeconds');
    return storedSeconds ? parseInt(storedSeconds, 10) : getInitialTime();
  };

  const [secondsRemaining, setSecondsRemaining] = useState(getRemainingSeconds);

  useEffect(() => {
    localStorage.setItem('countdownTimerInitialTime', getInitialTime().toString());

    const intervalId = setInterval(() => {
      setSecondsRemaining((prevSeconds) => Math.max(prevSeconds - 1, 0));
      localStorage.setItem('countdownTimerRemainingSeconds', secondsRemaining.toString());
    }, 1000);

    return () => clearInterval(intervalId); // Cleanup the interval on component unmount
  }, [secondsRemaining]);

  const formatTime = (timeInSeconds) => {
    const days = Math.floor(timeInSeconds / (24 * 3600));
    const hours = Math.floor((timeInSeconds % (24 * 3600)) / 3600);
    const minutes = Math.floor((timeInSeconds % 3600) / 60);
    const seconds = timeInSeconds % 60;

    return {
      days,
      hours,
      minutes,
      seconds,
    };
  };

  const { days, hours, minutes, seconds } = formatTime(secondsRemaining);

  const inputHandler = (e) => {
    setInput(e.target.value);
  };

  const submitHandler = async (e) => {
    e.preventDefault();
    if (input) {
      const emailsCollection = collection(db, 'emails');

      try {
        const docRef = await addDoc(emailsCollection, {
          email: input,
          time: serverTimestamp(),
        });

        toast.success('Email Successfully deliver', { position: 'top-right' });

        console.log('Document written with ID: ', docRef.id);
        setInput("");
      } catch (error) {
        toast.error('Error adding document: ' + error.message, { position: 'top-right' });
        console.error('Error adding document: ', error);
      }
    }
  };

  return (
    <div className="main">
      <div className="w-full  mx-auto h-full relative flex-col justify-center items-center inline-flex">
      <div className="w-full md:w-[80%] lg:w-[70%] xl:w-[60%] 2xl:w-[50%] h-[657.52px] relative  flex-col justify-center items-center inline-flex">
        <img className="img" src={img} alt="Your Image" />
        <h1 className="text-white text-3xl md:text-4xl lg:text-5xl font-bold pb-6 font-montserrat">
          A Beginning of New Era
        </h1>
        <div className="f d shadow flex flex-wrap justify-start items-start gap-4 md:gap-8 lg:gap-12 inline-flex b">
        <div className=" px-[33.46px] py-[16.73px] bg-white radius-9 justify-start items-start gap-[8.37px] flex">
        <div className="e flex-col justify-start items-center inline-flex ">
            <div className="text-violet-600 text-3xl font-bold font-montserrat">{days}</div>
            <div className="text-violet-600 text-lg font-medium font-montserrat">Days</div>
          </div>
        </div>
      <div className="px-[33.46px] py-[16.73px] bg-white radius-9 justify-start items-start gap-[8.37px] flex">
      <div className="e flex-col justify-start items-center inline-flex ">
          <div className="text-violet-600 text-3xl font-bold font-montserrat">{hours}</div>
          <div className="text-violet-600 text-lg font-medium font-montserrat">Hours</div>
        </div>
      </div>
    <div className="px-[33.46px] py-[16.73px] bg-white radius-9 justify-start items-start md:gap-[8.37px] flex">
      <div className="e flex-col justify-start items-center inline-flex">
          <div className="text-violet-600 text-3xl font-bold font-montserrat">{minutes}</div>
          <div className="text-violet-600 text-lg font-medium font-montserrat">Min</div>
      </div>
    </div>
    <div className="px-[33.46px] py-[16.73px] bg-white radius-9 justify-start items-start md:gap-[8.37px] flex ">
      <div className="e flex-col justify-start items-center inline-flex">
          <div className="text-violet-600 text-3xl font-bold font-montserrat">{seconds}</div>
          <div className="text-violet-600 text-lg font-medium font-montserrat">Sec</div>
        </div>
        </div>
      </div>
      <h1 className="text-white text-2xl md:text-3xl font-bold font-montserrat mb-6 mt-6 uppercase b">
        Get Notified when we are ready
      </h1>
      <div className="relative  flex-col justify-center items-center inline-flex">
      <form onSubmit={submitHandler} className="md:flex block">
      <input
        onChange={inputHandler}
        value={input}
        className="ac w-full md:w-[597px] h-14 bg-white p-5 rounded-[49.36px] shadow text-stone-500 text-xl font-normal font-montserrat"
        placeholder="Email Address"
        type="email"
        required
      />
      <div className="md:relative a">
        <button
          className="md:absolute md:right-0 md:top-0 w-[138px] h-14 bg-blue-600 md:rounded-tr-[49.36px] md:rounded-br-[49.36px] rounded-lg text-white"
          type="submit"
        >
          SEND
        </button>
      </div>
    </form>
      </div>
      <div className="flex p-4">
      <a href='https://www.facebook.com/profile.php?id=100095270256563' target='_blank'><FaFacebook className="text-[30px]  text-white m-2  hover:text-blue-500" /></a>
      <a href='https://www.instagram.com' target='_blank'><FaInstagram className="text-[30px]  text-white m-2 hover:text-red-500" /></a>
      <a href='https://www.linkedin.com/company/nepal-filili-tech-pvt-ltd/' target='_blank'><FaLinkedinIn className="text-[30px]  text-white m-2  hover:text-blue-500" /></a>
    </div>
      </div>
    </div>
    <ToastContainer />
  </div>


  )
}

export default App