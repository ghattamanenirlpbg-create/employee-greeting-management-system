import { DataGrid } from "@mui/x-data-grid";
import { Box, Chip } from "@mui/material";

function EmployeeDataGrid() {

    const columns = [
        {
            field: "id",
            headerName: "ID",
            width: 90,
        },
        {
            field: "name",
            headerName: "Employee Name",
            flex: 1,
        },
        {
            field: "department",
            headerName: "Department",
            width: 150,
        },
        {
            field: "designation",
            headerName: "Designation",
            width: 180,
        },
        {
            field: "status",
            headerName: "Status",
            width: 130,
            renderCell: (params) => (
                <Chip
                    label={params.value}
                    color={params.value === "Active" ? "success" : "default"}
                    size="small"
                />
            ),
        },
    ];

    const rows = [
        {
            id: 1001,
            name: "Ravi Kumar",
            department: "IT",
            designation: "Software Engineer",
            status: "Active",
        },
        {
            id: 1002,
            name: "Anita Sharma",
            department: "HR",
            designation: "HR Manager",
            status: "Active",
        },
        {
            id: 1003,
            name: "Rahul Verma",
            department: "Finance",
            designation: "Accountant",
            status: "Inactive",
        },
    ];

    return (
        <Box sx={{ height: 500, width: "100%" }}>
            <DataGrid
                rows={rows}
                columns={columns}
                pageSizeOptions={[5, 10, 20]}
                initialState={{
                    pagination: {
                        paginationModel: {
                            pageSize: 5,
                        },
                    },
                }}
                disableRowSelectionOnClick
            />
        </Box>
    );
}

export default EmployeeDataGrid;