import { useLocation } from "react-router-dom";

import {
    Box,
    Button,
    Paper,
    Typography
} from "@mui/material";


function GreetingPreview() {

    const location = useLocation();

    const image = location.state?.image;

    const downloadCard = () => {

        const link = document.createElement("a");

        link.href = `http://127.0.0.1:8000/${image}`;

        link.download = "Appreciation_Card.png";

        document.body.appendChild(link);

        link.click();

        document.body.removeChild(link);

    };

    return (

        <Box
            sx={{
                display: "flex",
                justifyContent: "center",
                mt: 5
            }}
        >

            <Paper
                sx={{
                    p: 4,
                    width: 900,
                    textAlign: "center"
                }}
            >

                <Typography
                    variant="h4"
                    mb={3}
                >

                    Appreciation Card

                </Typography>

                <img

                    src={`http://127.0.0.1:8000/${image}`}

                    alt="Greeting"

                    style={{
                        width: "100%",
                        borderRadius: 12,
                        border: "1px solid #ddd"
                    }}

                />

                <br /><br />

                <Button

                    variant="contained"

                    size="large"

                    onClick={downloadCard}

                >

                    Download Appreciation Card

                </Button>

            </Paper>

        </Box>

    );

}

export default GreetingPreview;