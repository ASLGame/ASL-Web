import logo from "./logo.svg";
import { Counter } from "./features/counter/Counter";
import  { SignIn }  from "./features/signin/SignIn";
import { Profile } from "./features/profile/Profile";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

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
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </header>
      </div>
    </Router>
  );
}

export default App;
