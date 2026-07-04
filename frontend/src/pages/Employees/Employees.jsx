import { useState, useMemo, useEffect } from "react";
import MainLayout from "../../layouts/MainLayout/MainLayout";
import api from "../../services/api";

import {
    Box,
    Button,
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Grid,
    TextField
} from "@mui/material";

import {
    DataGrid,
    GridActionsCellItem
} from "@mui/x-data-grid";

import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

import "./Employees.css";


function Employees() {

    const [open, setOpen] = useState(false);

    const [editId, setEditId] = useState(null);

    const [search, setSearch] = useState("");

    const [rows, setRows] = useState([]);

    const [employee, setEmployee] = useState({
        empId: "",
        name: "",
        designation: "",
        role: "",
        email: ""
    });

    const handleChange = (e) => {

        setEmployee({
            ...employee,
            [e.target.name]: e.target.value
        });

    };

    const handleEdit = (row) => {

        setEmployee(row);

        setEditId(row.id);

        setOpen(true);

    };

    const handleDelete = async (id) => {
        const confirmDelete = window.confirm(
            "Are you sure you want to delete this employee?"
        );

        if (!confirmDelete) return;

        try {

            await api.delete(`/employees/${id}`);

            await loadEmployees();

        } catch (error) {
            console.error(error);
            alert("Unable to delete employee.");
        }
    };  

    const loadEmployees = async () => {
        try {
            const response = await api.get("/employees/");
            console.log("Employees API:", response.data);
            const data = response.data.map((emp) => ({
                id: emp.id,
                empId: emp.emp_id,
                name: emp.name,
                designation: emp.designation,
                role: emp.role,
                email: emp.email
            }));

            setRows(data);

        } catch (error) {
            console.error(error);
        }
    };

    const handleSave = async () => {
        try {

            const payload = {
                emp_id: employee.empId,
                name: employee.name,
                designation: employee.designation,
                role: employee.role,
                email: employee.email
            };

            if (editId !== null) {

                await api.put(`/employees/${editId}`, payload);

            } else {

                await api.post("/employees/", payload);

            }

            await loadEmployees();

            setEmployee({
                empId: "",
                name: "",
                designation: "",
                role: "",
                email: ""
            });

            setEditId(null);
            setOpen(false);

        } catch (error) {
            console.error(error);
            alert("Unable to save employee.");
        }
    };

    const columns = [
        {
            field: "empId",
            headerName: "Employee ID",
            flex: 1
        },
        {
            field: "name",
            headerName: "Employee Name",
            flex: 1
        },
        {
            field: "designation",
            headerName: "Designation",
            flex: 1
        },
        {
            field: "role",
            headerName: "Role",
            flex: 1
        },
        {
            field: "email",
            headerName: "Email ID",
            flex: 1.5
        },
        {
            field: "actions",
            type: "actions",
            headerName: "Actions",
            width: 120,
            getActions: (params) => [
                <GridActionsCellItem
                    icon={<EditIcon />}
                    label="Edit"
                    onClick={() => handleEdit(params.row)}
                />,
                <GridActionsCellItem
                    icon={<DeleteIcon />}
                    label="Delete"
                    onClick={() => handleDelete(params.row.id)}
                />
            ]
        }
    ];

    const filteredRows = useMemo(() => {
        return rows.filter((row) =>
            row.empId.toLowerCase().includes(search.toLowerCase()) ||
            row.name.toLowerCase().includes(search.toLowerCase()) ||
            row.designation.toLowerCase().includes(search.toLowerCase()) ||
            row.role.toLowerCase().includes(search.toLowerCase()) ||
            row.email.toLowerCase().includes(search.toLowerCase())
        );
    }, [rows, search]);

    useEffect(() => {
        loadEmployees();
    }, []);
    return (

        <MainLayout>

            <div className="employees-container">

                <div className="employees-header">

                    <h1>Employee Management</h1>

                    <Button
                        variant="contained"
                        onClick={() => {

                            setEmployee({
                                empId: "",
                                name: "",
                                designation: "",
                                role: "",
                                email: ""
                            });

                            setEditId(null);

                            setOpen(true);

                        }}
                    >
                        Add Employee
                    </Button>

                </div>

                <TextField

                    fullWidth

                    label="Search Employee"

                    sx={{ mb: 2 }}

                    value={search}

                    onChange={(e) => setSearch(e.target.value)}

                />

                <Box
                    sx={{
                        height: 550,
                        background: "#ffffff",
                        borderRadius: 2,
                        mt: 2
                    }}
                >

                    <DataGrid
                        rows={filteredRows}
                        columns={columns}
                        pageSizeOptions={[5, 10, 20]}
                        initialState={{
                            pagination: {
                                paginationModel: {
                                    pageSize: 5
                                }
                            }
                        }}
                    />

                </Box>

            </div>

            <Dialog
                open={open}
                onClose={() => setOpen(false)}
                maxWidth="sm"
                fullWidth
            >

                <DialogTitle>

                    {editId !== null
                        ? "Edit Employee"
                        : "Add Employee"}

                </DialogTitle>

                <DialogContent>

                    <Grid
                        container
                        spacing={2}
                        sx={{ mt: 1 }}
                    >

                        <Grid item xs={6}>

                            <TextField
                                fullWidth
                                label="Employee ID"
                                name="empId"
                                value={employee.empId}
                                onChange={handleChange}
                            />

                        </Grid>

                        <Grid item xs={6}>

                            <TextField
                                fullWidth
                                label="Employee Name"
                                name="name"
                                value={employee.name}
                                onChange={handleChange}
                            />

                        </Grid>


                        <Grid item xs={6}>

                            <TextField
                                fullWidth
                                label="Designation"
                                name="designation"
                                value={employee.designation}
                                onChange={handleChange}
                            />

                        </Grid>

                        <Grid item xs={6}>
                            <TextField
                                fullWidth
                                label="Role"
                                name="role"
                                value={employee.role}
                                onChange={handleChange}
                            />
                        </Grid>

                        <Grid item xs={12}>

                            <TextField
                                fullWidth
                                label="Email ID"
                                name="email"
                                value={employee.email}
                                onChange={handleChange}
                            />

                        </Grid>


                    </Grid>

                </DialogContent>

                <DialogActions>

                    <Button
                        onClick={() => setOpen(false)}
                    >
                        Cancel
                    </Button>

                    <Button
                        variant="contained"
                        onClick={handleSave}
                    >
                        Save
                    </Button>

                </DialogActions>

            </Dialog>

        </MainLayout>

    );

}

export default Employees;