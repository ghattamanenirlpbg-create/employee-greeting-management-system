import "./Header.css";

import { useNavigate } from "react-router-dom";

function Header() {

    const navigate = useNavigate();

    const handleLogout = () => {

        localStorage.removeItem("username");

        localStorage.removeItem("role");

        navigate("/", { replace: true });

    };

    return (

        <header className="header">

            <div className="header-left">

                <h2>Employee Greeting Management System</h2>

            </div>

            <div className="header-right">

                <span>

                    Welcome, {localStorage.getItem("username")}

                </span>

                <button

                    className="logout-button"

                    onClick={handleLogout}

                >

                    Logout

                </button>

            </div>

        </header>

    );

}

export default Header;