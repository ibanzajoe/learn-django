import React from "react";
import { Outlet } from "react-router-dom";

export default function AdminLayout() {
    return (
        <div className="layout">
            <p>this is layout</p>
            <Outlet />
        </div>
    );
}
