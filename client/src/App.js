import './App.css';
import axios from "axios";
import React, {useState } from "react";

function App() {

  const [data, setData] = useState(null);
  const [isQuery, setIsQuery] = useState(false);

  function getData() {
    setIsQuery(true);
    axios({
      method: "GET",
      url: "/data",
    })
    .then((response) => {
      const res =response.data
      setData({
        numOfCountries: res.numOfCountries,
        landSum : res.landSum,
        populationSum : res.popSum      
      })
      setIsQuery(false);
    })
    .catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

  function clearData() {
    setData(null);
  }
    

  return (
    <div className="App">
      <h1>Scraper for <a href="https://www.scrapethissite.com/pages/simple/"a>Countries in the Worlds</a></h1>

      <br />
      <button onClick={getData}> Click here to view sum data </button>
      <button onClick={clearData}> Click here to clear data</button>
      {data && <div>
        <p>Number of countries: {data.numOfCountries}</p>
        <p>Land mass in the world: {data.landSum} km^2</p>
        <p>Population of the world: {data.populationSum} people</p>
      </div> }
      {isQuery && <div>
        <p>Querying...</p>
      </div> }
    </div>
  );
}

export default App;
