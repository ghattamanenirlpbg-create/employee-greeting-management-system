import { useNavigate } from "react-router-dom";

import "../../styles/Login.css";

import Button from "../../components/Button/Button";
import Card from "../../components/Card/Card";
import InputField from "../../components/InputField/InputField";

function Login() {

    const navigate = useNavigate();

    function handleLogin() {
        // Temporary navigation
        // Backend authentication will be added later
        navigate("/dashboard");
    }

    return (
    <div className="login-container">

        <Card>

            <h2 className="login-title">
                Employee Greeting Management System
            </h2>

            <InputField placeholder="Username" />
            <InputField placeholder="Password" type="password" />

            <Button onClick={handleLogin}>
                Login
            </Button>

        </Card>

    </div>
);
}

export default Login;