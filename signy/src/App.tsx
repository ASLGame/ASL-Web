import logo from "./logo.svg";
import { Counter } from "./features/counter/Counter";
import { Authorization } from "./features/authorization/Authorization";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <Routes>
            {/* 
                List of routes with respective views
            */}
            <Route path="/" element={<Counter />} />
            <Route path="/login" element={<Authorization />} />
          </Routes>
        </header>
      </div>
    </Router>
  );
}

export default App;
