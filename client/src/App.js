import './App.css';
import axios from "axios";
import React, {useState } from "react";

function App() {

  const [data, setData] = useState(null);

  function getData() {
    axios({
      method: "GET",
      url: "/test",
    })
    .then((response) => {
      const res =response.data
      setData({
        profile_name: res.name,
        greeting: res.greeting
      })
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

  return (
    <div className="App">
      <button onClick={getData}> Click here</button>
      {data && <div>
        <p>Profile name: {data.profile_name}</p>
        <p>Greeting: {data.greeting} </p>
      </div>}
    </div>
  );
}

export default App;
