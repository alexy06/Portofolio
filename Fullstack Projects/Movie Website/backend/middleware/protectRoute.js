import jwt from "jsonwebtoken";
import { User } from "../models/user.model.js";
import { ENV_VARS } from "../config/envVars.js";

export const protectRoute = async (req, res, next) => {
  try {
    const token = req.cookies["jwt-netflix"];

    if (!token) {
      return res
        .status(401)
        .json({ success: false, message: "No token, authorization denied" });
    }

    const decoded = jwt.verify(token, ENV_VARS.JWT_SECRET);

    if (!decoded) {
      return res.status(401).json({
        success: false,
        message: "Token is invalid, authorization denied",
      });
    }

    const user = User.findById(decoded.userId).select("-password");
    if (!user) {
      return res
        .status(404)
        .json({ success: false, message: "User not found" });
    }

    req.user = user;
    req.user = { _id: decoded.userID };

    next();
  } catch (error) {
    console.log("Error in protected request: ", error.message);
    res.status(500).json({ success: false, message: "Server error" });
  }
};
