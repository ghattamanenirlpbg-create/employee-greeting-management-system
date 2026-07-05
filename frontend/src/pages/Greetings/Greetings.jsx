import { useState } from "react";
import MainLayout from "../../layouts/MainLayout/MainLayout";
import api from "../../services/api";

import {
    Box,
    Button,
    Typography
} from "@mui/material";

function Greetings() {

    const [file, setFile] = useState(null);

    const [preview, setPreview] = useState("");

    const uploadPhoto = async () => {

        if (!file) return;

        const formData = new FormData();

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

            alert("Photo Uploaded Successfully");

            console.log(response.data);

        } catch (error) {

            console.error(error);

            alert("Upload Failed");

        }

    };

    return (

        <MainLayout>

            <Typography
                variant="h4"
                mb={3}
            >
                Appreciation Greeting
            </Typography>

            <Box
                sx={{
                    width: 500,
                    p: 4,
                    background: "#fff",
                    borderRadius: 3
                }}
            >

                <input

                    type="file"

                    accept="image/*"

                    onChange={(e) => {

                        setFile(e.target.files[0]);

                        setPreview(
                            URL.createObjectURL(
                                e.target.files[0]
                            )
                        );

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

                    onClick={uploadPhoto}

                >

                    Upload Photo

                </Button>

            </Box>

        </MainLayout>

    );

}

export default Greetings;