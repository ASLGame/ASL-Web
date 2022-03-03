import logo from "./logo.svg";
import { Counter } from "./features/counter/Counter";
import  { SignIn }  from "./features/signin/SignIn";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SignUp } from "./features/signup/SignUp";

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          {/* <img src={logo} className="App-logo" alt="logo" /> */}
          <Routes>
            {/* 
                List of routes with respective views
            */}
            <Route path="/" element={<Counter />} />
            <Route path="/signin" element={<SignIn />} />
            <Route path="/signup" element={<SignUp />} />
          </Routes>
        </header>
      </div>
    </Router>
  );
}

export default App;
