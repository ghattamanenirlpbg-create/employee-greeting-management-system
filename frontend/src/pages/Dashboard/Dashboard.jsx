import { useNavigate } from "react-router-dom";

import MainLayout from "../../layouts/MainLayout/MainLayout";
import DashboardCard from "../../components/DashboardCard/DashboardCard";

import "./Dashboard.css";

function Dashboard() {

    const navigate = useNavigate();

    return (
        <MainLayout>

            <h1 className="dashboard-heading">
                Dashboard
            </h1>

            <p className="dashboard-welcome">
                Welcome to Employee Greeting Management System
            </p>

            <div className="dashboard-grid">

                <DashboardCard
                    title="Employees"
                    subtitle="Manage Employees"
                    icon="👥"
                    onClick={() => navigate("/employees")}
                />

                <DashboardCard
                    title="Greetings"
                    subtitle="Generate Greeting Cards"
                    icon="🎉"
                />

                <DashboardCard
                    title="Templates"
                    subtitle="Manage Templates"
                    icon="🖼️"
                />

                <DashboardCard
                    title="Users"
                    subtitle="Manage Users"
                    icon="👤"
                />

                <DashboardCard
                    title="Reports"
                    subtitle="View Reports"
                    icon="📊"
                />

                <DashboardCard
                    title="Settings"
                    subtitle="Application Settings"
                    icon="⚙️"
                />

            </div>

        </MainLayout>
    );
}

export default Dashboard;