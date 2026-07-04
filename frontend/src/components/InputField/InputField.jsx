import "./InputField.css";

function InputField({
    label,
    type = "text",
    placeholder,
    value,
    onChange
}) {

    return (
        <div className="input-group">

            <label className="input-label">
                {label}
            </label>

            <input
                className="input-box"
                type={type}
                placeholder={placeholder}
                value={value}
                onChange={onChange}
            />

        </div>
    );
}

export default InputField;