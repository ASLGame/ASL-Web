import logo from "./logo.svg";
import { Counter } from "./features/counter/Counter";
import { SignIn } from "./features/signin/SignIn";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SignUp } from "./features/signup/SignUp";
import Home from "./features/home/Home";
import Games from "./features/games/Games";

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <Routes>
            {/* 
                List of routes with respective views
            */}
            <Route path="/" element={<Counter />} />
            <Route path="/signin" element={<SignIn />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/home" element={<Home />} />
            <Route path="/games" element={<Games />} />
          </Routes>
        </header>
      </div>
    </Router>
  );
}

export default App;
