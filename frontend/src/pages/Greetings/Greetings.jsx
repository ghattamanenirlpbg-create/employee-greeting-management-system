import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { DataGrid } from "@mui/x-data-grid";

import MainLayout from "../../layouts/MainLayout/MainLayout";
import api from "../../services/api";


import {
    Box,
    Button,
    Grid,
    Paper,
    Tab,
    Tabs,
    TextField,
    Typography
} from "@mui/material";

// Generate Card States

const Greetings = () => {
    const navigate = useNavigate();

    const [tab, setTab] = useState(0);

    const [empId, setEmpId] = useState("");

    const [employees, setEmployees] = useState([]);
    // ==========================


    const [employee, setEmployee] = useState(null);

    const [selectedRows, setSelectedRows] = useState([]);

    const [file, setFile] = useState(null);

    const [preview, setPreview] = useState("");

    // ==========================
    // Auto Email States
    // ==========================


    // ==========================
    // Fetch Employee
    // ==========================

    const fetchEmployee = async () => {

        try {

            const response = await api.get(
                `/employees/empid/${empId}`
            );

            setEmployee(response.data);

        }

        catch {

            alert("Employee not found");

            setEmployee(null);

        }

    };

    const generateGreeting = async () => {

        if (!employee) {

            alert("Fetch Employee First");

            return;

        }

        if (!file) {

            alert("Please select employee photograph");

            return;

        }

        const formData = new FormData();

        formData.append("emp_id", employee.emp_id);

        formData.append("file", file);

        try {

            const response = await api.post(

                "/greetings/generate",

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

        }

        catch (error) {

            console.error(error);

            alert("Greeting Generation Failed");

        }

    };

    // ==========================
    // Generate Greeting
    // ==========================

    const generateLinks = async () => {

        console.log("Selected Rows:", selectedRows);

        if (selectedRows.length === 0) {

            alert("Please select at least one employee.");

            return;

        }

        try {

            const response = await api.post(

                "/greeting-links/generate",

                selectedRows

            );

            console.log(response.data);

            alert(response.data.message);

        }

        catch (error) {

            console.log(JSON.stringify(error.response?.data));

            console.error(error);

            alert("Unable to generate secure links.");

        }

    };

    const loadEmployees = async () => {

        try {

            const response = await api.get("/employees");

            console.log(response.data);

            setEmployees(response.data);

            console.log("First Employee ID:", response.data[0].id);
            console.log("First Employee:", response.data[0]);

        }

        catch (error) {

            console.error(error);

            alert("Unable to load employees.");

        }

    };

    const columns = [

        {
            field: "emp_id",
            headerName: "Employee ID",
            width: 130
        },

        {
            field: "name",
            headerName: "Employee Name",
            width: 220
        },

        {
            field: "designation",
            headerName: "Designation",
            width: 220
        },

        {
            field: "role",
            headerName: "Role",
            width: 180
        },

        {
            field: "email",
            headerName: "Email",
            flex: 1
        }

    ];

    return (

        <MainLayout>

            <Typography
                variant="h4"
                mb={3}
            >

                Greeting Management

            </Typography>

            <Tabs

                value={tab}

                onChange={(event, value) => setTab(value)}

                sx={{ mb: 3 }}

            >

                <Tab label="Generate Card" />

                <Tab label="Auto Email" />

            </Tabs>

            {tab === 0 && (
                <Paper sx={{ p: 4 }}>
                    <Grid container spacing={2}>

                        <Grid size={8}>
                            <TextField
                                fullWidth
                                label="Employee ID"
                                value={empId}
                                onChange={(e) => setEmpId(e.target.value)}
                            />
                        </Grid>

                        <Grid size xs={4}>
                            <Button
                                fullWidth
                                variant="contained"
                                sx={{ height: "56px" }}
                                onClick={fetchEmployee}
                            >
                                Fetch
                            </Button>
                        </Grid>
                    </Grid>

                    {employee && (
                        <>
                            <Box mt={4}>
                                <TextField
                                    fullWidth
                                    label="Employee Name"
                                    value={employee.name}
                                    InputProps={{ readOnly: true }}
                                />
                            </Box>
                            <Box mt={2}>

                                <TextField

                                    fullWidth

                                    label="Designation"

                                    value={employee.designation}

                                    InputProps={{
                                        readOnly: true
                                    }}

                                />

                            </Box>

                            <Box mt={2}>

                                <TextField

                                    fullWidth

                                    label="Role"

                                    value={employee.role}

                                    InputProps={{
                                        readOnly: true
                                    }}

                                />

                            </Box>

                            <Box mt={2}>

                                <TextField

                                    fullWidth

                                    label="Email"

                                    value={employee.email}

                                    InputProps={{
                                        readOnly: true
                                    }}

                                />

                            </Box>

                            <Box mt={3}>

                                <input

                                    type="file"

                                    accept="image/*"

                                    onChange={(e) => {

                                        const selected = e.target.files[0];

                                        setFile(selected);

                                        if (selected) {

                                            setPreview(

                                                URL.createObjectURL(
                                                    selected
                                                )

                                            );

                                        }

                                    }}

                                />

                            </Box>

                            {

                                preview && (

                                    <Box mt={3}>

                                        <img

                                            src={preview}

                                            alt="Preview"

                                            style={{
                                                width: 250,
                                                borderRadius: 12
                                            }}

                                        />

                                    </Box>

                                )

                            }

                            <Box mt={3}>

                                <Button

                                    variant="contained"

                                    onClick={
                                        generateGreeting
                                    }

                                >

                                    Generate Greeting

                                </Button>

                            </Box>

                        </>

                    )

                    }

                </Paper>

            )
            }
            {

                tab === 1 && (

                    <Paper
                        sx={{
                            p: 4
                        }}
                    >

                        <Typography
                            variant="h5"
                            mb={3}
                        >

                            Auto Email Greeting

                        </Typography>

                        <Typography
                            mb={3}
                        >

                            Select one or more employees and send greeting links.

                        </Typography>

                        <Box
                            sx={{
                                display: "flex",
                                gap: 2,
                                mb: 3
                            }}
                        >

                            <Button
                                variant="contained"
                                onClick={loadEmployees}
                            >

                                Load Employees

                            </Button>

                            <Button
                                variant="outlined"
                                onClick={() => {

                                    setSelectedRows(

                                        employees.map((emp) => emp.id)

                                    );

                                }}
                            >

                                Select All

                            </Button>

                            <Button
                                variant="outlined"
                                onClick={() => {

                                    setSelectedRows([]);

                                }}
                            >

                                Clear Selection

                            </Button>

                        </Box>

                        <Paper
                            sx={{
                                height: 500,
                                width: "100%"
                            }}
                        >

                            <DataGrid

                                rows={employees}

                                getRowId={(row) => row.id}

                                columns={columns}

                                checkboxSelection

                                disableRowSelectionOnClick

                                pageSizeOptions={[10, 20, 50]}

                                initialState={{

                                    pagination: {

                                        paginationModel: {

                                            pageSize: 10,

                                            page: 0

                                        }

                                    }

                                }}

                                onRowSelectionModelChange={(selection) => {

                                    setSelectedRows(

                                        Array.from(selection.ids)

                                    );

                                }}

                            />

                        </Paper>

                        <Box
                            mt={3}
                        >

                            <TextField

                                fullWidth

                                multiline

                                rows={4}

                                label="Email Message (Optional)"

                                placeholder="Enter custom message..."

                            />

                        </Box>

                        <Box
                            mt={3}
                            sx={{
                                display: "flex",
                                gap: 2
                            }}
                        >

                            <Button
                                variant="contained"
                                color="primary"
                                onClick={generateLinks}
                            >

                                Generate Secure Links

                            </Button>

                            <Button
                                variant="contained"
                                color="success"
                            >

                                Send Email

                            </Button>

                        </Box>

                    </Paper>

                )

            }
        </MainLayout >

    );

}

export default Greetings;