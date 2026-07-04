import { Routes, Route } from "react-router-dom";

import Login from "./pages/Login/Login";
import Dashboard from "./pages/Dashboard/Dashboard";
import Employees from "./pages/Employees/Employees";
import Users from "./pages/Users/Users";


function App() {
    return (
        <Routes>

            <Route
                path="/"
                element={<Login />}
            />

            <Route
                path="/dashboard"
                element={<Dashboard />}
            />

            <Route
                path="/employees"
                element={<Employees />}
            />
            <Route
                path="/users"
                element={<Users />}
            />

        </Routes>
    );
}

export default App;