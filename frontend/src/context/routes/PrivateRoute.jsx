import { Navigate, Outlet } from "react-router-dom";
import { useAuthContext } from "../authContext";
import React from "react";

export default function PrivateRoute() {
  const { isAuthenticated } = useAuthContext();

  if (!isAuthenticated) {
    return <Navigate to="/" />;
  }

  return (
    <div>
      <Outlet />
    </div>
  );
}
