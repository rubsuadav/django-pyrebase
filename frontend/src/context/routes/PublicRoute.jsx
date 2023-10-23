import { Outlet } from "react-router-dom";
import React from "react";

export default function PublicRoute() {
  return (
    <div>
      <Outlet />
    </div>
  );
}
