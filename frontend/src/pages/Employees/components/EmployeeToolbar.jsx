import { Box, Button, TextField, Typography } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";

function EmployeeToolbar() {
    return (
        <Box
            sx={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: 3,
            }}
        >
            <Typography variant="h4" fontWeight="bold">
                Employees
            </Typography>

            <Button
                variant="contained"
                startIcon={<AddIcon />}
            >
                Add Employee
            </Button>
        </Box>
    );
}

export default EmployeeToolbar;