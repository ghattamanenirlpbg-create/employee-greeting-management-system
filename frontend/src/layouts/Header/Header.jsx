import "./Header.css";

function Header() {
    return (
        <header className="header">

            <div className="header-left">
                <h2>Employee Greeting Management System</h2>
            </div>

            <div className="header-right">
                <span>Welcome, Admin</span>

                <button className="logout-button">
                    Logout
                </button>
            </div>

        </header>
    );
}

export default Header;