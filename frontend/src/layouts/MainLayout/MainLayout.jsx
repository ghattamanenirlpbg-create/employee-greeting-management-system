import Header from "../Header/Header";
import Sidebar from "../Sidebar/Sidebar";

import "./MainLayout.css";

function MainLayout({ children }) {
    return (
        <>
            <Header />

            <div className="layout-container">

                <Sidebar />

                <main className="layout-content">
                    {children}
                </main>

            </div>
        </>
    );
}

export default MainLayout;