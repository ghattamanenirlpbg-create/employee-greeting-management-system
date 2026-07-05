import { Navigate } from "react-router-dom";

function ProtectedRoute({ children }) {

    const username = localStorage.getItem("username");

    if (!username) {

        return <Navigate to="/" replace />;

    }

    return children;

}

export default ProtectedRoute;