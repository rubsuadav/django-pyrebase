import React, { useState } from "react";
import { useAuthContext } from "../../context/authContext";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { login } = useAuthContext();
  let navigate = useNavigate();

  async function handleLogin(e) {
    e.preventDefault();
    const response = await fetch("https://django-pyrebase.onrender.com/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    if (response.status === 400) {
      setErrors(["Invalid credentials"]);
      return;
    }

    const data = await response.json();

    login(data.token);
    navigate("/");
  }

  return (
    <div className="w-full h-screen flex items-center justify-center">
      <form className="w-full md:w-1/3 rounded-lg" onSubmit={handleLogin}>
        <div className="flex font-bold justify-center mt-6">
          <img className="h-20 w-20 mb-3" src="https://dummyimage.com/64x64" />
        </div>
        <h2 className="text-2xl text-center text-gray-500 mb-8">Login</h2>
        <div className="px-12 pb-10">
          <div className="w-full mb-2">
            <div className="flex items-center">
              <input
                type="text"
                placeholder="Email Address"
                className="
                  w-full
                  border
                  rounded
                  px-3
                  py-2
                  text-gray-700
                  focus:outline-none
                "
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
          </div>
          <div className="w-full mb-2">
            <div className="flex items-center">
              <input
                type="password"
                placeholder="Password"
                className="
                  w-full
                  border
                  rounded
                  px-3
                  py-2
                  text-gray-700
                  focus:outline-none
                "
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>
          {errors.length > 0 && (
            <div className="text-red-500 mb-4">
              {errors.map((error, index) => (
                <p key={index}>{error}</p>
              ))}
            </div>
          )}
          <button
            type="submit"
            className="
              w-full
              py-2
              mt-8
              rounded-full
              bg-blue-400
              text-gray-100
              focus:outline-none
            "
          >
            Login
          </button>
        </div>
      </form>
    </div>
  );
}
