import "./App.css";
import { Routes, Route } from "react-router-dom";
import HomePage from "./views/Home";
import SummaryPage from "./views/Summarize";
import ScorePage from "./views/Score";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/summarize" element={<SummaryPage />} />
        <Route path="/score" element={<ScorePage />} />
      </Routes>
    </div>
  );
}

export default App;
