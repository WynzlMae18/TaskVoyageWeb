// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Register from "./components/Register";
import Login from "./components/Login";
import EmailConfirmation from "./components/EmailConfirmation";
import Dashboard from "./components/Dashboard";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Login />} />{" "}
        {/* Define a route for the root URL */}
        <Route exact path="/register" element={<Register />} />
        <Route exact path="/login" element={<Login />} />
        <Route exact path="/dashboard" element={<Dashboard/>} />
        <Route
          exact
          path="/email-confirm/:uid/:token"
          element={<EmailConfirmation />}
        />
      </Routes>
    </Router>
  );
};

export default App;
