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

import "./Users.css";


function Users() {

    const [open, setOpen] = useState(false);

    const [editId, setEditId] = useState(null);

    const [search, setSearch] = useState("");

    const [rows, setRows] = useState([]);

    const [user, setUser] = useState({
        username: "",
        password: "",
        role: "",
        status: ""
    });

    const handleChange = (e) => {

        setUser({
            ...user,
            [e.target.name]: e.target.value
        });
    };
    const handleEdit = (row) => {

        setUser(row);

        setEditId(row.id);

        setOpen(true);

    };

    const handleDelete = async (id) => {
        const confirmDelete = window.confirm(
            "Are you sure you want to delete this User?"
        );

        if (!confirmDelete) return;

        try {

            await api.delete(`/users/${id}`);

            await loadUsers();

        } catch (error) {
            console.error(error);
            alert("Unable to delete User.");
        }
    };

    const loadUsers = async () => {
        try {
            const response = await api.get("/users/");
            console.log("Users API:", response.data);
            const data = response.data.map((u) => ({
                id: u.id,
                username: u.username,
                password: u.password,
                role: u.role,
                status: u.status
            }));

            setRows(data);

        } catch (error) {
            console.error(error);
        }
    };

    const handleSave = async () => {
        try {

            const payload = {
                username: user.username,
                password: user.password,
                role: user.role,
                status: user.status
            };

            if (editId !== null) {

                await api.put(`/users/${editId}`, payload);

            } else {

                await api.post("/users/", payload);

            }

            await loadUsers();

            setUser({
                username: "",
                password: "",
                role: "",
                status: ""
            });

            setEditId(null);
            setOpen(false);

        } catch (error) {
            console.error(error);
            alert("Unable to save User.");
        }
    };

    const columns = [
        {
            field: "username",
            headerName: "Username",
            flex: 1.5
        },
        {
            field: "role",
            headerName: "Role",
            flex: 1
        },
        {
            field: "status",
            headerName: "Status",
            flex: 1
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
            row.username.toLowerCase().includes(search.toLowerCase()) ||
            row.role.toLowerCase().includes(search.toLowerCase()) ||
            row.status.toLowerCase().includes(search.toLowerCase())
        );
    }, [rows, search]);

    useEffect(() => {
        loadUsers();
    }, []);

    return (

        <MainLayout>

            <div className="users-container">

                <div className="employees-header">

                    <h1>User Management</h1>

                    <Button
                        variant="contained"
                        onClick={() => {

                            setUser({
                                username: "",
                                password: "",
                                role: "",
                                status: ""
                            });

                            setEditId(null);

                            setOpen(true);

                        }}
                    >
                        Add User
                    </Button>

                </div>

                <TextField

                    fullWidth

                    label="Search User"

                    sx={{ mb: 2 }}

                    value={search}

                    onChange={(e) => setSearch(e.target.value)}

                />

                <Box
                    sx={{
                        height: 550,
                        width: "100%",
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
                        ? "Edit User"
                        : "Add User"}

                </DialogTitle>

                <DialogContent>

                    <Grid
                        container
                        spacing={2}
                        sx={{ mt: 1 }}
                    >

                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="Username"
                                name="username"
                                value={user.username}
                                onChange={handleChange}
                            />
                        </Grid>

                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                type="password"
                                label="Password"
                                name="password"
                                value={user.password}
                                onChange={handleChange}
                            />
                        </Grid>

                        <Grid item xs={6}>
                            <TextField
                                fullWidth
                                label="Role"
                                name="role"
                                value={user.role}
                                onChange={handleChange}
                            />
                        </Grid>

                        <Grid item xs={6}>
                            <TextField
                                fullWidth
                                label="Status"
                                name="status"
                                value={user.status}
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

export default Users;