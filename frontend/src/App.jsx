import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

//local imports
import { AuthContextProvider } from "./context/authContext";
import PublicRoute from "./context/routes/PublicRoute";
import PrivateRoute from "./context/routes/PrivateRoute";
import ProtectedRoute from "./context/routes/ProtectedRoute";

import Home from "./pages/Home";
import Contact from "./pages/Contact";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import Profile from "./pages/Profile";

import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div className="w-full h-full bg-gray-100">
      <AuthContextProvider>
        <Router>
          <Navbar />
          <Routes>
            <Route path="/" element={<PublicRoute />}>
              <Route index element={<Home />} />
              <Route path="/contact" element={<Contact />} />
            </Route>
            <Route element={<ProtectedRoute />}>
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
            </Route>
            <Route element={<PrivateRoute />}>
              <Route path="/profile" element={<Profile />} />
            </Route>
          </Routes>
          <Footer />
        </Router>
      </AuthContextProvider>
    </div>
  );
}
