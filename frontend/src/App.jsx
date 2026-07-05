import { Routes, Route } from "react-router-dom";
import Greetings from "./pages/Greetings/Greetings";
import Login from "./pages/Login/Login";
import Dashboard from "./pages/Dashboard/Dashboard";
import Employees from "./pages/Employees/Employees";
import Users from "./pages/Users/Users";
import GreetingUpload from "./pages/GreetingUpload/GreetingUpload";
import GreetingPreview from "./pages/GreetingPreview/GreetingPreview";
import ProtectedRoute from "./components/ProtectedRoute";


function App() {
    return (
        <Routes>

            <Route
                path="/"
                element={<Login />}
            />

            <Route
                path="/dashboard"
                element={
                    <ProtectedRoute>
                        <Dashboard />
                    </ProtectedRoute>
                }
            />

            <Route
                path="/employees"
                element={
                    <ProtectedRoute>
                        <Employees />
                    </ProtectedRoute>
                }
            />
            <Route
                path="/users"
                element={
                    <ProtectedRoute>
                        <Users />
                    </ProtectedRoute>
                }
            />

            <Route
                path="/greetings"
                element={
                    <ProtectedRoute>
                        <Greetings />
                    </ProtectedRoute>
                }
            />

            <Route
                path="/greeting/:token"
                element={<GreetingUpload />}
            />

            <Route
                path="/greeting-preview"
                element={<GreetingPreview />}
            />

        </Routes>
    );
}

export default App;