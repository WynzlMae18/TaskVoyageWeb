import React from 'react';
import './Dashboard.css'; // Import the CSS file

const Dashboard = () => {
  return (
    <div className="dashboard">
      <div className="sidebar">
        <div className="logo">
          <img src="./img/ship.png" alt="Ship Icon3" className="ship-icon3"/>  <span>TaskVoyage</span>
        </div>
        <ul className="navigation">
          <li><a href="/dashboard">Home</a></li>
          <li><a href="/tasks">Tasks</a></li>
          <li><a href="/calendar">Calendar</a></li>
          <li><a href="/settings">Settings</a></li>
          <li><a href="/logout">Logout</a></li>
        </ul>
      </div>
      <div className="content-area">
        {/* Dashboard content goes here */}
      </div>
    </div>
  );
};

export default Dashboard;
