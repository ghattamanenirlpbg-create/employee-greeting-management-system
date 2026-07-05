import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../../services/api";

import {
    Box,
    Button,
    Typography
} from "@mui/material";

function GreetingUpload() {

    const { token } = useParams();

    const navigate = useNavigate();

    const [file, setFile] = useState(null);

    const [preview, setPreview] = useState("");

    const [valid, setValid] = useState(false);

    useEffect(() => {

        api
            .get(`/greeting-links/${token}`)
            .then(() => setValid(true))
            .catch(() => setValid(false));

    }, [token]);

    const upload = async () => {

        if (!file) {
            alert("Please select a photo.");
            return;
        }

        const formData = new FormData();

        formData.append("token", token);
        formData.append("file", file);

        try {

            const response = await api.post(

                "/uploads/photo",

                formData,

                {

                    headers: {

                        "Content-Type": "multipart/form-data"

                    }

                }

            );

            navigate(

                "/greeting-preview",

                {

                    state: {

                        image: response.data.image

                    }

                }

            );

        } catch (error) {

            console.error(error);

            alert("Upload failed.");

        }

    };

    if (!valid) {

        return (

            <Box
                sx={{
                    mt: 10,
                    textAlign: "center"
                }}
            >

                <Typography variant="h4">

                    Invalid or Expired Link

                </Typography>

            </Box>

        );

    }

    return (

        <Box
            sx={{
                mt: 5,
                textAlign: "center"
            }}
        >

            <Typography
                variant="h4"
                mb={3}
            >

                Upload Your Photograph

            </Typography>

            <input

                type="file"

                accept="image/*"

                onChange={(e) => {

                    const selected = e.target.files[0];

                    setFile(selected);

                    if (selected) {

                        setPreview(

                            URL.createObjectURL(selected)

                        );

                    }

                }}

            />

            <br /><br />

            {

                preview && (

                    <img

                        src={preview}

                        alt="Preview"

                        style={{

                            width: 250,

                            borderRadius: 12

                        }}

                    />

                )

            }

            <br /><br />

            <Button

                variant="contained"

                onClick={upload}

            >

                Submit Photograph

            </Button>

        </Box>

    );

}

export default GreetingUpload;