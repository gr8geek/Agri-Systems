const express = require("express");
const path = require("path");
const ejs = require("ejs");
const cookieParser = require("cookie-parser");
const connectDB = require("./src/db/mongoose");

const app = express();

// Connect to database
connectDB();

app.get("/", (req, res) => {
  res.send({ msg: "Api Running" });
});

// middleware
app.use(express.json({ extended: false }));
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

const publicDirectoryPath = path.join(__dirname, "../public");
app.use(express.static(path.join(__dirname, "/public")));
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "/public/views"));

// Define routes
app.use("/api/users", require("./src/routers/api/userRouter"));

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log("Server started on port", PORT);
});
