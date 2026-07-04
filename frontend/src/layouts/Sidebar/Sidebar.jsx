import "./Sidebar.css";
import { NavLink } from "react-router-dom";

import {
    FaHome,
    FaUsers,
    FaUserShield,
    FaBirthdayCake,
    FaChartBar,
    FaCog
} from "react-icons/fa";

function Sidebar() {

    const menuItems = [
        { icon: <FaHome />, text: "Dashboard", path: "/dashboard" },
        { icon: <FaUsers />, text: "Employees", path: "/employees" },
        { icon: <FaUserShield />, text: "Users", path: "/users" },
        { icon: <FaBirthdayCake />, text: "Greetings", path: "/greetings" },
        { icon: <FaChartBar />, text: "Reports", path: "/reports" },
        { icon: <FaCog />, text: "Settings", path: "/settings" }
    ];

    return (
        <aside className="sidebar">

            <div className="sidebar-title">
                MENU
            </div>

            <ul className="menu-list">

                {menuItems.map((item, index) => (

                    <NavLink
                        key={index}
                        to={item.path}
                        className="menu-item"
                    >
                        <span className="menu-icon">
                            {item.icon}
                        </span>

                        <span className="menu-text">
                            {item.text}
                        </span>
                    </NavLink>

                ))}

            </ul>

        </aside>
    );
}

export default Sidebar;