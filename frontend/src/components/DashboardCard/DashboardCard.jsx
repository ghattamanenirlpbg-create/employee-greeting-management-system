import "./DashboardCard.css";

function DashboardCard({
    title,
    subtitle,
    icon,
    onClick
}) {
    return (
        <div
            className="dashboard-card"
            onClick={onClick}
            style={{ cursor: "pointer" }}
        >
            <div className="dashboard-icon">
                {icon}
            </div>

            <h3 className="dashboard-title">
                {title}
            </h3>

            <p className="dashboard-subtitle">
                {subtitle}
            </p>
        </div>
    );
}

export default DashboardCard;