import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../../services/api";

import "../../styles/Login.css";

import Button from "../../components/Button/Button";
import Card from "../../components/Card/Card";
import InputField from "../../components/InputField/InputField";

function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    async function handleLogin() {

        try {

            const response = await api.post(

                "/login",

                null,

                {

                    params: {

                        username,

                        password

                    }

                }

            );

            localStorage.setItem(

                "username",

                response.data.username

            );

            localStorage.setItem(

                "role",

                response.data.role

            );

            navigate("/dashboard");

        }

        catch (error) {

            if (error.response) {

                alert(error.response.data.detail);

            }

            else {

                alert("Unable to connect to server.");

            }

        }

    }

    return (

        <div className="login-container">

            <Card>

                <h2 className="login-title">

                    Employee Greeting Management System

                </h2>

                <InputField

                    placeholder="Username"

                    value={username}

                    onChange={(e) => setUsername(e.target.value)}

                />

                <InputField

                    placeholder="Password"

                    type="password"

                    value={password}

                    onChange={(e) => setPassword(e.target.value)}

                />

                <Button onClick={handleLogin}>

                    Login

                </Button>

            </Card>

        </div>

    );

}

export default Login;