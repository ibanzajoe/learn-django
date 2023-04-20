import React, { Component, useEffect } from "react";
import { createBrowserRouter, Route, Routes } from "react-router-dom";

import AdminLayout from "./layouts/AdminLayout";
import HomePage from "./HomePage";
import { rawPokemon$ } from "../store/index";

/* import AdminLayout from "./admin/Layout";
import HomePage from "./HomePage";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import RoomPage from "./Room";
import RoomLayout from "./admin/RoomLayout"; */

export default function App() {
    useEffect(() => {
        rawPokemon$.subscribe(console.log);
    }, []);
    return (
        <div className="app">
            <Routes>
                <Route path="/reactadmin" element={<AdminLayout />}>
                    <Route index element={<HomePage />} />
                </Route>
                {/* }>
                    
                    <Route path="join" element={<RoomJoinPage />} />
                    <Route path="create" element={<CreateRoomPage />} />
                    <Route path="room">
                        <Route path=":roomCode" element={<RoomPage />} />
                    </Route>
                </Route> */}
            </Routes>
        </div>
    );
}
