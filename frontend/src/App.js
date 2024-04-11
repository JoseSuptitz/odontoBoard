import './App.css';
import axios from "axios";
import React from 'react';

const baseURL = "http://localhost:8000/api/pacients/"

export default function App() {

  const [pacients, setPacients] = React.useState(null);

  React.useEffect(() => {
    axios.get(baseURL).then((Response) => {
      setPacients(Response.data);
    })
  }, []);

  if (!pacients) return null;

  return (
    <div className="App">
      <h1>Pacientes</h1>
      <p className="Line">------------------------------------------------------</p>
      {pacients.map((pacient) => (
        <div key={pacient.position}>
        <h2>{pacient.name}</h2>
        <h2>{pacient.description}</h2>
        </div>
      ))}
    </div>
  );
}

